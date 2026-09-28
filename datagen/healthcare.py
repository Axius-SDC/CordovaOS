"""
Healthcare Record 4.4.0: one record per encounter.

The model composes the FHIR library's patient, condition, allergy intolerance,
medication order, immunization, encounter and vital signs panel, each coded
value carried as the code system's code beside its display text (ICD-10-CM,
SNOMED CT, RxNorm, CVX), with Cordova's CID as the join to every other domain.

Carlos's Contagion visit, Elena's baseline, and background encounters (~5,000
full, 242 demo). Every 40th background record states an absence: the patient
reports a medication but cannot recall the dose, so the dose is ASKU, "Asked
but Unknown", and the instance is invalid on purpose.
"""
import random

from shared import (
    ASKU, CAST, PERSONS, COR, Quantity,
    random_date, full_name, record, write_record, import_dir,
)

TITLE = "Healthcare Record"
SYSTEM = "Cordova Healthcare System"
OUTPUT_DIR = import_dir("healthcare_record")

# ICD-10-CM diagnosis (code, display) and the SNOMED CT encounter reason that brought the patient in.
DIAGNOSES = {
    "Hypertension management": ("I10", "Essential (primary) hypertension", ("38341003", "Hypertensive disorder")),
    "Type 2 diabetes follow-up": ("E11.9", "Type 2 diabetes mellitus without complications", ("44054006", "Type 2 diabetes mellitus")),
    "Upper respiratory infection": ("J06.9", "Acute upper respiratory infection, unspecified", ("54150009", "Upper respiratory infection")),
    "Minor laceration - sutured": ("S01.01XA", "Laceration without foreign body of scalp, initial encounter", ("312608009", "Laceration - injury")),
    "Annual physical": ("Z00.00", "Encounter for general adult medical examination without abnormal findings", ("185349003", "Encounter for check up")),
    "Back pain": ("M54.50", "Low back pain, unspecified", ("279039007", "Low back pain")),
    "Gastroenteritis": ("A09", "Infectious gastroenteritis and colitis, unspecified", ("25374005", "Gastroenteritis")),
    "Mild allergic reaction": ("T78.40XA", "Allergy, unspecified, initial encounter", ("419076005", "Allergic reaction")),
    "Ankle sprain": ("S93.409A", "Sprain of unspecified ligament of unspecified ankle, initial encounter", ("44465007", "Sprain of ankle")),
    "Migraine": ("G43.909", "Migraine, unspecified, not intractable, without status migrainosus", ("37796009", "Migraine")),
    "Asthma exacerbation": ("J45.901", "Unspecified asthma with (acute) exacerbation", ("195967001", "Asthma")),
    "Urinary tract infection": ("N39.0", "Urinary tract infection, site not specified", ("68566005", "Urinary tract infectious disease")),
    "Otitis media": ("H66.90", "Otitis media, unspecified, unspecified ear", ("65363002", "Otitis media")),
    "Conjunctivitis": ("H10.9", "Unspecified conjunctivitis", ("9826008", "Conjunctivitis")),
    "Dermatitis": ("L30.9", "Dermatitis, unspecified", ("182782007", "Dermatitis")),
    "Fracture - closed reduction": ("S52.501A", "Unspecified fracture of the lower end of right radius, initial encounter for closed fracture", ("125605004", "Fracture of bone")),
    "Dental abscess referral": ("K04.7", "Periapical abscess without sinus", ("109713004", "Dental abscess")),
    "Prenatal checkup": ("Z34.90", "Encounter for supervision of normal pregnancy, unspecified, unspecified trimester", ("424441002", "Prenatal initial visit")),
    "Well-child visit": ("Z00.129", "Encounter for routine child health examination without abnormal findings", ("410620009", "Well child visit")),
    "Chronic pain management": ("G89.29", "Other chronic pain", ("82423001", "Chronic pain")),
    "Anxiety disorder follow-up": ("F41.9", "Anxiety disorder, unspecified", ("197480006", "Anxiety disorder")),
    "Iron deficiency anemia": ("D50.9", "Iron deficiency anemia, unspecified", ("87522002", "Iron deficiency anemia")),
    "Bronchitis": ("J40", "Bronchitis, not specified as acute or chronic", ("32398004", "Bronchitis")),
    "Sinusitis": ("J01.90", "Acute sinusitis, unspecified", ("36971009", "Sinusitis")),
    "Knee injury": ("S80.91XA", "Unspecified superficial injury of right knee, initial encounter", ("125606003", "Knee injury")),
    "Shoulder strain": ("S46.011A", "Strain of muscle(s) and tendon(s) of the rotator cuff of right shoulder, initial encounter", ("45326000", "Shoulder strain")),
    "Insect bite reaction": ("T63.481A", "Toxic effect of venom of other arthropod, accidental, initial encounter", ("276164006", "Insect bite")),
    "Food poisoning": ("A05.9", "Bacterial foodborne intoxication, unspecified", ("75258005", "Food poisoning")),
    "Dehydration - mild": ("E86.0", "Dehydration", ("34095006", "Dehydration")),
    "Vaccination visit": ("Z23", "Encounter for immunization", ("33879002", "Administration of vaccine to produce active immunity")),
}
SEVERITY = {"mild": ("255604002", "Mild"), "moderate": ("6736007", "Moderate"), "severe": ("24484000", "Severe")}
ALLERGENS = [("764146007", "Penicillin", "medication"), ("256349002", "Peanut", "food"), ("111088007", "Latex", "environment")]
MEDICATIONS = {"Metformin": ("6809", "metformin"), "Amlodipine": ("17767", "amlodipine"), "Levothyroxine": ("10582", "levothyroxine"), "Oseltamivir": ("260101", "oseltamivir")}
FLU_VACCINE = ("141", "Influenza, seasonal, injectable")
CHILD_DIAGNOSES = ["Well-child visit", "Otitis media", "Vaccination visit", "Upper respiratory infection", "Dermatitis", "Asthma exacerbation"]
ELDER_DIAGNOSES = ["Hypertension management", "Type 2 diabetes follow-up", "Chronic pain management", "Annual physical", "Back pain", "Dehydration - mild"]
FACILITIES = ["Porto Sereno General Hospital", "Campoluz Medical Clinic", "Novaciudad Central Hospital", "Montecara Community Clinic", "Vistamar Health Post",
              "Tierraverde Rural Clinic", "Piedrasol Medical Center", "Lagunavista Health Post", "Rioseco Rural Clinic"]
