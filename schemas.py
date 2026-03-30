from pydantic import BaseModel

class CountryPRBase(BaseModel):
    country: str
    pr_name: str
    pr_years: str
    student_route: str
    work_route: str
    family_route: str
    language_required: str
    income_requirement: str
    absence_rule: str
    citizenship_years: str
    spouse_allowed: str
    spouse_work_allowed: str
    official_source: str
    last_updated: str

class CountryPROut(CountryPRBase):
    id: int

    class Config:
        from_attributes = True