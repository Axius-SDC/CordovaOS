"""
Tax and Revenue Record 4.4.0: one record per filing.

The model composes Cordova's own filing, assessment, payment and source
reference clusters with the CID (individual filers) and the Business Registry
Number (business filers), so a filing joins the taxpayer's civil or business
record on the identifier itself. Every amount is a quantity in the Cordova
Córdoba (COR). Cast income filings, business filings for every registered
business, and income filings for 85% of working-age residents.
"""
import random

from business_registry import employer_roster
from shared import (
    COR, CAST, PERSONS, Quantity,
    random_date, full_name, record, write_record, import_dir,
)

TITLE = "Tax and Revenue Record"
SYSTEM = "Cordova Tax and Revenue System"
OUTPUT_DIR = import_dir("tax_and_revenue_record")
AUTHORITY = "Cordova National Revenue Authority"

# The model's payment method codes; Cordova's bank transfers and payroll deductions have no code of their own.
PAY_METHODS = {"Bank Transfer": "Other", "Check": "Check", "Cash": "Cash", "Payroll Deduction": "Other"}
PAY_STATUSES = ["Paid", "Paid", "Paid", "Invoiced", "Overdue"]
# The payment workflow: the state follows the payment. (4.3.1's Filed/Assessed/Closed were labels with no workflow behind them.)
STATE_OF = {"Paid": "PaymentComplete", "Invoiced": "PaymentDue", "Overdue": "PaymentPastDue"}

_filing_counter = 0


def next_filing():
    global _filing_counter
    _filing_counter += 1
    return f"TF-2025-{_filing_counter:06d}"


def _registered_name(brn):
    for biz in employer_roster():
        if biz["brn"] == brn:
            return biz["name"]
    return None


def build_instance(rec):
    """One Tax and Revenue record for one filing."""
    pay_status = rec.get("pay_status", "Paid")
    values = {
        "Tax Filing/Filing ID": rec["filing_id"],
        "Tax Filing/National ID (CID)": rec.get("cid"),
        "Tax Filing/Business Registry Number": rec.get("brn"),
        "Tax Filing/Tax Type": rec["tax_type"],
        "Tax Filing/Tax Filing Status": rec["filing_status"],
        "Tax Filing/Filing Date": rec["filing_date"],
        "Tax Assessment/Taxable Income": Quantity(str(rec["taxable_income"]), COR),
        "Tax Assessment/Tax Assessment Amount": Quantity(str(rec["tax_amount"]), COR),
        "Payment/Payment Amount": Quantity(str(rec["pay_amount"]), COR),
        "Payment/Payment Status": pay_status,
        "Payment/Payment Method Code": PAY_METHODS[rec.get("pay_method", "Bank Transfer")],
        "Payment/Payment Date": rec["pay_date"] if pay_status == "Paid" else None,
        "Source Reference/Source Domain": rec["src_domain"],
        "Source Reference/Source Record ID": rec.get("brn") or rec.get("cid"),
    }
    return record(TITLE, values, state=STATE_OF[pay_status], system=SYSTEM, activity_type="TaxAssessment",
                  when=rec["filing_date"], city=rec["city"], province=rec["province"], cid=rec.get("cid"),
                  subject=("Taxpayer", rec["taxpayer_name"]), provider=("Revenue Authority", AUTHORITY),
                  attestation_reason=f"Filing assessed by the {AUTHORITY}", committer=AUTHORITY)


def _pay_date(filing_date):
    y, m, d = filing_date.split("-")
    m = int(m) + 1
    return f"{int(y) + (m > 12)}-{(m - 1) % 12 + 1:02d}-{d}"


