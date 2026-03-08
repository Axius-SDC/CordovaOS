"""
Generate Healthcare Record XML instances for CordovaOS demo.

Carlos's contagion visit, Elena baseline, background patients.
Output: import_data/healthcare_record/
"""
import os
import random

from shared import (
    CAST, PERSONS, random_date,
    xml_header, xml_preamble, xml_footer, write_xml,
    xdstring, xdtoken, xdtemporal, xdtemporal_multi, xdquantity, xdordinal_stub,
    cluster_open, cluster_close, party_stub,
    cuid_generator,
)

CT_ID = "ftluo2nybgxmn7mawttoos20"
DM_LABEL = "Healthcare Record"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "sdc4", "import_data", "healthcare_record")

CL_ROOT       = "ms-ygtbvvmzcw3ukfsg3axqry97"
W_CID         = ("ms-nj7s1gk45tfgyooxpz0qaha3", "ms-mn42o5y6zxlsv6xng1rhnyiy")
W_MRN         = ("ms-jz2hqntyol8lopw6q6zdud78", "ms-zm4didht9y39r2fjm56w04ma")

CL_ALLERGY    = "ms-xplqihmynccwa3o4o8s7gqml"
W_ALLERGY_DESC = ("ms-ntk4zsr15bcca2jmocdkcpcc", "ms-rumj70a3387aozf7dzg7xbl4")
W_CHRONIC     = ("ms-cm0nqqnjcylc8vkfph7db2lh", "ms-ot7m3t4bsnhfkfo7wddyhutk")
W_COND_STATUS = ("ms-tz13p9d4dpbw3pe9bx51nbou", "ms-rf37fksbjrh8xn0pw7utsv5j")
W_SEVERITY    = ("ms-07osold8ovbjsqzvz00f3ked2", "ms-xrftuu6rtm27x56a5fztuxze")
W_ONSET       = ("ms-p14jkmk8xqs97daq3zvyhrsj", "ms-tyhzcxqbodyf9inbhyibnotx")  # date+year+year-month

CL_MEDS       = "ms-vhjvhm6vz2om2jfn6b923gw7"
W_DOSAGE      = ("ms-z28bjtjekyybe300ukuyjpi4", "ms-a10r6dyuuepetoyfvotczf38")
W_MED_NAME    = ("ms-nomiekce61caq5n9a49d0eu6", "ms-v8rbx36co2xf1878lp9ukqgv")
W_FREQUENCY   = ("ms-iprf7jqg9emvm92wo9gkiqcu", "ms-ed34in9qv3inpzuppsgqfvpr")
W_MED_DOSE_AMT = ("ms-y7k4p12co0b9v6asll531fhv", "ms-b8jz8cnoox36zm0rlcjimy77")
W_RX_DATE     = ("ms-cq6m46w59ouu1cu8tkw1fhib", "ms-oojdpktov9pc34u1d4yw292e")

CL_VACCINE    = "ms-eq4h86worv571cl5iiy9unkw"
W_LOT_NUM     = ("ms-td5j1frz2fa8g4uh1hor7w11", "ms-hblhzbdl5udz5wu0iz5uzrx0")
W_VACCINE_NAME = ("ms-fi1qu4j2zd0801fcqtix35h5", "ms-b7xsratjct5ajr7yg6y8hnys")
W_VACCINE_DATE = ("ms-dyfz05n20jhc1elhozrbjug0", "ms-bo0ytaahd9jx6a331fx8v2xj")  # date+year-month

