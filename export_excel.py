import pandas as pd
from sqlalchemy.orm import Session
from models import CountryPR

def export_countries_to_excel(db: Session):
    rows = db.query(CountryPR).all()

    data = []
    for r in rows:
        data.append({
            "Country": r.country,
            "PR Name": r.pr_name,
            "PR Years": r.pr_years,
            "Student Route": r.student_route,
            "Work Route": r.work_route,
            "Family Route": r.family_route,
            "Language Required": r.language_required,
            "Income Requirement": r.income_requirement,
            "Absence Rule": r.absence_rule,
            "Citizenship Years": r.citizenship_years,
            "Spouse Allowed": r.spouse_allowed,
            "Spouse Work Allowed": r.spouse_work_allowed,
            "Official Source": r.official_source,
            "Last Updated": r.last_updated,
        })

    df = pd.DataFrame(data)
    file_path = "EU_PR_System_Comparison_V2.xlsx"
    df.to_excel(file_path, index=False)

    return file_path