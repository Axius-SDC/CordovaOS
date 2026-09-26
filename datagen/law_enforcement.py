"""
Law Enforcement Record 4.4.0: one record per incident.

The model composes the NIEM library's incident (with its arrest, charge,
disposition and location), Cordova's charge details in the kept COR units,
and a quarantine enforcement cluster whose court order is the NIEM one, with
Cordova's CID naming the involved resident so the incident is a join on the
CID component. Three Contagion quarantine beats + 5 routine incidents +
scaled(192, 38) background incidents.
"""
import random

from shared import (
    COR, PERSONS, Quantity, ALL_CITIES, CITY_TO_PROVINCE,
    random_address, random_date, full_name, record, write_record, import_dir,
)

TITLE = "Law Enforcement Record"
SYSTEM = "Cordova Police System"
OUTPUT_DIR = import_dir("law_enforcement_record")

# Cordova's Incident Status (Open / Closed / Pending) from the 4.3.1 statuses, and the act-lifecycle workflow state
# bound to the model: an open incident is an active act, a closed one is completed, a pending one is held.
STATUS_MAP = {"Active": "Open", "Under Investigation": "Pending", "Monitoring": "Pending", "Open": "Open", "Closed": "Closed", "Pending": "Pending"}
STATE_OF = {"Open": "active", "Closed": "completed", "Pending": "held"}
# NIEM Incident Status Code beside Cordova's coarse status.
NIEM_STATUS = {"Open": "OPEN", "Closed": "CLOSED", "Pending": "PENDING"}
# The 4.3.1 categories onto the NIEM UCR offense codes the model enumerates. Categories that are not offenses
# (a health order, a lost wallet, a welfare check) carry no UCR code; the NIEM Incident Category Code list is
# about drug and gang involvement, so it is "NONE" for every incident here.
UCR_MAP = {
    "Traffic": None, "Property Crime": "LARCENY", "Civil Disturbance": "DISORDERLY_CONDUCT", "Lost Property": None,
    "Trespass": "TRESPASSING", "Fraud": "FRAUD-FALSE_PRETENSES-SWINDLE-CONFIDENCE_GAME", "DUI": "DRIVING_UNDER_INFLUENCE",
    "Missing Person": None, "Animal Control": None, "Suspicious Activity": None, "Welfare Check": None, "Assault": "SIMPLE_ASSAULT",
    "Public Health Emergency": None, "Quarantine Enforcement": None, "Contact Tracing": None,
}
CHARGE_UCR = {"Traffic Violation": "ALL_OTHER_OFFENSES", "Petty Theft": "LARCENY", "Public Intoxication": "DRUNKENNESS",
              "Trespassing": "TRESPASSING", "Disorderly Conduct": "DISORDERLY_CONDUCT", "Minor Vandalism": "DAMAGE-DESTRUCTION-VANDALISM_OF_PROPERTY"}
CHARGE_CATS = list(CHARGE_UCR)
DISPOSITIONS = ["Fine", "Community Service", "Case Dismissed", "Pending"]
COMPLIANCE_MAP = {"Enforced": "Compliant", "Compliant": "Compliant", "Monitoring": "Under Review", "Violation": "Violation Detected"}

_inc_counter = 0


def next_inc():
    global _inc_counter
    _inc_counter += 1
    return f"IR-2026-{_inc_counter:04d}"


