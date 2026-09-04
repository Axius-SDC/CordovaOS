"""
Generate Healthcare Record XML instances for CordovaOS demo.

Governance-composed model (v2 envelope): Governed Record Item wrapping the
Patient Record data cluster + Provenance Components cluster, then native DM
subject (Patient) / provider slots, a modeled System Audit, and attestation.

Carlos's contagion visit, Elena baseline, background patients.
Output: import_data/healthcare_record/
"""
import os
import random

from shared import (
    NA,
    CAST, PERSONS, random_date,
    xml_header, xml_preamble, xml_footer, write_xml,
    xdstring, xdtoken, xdtemporal, xdquantity,
    cluster_open, cluster_close, native_partytype,
    make_provenance_values, audit, attestation,
    cuid_generator, _esc,
)

CT_ID = "ftluo2nybgxmn7mawttoos20"
DM_LABEL = "Healthcare Record"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "sdc4", "import_data", "healthcare_record")

# ─── Governance envelope (re-keyed adapter wrappers from template dm-*.xml) ───

GOVERNED_RECORD = "ms-w0lu0us3nbxaedfum9i8itpc"   # Item: Healthcare Governed Record
CL_PROV         = "ms-hdhjfg00tngir2txgqyka9cv"   # Provenance Components cluster
AUDIT_ID        = "ms-fotc5adg15ek2b9ermx2mcih"   # System Audit component

CL_ROOT = "ms-ygtbvvmzcw3ukfsg3axqry97"           # Patient Record data cluster

# Scalar leaves, direct children of Patient Record (component, wrapper)
W_CID = ("ms-nj7s1gk45tfgyooxpz0qaha3", "ms-z16xo5uj1mi3dibl3ro3ufrl")
W_MRN = ("ms-jz2hqntyol8lopw6q6zdud78", "ms-zdd1wtyrryiurmvqseaivjr1")

# Allergies and Conditions sub-cluster
CL_ALLERGY     = "ms-xplqihmynccwa3o4o8s7gqml"
W_ALLERGY_DESC = ("ms-ntk4zsr15bcca2jmocdkcpcc", "ms-fiyhm1yos1t6svmprr836bx0")
W_CHRONIC      = ("ms-cm0nqqnjcylc8vkfph7db2lh", "ms-rzf4dwte7xet6gdue6lmj6py")
W_COND_STATUS  = ("ms-tz13p9d4dpbw3pe9bx51nbou", "ms-kvgfcr3rme6fqpt6nn5h66qn")
W_SEVERITY     = ("ms-07osold8ovbjsqzvz00f3ked2", "ms-bofw0qcwpbypofxuwwcxiq2o")
W_ONSET        = ("ms-p14jkmk8xqs97daq3zvyhrsj", "ms-fy92af172lvw70id7u1jgskn")

# Medications sub-cluster
CL_MEDS        = "ms-vhjvhm6vz2om2jfn6b923gw7"
W_DOSAGE       = ("ms-z28bjtjekyybe300ukuyjpi4", "ms-dk7pfc5jk1cn2b7n4zj6m6so")
W_MED_NAME     = ("ms-nomiekce61caq5n9a49d0eu6", "ms-abx0p7u2r7v3ld052qonnyjo")
W_FREQUENCY    = ("ms-iprf7jqg9emvm92wo9gkiqcu", "ms-wbv46a4twbyuwpwr7ybz3j2z")
W_MED_DOSE_AMT = ("ms-y7k4p12co0b9v6asll531fhv", "ms-pfpxhdvami9iviftg37r2la2")
W_RX_DATE      = ("ms-cq6m46w59ouu1cu8tkw1fhib", "ms-x6ld5whgo7cyb51uusixmd3d")

# Vaccination History sub-cluster
CL_VACCINE     = "ms-eq4h86worv571cl5iiy9unkw"
W_LOT_NUM      = ("ms-td5j1frz2fa8g4uh1hor7w11", "ms-el0cz3iurka072fggj4hx49f")
W_VACCINE_NAME = ("ms-fi1qu4j2zd0801fcqtix35h5", "ms-j7ar4kki6mv0r7ocr6ow3qhl")
W_VACCINE_DATE = ("ms-dyfz05n20jhc1elhozrbjug0", "ms-qydut841yrwpnp46ookn2ggn")

