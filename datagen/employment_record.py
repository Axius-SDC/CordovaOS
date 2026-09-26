"""
Employment Record 4.4.0: one record per job.

The model composes the NIEM library's employment association (the position, the
employee's occupation and status, hours and pay basis) and Cordova's compensation
cluster in COR, with the employee's CID and the employer's Business Registry
Number as the joins to the Civil and Business registries. Eight cast jobs plus
85% of the working-age background population.
"""
import random

from business_registry import employer_roster
from shared import (
    CAST, PERSONS, COR, Quantity, random_date, full_name,
    record, write_record, import_dir,
)

TITLE = "Employment Record"
SYSTEM = "Cordova Employment System"
OUTPUT_DIR = import_dir("employment_record")

# Cordova's employment statuses, and the NIEM position basis each implies.
EMP_STATUSES = ["Full-Time", "Part-Time", "Contract", "Self-Employed"]
BASIS_OF = {"Full-Time": "permanent", "Part-Time": "permanent", "Contract": "contractor", "Self-Employed": "non-permanent"}
PAY_FREQS = ["Monthly", "Monthly", "Bi-Weekly", "Weekly"]
# The activity-lifecycle workflow: an employment that is current is ongoing; one that has ended is completed.
STATE_OF = {"current": "ActivityOngoing", "ended": "ActivityCompleted"}

CAST_JOBS = [
    ("carlos", "Deck Operations", "Able Seaman", "Porto Sereno", "Aldara", "2018-03-15", 28000),
    ("elena", "Marine Biology Department", "Associate Professor", "Campoluz", "Brevina", "2022-09-01", 65000),
    ("dr_reyes", "Emergency Medicine", "Senior Physician", "Porto Sereno", "Aldara", "2008-06-01", 95000),
    ("governor_avila", "Executive Office", "Provincial Governor", "Novaciudad", "Celara", "2022-01-15", 120000),
    ("sgt_santos", "Porto Sereno Precinct", "Sergeant", "Porto Sereno", "Aldara", "2010-04-01", 42000),
    ("dr_ferrer", "Provincial Health Office", "Provincial Health Officer", "Porto Sereno", "Aldara", "2005-08-01", 88000),
    ("dr_gutierrez", "Biology Department", "Professor", "Campoluz", "Brevina", "2012-09-01", 72000),
    ("prof_lucero", "Chemistry Department", "Professor", "Campoluz", "Brevina", "2008-09-01", 74000),
]
# The cast work where the narrative says they do: Carlos for the shipping line, Elena and the professors at the
# university, the physicians at the hospital, the sergeant for the national police, the health officer for the office.
CAST_EMPLOYERS = {"carlos": "BIZ-001102", "elena": "BIZ-000847", "dr_reyes": "BIZ-000523", "sgt_santos": "BIZ-000101",
                  "dr_ferrer": "BIZ-000205", "dr_gutierrez": "BIZ-000847", "prof_lucero": "BIZ-000847"}

BG_DEPARTMENTS = [
    "Operations", "Administration", "Sales", "Maintenance", "Security",
    "Finance", "IT", "Human Resources", "Marketing", "Production",
    "Customer Service", "Quality Control", "Logistics", "Research",
    "Procurement", "Legal", "Engineering", "Training",
]
BG_TITLES = [
    "Clerk", "Manager", "Technician", "Analyst", "Coordinator",
    "Supervisor", "Driver", "Worker", "Assistant", "Specialist",
    "Director", "Associate", "Inspector", "Operator", "Receptionist",
    "Accountant", "Sales Representative", "Foreman", "Secretary",
    "Guard", "Mechanic", "Chef", "Server", "Teacher",
    "Nurse", "Pharmacist", "Electrician", "Plumber", "Carpenter",
]


def _pick_employer(city, brn=None):
    """
    A registered organisation to employ this person: the one with ``brn`` when given,
    else one in the same city. Returns (name, brn) or (None, None) when the registry
    has not run.

    Employment and Business Registry use the SAME published component for the
    registry number, so an employer recorded as a BRN joins the two domains with
    no mapping table. Recorded as a name it joins nothing.
    """
    roster = employer_roster()
    if not roster:
        return None, None
    if brn:
        for biz in roster:
            if biz["brn"] == brn:
                return biz["name"], brn
    local = [b for b in roster if b.get("city") == city]
    biz = random.choice(local or roster)
    return biz["name"], biz["brn"]


