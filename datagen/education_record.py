"""
Generate Education Record XML instances for CordovaOS demo.

Elena as faculty, UNC students, some completed credentials.
Output: import_data/education_record/
"""
import os
import random

from shared import (
    CAST, PERSONS, random_date,
    xml_header, xml_preamble, xml_footer, write_xml,
    xdstring, xdtoken, xdtemporal, xdboolean_stub, xdordinal_stub,
    cluster_open, cluster_close, party_stub,
    cuid_generator, generate_cid_for_city,
)

CT_ID = "upq7w1bqbix5v5ss0mu3kq5n"
DM_LABEL = "Education Record"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "sdc4", "import_data", "education_record")

CL_ROOT       = "ms-ifgq7a670csnbv7vcpuiabp0"
W_CID         = ("ms-nj7s1gk45tfgyooxpz0qaha3", "ms-juovhrpa2stdsipyc24lizt9")
W_STUDENT_ID  = ("ms-khbvruwpu9hnttg8y0mnih6a", "ms-iqrherkjrps71itxidwzsznm")
W_CITY        = ("ms-atdtdfzruh7tya0iv5cz365l", "ms-b55nc510dfbznraizimlazlz")
W_PROVINCE    = ("ms-kv5qqs3o4jwcwz9javgw1pzh", "ms-qgf62cnfeqmpy6llv0pgxqdx")

CL_CRED       = "ms-nyf0w3u2hs0svcjnqkb6zzlb"
W_YESNO       = ("ms-ht98owgvxhff3ge85i4h80lp", "ms-re8yd9oeqeg2x9kpex3ftddj")
W_FIELD       = ("ms-ouqi09d8kjqeojlr7vnclysj", "ms-eaadqsalk8480aacxdkqnwla")
W_CRED_TYPE   = ("ms-sxkjp09cbjb6n13j8a0eg37i", "ms-jn3w03mloklangi4d47esyao")
W_HONORS      = ("ms-c7qvfjtu0omg4wagiaiy5hej", "ms-pm71mysjm8dzz63qm55rte35")
W_DATE_AWARD  = ("ms-xi99tao4v75wdrkq0ot02vfd", "ms-hthzohj8yfa5rv4y8ewctjho")

CL_ENROLL     = "ms-r97mt4prbpxp04qmdc8iimb8"
W_ENR_STATUS  = ("ms-squd8e2s6pk8xoafu9ec0t9k", "ms-eexkhtt84h5ym18n3nkz0fub")
W_EDU_LEVEL   = ("ms-1ylumrkck2vv635djov01tte4", "ms-zau2plaxqbg16mjj2w3alxs2")
W_ENR_DATE    = ("ms-z72jnzdib9hi311s338zwdog", "ms-pfeyaloy73eckb55cohcuih9")
W_EXPECT_DATE = ("ms-g6ntdb41otp1mtwsyb52mez3", "ms-h99xoiujvz9hh036e79y774x")

PS_STUDENT    = "ms-i4bkuj6quo2gv9sbghhdocaj"
PS_INSTITUTION = "ms-fpxka4mvhbmka33c0enhzfxl"

FIELDS = [
    "Marine Biology", "Environmental Science", "Computer Science",
    "Economics", "Political Science", "Engineering", "Medicine",
    "Literature", "History", "Chemistry", "Physics", "Mathematics",
    "Nursing", "Public Health", "Business Administration",
]
CRED_TYPES = ["Bachelor", "Master", "Doctorate", "Certificate", "Diploma"]
HONORS = ["None", "Cum Laude", "Magna Cum Laude", "Summa Cum Laude"]

_sid_counter = 0


def next_sid():
    global _sid_counter
    _sid_counter += 1
    return f"UNC-{_sid_counter:06d}"


