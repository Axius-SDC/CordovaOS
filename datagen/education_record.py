"""
Education Record 4.4.0: one record per enrollment.

The model composes the NIEM library's education (level, status, qualification,
institution reference) with Cordova's enrollment and credential, keyed by the
Cordova CID and a student identifier, with city and province for the institution.

Three cast doctorates at the Universidad Nacional de Cordova (BIZ-000847, Campoluz),
then every background resident aged 5 to 30: primary and secondary schools in the
resident's own city, the university for the rest.
"""
import random

from shared import (
    CAST, PERSONS, PROVINCE_CITIES, full_name,
    record, write_record, import_dir,
)

TITLE = "Education Record"
SYSTEM = "Cordova Education Registry"
OUTPUT_DIR = import_dir("education_record")

# The activity-lifecycle workflow the model binds, from the enrollment status
# (4.3.1 carried the enrollment status itself as the state).
STATE_OF_ENROLLMENT = {"Active": "ActivityOngoing", "Graduated": "ActivityCompleted", "Withdrawn": "ActivityNotCompleted",
                       "Suspended": "ActivityHalted", "On Leave": "ActivityHalted"}
FIELDS = [
    "Marine Biology", "Environmental Science", "Computer Science", "Economics", "Political Science", "Engineering", "Medicine",
    "Literature", "History", "Chemistry", "Physics", "Mathematics", "Nursing", "Public Health", "Business Administration",
]
HONORS = ["None", "Cum Laude", "Magna Cum Laude", "Summa Cum Laude"]
# Tier -> (NIEM education level code, credential type, level text)
TIERS = {
    "primary": ("less-than-high-school", "Primary Certificate", "Primary education"),
    "secondary": ("high-school", "Secondary Diploma", "Secondary education"),
    "associate": ("associate", "Associate Degree", "Associate degree"),
    "bachelor": ("bachelor", "Bachelor's Degree", "Bachelor's degree"),
    "master": ("master", "Master's Degree", "Master's degree"),
    "doctorate": ("academic-doctorate", "Doctoral Degree", "Doctoral degree"),
}
UNIVERSITY = ("Universidad Nacional de Cordova", "Campoluz", "Brevina")
UNIVERSITY_BRN = "BIZ-000847"

_sid_counter = 0


def next_sid():
    global _sid_counter
    _sid_counter += 1
    return f"UNC-{_sid_counter:06d}"


def _institution_ref(name):
    slug = "".join(ch if ch.isalnum() else "-" for ch in name.lower()).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return f"urn:cordova:institution:{slug}"


def build_instance(rec):
    """One Education Record for one enrollment."""
    level_code, cred_type, level_text = TIERS[rec["tier"]]
    completed = rec["enr_status"] == "Graduated"
    values = {
        "Education Record/National ID (CID)": rec["cid"],
        "Education Record/Student ID": rec["student_id"],
        "Education Record/City": rec["city"],
        "Education Record/Province": rec["province"],
        "Enrollment/Enrollment Status": rec["enr_status"],
        "Enrollment/Education Level": level_code,
        "Enrollment/Education Qualification Text": rec["field"],
        "Enrollment/Enrollment Date": rec["enr_date"],
        "Enrollment/Expected Completion Date": rec["expect_date"],
        "Education/Education Level": level_code,
        "Education/Education Level Text": level_text,
        "Education/Education Status": rec["enr_status"],
        "Education/Education In Progress Indicator": not completed,
        "Education/Education Qualification Text": rec["field"],
        "Education/Education Qualification Description": f"{cred_type} in {rec['field']}, {rec['institution']}",
        "Education/Education Qualification Institution Reference": _institution_ref(rec["institution"]),
    }
    if completed:
        values.update({
            "Credential/Credential Type": cred_type,
            "Credential/Education Qualification Text": rec["field"],
            "Credential/Honors": rec["honors"],
            "Credential/Date Awarded": rec["date_awarded"],
            "Education/Education Qualification Issued Date": rec["date_awarded"],
        })
    return record(TITLE, values, state=STATE_OF_ENROLLMENT[rec["enr_status"]], system=SYSTEM, activity_type="RecordRegistration",
                  when=rec["enr_date"], city=rec["city"], province=rec["province"], cid=rec["cid"],
                  subject=("Student", rec["student_name"]), provider=("Institution", rec["institution"]),
                  attestation_reason="Enrollment verified by the registrar's office", committer=rec["institution"])