def build_instance(rec):
    """One Employment Record for one job."""
    p = rec["person"]
    status = rec["status"]
    full_time = status == "Full-Time"
    hourly = status in ("Part-Time", "Contract")
    weekly_hours = 40 if full_time else random.choice([16, 20, 24, 30])
    values = {
        "Employment Record/National ID (CID)": p["cid"],
        "Employment Record/Business Registry Number": rec.get("employer_brn"),
        "Employment Record/City": rec["city"],
        "Employment Record/Province": rec["province"],
        "Employment Association/Employee Identification": p["cid"],
        "Employment Association/Employee Reference": f"urn:cordova:cid:{p['cid']}",
        "Employment Association/Employer Reference": f"urn:cordova:brn:{rec['employer_brn']}" if rec.get("employer_brn") else None,
        "Employment Association/Employee Occupation": rec["title"],
        "Employment Association/Employee Rank": rec["title"],
        "Employment Association/Employment Status": status,
        "Employment Association/Employee Full Time Indicator": full_time,
        "Employment Association/Employee Pay Hourly Indicator": hourly,
        "Employment Association/Employee Supervisor Indicator": rec["title"] in ("Manager", "Supervisor", "Director", "Foreman", "Provincial Governor", "Sergeant"),
        "Employment Association/Employee Hours Weekly Quantity": Quantity(str(weekly_hours), "h/wk"),
        "Employment Association/Employee Hours Daily Quantity": Quantity(str(8 if full_time else weekly_hours // 5), "h/d"),
        "Employment Association/Employment Pay Rate Amount": Quantity(str(rec["salary"]), COR),
        "Employment Association/Employment Location Reference": f"urn:cordova:city:{rec['city'].lower().replace(' ', '-')}",
        "Employment Position/Employment Position Department Name": rec["dept"],
        "Employment Position/Employment Position Name": rec["title"],
        "Employment Position/Employment Position Basis Code": BASIS_OF[status],
        "Employment Position/Employment Position Temporary Indicator": status == "Contract",
        "Compensation/Salary Amount": Quantity(str(rec["salary"]), COR),
        "Compensation/Pay Frequency": rec["pay_freq"],
    }
    provider = ("Employer Organization", rec["employer_name"])
    return record(TITLE, values, state=STATE_OF[rec.get("tenure", "current")], system=SYSTEM, activity_type="RecordCreation",
                  when=rec["start_date"], city=rec["city"], province=rec["province"], cid=p["cid"],
                  subject=("Subject Employee", full_name(p)), provider=provider,
                  attestation_reason="Employment reported by the employer organization", committer=rec["employer_name"])


def generate():
    count = 0

    # Cast employment
    for key, dept, title, city, prov, start, salary in CAST_JOBS:
        c = CAST[key]
        rec = {
            "person": c, "dept": dept, "title": title, "city": city, "province": prov,
            "start_date": start, "salary": salary, "status": "Full-Time", "pay_freq": "Monthly",
        }
        rec["employer_name"], rec["employer_brn"] = _pick_employer(city, CAST_EMPLOYERS.get(key))
        if not rec["employer_name"]:
            rec["employer_name"] = f"{dept}, {city}"
        write_record(OUTPUT_DIR, "em", build_instance(rec))
        count += 1

    # Background employment: all working-age (18-67) bg persons, ~85% employed
    if not PERSONS:
        from civil_registry import generate as gen_cr
        gen_cr()

    working_age = [p for p in PERSONS if p.get("key", "").startswith("bg_")
                   and 18 <= (2026 - int(p["dob"][:4])) <= 67]
    employed = random.sample(working_age, k=int(len(working_age) * 0.85))
    for p in employed:
        dept = random.choice(BG_DEPARTMENTS)
        rec = {
            "person": p, "dept": dept, "title": random.choice(BG_TITLES),
            "city": p["city"], "province": p["province"],
            "start_date": random_date(2005, 2024), "salary": random.randint(15000, 80000),
            "status": random.choice(EMP_STATUSES), "pay_freq": random.choice(PAY_FREQS),
        }
        rec["employer_name"], rec["employer_brn"] = _pick_employer(p["city"])
        if not rec["employer_name"]:
            rec["employer_name"] = f"{dept}, {p['city']}"
        write_record(OUTPUT_DIR, "em", build_instance(rec))
        count += 1

    print(f"Employment Record: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    random.seed("cordovaos")
    from civil_registry import generate as gen_cr
    from business_registry import generate as gen_br
    random.seed("cordovaos:Civil Registry"); gen_cr()
    random.seed("cordovaos:Business Registry"); gen_br()
    random.seed("cordovaos:Employment Record"); generate()
