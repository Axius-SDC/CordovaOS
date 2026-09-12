"""
Generate Law Enforcement Record XML instances for CordovaOS demo.

Governance-composed model: Governed Record (Incident Report data cluster +
Provenance Components) then native subject/provider, Audit and attestation.

Quarantine enforcement from the Contagion narrative + routine incidents.
Output: import_data/law_enforcement_record/
"""
import os
import random

from shared import (
    OMIT,
    scaled,
    random_address, random_date, ALL_CITIES, CITY_TO_PROVINCE,
    xml_header, xml_preamble, xml_footer, write_xml,
    xdstring, xdtoken, xdtemporal, xdquantity,
    cluster_open, cluster_close, native_partytype,
    make_provenance_values, audit, attestation,
    cuid_generator,
)

CT_ID = "yh0opq0bnu6y9y56oukg92uf"
DM_LABEL = "Law Enforcement Record"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "sdc4", "import_data", "law_enforcement_record")

# ─── Governance envelope (adapters re-keyed for v2) ──────────────────────────
GOVERNED_RECORD = "ms-kcam9lm7091vqtvb253ixjxr"   # Item: Law Enforcement Governed Record
CL_ROOT         = "ms-songhwxr1fp8niqba4fd0yd9"   # data cluster: Incident Report
CL_PROV         = "ms-hdhjfg00tngir2txgqyka9cv"   # Provenance Components

SYSTEM_AUDIT_ID = "ms-fotc5adg15ek2b9ermx2mcih"   # substitutionGroup="sdc4:Audit"

# ─── Incident Report scalar adapters (leaf, adapter) ─────────────────────────
W_INC_NUM     = ("ms-yi2189u4pinqitlmm5t6ccrd", "ms-az983a35e58cukvslxligqjr")
W_SUMMARY     = ("ms-rguhpkd7s2d9a51392aon7ir", "ms-u3kvtw5ejhoqk63fai5b7xnb")
W_LOCATION    = ("ms-b6nahtg2we4rh5qsk2j7qfvz", "ms-o27nnspq7e8un86jxvz0ag88")
W_CITY        = ("ms-atdtdfzruh7tya0iv5cz365l", "ms-jthcb1tovzlllactd1ohpvdc")
W_INC_STATUS  = ("ms-e83h36jqgi59dhy1dttp22qm", "ms-hm1gwdyk2gvrt79x5l37vlb6")
W_PROVINCE    = ("ms-kv5qqs3o4jwcwz9javgw1pzh", "ms-wy0j5q9i656h90lir07pgacq")
W_INC_CAT     = ("ms-nc7aq6ofnccavkmczsb2dudy", "ms-yr8yxumfg98ryudcytcmw6ep")
W_INC_DATE    = ("ms-ohk2uwcomsz8wegfvz0v0yod", "ms-eh937af6mvmnoc7d4fce756m")

# ─── Charge and Disposition cluster ──────────────────────────────────────────
CL_CHARGE     = "ms-c3eoo0vfid9c8riruf7uoyz2"
W_CHARGE_DESC = ("ms-eoqim4xj9gsxtxrqko1hh55o", "ms-v3ff1ydvzde3lp80jkszoh8x")
W_CHARGE_CAT  = ("ms-hc91pdnj3bb6997l5z4ndchz", "ms-y1c1x7fxqnkf8edoolcsmr6v")
W_DISPOSITION = ("ms-rnje7nq6m08vh01g8eg23say", "ms-bk9riq95cv32w7opvh084kxo")
W_FINE_AMT    = ("ms-yahksk4xc5to981ows7bpp6z", "ms-lxfwjedo8p9369xcedmzg3ch")
W_DISP_DATE   = ("ms-qse1jwofk5lm2wnsrn3f06l0", "ms-f6a0jvg7jxvpj56al42uv5a6")
W_FILING_DATE = ("ms-l0esdclu01pg7qw429oe7kjk", "ms-w9y98yuptbyypnu4vxtg5wl0")

# ─── Quarantine Enforcement cluster ──────────────────────────────────────────
CL_QUARANTINE = "ms-avmmc3r38dol0ghko42yeyp4"
W_ISSUING     = ("ms-ixmedhicidzpi7g6g2huqzvv", "ms-vd7vjy30xwfuispyxa2e14gz")
W_QZ_ZONE     = ("ms-r34gm210y9jifbyxa0fcxy96", "ms-kuikghw52vsz51wyan8gtp60")
W_COMPLIANCE  = ("ms-ihoatduhb7fckjw0ezq5u7g1", "ms-j1lr73r3x2x8a20jfminwc7t")
W_QZ_END      = ("ms-lohvu07ok3c3xvesa16htf2m", "ms-rjevh6x8rhbl4qwgcghp9d1w")
W_QZ_START    = ("ms-vq30hd0dl6v59d3ttyyvg6rp", "ms-k76ev49xpsuisdez3l7ptpat")

