"""
Vital Statistics Record 4.4.0: one record per vital event.

The model composes Cordova's vital event (certificate, event type, status, dates,
city, province) with one sub-record per event type: birth, death, marriage and
divorce, each naming the person by the Cordova CID and the NIEM person name
composed from the Default library's full name. A death carries its cause as an
ICD-10-CM coded value from the FHIR library, so cause of death is a code beside
its display text rather than free text.

Birth certificates for every resident, marriages for the married cast and up to
500 background couples, and up to 200 deaths among elders.
"""
import random

from shared import (
    CAST, PERSONS, random_date, full_name,
    record, write_record, import_dir,
)

TITLE = "Vital Statistics Record"
SYSTEM = "Cordova Vital Statistics System"
OUTPUT_DIR = import_dir("vital_statistics_record")

# The document-publishing workflow the model binds: a certificate on file is the version of
# record; an amended one has been revised. (4.3.1 carried "Active" / "Amended" as its states.)
STATE_OF_STATUS = {"Active": "version-of-record", "Amended": "revised", "Voided": "withdrawn-from-submission"}
MANNERS = ["Natural", "Accident", "Undetermined"]
PLACES = ["Hospital", "Residence", "Other"]
# Cause of death as ICD-10-CM: (code, display text).
CAUSES = [
    ("I25.10", "Atherosclerotic heart disease of native coronary artery without angina pectoris"),
    ("J96.00", "Acute respiratory failure, unspecified whether with hypoxia or hypercapnia"),
    ("I63.9", "Cerebral infarction, unspecified"),
    ("C80.1", "Malignant (primary) neoplasm, unspecified"),
    ("A41.9", "Sepsis, unspecified organism"),
    ("N19", "Unspecified kidney failure"),
    ("T14.91XA", "Suicide attempt, initial encounter"),
]
ACTIVITY = {"Birth": "BirthRegistration", "Death": "DeathRegistration", "Marriage": "MarriageRegistration", "Divorce": "DivorceRegistration"}

_cert_counter = 0


def next_cert():
    global _cert_counter
    _cert_counter += 1
    return f"VS-{_cert_counter:06d}"


def _person_values(sub, person):
    """The person a sub-record is about: the CID join and the NIEM person name."""
    return {
        f"{sub}/National ID (CID)": person["cid"],
        f"{sub}/Person Name (NIEM)/Full Name (Person)/Given Name (Person)": person["given"],
        f"{sub}/Person Name (NIEM)/Full Name (Person)/Middle Name (Person)": person.get("middle") or None,
        f"{sub}/Person Name (NIEM)/Full Name (Person)/Surname (Person)": person["surname"],
        f"{sub}/Person Name (NIEM)/Full Name (Person)/Name Use": "official",
    }


def build_instance(rec):
    """One Vital Statistics record for one event.

    rec: event_type (Birth | Death | Marriage | Divorce), person, city, province, event_date, reg_date,
    cert_num, status; a death adds cause (code, display), manner, place; a divorce adds marriage_cert, decree_date;
    a marriage adds marriage_cert.
    """
    event_type = rec["event_type"]
    person = rec["person"]
    values = {
        "Vital Event/Certificate Number": rec["cert_num"],
        "Vital Event/Event Type": event_type,
        "Vital Event/Record Status": rec["status"],
        "Vital Event/Event Date": rec["event_date"],
        "Vital Event/Registration Date": rec["reg_date"],
        "Vital Event/City": rec["city"],
        "Vital Event/Province": rec["province"],
    }
    if event_type == "Birth":
        values.update(_person_values("Birth Record", person))
        values.update({
            "Birth Record/Date of Birth": person["dob"],
            "Birth Record/Sex (Recorded)": person["sex"].lower(),
            "Birth Record/Birth Facility": rec["facility"],
        })
    elif event_type == "Death":
        code, display = rec["cause"]
        values.update(_person_values("Death Record", person))
        values.update({
            "Death Record/Diagnosis (ICD-10-CM)/Diagnosis Code (ICD-10-CM)": code,
            "Death Record/Diagnosis (ICD-10-CM)/Code Display Text": display,
            "Death Record/Manner of Death": rec["manner"],
            "Death Record/Place of Death": rec["place"],
            "Death Record/Person Death Date": rec["event_date"],
        })
    elif event_type == "Marriage":
        values.update(_person_values("Marriage Record", person))
        values.update({
            "Marriage Record/Marriage Certificate Number": rec["marriage_cert"],
            "Marriage Record/Officiant Title": rec["officiant"],
        })
    else:
        values.update(_person_values("Divorce Record", person))
        values.update({
            "Divorce Record/Marriage Certificate Number": rec["marriage_cert"],
            "Divorce Record/Decree Date": rec["decree_date"],
        })
    return record(TITLE, values, state=STATE_OF_STATUS[rec["status"]], system=SYSTEM, activity_type=ACTIVITY[event_type],
                  when=rec["reg_date"], city=rec["city"], province=rec["province"], cid=person["cid"],
                  subject=("Subject Person", full_name(person)), provider=("Vital Statistics Office", f"{rec['city']} Vital Statistics Office"),
                  attestation_reason=f"{event_type} record certified by the vital statistics office", committer="Vital Statistics Office")


