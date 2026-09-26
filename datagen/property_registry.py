"""
Property Registry 4.4.0: one record per parcel.

The model composes the NIEM location (address, geolocation, locale) with
Cordova's own parcel number, owner CID, city, province and property statuses,
and Cordova-owned clusters for the value assessment, the lien and the transfer.
Every amount is a quantity in the Cordova Córdoba (COR). Cast residences, four
institutional parcels, and background parcels (7,988 full, 94 demo) whose owners
are residents from the Civil Registry, so the owner join on the CID is real.
"""
import random

from shared import (
    COR, CAST, PERSONS, Quantity, CITY_TO_PROVINCE, PROVINCE_CODES, CITY_CODES,
    scaled, random_city_province, random_address, random_date, generate_parcel, full_name,
    record, write_record, import_dir,
)

TITLE = "Property Registry"
SYSTEM = "Cordova Property Registry"
OUTPUT_DIR = import_dir("property_registry")

LIEN_TYPES = ["Mortgage", "Tax Lien", "Judgment Lien", "Mechanic's Lien", "Easement"]
LIEN_HOLDERS = ["Banco Nacional de Cordova", "Cordova National Revenue Authority", "Caja de Ahorros Aldara", "Banco del Pacifico Meridional"]
ASSESS_STATUSES = ["Final", "Under Appeal", "Preliminary"]
BG_PROP_TYPES = ["Residential"] * 65 + ["Commercial"] * 25 + ["Agricultural"] * 7 + ["Industrial"] * 3


def _state(prop):
    """The asset-status workflow: a registered parcel is Completed; one whose assessment is still preliminary is
    UnderDevelopment; an abandoned or seized one is Withdrawn. (4.3.1's Registered/Assessed/Transferred/Certified
    were labels with no workflow behind them.)"""
    if prop["status"] in ("Abandoned", "Government Seized"):
        return "Withdrawn"
    if prop["assess_status"] == "Preliminary":
        return "UnderDevelopment"
    return "Completed"


def build_instance(prop):
    """One Property Registry record for one parcel."""
    values = {
        "Property Record/Parcel Number": prop["parcel"],
        "Property Record/National ID (CID)": prop.get("owner_cid"),   # institutions have none
        "Property Record/City": prop["city"],
        "Property Record/Province": prop["province"],
        "Property Record/Property Type (Cordova)": prop["prop_type"],
        "Property Record/Property Status": prop["status"],
        "Property Record/Registration Date": prop["reg_date"],
        "Property Value Assessment/Assessed Value": Quantity(prop["value"], COR),
        "Property Value Assessment/Area": Quantity(prop["area"], "m2"),
        "Property Value Assessment/Assessment Status": prop["assess_status"],
        "Address (NIEM)/International Address/Address (Line 1)": prop["addr"],
        "Address (NIEM)/International Address/Address (Line 2)": prop.get("addr2") or None,
        "Address (NIEM)/International Address/City Name": prop["city"],
        "Address (NIEM)/International Address/Region Name": prop["province"],
        "Location (NIEM)/Location Name": prop["owner"] if not prop.get("owner_cid") else None,   # an institution's parcel is named for it
        "Location (NIEM)/Location Category": prop["prop_type"],
    }
    lien = prop.get("lien")
    if lien:
        values.update({
            "Lien/Lien Type": lien["type"],
            "Lien/Lien Status": lien["status"],
            "Lien/Lien Amount": Quantity(lien["amount"], COR),
            "Lien/Lien Date": lien["date"],
            "Lien/Lien Holder": lien["holder"],
        })
    return record(TITLE, values, state=_state(prop), system=SYSTEM, activity_type="PropertyRegistration",
                  when=prop["reg_date"], city=prop["city"], province=prop["province"], cid=prop.get("owner_cid"),
                  subject=("Property Owner", prop["owner"]), provider=("Property Registry Office", f"{prop['city']} Property Registry Office"),
                  attestation_reason="Registration certified by the property registry office", committer="Property Registry Office")


