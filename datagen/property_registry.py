"""
Generate Property Registry XML instances for CordovaOS demo.

Governance-composed model: Governed Record Item (Property Record data cluster
+ Provenance Components cluster), then native subject/provider/Audit/attestation
slots. Cast member residences + institutional + background properties.
Output: import_data/property_registry/
"""
import os
import random

from shared import (
    NA,
    scaled,
    CAST, PERSONS, random_city_province, random_address, random_date, random_name,
    generate_parcel, PROVINCE_CODES, CITY_CODES, CITY_TO_PROVINCE,
    xml_header, xml_preamble, xml_footer, write_xml,
    xdstring, xdtoken, xdtemporal, xdquantity,
    cluster_open, cluster_close, native_partytype,
    make_provenance_values, audit, attestation, cuid_generator,
)

CT_ID = "x44vt69qqri2bl7vwxb8ck7n"
DM_LABEL = "Property Registry"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "sdc4", "import_data", "property_registry")

# ─── Component → Wrapper mappings (from v2 governance template dm-*.xml) ──────

# Governance envelope: Item wrapper (Governed Record) + provenance cluster
GOVERNED_RECORD = "ms-jyx3v449tku745yxm6hte0eg"
CL_PROV         = "ms-hdhjfg00tngir2txgqyka9cv"

# Data cluster (Property Record). NOTE: the XSD sequence for this cluster lists
# the sub-clusters (Liens, Value, Transfer) BEFORE the scalar adapters, so
# emission order must follow suit (see build_instance).
CL_ROOT       = "ms-bgc4n3424bzb8gpgnjhxxha9"
W_PARCEL      = ("ms-hs7197k4s33eg7wbspgudu4u", "ms-x4e8k8g1uojewc6tdpt9t5yv")
W_ADDR1       = ("ms-l338k7nlvnq2am0owa19yxfc", "ms-ny0rsony9tpielhbefce5l1j")
W_ADDR2       = ("ms-ek5h6dsqpd9kz0l4mcckmxpt", "ms-fnd5eqtqwl10obbslkttrqnh")
W_CITY        = ("ms-atdtdfzruh7tya0iv5cz365l", "ms-jc4b7oxzp0aw60nqaczhqwf8")
W_PROP_STATUS = ("ms-xtljf8q6rfyfewdkgu4e5ouj", "ms-mdmo6qt9lop46jta9ev17t0n")
W_PROP_TYPE   = ("ms-l79ua955rihnjbrxyhu7z5ac", "ms-jdod00uzf3m9s59b98iaibgs")
W_PROVINCE    = ("ms-kv5qqs3o4jwcwz9javgw1pzh", "ms-w2v28k4z744jfpno33ab67p2")
W_REG_DATE    = ("ms-vo9jtmexkaaol3y657fm0xn8", "ms-fh0pqnu8d0nfx2yvyhcwh63b")

CL_LIENS      = "ms-tjkw46wy20kstzgg1y60clxx"
W_LIEN_STATUS = ("ms-kzalko16uuwdw74yohvr5t50", "ms-nh74asnvqqyz9jmqvnreq3oz")
W_LIEN_TYPE   = ("ms-cy92p3uebrmjf191wcs07t3o", "ms-onz6gcdg7dh7337mf6zn1l6w")
W_LIEN_AMT    = ("ms-da261k0tox4747gnkmmek15i", "ms-jvltpxpawjdlybxqkv8e883l")
W_LIEN_DATE   = ("ms-zicto01f2grmzuqtgdonv83w", "ms-c93mwzszezrgjw1n198haxiq")

CL_VALUE      = "ms-cexrgb7uy29kn6w27tpmujtv"
W_ASSESS_STAT = ("ms-j3y76yob1s958dry2d551tew", "ms-i2tiyvsynjio8e8uxoino4ye")
W_ASSESS_VAL  = ("ms-hlg1jmx1v9t4zkq16c1i66bg", "ms-s6axq01x3b13bizha9835168")
W_LAND_AREA   = ("ms-rbq2sjcb8h284c8dnzjdna5h", "ms-zicuiya98vrzmqki5xmhzd2q")

CL_TRANSFER   = "ms-vdf0oczbk8uxsm2le09l27ke"
W_TRANS_AMT   = ("ms-j8gn6xsrzbnzkqlnpk2dkwam", "ms-y7f9vpywfh64xlyn5jqsodc4")
W_TRANS_DATE  = ("ms-y6isg5qaxfpt1qpg102uwkn4", "ms-j13kh9kjqppr4q1uftft7xp5")