FACILITY_CITY = {f: f.split(" Health")[0].split(" Medical")[0].split(" General")[0].split(" Central")[0].split(" Community")[0].split(" Rural")[0] for f in FACILITIES}
MARITAL = {"Single": "S", "Married": "M", "Divorced": "D", "Widowed": "W"}
EV_DEMO_EVERY = 40   # one in this many background records carries the deliberate Exceptional Value

_mrn_counter = 0


def next_mrn():
    global _mrn_counter
    _mrn_counter += 1
    return f"MRN-{_mrn_counter:06d}"


def build_instance(rec):
    """One Healthcare Record: the patient, the encounter, its diagnosis and vital signs, and what else the visit recorded."""
    p = rec["person"]
    code, display, reason = DIAGNOSES[rec["diagnosis"]]
    start = rec["visit_start"]
    values = {
        "Patient Record/National ID (CID)": p["cid"],
        "Patient/Medical Record Number": rec["mrn"],
        "Patient/Marital Status": MARITAL.get(p.get("marital_status", "Single"), "U"),
        "Patient/Person (Demographics)/Full Name (Person)/Given Name (Person)": p["given"],
        "Patient/Person (Demographics)/Full Name (Person)/Surname (Person)": p["surname"],
        "Patient/Person (Demographics)/Administrative Gender": p["sex"].lower(),
        "Patient/Person (Demographics)/Date of Birth": p["dob"],
        "Patient/Managing Organization Reference": f"urn:cordova:facility:{rec['facility'].lower().replace(' ', '-')}",
        "Condition/Diagnosis (ICD-10-CM)/Diagnosis Code (ICD-10-CM)": code,
        "Condition/Diagnosis (ICD-10-CM)/Code Display Text": display,
        "Condition/Condition Category": "encounter-diagnosis",
        "Condition/Condition Clinical Status": rec.get("clinical_status", "active"),
        "Condition/Condition Verification Status": rec.get("verification", "confirmed"),
        "Condition/Onset Date": rec.get("onset") or None,
        "Condition/Condition Severity (SNOMED CT)/Condition Severity Code (SNOMED CT)": SEVERITY[rec["severity"]][0],
        "Condition/Condition Severity (SNOMED CT)/Code Display Text": SEVERITY[rec["severity"]][1],
        "Encounter/Encounter Class": rec.get("encounter_class", "AMB"),
        "Encounter/Encounter Status": rec["state"],
        "Encounter/Encounter Priority": rec.get("priority", "R"),
        "Encounter/Encounter Reason (SNOMED CT)/Encounter Reason Code (SNOMED CT)": reason[0],
        "Encounter/Encounter Reason (SNOMED CT)/Code Display Text": reason[1],
        "Encounter/Encounter Start": start,
        "Encounter/Encounter End": rec.get("visit_end") or None,
        "Vital Signs Panel/Observation Status": "final",
        "Vital Signs Panel/Observation Date Time": start,
        "Vital Signs Panel/Body Temperature": Quantity(rec["temp"], "°C"),
        "Vital Signs Panel/Body Height": Quantity(rec["height"], "cm"),
        "Vital Signs Panel/Body Weight": Quantity(rec["weight"], "kg"),
        "Vital Signs Panel/Heart Rate": Quantity(rec["pulse"], "/min"),
        "Vital Signs Panel/Respiratory Rate": Quantity(rec["resp"], "/min"),
        "Vital Signs Panel/Oxygen Saturation": Quantity(rec["spo2"], "%"),
        "Blood Pressure/Systolic Blood Pressure": Quantity(rec["bp_sys"], "mmHg"),
        "Blood Pressure/Diastolic Blood Pressure": Quantity(rec["bp_dias"], "mmHg"),
        "Blood Pressure/Observation Status": "final",
        "Blood Pressure/Observation Date Time": start,
    }
    if rec.get("medication"):
        rx_code, rx_display = MEDICATIONS[rec["medication"]]
        values.update({
            "Medication Order/Medication (RxNorm)/Medication Code (RxNorm)": rx_code,
            "Medication Order/Medication (RxNorm)/Code Display Text": rx_display,
            "Medication Order/Medication Request Status": "active",
            "Medication Order/Medication Request Intent": "order",
            "Medication Order/Dose Quantity": rec["dose"],   # a Quantity, or ASKU when the patient cannot recall it
            "Medication Order/Dose Frequency": rec.get("frequency", "BID"),
            "Medication Order/Prescription Date": rec.get("rx_date") or start,
            "Medication Order/Prescriber Reference": f"urn:cordova:practitioner:{rec['facility'].lower().replace(' ', '-')}",
        })
    if rec.get("vaccine"):
        values.update({
            "Immunization/Vaccine (CVX)/Vaccine Code (CVX)": FLU_VACCINE[0],
            "Immunization/Vaccine (CVX)/Code Display Text": FLU_VACCINE[1],
            "Immunization/Immunization Status": "completed",
            "Immunization/Vaccination Date": rec["vaccine"]["date"],
            "Immunization/Vaccine Lot Number": rec["vaccine"]["lot"],
        })
    if rec.get("allergy"):
        a_code, a_display, a_category = rec["allergy"]
        values.update({
            "Allergy Intolerance/Allergen (SNOMED CT)/Allergen Code (SNOMED CT)": a_code,
            "Allergy Intolerance/Allergen (SNOMED CT)/Code Display Text": a_display,
            "Allergy Intolerance/Allergy Category": a_category,
            "Allergy Intolerance/Allergy Type": "allergy",
            "Allergy Intolerance/Allergy Clinical Status": "active",
            "Allergy Intolerance/Allergy Verification Status": "confirmed",
            "Allergy Intolerance/Allergy Criticality": "low",
        })
    if rec.get("admitted"):
        values["Encounter/Hospitalization/Discharge Disposition"] = rec["admitted"]
    city = FACILITY_CITY[rec["facility"]]
    return record(TITLE, values, state=rec["state"], system=SYSTEM, activity_type="PatientEncounter", when=start, city=city,
                  province=rec["province"], cid=p["cid"], subject=("Patient", full_name(p)), provider=("Healthcare Provider", rec["facility"]),
                  attestation_reason="Encounter documented by the attending clinician", committer=rec["facility"])