# ─── Provenance Components leaves (leaf, adapter) ─────────────────────────────
P_ACT_DESC    = ("ms-m9xg6e182m1oq77ssrf9iujv", "ms-esulunekv30i422gyljz9dnm")
P_ACT_TYPE    = ("ms-ccj1yq2wtwknobszkgzzdbtr", "ms-hd1oyvkmpzh9h2gp5b3sgpft")
P_SYS_ID      = ("ms-bd3s8t23d6m3zizmpwavc32y", "ms-fft8d7a2ldo4sg8ljbqmrow5")
P_LOC_ID      = ("ms-zr59goe24qkocprl3feul3mt", "ms-pttfi6lus2rwf6e4awf9il3a")
P_LOC_NAME    = ("ms-fnodzqkbyskwe7nh58rs336k", "ms-dzp1gmpappibnbh24juqa69r")
P_TS_END      = ("ms-edvvjznmaoibzmfna0uuoo37", "ms-n8atmcxdbyyeikgr46pl0a39")
P_TS_START    = ("ms-o72s5793973fzho35rnaughs", "ms-v78xmuy301fp8ysgzhxd0xo1")

# ─── Enum maps (values MUST match the model's enum components exactly) ────────
# Incident Status: Open / Closed / Pending
STATUS_MAP = {
    "Active": "Open", "Under Investigation": "Pending", "Monitoring": "Pending",
    "Open": "Open", "Closed": "Closed", "Pending": "Pending",
}
# Incident Category Code enum
CATEGORY_MAP = {
    "Public Health Emergency": "other", "Quarantine Enforcement": "other",
    "Contact Tracing": "other", "Traffic": "traffic", "Property Crime": "theft",
    "Civil Disturbance": "other", "Lost Property": "other", "Trespass": "other",
    "Fraud": "fraud", "DUI": "dui", "Missing Person": "missing_person",
    "Animal Control": "other", "Suspicious Activity": "suspicious_activity",
    "Welfare Check": "medical", "Assault": "assault",
}
# Charge Category (Cordova) enum
CHARGE_CATS = ["Traffic Violation", "Petty Theft", "Public Intoxication",
               "Trespassing", "Disorderly Conduct", "Minor Vandalism"]
# Disposition (Cordova) enum
DISPOSITIONS = ["Fine", "Community Service", "Case Dismissed", "Pending"]
# Compliance Status enum
COMPLIANCE_MAP = {
    "Enforced": "Compliant", "Compliant": "Compliant",
    "Monitoring": "Under Review", "Violation": "Violation Detected",
}

_inc_counter = 0


def next_inc():
    global _inc_counter
    _inc_counter += 1
    return f"IR-2026-{_inc_counter:04d}"


