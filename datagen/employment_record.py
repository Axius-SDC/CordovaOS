"""
Generate Employment Record XML instances for CordovaOS demo.

Cast member employment + background workers.
Output: import_data/employment_record/
"""
import os
import random

from shared import (
    CAST, PERSONS, random_date, random_city_province,
    xml_header, xml_preamble, xml_footer, write_xml,
    xdstring, xdtoken, xdtemporal, xdquantity, xdboolean_stub,
    cluster_open, cluster_close, party_stub,
    cuid_generator,
)

CT_ID = "pm5cks82lnrvyna1xbwpfxic"
DM_LABEL = "Employment Record"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "sdc4", "import_data", "employment_record")

CL_ROOT       = "ms-ablvqv20fp33v8t8c985dlo2"
W_DEPT        = ("ms-bbu03oqjkniydmzb7pqcjg3m", "ms-c8m9eo2bfdf3q5wlfsvk2op8")
W_JOB_TITLE   = ("ms-wfws1oj1kgeaijciw7wkzdi7", "ms-u57ooe0a30kga0xde4xjry0p")
W_CITY        = ("ms-atdtdfzruh7tya0iv5cz365l", "ms-uhoxuq4o8xeeuqkwrm3nmqxy")
W_EMP_STATUS  = ("ms-tb3wwfwects1a6ap4ro7z5s8", "ms-gykp4x2cgr0k2r91ga3lpa14")
W_PROVINCE    = ("ms-kv5qqs3o4jwcwz9javgw1pzh", "ms-sis9vfoejjtn9xp3y0wkh5wu")
W_END_DATE    = ("ms-el43lwc0fnamy0v0ocub38t7", "ms-ju0zrm5w3gt653h25cs9qryw")
W_START_DATE  = ("ms-ghsjyyzudma3eq761dwd4j9p", "ms-pygvykba3py1elr8t0trhaow")

CL_COMP       = "ms-vzabxfc733qk7lo1knaggxfs"
W_YESNO       = ("ms-ht98owgvxhff3ge85i4h80lp", "ms-qlq395x4bisfdfo2dp3gfk19")
W_PAY_FREQ    = ("ms-ub0fwihnwu5x1pdv68pjwbeu", "ms-s59xgdrwxggiuxckp0ki7n4j")
W_SALARY      = ("ms-aw74ticc3fnjkz4vk4b03jr6", "ms-w6kn6sauh6lr2smq95ms4vud")

PS_EMPLOYEE   = "ms-yowhhhxm3qnk40qd3ekaluh0"
PS_EMPLOYER   = "ms-8fc8bd0qo44g5s4re0gwrhlr"

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

BG_DEPARTMENTS = ["Operations", "Administration", "Sales", "Maintenance", "Security", "Finance", "IT"]
BG_TITLES = ["Clerk", "Manager", "Technician", "Analyst", "Coordinator", "Supervisor", "Driver", "Worker"]


def build_instance(rec):
    xml = xml_header(CT_ID)
    xml += xml_preamble(DM_LABEL)
    xml += cluster_open(CL_ROOT, "Employment Record")

    xml += xdstring(*W_DEPT, "Department", rec["dept"])
    xml += xdstring(*W_JOB_TITLE, "Job Title", rec["title"])
    xml += xdtoken(*W_CITY, "City", rec["city"])
    xml += xdtoken(*W_EMP_STATUS, "Employment Status (Cordova)", rec.get("status", "Active"))
    xml += xdtoken(*W_PROVINCE, "Province", rec["province"])
    xml += xdtemporal(*W_END_DATE, "End Date", rec.get("end_date", "2099-12-31"), "date")
    xml += xdtemporal(*W_START_DATE, "Start Date", rec["start_date"], "date")

    xml += cluster_open(CL_COMP, "Compensation", indent=2)
    xml += xdboolean_stub(*W_YESNO, "Yes/No", indent=3)
    xml += xdtoken(*W_PAY_FREQ, "Pay Frequency", rec.get("pay_freq", "Monthly"), indent=3)
    xml += xdquantity(*W_SALARY, "Salary Amount", str(rec["salary"]),
                       "Cordova Córdoba (COR)", indent=3)
    xml += cluster_close(CL_COMP, indent=2)

    xml += cluster_close(CL_ROOT)
    xml += party_stub(PS_EMPLOYEE, "Employee")
    xml += party_stub(PS_EMPLOYER, "Employer")
    xml += xml_footer(CT_ID)
    return xml


def generate():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    count = 0

    # Cast employment
    for key, dept, title, city, prov, start, salary in CAST_JOBS:
        rec = {
            "dept": dept, "title": title,
            "city": city, "province": prov,
            "start_date": start, "salary": salary,
            "pay_freq": "Monthly",
        }
        write_xml(os.path.join(OUTPUT_DIR, f"em-{cuid_generator()}.xml"), build_instance(rec))
        count += 1

    # Background employment (~30)
    if not PERSONS:
        from civil_registry import generate as gen_cr
        gen_cr()

    bg = [p for p in PERSONS if p.get("key", "").startswith("bg_")][:30]
    for p in bg:
        rec = {
            "dept": random.choice(BG_DEPARTMENTS),
            "title": random.choice(BG_TITLES),
            "city": p["city"], "province": p["province"],
            "start_date": random_date(2010, 2024),
            "salary": random.randint(18000, 60000),
            "pay_freq": random.choice(["Monthly", "Bi-Weekly", "Weekly"]),
        }
        write_xml(os.path.join(OUTPUT_DIR, f"em-{cuid_generator()}.xml"), build_instance(rec))
        count += 1

    print(f"Employment Record: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    generate()