def build_instance(rec):
    """One Law Enforcement Record for one incident."""
    status = STATUS_MAP.get(rec.get("status", "Closed"), "Closed")
    subject = rec.get("subject")   # a resident dict from PERSONS, or None
    values = {
        "Incident Report/National ID (CID)": subject["cid"] if subject else None,
        "Incident Report/City": rec["city"],
        "Incident Report/Province": rec["province"],
        "Incident Report/Incident Status": status,
        "Incident/Activity Identification": rec["inc_num"],
        "Incident/Activity Description": rec["summary"],
        "Incident/Activity Date": rec["inc_date"],
        "Incident/Incident Reported Narrative": rec["summary"],
        "Incident/Incident General Category": rec["category"],
        "Incident/Incident Status Code": NIEM_STATUS[status],
        "Incident/Incident Category Code": "NONE",
        "Incident/Incident Category UCR Code": UCR_MAP.get(rec["category"]),
        "Incident/Incident Jurisdictional Organization Reference": f"urn:cordova:police:{rec['city'].lower().replace(' ', '-')}",
        "Incident/Incident Reporting Official Reference": f"urn:cordova:police:{rec['city'].lower().replace(' ', '-')}:duty-officer",
        "Incident/Incident Traffic Accident Involved Indicator": True if rec["category"] == "Traffic" and "accident" in rec["summary"].lower() else None,
        "Incident/Incident Arrest Made Indicator": "charge_cat" in rec,
        "Incident/Incident Criminal Indicator": bool(UCR_MAP.get(rec["category"])) or "charge_cat" in rec,
        "Incident/Incident Subject Reference": f"urn:cordova:cid:{subject['cid']}" if subject else None,
        "Incident/Location (NIEM)/Location Name": rec["location"],
        "Incident/Location (NIEM)/Address (NIEM)/Address Full": f"{rec['location']}, {rec['province']}, Republic of Cordova",
    }
    if "charge_cat" in rec:
        disposition = rec.get("disposition", "Pending")
        values.update({
            "Incident/Arrest/Activity Identification": f"{rec['inc_num']}-A1",
            "Incident/Arrest/Activity Date": rec["inc_date"],
            "Incident/Arrest/Arrest Category Code": "SUMMONED-CITED",
            "Incident/Arrest/Arrest Agency Reference": f"urn:cordova:police:{rec['city'].lower().replace(' ', '-')}",
            "Incident/Arrest/Arrest Subject Reference": f"urn:cordova:cid:{subject['cid']}" if subject else None,
            "Incident/Arrest/Charge/Charge Identification": f"{rec['inc_num']}-C1",
            "Incident/Arrest/Charge/Charge Description": rec.get("charge_desc", rec["summary"])[:200],
            "Incident/Arrest/Charge/Charge Category Description": rec["charge_cat"],
            "Incident/Arrest/Charge/Charge UCR Code": CHARGE_UCR[rec["charge_cat"]],
            "Incident/Arrest/Charge/Charge Filing Date": rec["inc_date"],
            "Incident/Arrest/Charge/Charge Felony Indicator": False,
            "Incident/Arrest/Charge/Disposition/Disposition Text": disposition,
            "Incident/Arrest/Charge/Disposition/Disposition Description": rec.get("charge_desc", rec["summary"])[:200],
            "Incident/Arrest/Charge/Disposition/Disposition Date": rec.get("disp_date", rec["inc_date"]) if disposition != "Pending" else None,
            "Charge Details (Cordova)/Fine or Bail Amount": Quantity(str(rec.get("fine", 0)), COR) if disposition == "Fine" else None,
            "Charge Details (Cordova)/Disposition Date": rec.get("disp_date", rec["inc_date"]) if disposition != "Pending" else None,
        })
    if "qz_zone" in rec:
        values.update({
            "Quarantine Enforcement/Issuing Authority": rec.get("qz_authority"),
            "Quarantine Enforcement/Quarantine Zone": rec["qz_zone"],
            "Quarantine Enforcement/Compliance Status": COMPLIANCE_MAP.get(rec.get("qz_compliance", "Compliant"), "Under Review"),
            "Quarantine Enforcement/Quarantine Start Date": rec.get("qz_start", "2026-01-01"),
            "Quarantine Enforcement/Quarantine End Date": rec.get("qz_end", "2026-12-31"),
            "Quarantine Enforcement/Court Order/Activity Identification": rec.get("qz_order", "Provincial Health Order 2026-003"),
            "Quarantine Enforcement/Court Order/Court Order Issuing Date": rec.get("qz_start", "2026-01-01"),
            "Quarantine Enforcement/Court Order/Court Order Status": "In force",
            "Quarantine Enforcement/Court Order/Court Order Request Entity Reference": "urn:cordova:org:" + rec.get("qz_authority", "provincial-health-office").lower().replace(" ", "-"),
            "Quarantine Enforcement/Court Order/Court Order Enforcement Agency Reference": f"urn:cordova:police:{rec['city'].lower().replace(' ', '-')}",
            "Quarantine Enforcement/Court Order/Court Order Designated Location Reference": "urn:cordova:zone:" + rec["qz_zone"].lower().replace(" ", "-"),
        })
    return record(TITLE, values, state=STATE_OF[status], system=SYSTEM, activity_type="IncidentRecording", when=rec["inc_date"],
                  city=rec["city"], province=rec["province"], cid=subject["cid"] if subject else None,
                  subject=("Involved Person", full_name(subject) if subject else "Unidentified Person"),
                  provider=("Reporting Officer", f"{rec['city']} Police Station"),
                  attestation_reason="Incident report filed and reviewed by station duty officer", committer="Reporting Officer")


