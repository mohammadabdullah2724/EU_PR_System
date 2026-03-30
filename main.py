from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import CountryPR
from scraper import seed_sample_data
from export_excel import export_countries_to_excel

app = FastAPI(title="EU PR Intelligence App")

Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(
    request: Request,
    country: str = "",
    route: str = "",
    db: Session = Depends(get_db)
):
    query = db.query(CountryPR)

    if country:
        query = query.filter(CountryPR.country.ilike(f"%{country}%"))

    if route == "student":
        query = query.filter(CountryPR.student_route.ilike("%Yes%") | CountryPR.student_route.ilike("%Conditional%"))
    elif route == "work":
        query = query.filter(CountryPR.work_route.ilike("%Yes%"))
    elif route == "family":
        query = query.filter(CountryPR.family_route.ilike("%Yes%"))

    countries = query.all()

    return templates.TemplateResponse("index.html", {
        "request": request,
        "countries": countries,
        "country_filter": country,
        "route_filter": route
    })


@app.get("/country/{country_id}", response_class=HTMLResponse)
def country_detail(country_id: int, request: Request, db: Session = Depends(get_db)):
    country = db.query(CountryPR).filter(CountryPR.id == country_id).first()
    return templates.TemplateResponse("country.html", {
        "request": request,
        "country": country
    })


@app.get("/compare", response_class=HTMLResponse)
def compare_page(request: Request, ids: str = "", db: Session = Depends(get_db)):
    selected = []
    if ids:
        id_list = [int(i) for i in ids.split(",") if i.strip().isdigit()]
        selected = db.query(CountryPR).filter(CountryPR.id.in_(id_list)).all()

    all_countries = db.query(CountryPR).all()

    return templates.TemplateResponse("compare.html", {
        "request": request,
        "selected": selected,
        "all_countries": all_countries
    })


@app.get("/seed")
def seed_data(db: Session = Depends(get_db)):
    message = seed_sample_data(db)
    return {"message": message}


@app.get("/export")
def export_excel(db: Session = Depends(get_db)):
    file_path = export_countries_to_excel(db)
    return FileResponse(
        path=file_path,
        filename="EU_PR_System_Comparison_V2.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


@app.post("/add")
def add_country(
    country: str = Form(...),
    pr_name: str = Form(...),
    pr_years: str = Form(...),
    student_route: str = Form(...),
    work_route: str = Form(...),
    family_route: str = Form(...),
    language_required: str = Form(...),
    income_requirement: str = Form(...),
    absence_rule: str = Form(...),
    citizenship_years: str = Form(...),
    spouse_allowed: str = Form(...),
    spouse_work_allowed: str = Form(...),
    official_source: str = Form(...),
    last_updated: str = Form(...),
    db: Session = Depends(get_db)
):
    new_country = CountryPR(
        country=country,
        pr_name=pr_name,
        pr_years=pr_years,
        student_route=student_route,
        work_route=work_route,
        family_route=family_route,
        language_required=language_required,
        income_requirement=income_requirement,
        absence_rule=absence_rule,
        citizenship_years=citizenship_years,
        spouse_allowed=spouse_allowed,
        spouse_work_allowed=spouse_work_allowed,
        official_source=official_source,
        last_updated=last_updated
    )
    db.add(new_country)
    db.commit()

    return RedirectResponse(url="/", status_code=303)


@app.get("/api/countries")
def api_countries(db: Session = Depends(get_db)):
    countries = db.query(CountryPR).all()
    return countries