def _random_city_province():
    prov = random.choice(list(PROVINCE_CITIES.keys()))
    return random.choice(PROVINCE_CITIES[prov]), prov


def _make_record(person, tier, field, enr_status, enr_year, expect_year, institution, city, province):
    honors, date_awarded = "None", None
    if enr_status == "Graduated":
        honors = random.choice(HONORS)
        date_awarded = f"{expect_year}-{random.randint(5, 6):02d}-{random.randint(1, 28):02d}"
    return {
        "cid": person["cid"], "student_id": next_sid(), "student_name": full_name(person),
        "institution": institution, "city": city, "province": province, "field": field, "tier": tier,
        "honors": honors, "date_awarded": date_awarded, "enr_status": enr_status,
        "enr_date": f"{enr_year}-09-01", "expect_date": f"{expect_year}-{random.randint(5, 6):02d}-15",
    }


def generate():
    if not PERSONS:
        from civil_registry import generate as gen_cr
        gen_cr()
    count = 0

    # Cast: completed doctorates at the university
    for key, field, enr_year, expect_year in (("elena", "Marine Biology", 2016, 2022), ("dr_reyes", "Medicine", 1998, 2004), ("dr_ferrer", "Public Health", 1994, 2000)):
        rec = _make_record(CAST[key], "doctorate", field, "Graduated", enr_year, expect_year, *UNIVERSITY)
        write_record(OUTPUT_DIR, "ed", build_instance(rec))
        count += 1

    # School-age residents and recent graduates from the background population
    eligible = [p for p in PERSONS if p.get("key", "").startswith("bg_") and 5 <= (2026 - int(p["dob"][:4])) <= 30]
    for p in eligible:
        age = 2026 - int(p["dob"][:4])
        if age <= 11:
            tier, enr_status, field = "primary", "Active", "General Education"
            city, province = _random_city_province()
            institution = f"Escuela Primaria {city}"
            enr_year = max(2020, 2026 - (age - 5)); expect_year = enr_year + 6
        elif age <= 17:
            tier = "secondary"
            city, province = _random_city_province()
            institution = random.choice([f"Liceo Nacional {city}", f"Colegio Tecnico {city}"])
            enr_status = random.choice(["Active", "Active", "Active", "On Leave"])
            field = random.choice(["General Studies", "Science Track", "Humanities Track", "Technical Track"])
            enr_year = max(2020, 2026 - (age - 12)); expect_year = enr_year + 6
        elif age <= 25:
            institution, city, province = UNIVERSITY
            tier = random.choice(["bachelor", "bachelor", "bachelor", "master"])
            enr_status = random.choice(["Active", "Active", "Active", "On Leave", "Graduated"])
            field = random.choice(FIELDS)
            enr_year = random.randint(2018, 2024); expect_year = enr_year + (4 if tier == "bachelor" else 2)
        else:
            institution, city, province = UNIVERSITY
            tier = random.choice(["bachelor", "master", "master"])
            enr_status, field = "Graduated", random.choice(FIELDS)
            enr_year = random.randint(2014, 2020); expect_year = enr_year + (4 if tier == "bachelor" else 2)
        rec = _make_record(p, tier, field, enr_status, enr_year, expect_year, institution, city, province)
        write_record(OUTPUT_DIR, "ed", build_instance(rec))
        count += 1

    print(f"Education Record: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    random.seed("cordovaos")
    from civil_registry import generate as gen_cr
    random.seed("cordovaos:Civil Registry"); gen_cr()
    random.seed("cordovaos:Education Record"); generate()