def _vitals(age):
    if age < 12:
        height, weight = random.randint(80, 155), random.randint(15, 50)
    elif age > 60:
        height, weight = random.randint(150, 185), random.randint(55, 100)
    else:
        height, weight = random.randint(155, 195), random.randint(50, 110)
    return {"temp": f"{random.uniform(36.0, 37.8):.1f}", "bp_sys": str(random.randint(100, 155)), "bp_dias": str(random.randint(60, 100)),
            "pulse": str(random.randint(55, 100)), "resp": str(random.randint(12, 20)), "spo2": str(random.randint(94, 100)),
            "height": str(height), "weight": str(weight)}


def generate():
    from shared import CITY_TO_PROVINCE
    count = 0

    # Carlos, the Contagion presentation (beat 1): febrile respiratory illness after maritime travel, admitted; the influenza
    # diagnosis is provisional, which is what the FHIR verification status is for.
    carlos = CAST["carlos"]
    rec = {
        "person": carlos, "mrn": next_mrn(), "facility": "Porto Sereno General Hospital", "province": "Aldara",
        "diagnosis": "Upper respiratory infection", "severity": "severe", "verification": "provisional", "clinical_status": "active",
        "onset": "2026-01-12T00:00:00", "visit_start": "2026-01-14T09:30:00", "state": "in-progress", "encounter_class": "EMER", "priority": "EM",
        "admitted": None, "medication": "Oseltamivir", "dose": Quantity("75", "mg"), "frequency": "BID", "rx_date": "2026-01-14T11:00:00",
        "vaccine": {"date": "2025-10-15T10:00:00", "lot": "FLU-2025-4821"},
        "temp": "39.2", "bp_sys": "128", "bp_dias": "82", "pulse": "104", "resp": "24", "spo2": "93", "height": "178", "weight": "82",
    }
    rec["diagnosis"] = "Upper respiratory infection"
    write_record(OUTPUT_DIR, "hc", build_instance(rec))
    count += 1

    # Elena, a baseline visit with nothing found.
    elena = CAST["elena"]
    rec = {
        "person": elena, "mrn": next_mrn(), "facility": "Novaciudad Central Hospital", "province": "Celara",
        "diagnosis": "Annual physical", "severity": "mild", "clinical_status": "resolved",
        "visit_start": "2025-11-20T09:00:00", "visit_end": "2025-11-20T09:40:00", "state": "finished",
        "temp": "36.6", "bp_sys": "118", "bp_dias": "76", "pulse": "68", "resp": "14", "spo2": "99", "height": "165", "weight": "62",
    }
    write_record(OUTPUT_DIR, "hc", build_instance(rec))
    count += 1

    # Background encounters: about a fifth of the population.
    if not PERSONS:
        from civil_registry import generate as gen_cr
        gen_cr()
    bg = [p for p in PERSONS if p.get("key", "").startswith("bg_")]
    patients = random.sample(bg, k=min(len(bg), 5000))
    for idx, p in enumerate(patients):
        age = 2026 - int(p["dob"][:4])
        diag = random.choice(CHILD_DIAGNOSES if age < 12 else ELDER_DIAGNOSES if age > 60 else list(DIAGNOSES))
        facility = random.choice(FACILITIES)
        day = random_date(2024, 2025)
        hour = random.randint(8, 17)
        rec = {
            "person": p, "mrn": next_mrn(), "facility": facility, "province": CITY_TO_PROVINCE[FACILITY_CITY[facility]],
            "diagnosis": diag, "severity": random.choice(["mild", "mild", "moderate", "severe"]),
            "clinical_status": random.choice(["active", "resolved", "inactive"]),
            "visit_start": f"{day}T{hour:02d}:00:00", "visit_end": f"{day}T{hour:02d}:{random.choice(['20', '30', '45'])}:00",
            "state": random.choice(["finished"] * 6 + ["in-progress", "arrived"]),
            **_vitals(age),
        }
        if diag == "Vaccination visit":
            rec["vaccine"] = {"date": rec["visit_start"], "lot": f"FLU-{day[:4]}-{random.randint(1000, 9999)}"}
        if random.random() < 0.08:
            rec["allergy"] = random.choice(ALLERGENS)
        # A deliberate Exceptional Value, on a fixed cadence so the set is reproducible: the patient reports a
        # medication but cannot recall the dose. The dose is written as ASKU rather than a made-up number, the
        # value element is mandatory, so the instance fails validation, and the Exceptional Value records why.
        if idx % EV_DEMO_EVERY == 0:
            rec["medication"] = random.choice(["Metformin", "Amlodipine", "Levothyroxine"])
            rec["dose"] = ASKU
            rec["frequency"] = "QD"
        write_record(OUTPUT_DIR, "hc", build_instance(rec))
        count += 1
    print(f"Healthcare Record: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    random.seed("cordovaos")
    from civil_registry import generate as gen_cr
    random.seed("cordovaos:Civil Registry"); gen_cr()
    random.seed("cordovaos:Healthcare"); generate()