# Visit Record sub-cluster
CL_VISIT     = "ms-hd9295k8o49j91lvgftul1a0"
W_DIAGNOSIS  = ("ms-nnu04d5qgrmn1bim8bpu0l65", "ms-whrsz97tqb4o168mzr4mflu6")
W_FACILITY   = ("ms-qvmb5f4xmy56y98q8raelpl9", "ms-xk9xcbv60fx8le5wx8b3owby")
W_REASON     = ("ms-qzmcum3kwmskrkj7nhkf8fkm", "ms-stzcsbchyfvy4z7r35fxkw6b")
W_IMPRESSION = ("ms-cntj1t9t2xjugnux1enpigmf", "ms-o03ksbpzw3yx4v9scegdc7el")
W_OUTCOME    = ("ms-lccs354vpxmtyo69ba5cu48v", "ms-mgms7fe9u8u1h96ljom48dc4")
W_VISIT_TYPE = ("ms-l9sjn7wj10y5b27ldkv3j8mt", "ms-meit785z0ugz2andc6ff2kgo")
W_BODY_TEMP  = ("ms-b5zse0kmvpkj74ggqvgk647l", "ms-dzafdnv507rgc8sxqqa2ltf5")
W_BP_DIAS    = ("ms-lu2w1avj9fic5wrmyftt9fhi", "ms-w9offwxy24rsztc11j7zx0ug")
W_HEIGHT     = ("ms-vh2scyehy68pw7sbvzdg3cn9", "ms-zvkl8ctcg237iqwtyyrwenoq")
W_WEIGHT     = ("ms-s6oo99lbq85kfz0v5nqv9yaf", "ms-vgq6d2vts14o1zo4491cf6d4")
W_BP_SYS     = ("ms-kokquuk73pm2ohlh4ftnu7wb", "ms-q867tp1yaobktelz3gpvfa64")
W_VISIT_DATE = ("ms-iufcfze52lha16v84kccgxyh", "ms-pe9rnuja4xuk2wyoyfkfdo9o")

# Provenance Components leaves (component, wrapper)
P_ACT_DESC = ("ms-m9xg6e182m1oq77ssrf9iujv", "ms-c5016skbmb8jg39cysvwc65a")
P_ACT_TYPE = ("ms-ccj1yq2wtwknobszkgzzdbtr", "ms-rpaz1widq2u7qox2n8r6lohf")
P_SYS_ID   = ("ms-bd3s8t23d6m3zizmpwavc32y", "ms-eu0hd4f95yni58yexux8yqek")
P_LOC_ID   = ("ms-zr59goe24qkocprl3feul3mt", "ms-dzaswthq3j4qi7yuqvkf9c04")
P_LOC_NAME = ("ms-fnodzqkbyskwe7nh58rs336k", "ms-qhgvqe89m9q7zz5l8clyufra")
P_TS_END   = ("ms-edvvjznmaoibzmfna0uuoo37", "ms-yyquv6xw4po00iif4c57j118")
P_TS_START = ("ms-o72s5793973fzho35rnaughs", "ms-y6rt146tgmkdixx2fs5d8ngf")

# ─── Domain enums (from XSD enumeration facets) ──────────────────────────────

CONDITION_STATUSES = ["Active", "Resolved", "In Remission"]
OUTCOMES = ["Treated and Released", "Admitted", "Referred",
            "Follow-up Scheduled", "No Treatment Required"]
VISIT_TYPES = ["Screening", "Baseline", "Follow-up",
               "Unscheduled", "Early termination", "Final"]
# XdOrdinal scales: (ordinal-decimal, symbol) pairs
SEVERITY_SCALE = [("0", "Mild"), ("1", "Moderate"), ("2", "Severe")]
FREQUENCY_SCALE = [("1", "Never"), ("2", "Rarely"), ("3", "Sometimes"),
                   ("4", "Often"), ("5", "Always")]

WORKFLOW_STATES = ["Documented", "Reviewed", "Finalized", "Amended"]

_mrn_counter = 0


def next_mrn():
    global _mrn_counter
    _mrn_counter += 1
    return f"MRN-{_mrn_counter:06d}"