def build_instance(rec):
    xml = xml_header(CT_ID)
    xml += xml_preamble(DM_LABEL)
    xml += cluster_open(CL_ROOT, "Education Record")

    xml += xdstring(*W_CID, "National ID (CID)", rec["cid"])
    xml += xdstring(*W_STUDENT_ID, "Student ID", rec["student_id"])
    xml += xdtoken(*W_CITY, "City", rec["city"])
    xml += xdtoken(*W_PROVINCE, "Province", rec["province"])

    # Credential
    xml += cluster_open(CL_CRED, "Credential", indent=2)
    xml += xdboolean_stub(*W_YESNO, "Yes/No", indent=3)
    xml += xdstring(*W_FIELD, "Field of Study", rec["field"], indent=3)
    xml += xdtoken(*W_CRED_TYPE, "Credential Type", rec["cred_type"], indent=3)
    xml += xdtoken(*W_HONORS, "Honors", rec.get("honors", "None"), indent=3)
    xml += xdtemporal(*W_DATE_AWARD, "Date Awarded", rec.get("date_awarded", "1900-01-01"), "date", indent=3)
    xml += cluster_close(CL_CRED, indent=2)

    # Enrollment
    xml += cluster_open(CL_ENROLL, "Enrollment", indent=2)
    xml += xdtoken(*W_ENR_STATUS, "Enrollment Status", rec["enr_status"], indent=3)
    xml += xdordinal_stub(*W_EDU_LEVEL, "Education Level", indent=3)
    xml += xdtemporal(*W_ENR_DATE, "Enrollment Date", rec["enr_date"], "date", indent=3)
    xml += xdtemporal(*W_EXPECT_DATE, "Expected Completion Date", rec["expect_date"], "date", indent=3)
    xml += cluster_close(CL_ENROLL, indent=2)

    xml += cluster_close(CL_ROOT)
    xml += party_stub(PS_STUDENT, "Student")
    xml += party_stub(PS_INSTITUTION, "Educational Institution")
    xml += xml_footer(CT_ID)
    return xml


