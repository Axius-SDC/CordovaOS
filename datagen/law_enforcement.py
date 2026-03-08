"""
Generate Law Enforcement Record XML instances for CordovaOS demo.

Quarantine enforcement from the Contagion narrative + routine incidents.
Output: import_data/law_enforcement_record/
"""
import os
import random

from shared import (
    random_city_province, random_address, random_date,
    xml_header, xml_preamble, xml_footer, write_xml,
    xdstring, xdtoken, xdtemporal, xdtemporal_multi, xdquantity,
    cluster_open, cluster_close, party_stub,
    cuid_generator,
)

CT_ID = "yh0opq0bnu6y9y56oukg92uf"
DM_LABEL = "Law Enforcement Record"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "sdc4", "import_data", "law_enforcement_record")

CL_ROOT       = "ms-songhwxr1fp8niqba4fd0yd9"
W_INC_NUM     = ("ms-yi2189u4pinqitlmm5t6ccrd", "ms-chethzdz7hskd3o2xw62c1er")
W_SUMMARY     = ("ms-rguhpkd7s2d9a51392aon7ir", "ms-pjqpd15ajj1ax0f1e0lfqu63")
W_LOCATION    = ("ms-b6nahtg2we4rh5qsk2j7qfvz", "ms-t74qjqgzsm7ieijc3uc2nobv")
W_CITY        = ("ms-atdtdfzruh7tya0iv5cz365l", "ms-i0s8oqbjp6xqohydi8ai4eci")
W_INC_STATUS  = ("ms-e83h36jqgi59dhy1dttp22qm", "ms-wuwrzhcqj9omz96comh5q4xl")
W_PROVINCE    = ("ms-kv5qqs3o4jwcwz9javgw1pzh", "ms-dftklc78nz0zam5of1okubn8")
W_INC_CAT     = ("ms-nc7aq6ofnccavkmczsb2dudy", "ms-segenmixvbvzqrdmtomkyh0y")
W_INC_DATE    = ("ms-ohk2uwcomsz8wegfvz0v0yod", "ms-ajdp3q8jw5peqiuodykpw0tk")  # date+year-month

CL_CHARGE     = "ms-c3eoo0vfid9c8riruf7uoyz2"
W_CHARGE_DESC = ("ms-eoqim4xj9gsxtxrqko1hh55o", "ms-b5soc6dekjmya7uz83z701fa")
W_CHARGE_CAT  = ("ms-hc91pdnj3bb6997l5z4ndchz", "ms-e4yj6vnrj5ayng5otauwr6so")
W_DISPOSITION = ("ms-rnje7nq6m08vh01g8eg23say", "ms-ng6hvaf1otno7mz5blls4qfs")
W_FINE_AMT    = ("ms-yahksk4xc5to981ows7bpp6z", "ms-r4gdeh4glsk08ryun163eypx")
W_DISP_DATE   = ("ms-qse1jwofk5lm2wnsrn3f06l0", "ms-krblpwogobrv713nczj9xeq9")
W_FILING_DATE = ("ms-l0esdclu01pg7qw429oe7kjk", "ms-q4e4b43wrcmp2j27uzxzypph")

CL_QUARANTINE = "ms-avmmc3r38dol0ghko42yeyp4"
W_ISSUING     = ("ms-ixmedhicidzpi7g6g2huqzvv", "ms-s0h7z1f3iialia4o1rz2xkni")
W_QZ_ZONE     = ("ms-r34gm210y9jifbyxa0fcxy96", "ms-uww7ry5lzdh4upf6xcebpj4p")
W_COMPLIANCE  = ("ms-ihoatduhb7fckjw0ezq5u7g1", "ms-vom57pue9a14j072h22cmf4t")
W_QZ_END      = ("ms-lohvu07ok3c3xvesa16htf2m", "ms-ti8di97drly1ivwjv62jl0sw")
W_QZ_START    = ("ms-vq30hd0dl6v59d3ttyyvg6rp", "ms-c3xl0avrvp7qsarvqtcncwhe")

PS_PERSON     = "ms-7i4jw2wkw7om94135c1bq03h"
PS_OFFICER    = "ms-m2lj6lu22oez88prwrdgmnc2"

_inc_counter = 0


def next_inc():
    global _inc_counter
    _inc_counter += 1
    return f"IR-2026-{_inc_counter:04d}"


def build_instance(rec):
    xml = xml_header(CT_ID)
    xml += xml_preamble(DM_LABEL)
    xml += cluster_open(CL_ROOT, "Incident Report")

    xml += xdstring(*W_INC_NUM, "Incident Report Number", rec["inc_num"])
    xml += xdstring(*W_SUMMARY, "Incident Summary", rec["summary"])
    xml += xdstring(*W_LOCATION, "Location Street Full Text", rec["location"])
    xml += xdtoken(*W_CITY, "City", rec["city"])
    xml += xdtoken(*W_INC_STATUS, "Incident Status", rec.get("status", "Closed"))
    xml += xdtoken(*W_PROVINCE, "Province", rec["province"])
    xml += xdtoken(*W_INC_CAT, "Incident Category Code", rec["category"])
    xml += xdtemporal_multi(*W_INC_DATE, "Incident Date", rec["inc_date"], ("date", "year-month"))

    # Charge and Disposition
    xml += cluster_open(CL_CHARGE, "Charge and Disposition", indent=2)
    xml += xdstring(*W_CHARGE_DESC, "Charge Description", rec.get("charge_desc", "N/A"), indent=3)
    xml += xdtoken(*W_CHARGE_CAT, "Charge Category (Cordova)", rec.get("charge_cat", "None"), indent=3)
    xml += xdtoken(*W_DISPOSITION, "Disposition (Cordova)", rec.get("disposition", "No Charge"), indent=3)
    xml += xdquantity(*W_FINE_AMT, "Fine or Bail Amount", str(rec.get("fine", 0)),
                       "Cordova Córdoba (COR)", indent=3)
    xml += xdtemporal(*W_DISP_DATE, "Disposition Date", rec.get("disp_date", rec["inc_date"]), "date", indent=3)
    xml += xdtemporal(*W_FILING_DATE, "Charge Filing Date", rec["inc_date"], "date", indent=3)
    xml += cluster_close(CL_CHARGE, indent=2)

    # Quarantine Enforcement
    xml += cluster_open(CL_QUARANTINE, "Quarantine Enforcement", indent=2)
    xml += xdstring(*W_ISSUING, "Issuing Authority", rec.get("qz_authority", "N/A"), indent=3)
    xml += xdstring(*W_QZ_ZONE, "Quarantine Zone", rec.get("qz_zone", "N/A"), indent=3)
    xml += xdtoken(*W_COMPLIANCE, "Compliance Status", rec.get("qz_compliance", "N/A"), indent=3)
    xml += xdtemporal(*W_QZ_END, "Quarantine End Date", rec.get("qz_end", "1900-01-01"), "date", indent=3)
    xml += xdtemporal(*W_QZ_START, "Quarantine Start Date", rec.get("qz_start", "1900-01-01"), "date", indent=3)
    xml += cluster_close(CL_QUARANTINE, indent=2)

    xml += cluster_close(CL_ROOT)
    xml += party_stub(PS_PERSON, "Involved Person")
    xml += party_stub(PS_OFFICER, "Reporting Officer")
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

    # Routine background incidents
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

    print(f"Law Enforcement: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    generate()