def generate():
    count = 0

    # Income tax for cast members
    cast_incomes = {"carlos": 28000, "elena": 65000, "dr_reyes": 95000, "governor_avila": 120000,
                    "sgt_santos": 42000, "dr_ferrer": 88000, "dr_gutierrez": 72000, "prof_lucero": 74000}
    for key, income in cast_incomes.items():
        c = CAST[key]
        tax_amount = int(income * 0.15)
        rec = {"filing_id": next_filing(), "tax_type": "Income Tax", "filing_status": "Individual",
               "filing_date": "2025-04-15", "pay_date": "2025-05-15", "pay_status": "Paid", "pay_method": "Payroll Deduction",
               "pay_amount": tax_amount, "taxable_income": income, "tax_amount": tax_amount, "src_domain": "Employment",
               "taxpayer_name": full_name(c), "cid": c["cid"], "city": c["city"], "province": c["province"]}
        write_record(OUTPUT_DIR, "tx", build_instance(rec))
        count += 1

    # Business tax for the narrative businesses (only the non-exempt one files)
    narrative_brns = [("BIZ-001102", 2500000), ("BIZ-000847", 0), ("BIZ-000523", 0), ("BIZ-000101", 0), ("BIZ-000205", 0)]
    roster = {b["brn"]: b for b in employer_roster()}
    for brn, revenue in narrative_brns:
        if revenue > 0:
            biz = roster.get(brn, {})
            tax_amount = int(revenue * 0.12)
            rec = {"filing_id": next_filing(), "tax_type": "Business Tax", "filing_status": "Business",
                   "filing_date": "2025-03-31", "pay_date": "2025-04-30", "pay_status": "Paid", "pay_method": "Bank Transfer",
                   "pay_amount": tax_amount, "taxable_income": revenue, "tax_amount": tax_amount, "src_domain": "Business Registry",
                   "taxpayer_name": _registered_name(brn) or "Pacifico Meridional Shipping S.A.", "brn": brn,
                   "city": biz.get("city", "Porto Sereno"), "province": biz.get("province", "Aldara")}
            write_record(OUTPUT_DIR, "tx", build_instance(rec))
            count += 1

    # One business filing per registered business that has not filed above; the BRN comes from the registry.
    filed = {b for b, _ in narrative_brns}
    for biz in [b for b in employer_roster() if b["brn"] not in filed]:
        revenue = random.randint(50000, 3000000)
        tax_amount = int(revenue * 0.12)
        filing_date = random_date(2024, 2025)
        rec = {"filing_id": next_filing(), "tax_type": "Business Tax", "filing_status": "Business",
               "filing_date": filing_date, "pay_date": _pay_date(filing_date),
               "pay_method": random.choice(list(PAY_METHODS)), "pay_status": random.choice(PAY_STATUSES),
               "pay_amount": tax_amount, "taxable_income": revenue, "tax_amount": tax_amount, "src_domain": "Business Registry",
               "taxpayer_name": biz["name"], "brn": biz["brn"], "city": biz["city"], "province": biz["province"]}
        write_record(OUTPUT_DIR, "tx", build_instance(rec))
        count += 1

    # Individual income tax for 85% of working-age residents
    if not PERSONS:
        from civil_registry import generate as gen_cr
        gen_cr()
    working_age = [p for p in PERSONS if p.get("key", "").startswith("bg_") and 18 <= (2026 - int(p["dob"][:4])) <= 67]
    for p in random.sample(working_age, k=int(len(working_age) * 0.85)):
        income = random.randint(15000, 80000)
        tax_amount = int(income * 0.15)
        filing_date = random_date(2024, 2025)
        rec = {"filing_id": next_filing(), "tax_type": "Income Tax", "filing_status": random.choice(["Individual", "Individual", "Joint"]),
               "filing_date": filing_date, "pay_date": _pay_date(filing_date),
               "pay_method": random.choice(list(PAY_METHODS)), "pay_status": random.choice(PAY_STATUSES),
               "pay_amount": tax_amount, "taxable_income": income, "tax_amount": tax_amount, "src_domain": "Employment",
               "taxpayer_name": full_name(p), "cid": p["cid"], "city": p["city"], "province": p["province"]}
        write_record(OUTPUT_DIR, "tx", build_instance(rec))
        count += 1

    print(f"Tax and Revenue: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    from civil_registry import generate as gen_cr
    from business_registry import generate as gen_br
    random.seed("cordovaos:Civil Registry"); gen_cr()
    random.seed("cordovaos:Business Registry"); gen_br()
    random.seed("cordovaos:Tax & Revenue"); generate()