def build_instance(rec):
    """Build a governance-composed Law Enforcement Record instance for one incident."""
    prov = make_provenance_values("Cordova Police System", "IncidentRecording", rec["city"])
    status = STATUS_MAP.get(rec.get("status", "Closed"), "Closed")

    xml = xml_header(CT_ID)
    xml += xml_preamble(DM_LABEL, current_state=status)

    # Item: Governed Record wrapper
    xml += cluster_open(GOVERNED_RECORD, "Law Enforcement Governed Record", indent=1)

    # Data cluster (Incident Report). XSD sequence puts the Charge and
    # Quarantine sub-clusters BEFORE the scalar adapters.
    xml += cluster_open(CL_ROOT, "Incident Report", indent=2)

    # Charge and Disposition (optional; only when charge data present)
    if "charge_cat" in rec:
        xml += cluster_open(CL_CHARGE, "Charge and Disposition", indent=3)
        xml += xdstring(*W_CHARGE_DESC, "Charge Description",
                        rec.get("charge_desc", rec["summary"])[:200], indent=4)
        xml += xdtoken(*W_CHARGE_CAT, "Charge Category (Cordova)", rec["charge_cat"], indent=4)
        xml += xdtoken(*W_DISPOSITION, "Disposition (Cordova)",
                       rec.get("disposition", "Pending"), indent=4)
        xml += xdquantity(*W_FINE_AMT, "Fine or Bail Amount", str(rec.get("fine", 0)),
                          "Cordova Córdoba (COR)", indent=4)
        xml += xdtemporal(*W_DISP_DATE, "Disposition Date",
                          rec.get("disp_date", rec["inc_date"]), "date", indent=4)
        xml += xdtemporal(*W_FILING_DATE, "Charge Filing Date", rec["inc_date"], "date", indent=4)
        xml += cluster_close(CL_CHARGE, indent=3)

    # Quarantine Enforcement (optional; only when quarantine data present)
    if "qz_zone" in rec:
        xml += cluster_open(CL_QUARANTINE, "Quarantine Enforcement", indent=3)
        xml += xdstring(*W_ISSUING, "Issuing Authority", rec.get("qz_authority", OMIT), indent=4)
        xml += xdstring(*W_QZ_ZONE, "Quarantine Zone", rec["qz_zone"], indent=4)
        xml += xdtoken(*W_COMPLIANCE, "Compliance Status",
                       COMPLIANCE_MAP.get(rec.get("qz_compliance", "Compliant"), "Under Review"),
                       indent=4)
        xml += xdtemporal(*W_QZ_END, "Quarantine End Date", rec.get("qz_end", "2026-12-31"), "date", indent=4)
        xml += xdtemporal(*W_QZ_START, "Quarantine Start Date", rec.get("qz_start", "2026-01-01"), "date", indent=4)
        xml += cluster_close(CL_QUARANTINE, indent=3)

    # Scalars
    xml += xdstring(*W_INC_NUM, "Incident Report Number", rec["inc_num"], indent=3)
    xml += xdstring(*W_SUMMARY, "Incident Summary", rec["summary"][:2000], indent=3)
    xml += xdstring(*W_LOCATION, "Location Street Full Text", rec["location"][:200], indent=3)
    xml += xdtoken(*W_CITY, "City", rec["city"], indent=3)
    xml += xdtoken(*W_INC_STATUS, "Incident Status", status, indent=3)
    xml += xdtoken(*W_PROVINCE, "Province", rec["province"], indent=3)
    xml += xdtoken(*W_INC_CAT, "Incident Category Code",
                   CATEGORY_MAP.get(rec["category"], "other"), indent=3)
    xml += xdtemporal(*W_INC_DATE, "Incident Date", rec["inc_date"], "date", indent=3)
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
    xml += native_partytype("subject", "Involved Person", rec.get("subject_name", "Unidentified Person"))
    xml += native_partytype("provider", "Reporting Officer",
                            f"{rec['city']} Police Station")
    xml += audit(SYSTEM_AUDIT_ID, prov["activity_timestamp_start"],
                 system_id_value=prov["system_identifier"])
    xml += attestation(pending=False, reason="Incident report filed and reviewed by station duty officer",
                       committer="Reporting Officer", committed=prov["activity_timestamp_end"])

    xml += xml_footer(CT_ID)
    return xml


def generate():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
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
        },
    ]

    for rec in quarantine_records:
        write_xml(os.path.join(OUTPUT_DIR, f"le-{cuid_generator()}.xml"), build_instance(rec))
        count += 1

    # Original 5 routine incidents (preserved)
    routine_incidents = [
        ("Traffic accident - minor property damage", "Traffic", "Porto Sereno", "Aldara"),
        ("Petty theft reported at Central Market", "Property Crime", "Novaciudad", "Celara"),
        ("Noise complaint - residential area", "Civil Disturbance", "Campoluz", "Brevina"),
        ("Lost property report - wallet", "Lost Property", "Porto Sereno", "Aldara"),
        ("Trespassing at port restricted area", "Trespass", "Porto Sereno", "Aldara"),
    ]
    for summary, cat, city, prov in routine_incidents:
        rec = {
            "inc_num": next_inc(), "summary": summary,
            "location": random_address() + f", {city}",
            "city": city, "province": prov,
            "category": cat, "inc_date": random_date(2025, 2025),
        }
        write_xml(os.path.join(OUTPUT_DIR, f"le-{cuid_generator()}.xml"), build_instance(rec))
        count += 1

    # Additional routine incidents (~192 more for ~200 total)
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

    import random as _rand
    for _ in range(scaled(192, 38)):
        summary_template, cat = _rand.choice(incident_templates)
        city = _rand.choice(ALL_CITIES)
        prov = CITY_TO_PROVINCE[city]
        rec = {
            "inc_num": next_inc(),
            "summary": f"{summary_template} at {random_address()}, {city}",
            "location": random_address() + f", {city}",
            "city": city, "province": prov,
            "category": cat,
            "inc_date": random_date(2025, 2025),
            "status": _rand.choice(["Closed", "Closed", "Closed", "Open", "Under Investigation"]),
            "charge_desc": summary_template,
            "charge_cat": _rand.choice(CHARGE_CATS),
            "disposition": _rand.choice(DISPOSITIONS),
            "fine": _rand.choice([0, 0, 0, 50, 100, 200, 500]),
        }
        write_xml(os.path.join(OUTPUT_DIR, f"le-{cuid_generator()}.xml"), build_instance(rec))
        count += 1

    print(f"Law Enforcement: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    generate()