def generate():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    count = 0

    # Elena - completed PhD, now faculty
    elena = CAST["elena"]
    rec = {
        "cid": elena["cid"], "student_id": next_sid(),
        "city": "Campoluz", "province": "Brevina",
        "field": "Marine Biology", "cred_type": "Doctorate",
        "honors": "Magna Cum Laude", "date_awarded": "2022-05-15",
        "enr_status": "Graduated", "enr_date": "2016-09-01",
        "expect_date": "2022-05-15",
    }
    write_xml(os.path.join(OUTPUT_DIR, f"ed-{cuid_generator()}.xml"), build_instance(rec))
    count += 1

    # Dr. Reyes - medical degree
    dr_reyes = CAST["dr_reyes"]
    rec = {
        "cid": dr_reyes["cid"], "student_id": next_sid(),
        "city": "Campoluz", "province": "Brevina",
        "field": "Medicine", "cred_type": "Doctorate",
        "honors": "Cum Laude", "date_awarded": "2004-06-20",
        "enr_status": "Graduated", "enr_date": "1998-09-01",
        "expect_date": "2004-06-20",
    }
    write_xml(os.path.join(OUTPUT_DIR, f"ed-{cuid_generator()}.xml"), build_instance(rec))
    count += 1

    # Dr. Ferrer - public health
    dr_ferrer = CAST["dr_ferrer"]
    rec = {
        "cid": dr_ferrer["cid"], "student_id": next_sid(),
        "city": "Campoluz", "province": "Brevina",
        "field": "Public Health", "cred_type": "Doctorate",
        "honors": "None", "date_awarded": "2000-05-30",
        "enr_status": "Graduated", "enr_date": "1994-09-01",
        "expect_date": "2000-05-30",
    }
    write_xml(os.path.join(OUTPUT_DIR, f"ed-{cuid_generator()}.xml"), build_instance(rec))
    count += 1

    # Education records for school-age and recent graduates (age 5-30)
    if not PERSONS:
        from civil_registry import generate as gen_cr
        gen_cr()

    eligible = [p for p in PERSONS if p.get("key", "").startswith("bg_")
                and 5 <= (2026 - int(p["dob"][:4])) <= 30]

    # Education institutions by level
    primary_schools = [
        ("Escuela Primaria Porto Sereno", "Porto Sereno", "Aldara"),
        ("Escuela Primaria Montecalvo", "Montecalvo", "Aldara"),
        ("Escuela Primaria Bahia Linda", "Bahia Linda", "Aldara"),
        ("Escuela Primaria Campoluz", "Campoluz", "Brevina"),
        ("Escuela Primaria Sierra Verde", "Sierra Verde", "Brevina"),
        ("Escuela Primaria Novaciudad", "Novaciudad", "Celara"),
        ("Escuela Primaria Costa Brava", "Costa Brava", "Celara"),
        ("Escuela Primaria Lago Azul", "Lago Azul", "Celara"),
        ("Escuela Primaria Tierra Roja", "Tierra Roja", "Brevina"),
    ]
    secondary_schools = [
        ("Liceo Nacional Porto Sereno", "Porto Sereno", "Aldara"),
        ("Liceo Nacional Campoluz", "Campoluz", "Brevina"),
        ("Liceo Nacional Novaciudad", "Novaciudad", "Celara"),
        ("Colegio Tecnico Montecalvo", "Montecalvo", "Aldara"),
        ("Colegio Tecnico Sierra Verde", "Sierra Verde", "Brevina"),
        ("Colegio Tecnico Costa Brava", "Costa Brava", "Celara"),
    ]

    for p in eligible:
        age = 2026 - int(p["dob"][:4])
        if age <= 11:
            # Primary school
            school = random.choice(primary_schools)
            cred_type = "Certificate"
            enr_status = "Active"
            field = "General Education"
            enr_year = max(2020, 2026 - (age - 5))
            expect_year = enr_year + 6
        elif age <= 17:
            # Secondary school
            school = random.choice(secondary_schools)
            cred_type = "Diploma"
            enr_status = random.choice(["Active", "Active", "Active", "On Leave"])
            field = random.choice(["General Studies", "Science Track", "Humanities Track", "Technical Track"])
            enr_year = max(2020, 2026 - (age - 12))
            expect_year = enr_year + 6
        elif age <= 25:
            # University
            school = ("Universidad Nacional de Cordova", "Campoluz", "Brevina")
            cred_type = random.choice(["Bachelor", "Bachelor", "Bachelor", "Master"])
            enr_status = random.choice(["Active", "Active", "Active", "On Leave", "Graduated"])
            field = random.choice(FIELDS)
            enr_year = random.randint(2018, 2024)
            expect_year = enr_year + (4 if cred_type == "Bachelor" else 2)
        else:
            # Recent graduates (26-30)
            school = ("Universidad Nacional de Cordova", "Campoluz", "Brevina")
            cred_type = random.choice(["Bachelor", "Master", "Master"])
            enr_status = "Graduated"
            field = random.choice(FIELDS)
            enr_year = random.randint(2014, 2020)
            expect_year = enr_year + (4 if cred_type == "Bachelor" else 2)

        honors = "None"
        date_awarded = "1900-01-01"
        if enr_status == "Graduated":
            honors = random.choice(HONORS)
            date_awarded = f"{expect_year}-{random.randint(5,6):02d}-{random.randint(1,28):02d}"

        rec = {
            "cid": p["cid"], "student_id": next_sid(),
            "city": school[1], "province": school[2],
            "field": field, "cred_type": cred_type,
            "honors": honors, "date_awarded": date_awarded,
            "enr_status": enr_status,
            "enr_date": f"{enr_year}-09-01",
            "expect_date": f"{expect_year}-{random.randint(5,6):02d}-15",
        }
        write_xml(os.path.join(OUTPUT_DIR, f"ed-{cuid_generator()}.xml"), build_instance(rec))
        count += 1

    print(f"Education Record: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    generate()