CL_VISIT      = "ms-hd9295k8o49j91lvgftul1a0"
W_DIAGNOSIS   = ("ms-nnu04d5qgrmn1bim8bpu0l65", "ms-k91mtql09fkvqelg6zreuzpj")
W_FACILITY    = ("ms-qvmb5f4xmy56y98q8raelpl9", "ms-jhbgtf5x1cbyqo6btr7re4ie")
W_REASON      = ("ms-qzmcum3kwmskrkj7nhkf8fkm", "ms-kft6yrp13qqad3fjevhg3rrs")
W_IMPRESSION  = ("ms-cntj1t9t2xjugnux1enpigmf", "ms-v8tpor1vuilwav5juaodgkkt")
W_OUTCOME     = ("ms-lccs354vpxmtyo69ba5cu48v", "ms-dht8a8ivh5tvck9jingpp2sg")
W_VISIT_TYPE  = ("ms-l9sjn7wj10y5b27ldkv3j8mt", "ms-omh5x1hat859qyb26ex1kgoe")
W_BODY_TEMP   = ("ms-b5zse0kmvpkj74ggqvgk647l", "ms-ne7i45poujmsrxzv0wvsihst")
W_BP_DIAS     = ("ms-lu2w1avj9fic5wrmyftt9fhi", "ms-la7dfca8p7vtm3tjt8bh4vcj")
W_HEIGHT      = ("ms-vh2scyehy68pw7sbvzdg3cn9", "ms-yh4bxxuzv1lq8bxe1ufm66pi")
W_WEIGHT      = ("ms-s6oo99lbq85kfz0v5nqv9yaf", "ms-r6l7mrp6b4bbkfohcxjnpfg2")
W_BP_SYS      = ("ms-kokquuk73pm2ohlh4ftnu7wb", "ms-pi5atxwjac2myjhvy1yyo0ws")
W_VISIT_DATE  = ("ms-iufcfze52lha16v84kccgxyh", "ms-afoennq016oob2me7gjpucuc")

PS_PRIMARY    = "ms-bc1ivx4vqa5gh3p5l1pjs1q2"
PS_PROVIDER   = "ms-vyscq0dtz0hsigh2hbsvqajr"

_mrn_counter = 0


def next_mrn():
    global _mrn_counter
    _mrn_counter += 1
    return f"MRN-{_mrn_counter:06d}"


def build_instance(rec):
    xml = xml_header(CT_ID)
    xml += xml_preamble(DM_LABEL)
    xml += cluster_open(CL_ROOT, "Patient Record")

    xml += xdstring(*W_CID, "National ID (CID)", rec["cid"])
    xml += xdstring(*W_MRN, "Medical Record Number", rec["mrn"])

    # Allergies and Conditions
    xml += cluster_open(CL_ALLERGY, "Allergies and Conditions", indent=2)
    xml += xdstring(*W_ALLERGY_DESC, "Allergy Description", rec.get("allergy", "None known"), indent=3)
    xml += xdstring(*W_CHRONIC, "Chronic Condition", rec.get("chronic", "None"), indent=3)
    xml += xdtoken(*W_COND_STATUS, "Condition Status", rec.get("cond_status", "Normal"), indent=3)
    xml += xdordinal_stub(*W_SEVERITY, "Severity (3-Point)", indent=3)
    xml += xdtemporal_multi(*W_ONSET, "Onset Date", rec.get("onset", "1900-01-01"),
                             ("date", "year", "year-month"), indent=3)
    xml += cluster_close(CL_ALLERGY, indent=2)

    # Medications
    xml += cluster_open(CL_MEDS, "Medications", indent=2)
    xml += xdstring(*W_DOSAGE, "Dosage", rec.get("dosage", "N/A"), indent=3)
    xml += xdstring(*W_MED_NAME, "Medication Name", rec.get("med_name", "None"), indent=3)
    xml += xdordinal_stub(*W_FREQUENCY, "Frequency (5-Point)", indent=3)
    xml += xdquantity(*W_MED_DOSE_AMT, "Medication Dosage Amount", rec.get("dose_amt", "0"),
                       "Mass/Weight (SI - Metric)", indent=3)
    xml += xdtemporal(*W_RX_DATE, "Prescription Date", rec.get("rx_date", "1900-01-01"), "date", indent=3)
    xml += cluster_close(CL_MEDS, indent=2)

    # Vaccination History
    xml += cluster_open(CL_VACCINE, "Vaccination History", indent=2)
    xml += xdstring(*W_LOT_NUM, "Lot Number", rec.get("vax_lot", "N/A"), indent=3)
    xml += xdstring(*W_VACCINE_NAME, "Vaccine Name", rec.get("vax_name", "N/A"), indent=3)
    xml += xdtemporal_multi(*W_VACCINE_DATE, "Vaccine Date", rec.get("vax_date", "1900-01-01"),
                             ("date", "year-month"), indent=3)
    xml += cluster_close(CL_VACCINE, indent=2)

    # Visit Record
    xml += cluster_open(CL_VISIT, "Visit Record", indent=2)
    xml += xdstring(*W_DIAGNOSIS, "Diagnosis", rec["diagnosis"], indent=3)
    xml += xdstring(*W_FACILITY, "Facility", rec["facility"], indent=3)
    xml += xdstring(*W_REASON, "Reason for Visit", rec["reason"], indent=3)
    xml += xdstring(*W_IMPRESSION, "Clinical Impression", rec.get("impression", ""), indent=3)
    xml += xdtoken(*W_OUTCOME, "Outcome", rec.get("outcome", "Stable"), indent=3)
    xml += xdtoken(*W_VISIT_TYPE, "Visit Type", rec.get("visit_type", "Outpatient"), indent=3)
    xml += xdquantity(*W_BODY_TEMP, "Body Temperature", rec.get("temp", "36.8"),
                       "Temperature (SI - Metric)", indent=3)
    xml += xdquantity(*W_BP_DIAS, "Diastolic Blood Pressure", rec.get("bp_dias", "80"),
                       "Pressure", indent=3)
    xml += xdquantity(*W_HEIGHT, "Patient Height", rec.get("height", "170"),
                       "Length/Distance (SI - Metric)", indent=3)
    xml += xdquantity(*W_WEIGHT, "Patient Weight", rec.get("weight", "75"),
                       "Mass/Weight (SI - Metric)", indent=3)
    xml += xdquantity(*W_BP_SYS, "Systolic Blood Pressure", rec.get("bp_sys", "120"),
                       "Pressure", indent=3)
    xml += xdtemporal(*W_VISIT_DATE, "Visit Date", rec["visit_date"], "date", indent=3)
    xml += cluster_close(CL_VISIT, indent=2)

    xml += cluster_close(CL_ROOT)
    xml += party_stub(PS_PRIMARY, "Primary Care Assignment")
    xml += party_stub(PS_PROVIDER, "Healthcare Provider")
    xml += xml_footer(CT_ID)
    return xml


