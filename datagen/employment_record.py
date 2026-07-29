"""
Generate Employment Record XML instances for CordovaOS demo.

Governance-composed model: Governed Record (data cluster + Provenance
Components) wrapped by native subject / provider / Audit / attestation slots,
mirroring the proven Civil Registry generator.

Cast member employment + background workers.
Output: import_data/employment_record/
"""
import os
import random

from shared import (
    CAST, PERSONS, random_date, random_city_province,
    xml_header, xml_preamble, xml_footer, write_xml,
    xdstring, xdtoken, xdtemporal, xdquantity,
    cluster_open, cluster_close, native_partytype,
    make_provenance_values, audit, attestation,
    cuid_generator, _esc, _xdany_seq,
)

CT_ID = "pm5cks82lnrvyna1xbwpfxic"
DM_LABEL = "Employment Record"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "sdc4", "import_data", "employment_record")

# ─── Governance envelope wrappers (re-keyed for v2, from template dm-*.xml) ───
GOVERNED_RECORD = "ms-xdu3vqk4vhuko5mghl4y4xxk"   # Item: Employment Governed Record
CL_ROOT         = "ms-ablvqv20fp33v8t8c985dlo2"   # Data cluster: Employment Record
CL_COMP         = "ms-vzabxfc733qk7lo1knaggxfs"   # Compensation sub-cluster
CL_PROV         = "ms-hdhjfg00tngir2txgqyka9cv"   # Provenance Components cluster

# ─── Data leaves: (component_id, adapter_wrapper_id) ─────────────────────────
W_DEPT        = ("ms-bbu03oqjkniydmzb7pqcjg3m", "ms-wmtotsniozsvdua4d7ise8zx")  # xdstring
W_JOB_TITLE   = ("ms-wfws1oj1kgeaijciw7wkzdi7", "ms-lx5ruyske40b7vp6n5riiufc")  # xdstring
W_CITY        = ("ms-atdtdfzruh7tya0iv5cz365l", "ms-n9pfwprgod2qouisuwhqko8o")  # xdtoken (City enum)
W_EMP_STATUS  = ("ms-tb3wwfwects1a6ap4ro7z5s8", "ms-pt7n7cytal8g6gjrx6kbh5f1")  # xdtoken (status enum)
W_PROVINCE    = ("ms-kv5qqs3o4jwcwz9javgw1pzh", "ms-cexlqx0wsa67vgdad3za8teg")  # xdtoken (Province enum)
W_END_DATE    = ("ms-el43lwc0fnamy0v0ocub38t7", "ms-kx42d03x6vw5vv01jl0kr8l1")  # xdtemporal-date
W_START_DATE  = ("ms-ghsjyyzudma3eq761dwd4j9p", "ms-lc1ah1reo2pg2q5nsoks68fi")  # xdtemporal-date

# Compensation sub-cluster leaves
W_YESNO       = ("ms-ht98owgvxhff3ge85i4h80lp", "ms-r133uwmjw1wuynmwdo4ga475")  # xdboolean (true/false-value)
W_PAY_FREQ    = ("ms-ub0fwihnwu5x1pdv68pjwbeu", "ms-ej9uu2aj6kx4e5vtcigfo2ul")  # xdtoken (freq enum)
W_SALARY      = ("ms-aw74ticc3fnjkz4vk4b03jr6", "ms-zhhzu3xflqkgu7o6xo3cu06p")  # xdquantity

# Provenance Components leaves (component, adapter)
P_ACT_DESC    = ("ms-m9xg6e182m1oq77ssrf9iujv", "ms-m91g74q0tdsrlu39x7adfymg")
P_ACT_TYPE    = ("ms-ccj1yq2wtwknobszkgzzdbtr", "ms-blxow8ztfj7qhw5875fig9sv")
P_SYS_ID      = ("ms-bd3s8t23d6m3zizmpwavc32y", "ms-g8g03pnbivtfz57huxzyr98k")
P_LOC_ID      = ("ms-zr59goe24qkocprl3feul3mt", "ms-nfz5536uproqxs68fuvfpch2")
P_LOC_NAME    = ("ms-fnodzqkbyskwe7nh58rs336k", "ms-ne75pbg9h338xgo9v31fzclr")
P_TS_END      = ("ms-edvvjznmaoibzmfna0uuoo37", "ms-lnblyhkpxft5w1kogloulvtv")
P_TS_START    = ("ms-o72s5793973fzho35rnaughs", "ms-e1dqy0brdaczewgvf4pka7p6")

# System Audit ms- component (substitutionGroup="sdc4:Audit"); shares Civil's id,
# and its five fixed labels equal Civil's audit() defaults (confirmed in XSD).
AUDIT_COMPONENT = "ms-fotc5adg15ek2b9ermx2mcih"

# Enum values fixed by the model's components.
EMP_STATUSES = ["Full-Time", "Part-Time", "Contract", "Self-Employed"]
PAY_FREQS = ["Monthly", "Monthly", "Bi-Weekly", "Weekly"]

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