# Provenance Components leaves (component, adapter)
P_ACT_DESC    = ("ms-m9xg6e182m1oq77ssrf9iujv", "ms-wxh3ozwag8zszowx1gyxkjy3")
P_ACT_TYPE    = ("ms-ccj1yq2wtwknobszkgzzdbtr", "ms-da450ty7hz39wjwhws7nom94")
P_SYS_ID      = ("ms-bd3s8t23d6m3zizmpwavc32y", "ms-aojrjukmlrjecf0gguod2jp5")
P_LOC_ID      = ("ms-zr59goe24qkocprl3feul3mt", "ms-rvcd3crgw28j7osmm63cnuk3")
P_LOC_NAME    = ("ms-fnodzqkbyskwe7nh58rs336k", "ms-e0x6i4occnmtor5lg3uvrcm0")
P_TS_END      = ("ms-edvvjznmaoibzmfna0uuoo37", "ms-fkt9wapbdb7qqp5dz9ae4dxc")
P_TS_START    = ("ms-o72s5793973fzho35rnaughs", "ms-wc2gfcyp9kbryangjt8ny2c9")

# Domain's System Audit component (substitutionGroup="sdc4:Audit").
AUDIT_COMPONENT = "ms-fotc5adg15ek2b9ermx2mcih"

# ─── Enumerations (must match the model's XSD facets exactly) ─────────────────
PROP_TYPES     = ["Residential", "Commercial", "Agricultural", "Government", "Industrial"]
PROP_STATUSES  = ["Active", "Encumbered", "In Transfer", "Government Seized", "Abandoned"]
LIEN_STATUSES  = ["Active", "Satisfied", "Released"]
LIEN_TYPES     = ["Mortgage", "Tax Lien", "Judgment Lien", "Mechanic's Lien", "Easement"]
ASSESS_STATUSES = ["Final", "Under Appeal", "Preliminary"]
WORKFLOW_STATES = ["Registered", "Assessed", "Transferred", "Certified"]

COR = "Cordova Córdoba (COR)"


def build_instance(prop):
    """Build a governance-composed Property Registry XML instance for one property."""
    # System name kept short so the derived urn:cordova:system:<slug>
    # system_identifier stays within the provenance leaf's maxLength=50 facet.
    prov = make_provenance_values("Cordova Property Registry",
                                  "PropertyRegistration", prop["city"])
    state = random.choice(WORKFLOW_STATES)

    xml = xml_header(CT_ID)
    xml += xml_preamble(DM_LABEL, current_state=state)

    # Item: Governed Record wrapper
    xml += cluster_open(GOVERNED_RECORD, "Property Registry Governed Record", indent=1)

    # Data cluster. The Property Record XSD sequence lists the sub-clusters
    # (Liens, Value, Transfer) BEFORE the scalar adapters, so emit them first.
    xml += cluster_open(CL_ROOT, "Property Record", indent=2)

    xml += cluster_open(CL_LIENS, "Liens and Encumbrances", indent=3)
    xml += xdtoken(*W_LIEN_STATUS, "Lien Status", prop.get("lien_status", "Released"), indent=4)
    xml += xdtoken(*W_LIEN_TYPE, "Lien Type", prop.get("lien_type", "Easement"), indent=4)
    xml += xdquantity(*W_LIEN_AMT, "Lien Amount", prop.get("lien_amt", "0"), COR, indent=4)
    xml += xdtemporal(*W_LIEN_DATE, "Lien Date", prop.get("lien_date", NA), "date", indent=4)
    xml += cluster_close(CL_LIENS, indent=3)

    xml += cluster_open(CL_VALUE, "Property Value Assessment", indent=3)
    xml += xdtoken(*W_ASSESS_STAT, "Assessment Status", prop.get("assess_status", "Final"), indent=4)
    xml += xdquantity(*W_ASSESS_VAL, "Assessed Value", prop["value"], COR, indent=4)
    xml += xdquantity(*W_LAND_AREA, "Land Area", prop["area"], "Square Meters", indent=4)
    xml += cluster_close(CL_VALUE, indent=3)

    xml += cluster_open(CL_TRANSFER, "Transfer History", indent=3)
    xml += xdquantity(*W_TRANS_AMT, "Transfer Amount", prop.get("trans_amt", prop["value"]), COR, indent=4)
    xml += xdtemporal(*W_TRANS_DATE, "Transfer Date", prop["reg_date"], "date", indent=4)
    xml += cluster_close(CL_TRANSFER, indent=3)

    xml += xdstring(*W_PARCEL, "Parcel Number", prop["parcel"], indent=3)
    xml += xdstring(*W_ADDR1, "Address (Line 1)", prop["addr"], indent=3)
    xml += xdstring(*W_ADDR2, "Address (Line 2)", prop.get("addr2", ""), indent=3)
    xml += xdtoken(*W_CITY, "City", prop["city"], indent=3)
    xml += xdtoken(*W_PROP_STATUS, "Property Status", prop.get("status", "Active"), indent=3)
    xml += xdtoken(*W_PROP_TYPE, "Property Type (Cordova)", prop["prop_type"], indent=3)
    xml += xdtoken(*W_PROVINCE, "Province", prop["province"], indent=3)
    xml += xdtemporal(*W_REG_DATE, "Registration Date", prop["reg_date"], "date", indent=3)
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
    xml += native_partytype("subject", "Property Owner", prop.get("owner", "Property Owner"))
    xml += native_partytype("provider", "Property Registry Office",
                            f"{prop['city']} Property Registry Office")
    xml += audit(AUDIT_COMPONENT, prov["activity_timestamp_start"],
                 system_id_value=prov["system_identifier"])
    xml += attestation(pending=False, reason="Property record certified by the registry office",
                       committer="Property Registry Office", committed=prov["activity_timestamp_end"])

    xml += xml_footer(CT_ID)
    return xml


