"""
Generate Tax and Revenue Record XML instances for CordovaOS demo.

Governance-composed model: a Governed Record Item carrying (in XSD sequence)
the Provenance Components cluster FIRST, then the Tax Filing data cluster,
followed by native subject/provider/Audit/attestation slots.

Tax filings for cast members and businesses.
Output: import_data/tax_and_revenue_record/
"""
import os
import random

from shared import (
    NA,
    scaled,
    CAST, PERSONS, random_date,
    xml_header, xml_preamble, xml_footer, write_xml,
    xdstring, xdtoken, xdtemporal, xdquantity,
    cluster_open, cluster_close, native_partytype,
    make_provenance_values, audit, attestation,
    cuid_generator,
)

CT_ID = "vaw4g2kusit5z0kox5mog54g"
DM_LABEL = "Tax and Revenue Record"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "sdc4", "import_data", "tax_and_revenue_record")

CURRENCY = "Cordova Córdoba (COR)"

# ─── Governance envelope (Item wrapper + Provenance cluster) ─────────────────
GOVERNED_RECORD = "ms-pilbutha60g9r6v40hzcn4c8"   # Tax and Revenue Governed Record (Item)
CL_PROV         = "ms-hdhjfg00tngir2txgqyka9cv"   # Provenance Components

# Provenance Components leaves (component, adapter-wrapper) — re-keyed for v2
P_ACT_DESC      = ("ms-m9xg6e182m1oq77ssrf9iujv", "ms-pwko3409e5dwueag0j9e1pn8")
P_ACT_TYPE      = ("ms-ccj1yq2wtwknobszkgzzdbtr", "ms-ddyppb8qoic4ag81eua5xtwd")
P_SYS_ID        = ("ms-bd3s8t23d6m3zizmpwavc32y", "ms-cdmpbotfnkqpu6kfncdc02f2")
P_LOC_ID        = ("ms-zr59goe24qkocprl3feul3mt", "ms-qgb2r1n8hp1kzbtbo6nyd0u6")
P_LOC_NAME      = ("ms-fnodzqkbyskwe7nh58rs336k", "ms-pt0l79hw8xsyaliis0eamnsl")
P_TS_END        = ("ms-edvvjznmaoibzmfna0uuoo37", "ms-nr7m0bnchxeet9zaymmohnna")
P_TS_START      = ("ms-o72s5793973fzho35rnaughs", "ms-qg22adai0mzgmujh8601kysf")

# ─── Tax Filing data cluster ─────────────────────────────────────────────────
CL_ROOT       = "ms-w9v4eo1l0wy5r65tqx5mjyxh"   # Tax Filing

# Scalar adapters (component, adapter-wrapper) — re-keyed for v2
W_FILING_ID   = ("ms-a2yks4n49m6gcgpa7qc9hyg1", "ms-rfxzid0q4opct822c4l1y375")
W_FILING_STAT = ("ms-hwmy9yj7cbhe94pjnq0n2oo5", "ms-k2t1lv4uezhp0nq0lsrnbfrf")
W_TAX_TYPE    = ("ms-zb956wxcjf1fccvqezivgrv7", "ms-wzfhsei4z30g73rrpglo7gqc")
W_FILING_DATE = ("ms-cuazcmxeeo8osfybrgdpe9g7", "ms-tdpritgu7ap4s07fljekmnfm")

# Payment sub-cluster
CL_PAYMENT    = "ms-j4drl0w17dmw49maf3swgi18"
W_PAY_METHOD  = ("ms-fqgaf7s7gkwi6j4hh88meudp", "ms-np8re5oag1stra6vryzg1nvn")
W_PAY_STATUS  = ("ms-vt5nh89ol3g5gj0oz35tl6y0", "ms-wg06syaqs1atzgkg0uivfp7p")
W_PAY_AMOUNT  = ("ms-tzrg36a15rigk48nj20sbw4v", "ms-dghfng6fe4r3umyc6j3vnmm2")
W_PAY_DATE    = ("ms-xrjzng8dyk9eveyzi03abuhr", "ms-z7hjmdobtw1x0wzwbmjqd1zl")

# Source Reference sub-cluster
CL_SOURCE     = "ms-kwb0rpk8stxtaitb7k5hahlq"
W_SRC_ID      = ("ms-hcfz6urx5c2ayvt8npjl0t4l", "ms-ag3w1g9c7j27bphmo7dr2h1a")
W_SRC_DOMAIN  = ("ms-hh750k4i187bqzot5md216r1", "ms-di8sg0bdkn2bj3edkbo9rylx")

# Tax Assessment sub-cluster
CL_ASSESS     = "ms-ekmjsthf4vkzcff9pwodqg5n"
W_TAXABLE_INC = ("ms-q1sbdhsdk8glmdr8q1x3mlte", "ms-hq2fuvo34o9ellxq6lhsf0ea")
W_TAX_ASSESS  = ("ms-l5t2s5y0m4ybwom4ryndzaf9", "ms-i7gx4z34ryysoe2pfwnch7zw")

