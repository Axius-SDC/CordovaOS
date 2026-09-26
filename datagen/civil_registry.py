"""
Civil Registry 4.4.0: one record per resident.

The model composes the Default library's person demographics and name, the FHIR
contact point, Cordova's own address, identifier and administrative codes, and a
family relationship that names the related person by their CID, so the household
is a join on the CID component rather than a free-text relationship. 8 Contagion
cast members + background residents (24,992 full, 242 demo).
"""
import random

from shared import (
    CAST, PERSONS, AGE_DISTRIBUTION, CITY_TO_PROVINCE,
    scaled, random_name, random_city_province, random_address, random_dob,
    generate_cid_for_city, generate_phone, generate_email, full_name,
    record, write_record, import_dir,
)

TITLE = "Civil Registry"
SYSTEM = "Cordova Civil Registry System"
OUTPUT_DIR = import_dir("civil_registry")

# Marital status is the FHIR v3 code the library enumerates; Cordova's four words map onto it.
MARITAL = {"Single": "S", "Married": "M", "Divorced": "D", "Widowed": "W"}
CONTACT_METHOD = {"Phone": "phone", "Email": "email", "Mail": "other"}
# The activity-lifecycle workflow: a registration is complete, or still being verified.
STATES = ["ActivityCompleted"] * 8 + ["ActivityOngoing"]


def build_instance(person):
    """One Civil Registry record for one resident."""
    rel = person.get("relative")   # (relationship code, related person's CID, since) or None
    values = {
        "Civil Registry Record/National ID (CID)": person["cid"],
        "Civil Registry Record/Person Gender Identity Code": person["gender"],
        "Civil Registry Record/Marital Status": MARITAL[person["marital_status"]],
        "Full Name (Person)/Given Name (Person)": person["given"],
        "Full Name (Person)/Middle Name (Person)": person.get("middle") or None,
        "Full Name (Person)/Surname (Person)": person["surname"],
        "Full Name (Person)/Name Use": "official",
        "Person (Demographics)/Administrative Gender": person["sex"].lower(),
        "Person (Demographics)/Date of Birth": person["dob"],
        "Person (Demographics)/Language Code": "es",
        "Address (Cordova)/Address (Line 1)": person["address"],
        "Address (Cordova)/Address (Line 2)": person.get("address2") or None,
        "Address (Cordova)/City": person["city"],
        "Address (Cordova)/Province": person["province"],
        "Contact Point/Phone Number": person["phone"],
        "Contact Point/Email Address": person["email"],
        "Contact Point/Contact Method": CONTACT_METHOD[person["contact_pref"]],
        "Contact Point/Contact Use": "home",
    }
    if rel:
        code, related_cid, since = rel
        values.update({
            "Family Relationship/Relationship to Subject": code,
            "Family Relationship/National ID (CID)": related_cid,
            "Family Relationship/Date Range/Date Range Start": since,
        })
    return record(TITLE, values, state=random.choice(STATES), system=SYSTEM, activity_type="RecordRegistration",
                  when=person["registered"], city=person["city"], province=person["province"], cid=person["cid"],
                  subject=("Subject Person", full_name(person)), provider=("Civil Registry Office", f"{person['city']} Civil Registry Office"),
                  attestation_reason="Record verified by the civil registry office", committer="Civil Registry Office")


def make_cast_persons():
    """The Contagion cast as residents. Carlos and Elena are siblings; the household join is their CIDs."""
    persons = []
    for key, c in CAST.items():
        p = dict(c)
        p["key"] = key
        p["registered"] = p["dob"]
        persons.append(p)
    by_key = {p["key"]: p for p in persons}
    by_key["carlos"]["relative"] = ("SIB", by_key["elena"]["cid"], by_key["elena"]["dob"])
    by_key["elena"]["relative"] = ("SIB", by_key["carlos"]["cid"], by_key["elena"]["dob"])
    return persons


def make_background_persons(count):
    """Background residents spread across the nine cities; married adults are paired within a city."""
    persons = []
    for i in range(count):
        sex = random.choice(["Male", "Female"])
        given, middle, surname = random_name(sex)
        city, province = random_city_province()
        dob = random_dob(distribution=AGE_DISTRIBUTION)
        age = 2026 - int(dob[:4])
        marital = "Single" if age < 18 else random.choice(["Single", "Married", "Divorced", "Widowed"])
        persons.append({
            "key": f"bg_{i:05d}", "cid": generate_cid_for_city(city),
            "given": given, "middle": middle, "surname": surname,
            "sex": sex, "gender": sex, "dob": dob, "registered": dob,
            "city": city, "province": province,
            "address": random_address(), "address2": random.choice(["", "", "", f"Apt {random.randint(1, 50)}", f"Unit {random.randint(1, 20)}"]),
            "marital_status": marital,
            "phone": generate_phone(city), "email": generate_email(given, surname),
            "contact_pref": random.choice(["Phone", "Email", "Mail"]),
        })
    # spouses: married adults of a city, paired in order; an unpaired one keeps the status with no relative on file
    for city in CITY_TO_PROVINCE:
        married = [p for p in persons if p["city"] == city and p["marital_status"] == "Married"]
        for a, b in zip(married[0::2], married[1::2]):
            since = max(a["dob"], b["dob"])[:4]
            since = f"{int(since) + random.randint(20, 35)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
            since = min(since, "2025-12-31")
            a["relative"] = ("SPS", b["cid"], since)
            b["relative"] = ("SPS", a["cid"], since)
    return persons


def generate():
    """Generate all Civil Registry records and publish the residents to PERSONS for the other domains."""
    cast_persons = make_cast_persons()
    bg_persons = make_background_persons(scaled(24992, 242))
    all_persons = cast_persons + bg_persons
    PERSONS.clear()
    PERSONS.extend(all_persons)
    count = 0
    for person in all_persons:
        write_record(OUTPUT_DIR, "cr", build_instance(person))
        count += 1
    print(f"Civil Registry: generated {count} XML files in {OUTPUT_DIR}")
    return all_persons


if __name__ == "__main__":
    random.seed("cordovaos:Civil Registry")
    generate()
