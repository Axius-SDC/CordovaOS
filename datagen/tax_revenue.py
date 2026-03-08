"""
Generate Tax and Revenue Record XML instances for CordovaOS demo.

Tax filings for cast members and businesses.
Output: import_data/tax_and_revenue_record/
"""
import os
import random

from shared import (
    CAST, PERSONS, random_date,
    xml_header, xml_preamble, xml_footer, write_xml,
    xdstring, xdtoken, xdtemporal, xdquantity,
    cluster_open, cluster_close, party_stub,
    cuid_generator,
)

CT_ID = "vaw4g2kusit5z0kox5mog54g"
DM_LABEL = "Tax and Revenue Record"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "sdc4", "import_data", "tax_and_revenue_record")

CL_ROOT       = "ms-w9v4eo1l0wy5r65tqx5mjyxh"
W_FILING_ID   = ("ms-a2yks4n49m6gcgpa7qc9hyg1", "ms-wh6fdicb3g4jundl51skxobs")
W_FILING_STAT = ("ms-hwmy9yj7cbhe94pjnq0n2oo5", "ms-evsrbxdp1yemcx6q7ia1we3h")
W_TAX_TYPE    = ("ms-zb956wxcjf1fccvqezivgrv7", "ms-y84oq80on7xmsuqb99nb3oc7")
W_FILING_DATE = ("ms-cuazcmxeeo8osfybrgdpe9g7", "ms-cmb7v0otctobic5ilixs249r")

CL_PAYMENT    = "ms-j4drl0w17dmw49maf3swgi18"
W_PAY_METHOD  = ("ms-fqgaf7s7gkwi6j4hh88meudp", "ms-h2bf5896ghdx4zvfjsqtchc0")
W_PAY_STATUS  = ("ms-vt5nh89ol3g5gj0oz35tl6y0", "ms-w3z06rn4cg8p7o1c1n8odah7")
W_PAY_AMOUNT  = ("ms-tzrg36a15rigk48nj20sbw4v", "ms-fz588ql0ysiwfysyce7n3e9u")
W_PAY_DATE    = ("ms-xrjzng8dyk9eveyzi03abuhr", "ms-eraqd0tvi66nq1ti57gun3d8")

CL_SOURCE     = "ms-kwb0rpk8stxtaitb7k5hahlq"
W_SRC_ID      = ("ms-hcfz6urx5c2ayvt8npjl0t4l", "ms-xfob1384njajocihonlaf2p4")
W_SRC_DOMAIN  = ("ms-hh750k4i187bqzot5md216r1", "ms-lqhdz83iy3n7smcl7qqmp2kn")

CL_ASSESS     = "ms-ekmjsthf4vkzcff9pwodqg5n"
W_TAXABLE_INC = ("ms-q1sbdhsdk8glmdr8q1x3mlte", "ms-fr998l1wsocagp15jvkmcqt5")
W_TAX_ASSESS  = ("ms-l5t2s5y0m4ybwom4ryndzaf9", "ms-b87ov9k10xn8iutv6rwbvw98")

PS_TAXPAYER   = "ms-hbosti8lu7hhu5liq7klammn"
PS_AUTHORITY  = "ms-h809aepw09m83xjn7cav2f9m"

_filing_counter = 0


def next_filing():
    global _filing_counter
    _filing_counter += 1
    return f"TF-2025-{_filing_counter:06d}"


TAX_TYPES = ["Income Tax", "Property Tax", "Business Tax", "Sales Tax"]
PAY_METHODS = ["Bank Transfer", "Check", "Cash", "Electronic"]