# System Audit component (substitutionGroup="sdc4:Audit"); 5 fixed labels match
# civil defaults (System Audit / service_account_id / System User /
# Contact and Access / Software Agent Details), so audit() needs only these.
AUDIT_COMPONENT = "ms-fotc5adg15ek2b9ermx2mcih"

_filing_counter = 0


def next_filing():
    global _filing_counter
    _filing_counter += 1
    return f"TF-2025-{_filing_counter:06d}"


# Enum-conformant value pools (grep'd from the DM XSD).
# Tax Type enum: Income Tax, Business Tax, Property Tax, Port Fee, Fine Collection, Import Duty
TAX_TYPES = ["Income Tax", "Business Tax", "Property Tax", "Port Fee", "Import Duty"]
# Payment Method enum: Bank Transfer, Check, Cash, Payroll Deduction
PAY_METHODS = ["Bank Transfer", "Check", "Cash", "Payroll Deduction"]
# Payment Status enum: Paid, Invoiced, Overdue
PAY_STATUSES = ["Paid", "Paid", "Paid", "Invoiced", "Overdue"]
# Tax Filing Status enum: Individual, Joint, Business, Estate


def build_instance(rec):
    """Build a governance-composed Tax and Revenue XML instance for one filing."""
    prov = make_provenance_values("Cordova Tax and Revenue System", "TaxAssessment")
    state = rec.get("state", "Filed")

    xml = xml_header(CT_ID)
    xml += xml_preamble(DM_LABEL, current_state=state)

    # Item: Governed Record wrapper
    xml += cluster_open(GOVERNED_RECORD, "Tax and Revenue Governed Record", indent=1)

    # Provenance Components cluster FIRST (per XSD sequence in the Governed Record).
    xml += cluster_open(CL_PROV, "Provenance Components", indent=2)
    xml += xdstring(*P_ACT_DESC, "activity_description", prov["activity_description"], indent=3)
    xml += xdstring(*P_ACT_TYPE, "prov_activity_type", prov["prov_activity_type"], indent=3)
    xml += xdstring(*P_SYS_ID, "system_identifier", prov["system_identifier"], indent=3)
    xml += xdstring(*P_LOC_ID, "system_location_identifier", prov["system_location_identifier"], indent=3)
    xml += xdstring(*P_LOC_NAME, "system_location_name", prov["system_location_name"], indent=3)
    xml += xdtemporal(*P_TS_END, "activity_timestamp_end", prov["activity_timestamp_end"], "datetime", indent=3)
    xml += xdtemporal(*P_TS_START, "activity_timestamp_start", prov["activity_timestamp_start"], "datetime", indent=3)
    xml += cluster_close(CL_PROV, indent=2)

    # Tax Filing data cluster. XSD sequence: sub-clusters (Payment, Source
    # Reference, Tax Assessment) BEFORE the scalar adapters.
    xml += cluster_open(CL_ROOT, "Tax Filing", indent=2)

    xml += cluster_open(CL_PAYMENT, "Payment", indent=3)
    xml += xdtoken(*W_PAY_METHOD, "Payment Method", rec.get("pay_method", "Bank Transfer"), indent=4)
    xml += xdtoken(*W_PAY_STATUS, "Payment Status", rec.get("pay_status", "Paid"), indent=4)
    xml += xdquantity(*W_PAY_AMOUNT, "Payment Amount", str(rec["pay_amount"]), CURRENCY, indent=4)
    xml += xdtemporal(*W_PAY_DATE, "Payment Date", rec["filing_date"], "date", indent=4)
    xml += cluster_close(CL_PAYMENT, indent=3)

    xml += cluster_open(CL_SOURCE, "Source Reference", indent=3)
    xml += xdstring(*W_SRC_ID, "Source Record ID", rec.get("src_id", NA), indent=4)
    xml += xdtoken(*W_SRC_DOMAIN, "Source Domain", rec.get("src_domain", "Employment"), indent=4)
    xml += cluster_close(CL_SOURCE, indent=3)

    xml += cluster_open(CL_ASSESS, "Tax Assessment", indent=3)
    xml += xdquantity(*W_TAXABLE_INC, "Taxable Income", str(rec["taxable_income"]), CURRENCY, indent=4)
    xml += xdquantity(*W_TAX_ASSESS, "Tax Assessment Amount", str(rec["tax_amount"]), CURRENCY, indent=4)
    xml += cluster_close(CL_ASSESS, indent=3)

    xml += xdstring(*W_FILING_ID, "Filing ID", rec["filing_id"], indent=3)
    xml += xdtoken(*W_FILING_STAT, "Tax Filing Status", rec.get("filing_status", "Individual"), indent=3)
    xml += xdtoken(*W_TAX_TYPE, "Tax Type", rec["tax_type"], indent=3)
    xml += xdtemporal(*W_FILING_DATE, "Filing Date", rec["filing_date"], "date", indent=3)
    xml += cluster_close(CL_ROOT, indent=2)

    xml += cluster_close(GOVERNED_RECORD, indent=1)

    # Native governance slots, DM order: subject, provider, Audit, attestation.
    xml += native_partytype("subject", "Taxpayer", rec.get("taxpayer_name", "Cordova Taxpayer"))
    xml += native_partytype("provider", "Tax Authority",
                            "Cordova National Revenue Authority")
    xml += audit(AUDIT_COMPONENT, prov["activity_timestamp_start"],
                 system_id_value=prov["system_identifier"])
    xml += attestation(pending=False,
                       reason="Filing assessed by the Cordova National Revenue Authority",
                       committer="Cordova National Revenue Authority",
                       committed=prov["activity_timestamp_end"])

    xml += xml_footer(CT_ID)
    return xml