def _status():
    return random.choice(["Active"] * 9 + ["Amended"])


def make_birth_record(person):
    return {
        "event_type": "Birth", "person": person, "city": person["city"], "province": person["province"],
        "event_date": person["dob"], "reg_date": person["dob"], "cert_num": next_cert(), "status": _status(),
        "facility": random.choice([f"{person['city']} General Hospital", f"{person['city']} Maternity Clinic", "Home birth"]),
    }


def make_marriage_record(person, marriage_date, city, province):
    return {
        "event_type": "Marriage", "person": person, "city": city, "province": province,
        "event_date": marriage_date, "reg_date": marriage_date, "cert_num": next_cert(), "status": _status(),
        "marriage_cert": f"MC-{marriage_date[:4]}-{random.randint(1, 9999):04d}",
        "officiant": random.choice(["Civil Registrar", "Justice of the Peace", "Municipal Judge"]),
    }


def make_death_record(person, death_date):
    return {
        "event_type": "Death", "person": person, "city": person["city"], "province": person["province"],
        "event_date": death_date, "reg_date": death_date, "cert_num": next_cert(), "status": _status(),
        "cause": random.choice(CAUSES), "manner": random.choice(MANNERS), "place": random.choice(PLACES),
    }


def generate():
    """Generate all Vital Statistics records."""
    if not PERSONS:
        from civil_registry import generate as gen_cr
        gen_cr()
    count = 0

    # Birth certificates for every resident
    for person in PERSONS:
        write_record(OUTPUT_DIR, "vs", build_instance(make_birth_record(person)))
        count += 1

    # Marriage certificates for the married cast
    for key, c in CAST.items():
        if c.get("marital_status") == "Married":
            write_record(OUTPUT_DIR, "vs", build_instance(make_marriage_record(dict(c), random_date(2000, 2015), c["city"], c["province"])))
            count += 1

    # Background marriages: married adults paired up, up to 500 couples
    adults = [p for p in PERSONS if p.get("key", "").startswith("bg_") and (2026 - int(p["dob"][:4])) >= 18 and p.get("marital_status") == "Married"]
    random.shuffle(adults)
    for i in range(min(len(adults) // 2, 500)):
        p1 = adults[i * 2]
        write_record(OUTPUT_DIR, "vs", build_instance(make_marriage_record(p1, random_date(2005, 2024), p1["city"], p1["province"])))
        count += 1

    # A small number of deaths among older adults
    elders = [p for p in PERSONS if p.get("key", "").startswith("bg_") and (2026 - int(p["dob"][:4])) >= 70]
    random.shuffle(elders)
    for p in elders[:200]:
        write_record(OUTPUT_DIR, "vs", build_instance(make_death_record(p, random_date(2020, 2025))))
        count += 1

    print(f"Vital Statistics: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    random.seed("cordovaos")
    from civil_registry import generate as gen_cr
    random.seed("cordovaos:Civil Registry"); gen_cr()
    random.seed("cordovaos:Vital Statistics"); generate()