def _lien(value):
    """A minority of parcels carry a lien; the rest carry none, and say nothing about one."""
    if random.random() < 0.25:
        cap = max(5000, int(value) // 2)
        return {"type": random.choice(LIEN_TYPES), "status": random.choice(["Active", "Satisfied"]),
                "amount": str(random.randint(5000, cap)), "date": random_date(2010, 2024), "holder": random.choice(LIEN_HOLDERS)}
    return None


def _status(lien):
    return "Encumbered" if lien and lien["status"] == "Active" else "Active"


def generate():
    count = 0

    # Cast residences
    for key, c in CAST.items():
        prov, city = c["province"], c["city"]
        value = random.randint(80000, 350000)
        lien = _lien(value)
        prop = {
            "parcel": generate_parcel(PROVINCE_CODES[prov], CITY_CODES[city]),
            "addr": c["address"], "addr2": c.get("address2", ""),
            "city": city, "province": prov, "prop_type": "Residential",
            "reg_date": random_date(2005, 2020), "value": str(value), "area": str(random.randint(80, 500)),
            "assess_status": random.choice(ASSESS_STATUSES),
            "owner": full_name(c), "owner_cid": c["cid"], "lien": lien, "status": _status(lien),
        }
        write_record(OUTPUT_DIR, "pr", build_instance(prop))
        count += 1

    # Key institutional parcels
    institutions = [
        ("Porto Sereno General Hospital", "Porto Sereno", "Aldara", "Government", 5000),
        ("Universidad Nacional de Cordova", "Campoluz", "Brevina", "Government", 25000),
        ("Porto Sereno Port Terminal", "Porto Sereno", "Aldara", "Commercial", 15000),
        ("Cordova National Police HQ", "Novaciudad", "Celara", "Government", 3000),
    ]
    for name, city, prov, ptype, area in institutions:
        prop = {
            "parcel": generate_parcel(PROVINCE_CODES[prov], CITY_CODES[city]),
            "addr": f"1 {name}", "addr2": "", "city": city, "province": prov, "prop_type": ptype,
            "reg_date": random_date(1980, 2010), "value": str(random.randint(500000, 5000000)), "area": str(area),
            "assess_status": "Final", "owner": name, "owner_cid": None, "lien": None, "status": "Active",
        }
        write_record(OUTPUT_DIR, "pr", build_instance(prop))
        count += 1

    # Background parcels, owned by residents of the same city
    if not PERSONS:
        from civil_registry import generate as gen_cr
        gen_cr()
    adults_by_city = {}
    for p in PERSONS:
        if p.get("key", "").startswith("bg_") and (2026 - int(p["dob"][:4])) >= 18:
            adults_by_city.setdefault(p["city"], []).append(p)
    for _ in range(scaled(7988, 94)):
        city, prov = random_city_province()
        pt = random.choice(BG_PROP_TYPES)
        if pt == "Residential":
            value, area = random.randint(40000, 350000), random.randint(60, 400)
        elif pt == "Commercial":
            value, area = random.randint(100000, 1500000), random.randint(100, 2000)
        elif pt == "Agricultural":
            value, area = random.randint(20000, 500000), random.randint(500, 10000)
        else:
            value, area = random.randint(200000, 3000000), random.randint(500, 5000)
        owner = random.choice(adults_by_city.get(city) or [p for ps in adults_by_city.values() for p in ps])
        lien = _lien(value)
        prop = {
            "parcel": generate_parcel(PROVINCE_CODES[prov], CITY_CODES[city]),
            "addr": random_address(), "addr2": "", "city": city, "province": prov, "prop_type": pt,
            "reg_date": random_date(1980, 2024), "value": str(value), "area": str(area),
            "assess_status": random.choice(ASSESS_STATUSES),
            "owner": full_name(owner), "owner_cid": owner["cid"], "lien": lien, "status": _status(lien),
        }
        write_record(OUTPUT_DIR, "pr", build_instance(prop))
        count += 1

    print(f"Property Registry: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    from civil_registry import generate as gen_cr
    random.seed("cordovaos:Civil Registry"); gen_cr()
    random.seed("cordovaos:Property Registry"); generate()