def generate():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    count = 0

    # Income tax for cast members
    cast_incomes = {
        "carlos": 28000, "elena": 65000, "dr_reyes": 95000,
        "governor_avila": 120000, "sgt_santos": 42000,
        "dr_ferrer": 88000, "dr_gutierrez": 72000, "prof_lucero": 74000,
    }
    for key, income in cast_incomes.items():
        tax_amount = int(income * 0.15)
        c = CAST.get(key, {})
        taxpayer = f"{c.get('given','')} {c.get('surname','')}".strip() or "Cordova Taxpayer"
        rec = {
            "filing_id": next_filing(), "tax_type": "Income Tax",
            "filing_status": "Individual",
            "filing_date": "2025-04-15", "state": "Assessed",
            "pay_amount": tax_amount, "taxable_income": income,
            "tax_amount": tax_amount, "src_domain": "Employment",
            "taxpayer_name": taxpayer,
        }
        write_xml(os.path.join(OUTPUT_DIR, f"tx-{cuid_generator()}.xml"), build_instance(rec))
        count += 1

    # Business tax filings for narrative businesses (only non-exempt)
    narrative_brns = [
        ("BIZ-001102", 2500000),  # Pacifico Meridional
        ("BIZ-000847", 0),  # UNC exempt
        ("BIZ-000523", 0),  # Hospital exempt
        ("BIZ-000101", 0),  # CNP exempt (government)
        ("BIZ-000205", 0),  # Health Office exempt (government)
    ]
    for brn, revenue in narrative_brns:
        if revenue > 0:
            tax_amount = int(revenue * 0.12)
            rec = {
                "filing_id": next_filing(), "tax_type": "Business Tax",
                "filing_status": "Business",
                "filing_date": "2025-03-31", "state": "Assessed",
                "pay_amount": tax_amount, "taxable_income": revenue,
                "tax_amount": tax_amount,
                "src_id": brn, "src_domain": "Business Registry",
                "taxpayer_name": "Pacifico Meridional",
            }
            write_xml(os.path.join(OUTPUT_DIR, f"tx-{cuid_generator()}.xml"), build_instance(rec))
            count += 1

    # Background business tax filings (~495 background businesses)
    for i in range(scaled(495, 42)):
        brn = f"BIZ-{i+2:06d}"  # offset past narrative BRNs
        revenue = random.randint(50000, 3000000)
        tax_amount = int(revenue * 0.12)
        rec = {
            "filing_id": next_filing(), "tax_type": "Business Tax",
            "filing_status": "Business",
            "filing_date": random_date(2024, 2025),
            "state": random.choice(["Filed", "Assessed", "Closed"]),
            "pay_amount": tax_amount, "taxable_income": revenue,
            "tax_amount": tax_amount,
            "src_id": brn, "src_domain": "Business Registry",
            "pay_method": random.choice(PAY_METHODS),
            "pay_status": random.choice(PAY_STATUSES),
            "taxpayer_name": f"Cordova Business {brn}",
        }
        write_xml(os.path.join(OUTPUT_DIR, f"tx-{cuid_generator()}.xml"), build_instance(rec))
        count += 1

    # Individual income tax for all employed working-age persons
    if not PERSONS:
        from civil_registry import generate as gen_cr
        gen_cr()

    working_age = [p for p in PERSONS if p.get("key", "").startswith("bg_")
                   and 18 <= (2026 - int(p["dob"][:4])) <= 67]
    # ~85% have income tax filings (same as employment rate)
    filers = random.sample(working_age, k=int(len(working_age) * 0.85))
    for p in filers:
        income = random.randint(15000, 80000)
        tax_amount = int(income * 0.15)
        rec = {
            "filing_id": next_filing(), "tax_type": "Income Tax",
            "filing_status": random.choice(["Individual", "Individual", "Joint"]),
            "filing_date": random_date(2024, 2025),
            "state": random.choice(["Filed", "Assessed", "Closed"]),
            "pay_amount": tax_amount, "taxable_income": income,
            "tax_amount": tax_amount, "src_domain": "Employment",
            "pay_method": random.choice(PAY_METHODS),
            "pay_status": random.choice(PAY_STATUSES),
            "taxpayer_name": f"{p.get('given','')} {p.get('surname','')}".strip() or "Cordova Taxpayer",
        }
        write_xml(os.path.join(OUTPUT_DIR, f"tx-{cuid_generator()}.xml"), build_instance(rec))
        count += 1

    print(f"Tax and Revenue: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    generate()
