from sqlalchemy import Column, Integer, String, Text
from database import Base

class CountryPR(Base):
    __tablename__ = "countries_pr"

    id = Column(Integer, primary_key=True, index=True)
    country = Column(String, index=True)
    pr_name = Column(String)
    pr_years = Column(String)
    student_route = Column(String)
    work_route = Column(String)
    family_route = Column(String)
    language_required = Column(String)
    income_requirement = Column(Text)
    absence_rule = Column(Text)
    citizenship_years = Column(String)
    spouse_allowed = Column(String)
    spouse_work_allowed = Column(String)
    official_source = Column(Text)
    last_updated = Column(String)