def emp_boolean(component_id, wrapper_id, label, value, indent=2):
    """XdBoolean whose restricted content is a choice of true-value ("Yes") /
    false-value ("No"); the base xdboolean-value is not permitted here."""
    pad = "  " * indent
    ip = pad + "    "
    choice = ('<true-value>Yes</true-value>' if value
              else '<false-value>No</false-value>')
    return (f'{pad}<sdc4:{wrapper_id}>\n'
            f'{pad}  <sdc4:{component_id}>\n'
            f'{pad}    <label>{_esc(label)}</label>\n'
            f'{_xdany_seq(ip)}'
            f'{pad}    {choice}\n'
            f'{pad}  </sdc4:{component_id}>\n'
            f'{pad}</sdc4:{wrapper_id}>\n')


def build_instance(rec):
    """Build a governance-composed Employment Record instance for one record."""
    prov = make_provenance_values("Cordova Employment System", "RecordCreation", rec["city"])
    state = rec.get("status", "Full-Time")

    xml = xml_header(CT_ID)
    xml += xml_preamble(DM_LABEL, current_state=state)

    # Item: Governed Record wrapper
    xml += cluster_open(GOVERNED_RECORD, "Employment Governed Record", indent=1)

    # Data cluster. XSD sequence puts the Compensation sub-cluster BEFORE the
    # scalar adapters, so emission order follows the schema (not the template).
    xml += cluster_open(CL_ROOT, "Employment Record", indent=2)

    xml += cluster_open(CL_COMP, "Compensation", indent=3)
    xml += emp_boolean(*W_YESNO, "Yes/No", rec.get("benefits", True), indent=4)
    xml += xdtoken(*W_PAY_FREQ, "Pay Frequency", rec.get("pay_freq", "Monthly"), indent=4)
    xml += xdquantity(*W_SALARY, "Salary Amount", str(rec["salary"]),
                      "Cordova Córdoba (COR)", indent=4)
    xml += cluster_close(CL_COMP, indent=3)

    xml += xdstring(*W_DEPT, "Department", rec["dept"], indent=3)
    xml += xdstring(*W_JOB_TITLE, "Job Title", rec["title"], indent=3)
    xml += xdtoken(*W_CITY, "City", rec["city"], indent=3)
    xml += xdtoken(*W_EMP_STATUS, "Employment Status (Cordova)", rec.get("status", "Full-Time"), indent=3)
    xml += xdtoken(*W_PROVINCE, "Province", rec["province"], indent=3)
    xml += xdtemporal(*W_END_DATE, "End Date", rec.get("end_date", "2099-12-31"), "date", indent=3)
    xml += xdtemporal(*W_START_DATE, "Start Date", rec["start_date"], "date", indent=3)
    xml += cluster_close(CL_ROOT, indent=2)

    # Provenance Components cluster (sibling of data, inside Governed Record)
    xml += cluster_open(CL_PROV, "Provenance Components", indent=2)
    xml += xdstring(*P_ACT_DESC, "activity_description", prov["activity_description"], indent=3)
    xml += xdstring(*P_ACT_TYPE, "prov_activity_type", prov["prov_activity_type"], indent=3)
    xml += xdstring(*P_SYS_ID, "system_identifier", prov["system_identifier"], indent=3)
    xml += xdstring(*P_LOC_ID, "system_location_identifier", prov["system_location_identifier"], indent=3)
    xml += xdstring(*P_LOC_NAME, "system_location_name", prov["system_location_name"], indent=3)
    xml += xdtemporal(*P_TS_END, "activity_timestamp_end", prov["activity_timestamp_end"], "datetime", indent=3)
    xml += xdtemporal(*P_TS_START, "activity_timestamp_start", prov["activity_timestamp_start"], "datetime", indent=3)
    xml += cluster_close(CL_PROV, indent=2)

    xml += cluster_close(GOVERNED_RECORD, indent=1)

    # Native governance slots, DM order: subject, provider, Audit, attestation.
    xml += native_partytype("subject", "Subject Employee", rec["employee_name"])
    xml += native_partytype("provider", "Employer Organization", rec["employer_name"])
    xml += audit(AUDIT_COMPONENT, prov["activity_timestamp_start"],
                 system_id_value=prov["system_identifier"])
    xml += attestation(pending=False, reason="Employment record verified by the employer",
                       committer="Employer Organization", committed=prov["activity_timestamp_end"])

    xml += xml_footer(CT_ID)
    return xml


def generate():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    count = 0

    # Cast employment
    for key, dept, title, city, prov, start, salary in CAST_JOBS:
        c = CAST.get(key, {})
        emp_name = f"{c.get('given', '')} {c.get('surname', '')}".strip() or key
        rec = {
            "dept": dept, "title": title,
            "city": city, "province": prov,
            "start_date": start, "salary": salary,
            "status": "Full-Time",
            "pay_freq": "Monthly",
            "benefits": True,
            "employee_name": emp_name,
            "employer_name": f"{dept}, {city}",
        }
        write_xml(os.path.join(OUTPUT_DIR, f"em-{cuid_generator()}.xml"), build_instance(rec))
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
            "dept": dept,
            "title": random.choice(BG_TITLES),
            "city": p["city"], "province": p["province"],
            "start_date": random_date(2005, 2024),
            "salary": random.randint(15000, 80000),
            "status": random.choice(EMP_STATUSES),
            "pay_freq": random.choice(PAY_FREQS),
            "benefits": random.random() < 0.7,
            "employee_name": f"{p['given']} {p['surname']}",
            "employer_name": f"{dept}, {p['city']}",
        }
        write_xml(os.path.join(OUTPUT_DIR, f"em-{cuid_generator()}.xml"), build_instance(rec))
        count += 1

    print(f"Employment Record: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    generate()