def build_instance(rec):
    xml = xml_header(CT_ID)
    xml += xml_preamble(DM_LABEL)
    xml += cluster_open(CL_ROOT, "Tax Filing")

    xml += xdstring(*W_FILING_ID, "Filing ID", rec["filing_id"])
    xml += xdtoken(*W_FILING_STAT, "Tax Filing Status", rec.get("status", "Filed"))
    xml += xdtoken(*W_TAX_TYPE, "Tax Type", rec["tax_type"])
    xml += xdtemporal(*W_FILING_DATE, "Filing Date", rec["filing_date"], "date")

    xml += cluster_open(CL_PAYMENT, "Payment", indent=2)
    xml += xdtoken(*W_PAY_METHOD, "Payment Method", rec.get("pay_method", "Bank Transfer"), indent=3)
    xml += xdtoken(*W_PAY_STATUS, "Payment Status", rec.get("pay_status", "Paid"), indent=3)
    xml += xdquantity(*W_PAY_AMOUNT, "Payment Amount", str(rec["pay_amount"]),
                       "Cordova Córdoba (COR)", indent=3)
    xml += xdtemporal(*W_PAY_DATE, "Payment Date", rec["filing_date"], "date", indent=3)
    xml += cluster_close(CL_PAYMENT, indent=2)

    xml += cluster_open(CL_SOURCE, "Source Reference", indent=2)
    xml += xdstring(*W_SRC_ID, "Source Record ID", rec.get("src_id", "N/A"), indent=3)
    xml += xdtoken(*W_SRC_DOMAIN, "Source Domain", rec.get("src_domain", "Employment"), indent=3)
    xml += cluster_close(CL_SOURCE, indent=2)

    xml += cluster_open(CL_ASSESS, "Tax Assessment", indent=2)
    xml += xdquantity(*W_TAXABLE_INC, "Taxable Income", str(rec["taxable_income"]),
                       "Cordova Córdoba (COR)", indent=3)
    xml += xdquantity(*W_TAX_ASSESS, "Tax Assessment Amount", str(rec["tax_amount"]),
                       "Cordova Córdoba (COR)", indent=3)
    xml += cluster_close(CL_ASSESS, indent=2)

    xml += cluster_close(CL_ROOT)
    xml += party_stub(PS_TAXPAYER, "Taxpayer")
    xml += party_stub(PS_AUTHORITY, "Tax Authority")
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
        rec = {
            "filing_id": next_filing(), "tax_type": "Income Tax",
            "filing_date": "2025-04-15",
            "pay_amount": tax_amount, "taxable_income": income,
            "tax_amount": tax_amount, "src_domain": "Employment",
        }
        write_xml(os.path.join(OUTPUT_DIR, f"tx-{cuid_generator()}.xml"), build_instance(rec))
        count += 1

    # Business tax filings
    biz_names_brns = [
        ("BIZ-001102", 2500000), ("BIZ-000847", 0),  # UNC exempt
        ("BIZ-000523", 0),  # Hospital exempt
    ]
    for brn, revenue in biz_names_brns:
        if revenue > 0:
            tax_amount = int(revenue * 0.12)
            rec = {
                "filing_id": next_filing(), "tax_type": "Business Tax",
                "filing_date": "2025-03-31",
                "pay_amount": tax_amount, "taxable_income": revenue,
                "tax_amount": tax_amount,
                "src_id": brn, "src_domain": "Business Registry",
            }
            write_xml(os.path.join(OUTPUT_DIR, f"tx-{cuid_generator()}.xml"), build_instance(rec))
            count += 1

    # Background tax filings
    if not PERSONS:
        from civil_registry import generate as gen_cr
        gen_cr()

    bg = [p for p in PERSONS if p.get("key", "").startswith("bg_")][:20]
    for p in bg:
        income = random.randint(18000, 60000)
        tax_amount = int(income * 0.15)
        rec = {
            "filing_id": next_filing(), "tax_type": "Income Tax",
            "filing_date": random_date(2024, 2025),
            "pay_amount": tax_amount, "taxable_income": income,
            "tax_amount": tax_amount,
            "pay_method": random.choice(PAY_METHODS),
        }
        write_xml(os.path.join(OUTPUT_DIR, f"tx-{cuid_generator()}.xml"), build_instance(rec))
        count += 1

    print(f"Tax and Revenue: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    generate()