def generate():
    count = 0

    # Contagion Beat 5: Quarantine enforcement at Porto Sereno port
    quarantine_records = [
        {
            "inc_num": next_inc(),
            "summary": "Quarantine zone established at Porto Sereno Commercial Terminal per Provincial Health Order 2026-003. All port workers and recent vessel contacts under mandatory 14-day quarantine.",
            "location": "Porto Sereno Commercial Terminal, Berth 7 and surrounding area",
            "city": "Porto Sereno", "province": "Aldara",
            "category": "Public Health Emergency",
            "inc_date": "2026-01-16", "status": "Active",
            "qz_authority": "Provincial Health Office - Aldara",
            "qz_zone": "Porto Sereno Commercial Terminal - 500m radius",
            "qz_compliance": "Enforced",
            "qz_start": "2026-01-16", "qz_end": "2026-01-30",
        },
        {
            "inc_num": next_inc(),
            "summary": "Quarantine compliance check - MV Estrella del Sur crew members. 18 crew accounted for, all confined to vessel.",
            "location": "MV Estrella del Sur, Berth 7",
            "city": "Porto Sereno", "province": "Aldara",
            "category": "Quarantine Enforcement",
            "inc_date": "2026-01-17", "status": "Active",
            "qz_authority": "Cordova National Police",
            "qz_zone": "Porto Sereno Commercial Terminal - Berth 7",
            "qz_compliance": "Compliant",
            "qz_start": "2026-01-16", "qz_end": "2026-01-30",
        },
        {
            "inc_num": next_inc(),
            "summary": "Contact tracing checkpoint established at UNC campus entrance. Students and faculty with Porto Sereno travel history screened.",
            "location": "Universidad Nacional de Cordova, Main Gate",
            "city": "Campoluz", "province": "Brevina",
            "category": "Contact Tracing",
            "inc_date": "2026-01-18", "status": "Active",
            "qz_authority": "Provincial Health Office - Brevina",
            "qz_zone": "UNC Campus - Contact Monitoring Zone",
            "qz_compliance": "Monitoring",
            "qz_start": "2026-01-18", "qz_end": "2026-02-01",
            "qz_order": "Provincial Health Order 2026-004",
        },
    ]
    for rec in quarantine_records:
        write_record(OUTPUT_DIR, "le", build_instance(rec))
        count += 1

    # Original 5 routine incidents
    routine_incidents = [
        ("Traffic accident - minor property damage", "Traffic", "Porto Sereno", "Aldara"),
        ("Petty theft reported at Central Market", "Property Crime", "Novaciudad", "Celara"),
        ("Noise complaint - residential area", "Civil Disturbance", "Campoluz", "Brevina"),
        ("Lost property report - wallet", "Lost Property", "Porto Sereno", "Aldara"),
        ("Trespassing at port restricted area", "Trespass", "Porto Sereno", "Aldara"),
    ]
    for summary, cat, city, prov in routine_incidents:
        rec = {"inc_num": next_inc(), "summary": summary, "location": random_address() + f", {city}",
               "city": city, "province": prov, "category": cat, "inc_date": random_date(2025, 2025)}
        write_record(OUTPUT_DIR, "le", build_instance(rec))
        count += 1

    # Background incidents with a charge: the charged resident is a registered person of the same city, by CID.
    if not PERSONS:
        from civil_registry import generate as gen_cr
        gen_cr()
    adults_by_city = {}
    for p in PERSONS:
        if p.get("key", "").startswith("bg_") and (2026 - int(p["dob"][:4])) >= 18:
            adults_by_city.setdefault(p["city"], []).append(p)

    incident_templates = [
        ("Traffic accident - minor property damage", "Traffic"),
        ("Traffic stop - expired registration", "Traffic"),
        ("Traffic stop - speeding violation", "Traffic"),
        ("Vehicle collision - no injuries", "Traffic"),
        ("Petty theft reported", "Property Crime"),
        ("Shoplifting incident", "Property Crime"),
        ("Bicycle theft reported", "Property Crime"),
        ("Burglary - residential break-in", "Property Crime"),
        ("Vandalism - graffiti on public building", "Property Crime"),
        ("Vandalism - broken storefront window", "Property Crime"),
        ("Noise complaint - loud music", "Civil Disturbance"),
        ("Noise complaint - construction hours violation", "Civil Disturbance"),
        ("Domestic disturbance call", "Civil Disturbance"),
        ("Public intoxication", "Civil Disturbance"),
        ("Street fight - minor altercation", "Civil Disturbance"),
        ("Lost property report", "Lost Property"),
        ("Found property - turned in to station", "Lost Property"),
        ("Trespassing on private property", "Trespass"),
        ("Fraud report - phone scam", "Fraud"),
        ("Fraud report - forged document", "Fraud"),
        ("DUI checkpoint - positive test", "DUI"),
        ("DUI - erratic driving reported", "DUI"),
        ("Missing person report - juvenile", "Missing Person"),
        ("Missing person report - located safe", "Missing Person"),
        ("Animal control - stray dog complaint", "Animal Control"),
        ("Suspicious activity report", "Suspicious Activity"),
        ("Welfare check requested", "Welfare Check"),
        ("Parking violation - fire lane", "Traffic"),
        ("Hit and run - minor damage", "Traffic"),
        ("Assault - simple battery", "Assault"),
    ]
    from shared import scaled
    for _ in range(scaled(192, 38)):
        summary_template, cat = random.choice(incident_templates)
        city = random.choice(ALL_CITIES)
        prov = CITY_TO_PROVINCE[city]
        rec = {
            "inc_num": next_inc(),
            "summary": f"{summary_template} at {random_address()}, {city}",
            "location": random_address() + f", {city}",
            "city": city, "province": prov, "category": cat,
            "inc_date": random_date(2025, 2025),
            "status": random.choice(["Closed", "Closed", "Closed", "Open", "Under Investigation"]),
            "charge_desc": summary_template,
            "charge_cat": random.choice(CHARGE_CATS),
            "disposition": random.choice(DISPOSITIONS),
            "fine": random.choice([50, 100, 200, 500]),
        }
        if adults_by_city.get(city):
            rec["subject"] = random.choice(adults_by_city[city])
        write_record(OUTPUT_DIR, "le", build_instance(rec))
        count += 1

    print(f"Law Enforcement: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    from civil_registry import generate as gen_cr
    random.seed("cordovaos:Civil Registry"); gen_cr()
    random.seed("cordovaos:Law Enforcement"); generate()