def _lien_fields(value):
    """Return schema-valid lien fields; a minority of properties carry a real lien."""
    if random.random() < 0.25:
        cap = max(5000, int(value) // 2)
        return {
            "status": "Encumbered",
            "lien_status": random.choice(["Active", "Satisfied"]),
            "lien_type": random.choice(LIEN_TYPES),
            "lien_amt": str(random.randint(5000, cap)),
            "lien_date": random_date(2010, 2024),
        }
    return {
        "status": "Active",
        "lien_status": "Released",
        "lien_type": "Easement",
        "lien_amt": "0",
        "lien_date": NA,
    }


def generate():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    count = 0

    # Cast member residences
    for key, c in CAST.items():
        prov = c["province"]
        city = c["city"]
        pc = PROVINCE_CODES[prov]
        cc = CITY_CODES[city]
        value = random.randint(80000, 350000)
        prop = {
            "parcel": generate_parcel(pc, cc),
            "addr": c["address"], "addr2": c.get("address2", ""),
            "city": city, "province": prov,
            "prop_type": "Residential",
            "reg_date": random_date(2005, 2020),
            "value": str(value),
            "area": str(random.randint(80, 500)),
            "assess_status": random.choice(ASSESS_STATUSES),
            "owner": f"{c['given']} {c['surname']}",
        }
        prop.update(_lien_fields(value))
        xml = build_instance(prop)
        write_xml(os.path.join(OUTPUT_DIR, f"pr-{cuid_generator()}.xml"), xml)
        count += 1

    # Key institutional properties
    institutions = [
        ("Porto Sereno General Hospital", "Porto Sereno", "Aldara", "Government", 5000),
        ("Universidad Nacional de Cordova", "Campoluz", "Brevina", "Government", 25000),
        ("Porto Sereno Port Terminal", "Porto Sereno", "Aldara", "Commercial", 15000),
        ("Cordova National Police HQ", "Novaciudad", "Celara", "Government", 3000),
    ]
    for name, city, prov, ptype, area in institutions:
        pc = PROVINCE_CODES[prov]
        cc = CITY_CODES[city]
        value = random.randint(500000, 5000000)
        prop = {
            "parcel": generate_parcel(pc, cc),
            "addr": f"1 {name}", "addr2": "",
            "city": city, "province": prov,
            "prop_type": ptype,
            "reg_date": random_date(1980, 2010),
            "value": str(value),
            "area": str(area),
            "assess_status": "Final",
            "owner": name,
            "status": "Active", "lien_status": "Released",
            "lien_type": "Easement", "lien_amt": "0", "lien_date": NA,
        }
        xml = build_instance(prop)
        write_xml(os.path.join(OUTPUT_DIR, f"pr-{cuid_generator()}.xml"), xml)
        count += 1

    # Background properties (~7,988 to reach ~8,000 total)
    bg_prop_types = (
        ["Residential"] * 65 +
        ["Commercial"] * 25 +
        ["Agricultural"] * 7 +
        ["Industrial"] * 3
    )
    for _ in range(scaled(7988, 94)):
        city, prov = random_city_province()
        pc = PROVINCE_CODES[prov]
        cc = CITY_CODES[city]
        pt = random.choice(bg_prop_types)
        if pt == "Residential":
            value = random.randint(40000, 350000)
            area = random.randint(60, 400)
        elif pt == "Commercial":
            value = random.randint(100000, 1500000)
            area = random.randint(100, 2000)
        elif pt == "Agricultural":
            value = random.randint(20000, 500000)
            area = random.randint(500, 10000)
        else:  # Industrial
            value = random.randint(200000, 3000000)
            area = random.randint(500, 5000)
        given, _, surname = random_name(random.choice(["Male", "Female"]))
        prop = {
            "parcel": generate_parcel(pc, cc),
            "addr": random_address(), "addr2": "",
            "city": city, "province": prov,
            "prop_type": pt,
            "reg_date": random_date(1980, 2024),
            "value": str(value),
            "area": str(area),
            "assess_status": random.choice(ASSESS_STATUSES),
            "owner": f"{given} {surname}",
        }
        prop.update(_lien_fields(value))
        xml = build_instance(prop)
        write_xml(os.path.join(OUTPUT_DIR, f"pr-{cuid_generator()}.xml"), xml)
        count += 1

    print(f"Property Registry: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    generate()