def xdordinal(component_id, wrapper_id, label, ordinal, symbol, indent=3):
    """Build an XdOrdinal fragment with the required ordinal + symbol elements.

    The healthcare model makes both `ordinal` (decimal, enum) and `symbol`
    (string, enum) mandatory, so the shared xdordinal_stub (comments only)
    would not validate. Emits the full XdAny leaf sequence then ordinal+symbol.
    """
    pad = "  " * indent
    return f"""{pad}<sdc4:{wrapper_id}>
{pad}  <sdc4:{component_id}>
{pad}    <label>{label}</label>
{pad}    <act></act>
{pad}    <vtb>2020-01-01T00:00:00</vtb>
{pad}    <vte>9999-12-31T23:59:59</vte>
{pad}    <tr>2020-01-01T00:00:00</tr>
{pad}    <modified>2020-01-01T00:00:00</modified>
{pad}    <latitude>0.0</latitude>
{pad}    <longitude>0.0</longitude>
{pad}    <ordinal>{ordinal}</ordinal>
{pad}    <symbol>{_esc(symbol)}</symbol>
{pad}  </sdc4:{component_id}>
{pad}</sdc4:{wrapper_id}>
"""


def build_instance(rec):
    """Build a governance-composed Healthcare Record XML instance for one patient."""
    prov = make_provenance_values("Cordova Healthcare System", "PatientEncounter",
                                  rec.get("city"))
    state = random.choice(WORKFLOW_STATES)

    xml = xml_header(CT_ID)
    xml += xml_preamble(DM_LABEL, current_state=state)

    # Item: Governed Record wrapper
    xml += cluster_open(GOVERNED_RECORD, "Healthcare Governed Record", indent=1)

    # Data cluster. Child order follows the Patient Record XSD sequence
    # exactly: the four sub-clusters first, then the two scalar identifiers.
    xml += cluster_open(CL_ROOT, "Patient Record", indent=2)

    # Allergies and Conditions
    xml += cluster_open(CL_ALLERGY, "Allergies and Conditions", indent=3)
    xml += xdstring(*W_ALLERGY_DESC, "Allergy Description", rec.get("allergy", "None known"), indent=4)
    xml += xdstring(*W_CHRONIC, "Chronic Condition", rec.get("chronic", "None"), indent=4)
    xml += xdtoken(*W_COND_STATUS, "Condition Status", rec.get("cond_status", "Resolved"), indent=4)
    sev = rec.get("severity", SEVERITY_SCALE[0])
    xml += xdordinal(*W_SEVERITY, "Severity (3-Point)", sev[0], sev[1], indent=4)
    xml += xdtemporal(*W_ONSET, "Onset Date", rec.get("onset", NA), "date", indent=4)
    xml += cluster_close(CL_ALLERGY, indent=3)

    # Medications
    xml += cluster_open(CL_MEDS, "Medications", indent=3)
    xml += xdstring(*W_DOSAGE, "Dosage", rec.get("dosage", NA), indent=4)
    xml += xdstring(*W_MED_NAME, "Medication Name", rec.get("med_name", "None"), indent=4)
    freq = rec.get("frequency", FREQUENCY_SCALE[0])
    xml += xdordinal(*W_FREQUENCY, "Frequency (5-Point)", freq[0], freq[1], indent=4)
    xml += xdquantity(*W_MED_DOSE_AMT, "Medication Dosage Amount", rec.get("dose_amt", NA),
                      "Mass/Weight (SI - Metric)", indent=4)
    xml += xdtemporal(*W_RX_DATE, "Prescription Date", rec.get("rx_date", NA), "date", indent=4)
    xml += cluster_close(CL_MEDS, indent=3)

    # Vaccination History
    xml += cluster_open(CL_VACCINE, "Vaccination History", indent=3)
    xml += xdstring(*W_LOT_NUM, "Lot Number", rec.get("vax_lot", NA), indent=4)
    xml += xdstring(*W_VACCINE_NAME, "Vaccine Name", rec.get("vax_name", NA), indent=4)
    xml += xdtemporal(*W_VACCINE_DATE, "Vaccine Date", rec.get("vax_date", NA), "date", indent=4)
    xml += cluster_close(CL_VACCINE, indent=3)

    # Visit Record
    xml += cluster_open(CL_VISIT, "Visit Record", indent=3)
    xml += xdstring(*W_DIAGNOSIS, "Diagnosis", rec["diagnosis"], indent=4)
    xml += xdstring(*W_FACILITY, "Facility", rec["facility"], indent=4)
    xml += xdstring(*W_REASON, "Reason for Visit", rec["reason"], indent=4)
    xml += xdstring(*W_IMPRESSION, "Clinical Impression",
                    rec.get("impression") or "No acute findings noted", indent=4)
    xml += xdtoken(*W_OUTCOME, "Outcome", rec.get("outcome", "Treated and Released"), indent=4)
    xml += xdtoken(*W_VISIT_TYPE, "Visit Type", rec.get("visit_type", "Follow-up"), indent=4)
    xml += xdquantity(*W_BODY_TEMP, "Body Temperature", rec.get("temp", "36.8"),
                      "Temperature (SI - Metric)", indent=4)
    xml += xdquantity(*W_BP_DIAS, "Diastolic Blood Pressure", rec.get("bp_dias", "80"),
                      "Pressure", indent=4)
    xml += xdquantity(*W_HEIGHT, "Patient Height", rec.get("height", "170"),
                      "Length/Distance (SI - Metric)", indent=4)
    xml += xdquantity(*W_WEIGHT, "Patient Weight", rec.get("weight", "75"),
                      "Mass/Weight (SI - Metric)", indent=4)
    xml += xdquantity(*W_BP_SYS, "Systolic Blood Pressure", rec.get("bp_sys", "120"),
                      "Pressure", indent=4)
    xml += xdtemporal(*W_VISIT_DATE, "Visit Date", rec["visit_date"], "date", indent=4)
    xml += cluster_close(CL_VISIT, indent=3)

    # Scalar identifiers last, per the Patient Record XSD sequence.
    xml += xdstring(*W_CID, "National ID (CID)", rec["cid"], indent=3)
    xml += xdstring(*W_MRN, "Medical Record Number", rec["mrn"], indent=3)

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
    xml += native_partytype("subject", "Patient", rec.get("patient_name", "Unknown Patient"))
    xml += native_partytype("provider", "Healthcare Provider", rec["facility"])
    xml += audit(AUDIT_ID, prov["activity_timestamp_start"],
                 system_id_value=prov["system_identifier"])
    xml += attestation(pending=False,
                       reason="Encounter documented by the attending clinician",
                       committer="Healthcare Provider",
                       committed=prov["activity_timestamp_end"])

    xml += xml_footer(CT_ID)
    return xml


