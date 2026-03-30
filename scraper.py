from datetime import datetime
from sqlalchemy.orm import Session
from models import CountryPR

def seed_sample_data(db: Session):
    existing = db.query(CountryPR).count()
    if existing > 0:
        return "Sample data already exists."

    sample_data = [
        {
            "country": "Germany",
            "pr_name": "Settlement Permit / Long-Term Residence",
            "pr_years": "5 years",
            "student_route": "Conditional",
            "work_route": "Yes",
            "family_route": "Yes",
            "language_required": "Yes",
            "income_requirement": "Stable legal income required",
            "absence_rule": "Limited absences allowed",
            "citizenship_years": "5-8 years",
            "spouse_allowed": "Yes",
            "spouse_work_allowed": "Yes",
            "official_source": "https://www.make-it-in-germany.com/",
            "last_updated": datetime.now().strftime("%Y-%m-%d")
        },
        {
            "country": "Sweden",
            "pr_name": "Permanent Residence",
            "pr_years": "5 years",
            "student_route": "Conditional",
            "work_route": "Yes",
            "family_route": "Yes",
            "language_required": "Maybe",
            "income_requirement": "Self-support required",
            "absence_rule": "Continuous legal stay required",
            "citizenship_years": "5+ years",
            "spouse_allowed": "Yes",
            "spouse_work_allowed": "Yes",
            "official_source": "https://www.migrationsverket.se/",
            "last_updated": datetime.now().strftime("%Y-%m-%d")
        },
        {
            "country": "Portugal",
            "pr_name": "Permanent Residence",
            "pr_years": "5 years",
            "student_route": "Yes",
            "work_route": "Yes",
            "family_route": "Yes",
            "language_required": "Basic Portuguese may be needed",
            "income_requirement": "Proof of means required",
            "absence_rule": "Continuous residence rule",
            "citizenship_years": "5 years",
            "spouse_allowed": "Yes",
            "spouse_work_allowed": "Yes",
            "official_source": "https://eportugal.gov.pt/",
            "last_updated": datetime.now().strftime("%Y-%m-%d")
        },
        {
            "country": "Netherlands",
            "pr_name": "Permanent Residence / Long-Term Resident EU",
            "pr_years": "5 years",
            "student_route": "Conditional",
            "work_route": "Yes",
            "family_route": "Yes",
            "language_required": "Usually yes",
            "income_requirement": "Sufficient sustainable income",
            "absence_rule": "Limited long absences",
            "citizenship_years": "5 years",
            "spouse_allowed": "Yes",
            "spouse_work_allowed": "Yes",
            "official_source": "https://ind.nl/",
            "last_updated": datetime.now().strftime("%Y-%m-%d")
        },
        {
            "country": "Ireland",
            "pr_name": "Long-Term Residence / Stamp-based national route",
            "pr_years": "5 years",
            "student_route": "Conditional",
            "work_route": "Yes",
            "family_route": "Yes",
            "language_required": "No formal general PR language rule",
            "income_requirement": "Stable lawful residence and income helpful",
            "absence_rule": "Continuity matters",
            "citizenship_years": "5 years",
            "spouse_allowed": "Yes",
            "spouse_work_allowed": "Depends on permission type",
            "official_source": "https://www.irishimmigration.ie/",
            "last_updated": datetime.now().strftime("%Y-%m-%d")
        }
    ]

    for item in sample_data:
        country = CountryPR(**item)
        db.add(country)

    db.commit()
    return "Sample data inserted successfully."