def generate():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    count = 0

    # Carlos - The Contagion visit (Beat 3: symptomatic presentation)
    carlos = CAST["carlos"]
    rec = {
        "cid": carlos["cid"], "mrn": next_mrn(),
        "allergy": "None known", "chronic": "None",
        "cond_status": "Active", "onset": "2026-01-12",
        "dosage": "500mg twice daily", "med_name": "Oseltamivir",
        "dose_amt": "500", "rx_date": "2026-01-14",
        "vax_name": "Influenza 2025", "vax_lot": "FLU-2025-4821",
        "vax_date": "2025-10-15",
        "diagnosis": "Suspected novel respiratory pathogen - under investigation",
        "facility": "Porto Sereno General Hospital",
        "reason": "Persistent fever, cough, myalgia x3 days",
        "impression": "Febrile illness with respiratory symptoms. Recent maritime travel. Samples sent for PCR.",
        "outcome": "Admitted", "visit_type": "Emergency",
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
        "diagnosis": "Annual physical - no abnormalities",
        "facility": "UNC Campus Health Center",
        "reason": "Annual wellness exam",
        "impression": "Healthy female, no concerns",
        "outcome": "Stable", "visit_type": "Outpatient",
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
    # ~20% had a clinical encounter
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
        "Montecalvo Community Clinic",
        "Bahia Linda Health Post",
        "Sierra Verde Rural Clinic",
        "Costa Brava Medical Center",
        "Lago Azul Health Post",
        "Tierra Roja Rural Clinic",
    ]

    reasons = [
        "Follow-up", "New complaint", "Annual exam", "Referral",
        "Routine checkup", "Urgent care", "Prescription renewal",
        "Post-surgical follow-up", "Immunization", "Screening",
    ]

    for p in patients:
        age = 2026 - int(p["dob"][:4])
        # Children get well-child visits more often
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
            "diagnosis": diag,
            "facility": random.choice(facilities),
            "reason": random.choice(reasons),
            "outcome": random.choice(["Stable", "Improved", "Referred", "Stable", "Improved"]),
            "visit_type": random.choice(["Outpatient", "Outpatient", "Outpatient", "Emergency"]),
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