def generate():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    count = 0

    # Carlos - The Contagion visit (Beat 3: symptomatic presentation)
    carlos = CAST["carlos"]
    rec = {
        "cid": carlos["cid"], "mrn": next_mrn(),
        "patient_name": f"{carlos['given']} {carlos['surname']}",
        "city": carlos["city"],
        "allergy": "None known", "chronic": "None",
        "cond_status": "Active",
        "severity": ("2", "Severe"),
        "onset": "2026-01-12",
        "dosage": "500mg twice daily", "med_name": "Oseltamivir",
        "frequency": ("4", "Often"),
        "dose_amt": "500", "rx_date": "2026-01-14",
        "vax_name": "Influenza 2025", "vax_lot": "FLU-2025-4821",
        "vax_date": "2025-10-15",
        "diagnosis": "Suspected novel respiratory pathogen - under investigation",
        "facility": "Porto Sereno General Hospital",
        "reason": "Persistent fever, cough, myalgia x3 days",
        "impression": "Febrile illness with respiratory symptoms. Recent maritime travel. Samples sent for PCR.",
        "outcome": "Admitted", "visit_type": "Unscheduled",
        "temp": "39.2", "bp_sys": "128", "bp_dias": "82",
        "height": "178", "weight": "82",
        "visit_date": "2026-01-14",
    }
    write_xml(os.path.join(OUTPUT_DIR, f"hc-{cuid_generator()}.xml"), build_instance(rec))
    count += 1

    # Elena - baseline visit (no symptoms)
    elena = CAST["elena"]
    rec = {
        "cid": elena["cid"], "mrn": next_mrn(),
        "patient_name": f"{elena['given']} {elena['surname']}",
        "city": elena["city"],
        "cond_status": "Resolved",
        "diagnosis": "Annual physical - no abnormalities",
        "facility": "Novaciudad Central Hospital",
        "reason": "Annual wellness exam",
        "impression": "Healthy female, no concerns",
        "outcome": "Treated and Released", "visit_type": "Baseline",
        "temp": "36.6", "bp_sys": "118", "bp_dias": "76",
        "height": "165", "weight": "62",
        "visit_date": "2025-11-20",
    }
    write_xml(os.path.join(OUTPUT_DIR, f"hc-{cuid_generator()}.xml"), build_instance(rec))
    count += 1

    # Background patients: ~20% of population → ~5,000
    if not PERSONS:
        from civil_registry import generate as gen_cr
        gen_cr()

    bg = [p for p in PERSONS if p.get("key", "").startswith("bg_")]
    patients = random.sample(bg, k=min(len(bg), 5000))

    diagnoses = [
        "Hypertension management", "Type 2 diabetes follow-up",
        "Upper respiratory infection", "Minor laceration - sutured",
        "Annual physical", "Back pain", "Gastroenteritis",
        "Mild allergic reaction", "Ankle sprain", "Migraine",
        "Asthma exacerbation", "Urinary tract infection", "Otitis media",
        "Conjunctivitis", "Dermatitis", "Fracture - closed reduction",
        "Dental abscess referral", "Prenatal checkup", "Well-child visit",
        "Chronic pain management", "Anxiety disorder follow-up",
        "Iron deficiency anemia", "Bronchitis", "Sinusitis",
        "Knee injury", "Shoulder strain", "Insect bite reaction",
        "Food poisoning", "Dehydration - mild", "Vaccination visit",
    ]

    facilities = [
        "Porto Sereno General Hospital",
        "Campoluz Medical Clinic",
        "Novaciudad Central Hospital",
        "Montecara Community Clinic",
        "Vistamar Health Post",
        "Tierraverde Rural Clinic",
        "Piedrasol Medical Center",
        "Lagunavista Health Post",
        "Rioseco Rural Clinic",
    ]

    reasons = [
        "Follow-up", "New complaint", "Annual exam", "Referral",
        "Routine checkup", "Urgent care", "Prescription renewal",
        "Post-surgical follow-up", "Immunization", "Screening",
    ]

    for p in patients:
        age = 2026 - int(p["dob"][:4])
        if age < 12:
            diag = random.choice(["Well-child visit", "Otitis media", "Vaccination visit",
                                   "Upper respiratory infection", "Dermatitis", "Asthma exacerbation"])
            height = str(random.randint(80, 155))
            weight = str(random.randint(15, 50))
        elif age > 60:
            diag = random.choice(["Hypertension management", "Type 2 diabetes follow-up",
                                   "Chronic pain management", "Annual physical",
                                   "Back pain", "Dehydration - mild"])
            height = str(random.randint(150, 185))
            weight = str(random.randint(55, 100))
        else:
            diag = random.choice(diagnoses)
            height = str(random.randint(155, 195))
            weight = str(random.randint(50, 110))

        rec = {
            "cid": p["cid"], "mrn": next_mrn(),
            "patient_name": f"{p['given']} {p['surname']}",
            "city": p["city"],
            "cond_status": random.choice(CONDITION_STATUSES),
            "severity": random.choice(SEVERITY_SCALE),
            "frequency": random.choice(FREQUENCY_SCALE),
            "diagnosis": diag,
            "facility": random.choice(facilities),
            "reason": random.choice(reasons),
            "impression": f"Clinical impression: {diag.lower()}",
            "outcome": random.choice(OUTCOMES),
            "visit_type": random.choice(VISIT_TYPES),
            "temp": f"{random.uniform(36.0, 37.8):.1f}",
            "bp_sys": str(random.randint(100, 155)),
            "bp_dias": str(random.randint(60, 100)),
            "height": height,
            "weight": weight,
            "visit_date": random_date(2024, 2025),
        }
        write_xml(os.path.join(OUTPUT_DIR, f"hc-{cuid_generator()}.xml"), build_instance(rec))
        count += 1

    print(f"Healthcare Record: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    generate()
