"""
Generate Property Registry XML instances for CordovaOS demo.

Cast member residences + background properties.
Output: import_data/property_registry/
"""
import os
import random

from shared import (
    CAST, PERSONS, random_city_province, random_address, random_date,
    generate_parcel, PROVINCE_CODES, CITY_CODES, CITY_TO_PROVINCE,
    xml_header, xml_preamble, xml_footer, write_xml,
    xdstring, xdtoken, xdtemporal, xdquantity,
    cluster_open, cluster_close, party_stub,
    cuid_generator,
)

CT_ID = "x44vt69qqri2bl7vwxb8ck7n"
DM_LABEL = "Property Registry"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "sdc4", "import_data", "property_registry")

CL_ROOT       = "ms-bgc4n3424bzb8gpgnjhxxha9"
W_PARCEL      = ("ms-hs7197k4s33eg7wbspgudu4u", "ms-jkm0hop0jgs66z00kc6w9hvr")
W_ADDR1       = ("ms-l338k7nlvnq2am0owa19yxfc", "ms-sgw8qc0ybwwnl635cpizw1hl")
W_ADDR2       = ("ms-ek5h6dsqpd9kz0l4mcckmxpt", "ms-c4ngbzw39b1bvv6kf0omwhyd")
W_CITY        = ("ms-atdtdfzruh7tya0iv5cz365l", "ms-fqungc7f5kgfoz5qzmqi10bb")
W_PROP_STATUS = ("ms-xtljf8q6rfyfewdkgu4e5ouj", "ms-zk5qub7yt9hqndjhtmamrtzi")
W_PROP_TYPE   = ("ms-l79ua955rihnjbrxyhu7z5ac", "ms-p8cg8z82t0g4siccgmavagnx")
W_PROVINCE    = ("ms-kv5qqs3o4jwcwz9javgw1pzh", "ms-hdlgnjtjlqp4m5wjb9st8z8y")
W_REG_DATE    = ("ms-vo9jtmexkaaol3y657fm0xn8", "ms-wldymso9fl20lk4o8sm9kxsf")

CL_LIENS      = "ms-tjkw46wy20kstzgg1y60clxx"
W_LIEN_STATUS = ("ms-kzalko16uuwdw74yohvr5t50", "ms-ckvqjw4u56fma8fz2dxnv8be")
W_LIEN_TYPE   = ("ms-cy92p3uebrmjf191wcs07t3o", "ms-q0jgr01zl99zkt1f7bcqqm78")
W_LIEN_AMT    = ("ms-da261k0tox4747gnkmmek15i", "ms-b63hvh2c16a1prkj0fr859a0")
W_LIEN_DATE   = ("ms-zicto01f2grmzuqtgdonv83w", "ms-eo098i5l0zk4ppodpbvj8ojz")

CL_VALUE      = "ms-cexrgb7uy29kn6w27tpmujtv"
W_ASSESS_STAT = ("ms-j3y76yob1s958dry2d551tew", "ms-bd10l1zomg0x8bfr7nmt2qai")
W_ASSESS_VAL  = ("ms-hlg1jmx1v9t4zkq16c1i66bg", "ms-tg04fq61sbdf86c91ozd9ami")
W_LAND_AREA   = ("ms-rbq2sjcb8h284c8dnzjdna5h", "ms-r4tq1hz5ty5hs8397yjeif7k")

CL_TRANSFER   = "ms-vdf0oczbk8uxsm2le09l27ke"
W_TRANS_AMT   = ("ms-j8gn6xsrzbnzkqlnpk2dkwam", "ms-env90oec8uo1463kzgrl5zxw")
W_TRANS_DATE  = ("ms-y6isg5qaxfpt1qpg102uwkn4", "ms-wmx335x1c0nok4ibrfifseor")

PS_OWNER      = "ms-rnts5ygyfvpor7vvk0gn96uq"
PS_OFFICE     = "ms-ji4myggtxrapitnioimmzm7i"

PROP_TYPES = ["Residential", "Commercial", "Agricultural", "Industrial", "Government"]
PROP_STATUSES = ["Active", "Encumbered", "Vacant"]


def build_instance(prop):
    xml = xml_header(CT_ID)
    xml += xml_preamble(DM_LABEL)
    xml += cluster_open(CL_ROOT, "Property Record")

    xml += xdstring(*W_PARCEL, "Parcel Number", prop["parcel"])
    xml += xdstring(*W_ADDR1, "Address (Line 1)", prop["addr"])
    xml += xdstring(*W_ADDR2, "Address (Line 2)", prop.get("addr2", ""))
    xml += xdtoken(*W_CITY, "City", prop["city"])
    xml += xdtoken(*W_PROP_STATUS, "Property Status", prop.get("status", "Active"))
    xml += xdtoken(*W_PROP_TYPE, "Property Type (Cordova)", prop["prop_type"])
    xml += xdtoken(*W_PROVINCE, "Province", prop["province"])
    xml += xdtemporal(*W_REG_DATE, "Registration Date", prop["reg_date"], "date")

    # Liens
    xml += cluster_open(CL_LIENS, "Liens and Encumbrances", indent=2)
    xml += xdtoken(*W_LIEN_STATUS, "Lien Status", prop.get("lien_status", "Clear"), indent=3)
    xml += xdtoken(*W_LIEN_TYPE, "Lien Type", prop.get("lien_type", "None"), indent=3)
    xml += xdquantity(*W_LIEN_AMT, "Lien Amount", prop.get("lien_amt", "0"),
                       "Cordova Córdoba (COR)", indent=3)
    xml += xdtemporal(*W_LIEN_DATE, "Lien Date", prop.get("lien_date", "1900-01-01"), "date", indent=3)
    xml += cluster_close(CL_LIENS, indent=2)

    # Value Assessment
    xml += cluster_open(CL_VALUE, "Property Value Assessment", indent=2)
    xml += xdtoken(*W_ASSESS_STAT, "Assessment Status", "Current", indent=3)
    xml += xdquantity(*W_ASSESS_VAL, "Assessed Value", prop["value"],
                       "Cordova Córdoba (COR)", indent=3)
    xml += xdquantity(*W_LAND_AREA, "Land Area", prop["area"],
                       "Square Meters", indent=3)
    xml += cluster_close(CL_VALUE, indent=2)

    # Transfer History
    xml += cluster_open(CL_TRANSFER, "Transfer History", indent=2)
    xml += xdquantity(*W_TRANS_AMT, "Transfer Amount", prop.get("trans_amt", prop["value"]),
                       "Cordova Córdoba (COR)", indent=3)
    xml += xdtemporal(*W_TRANS_DATE, "Transfer Date", prop["reg_date"], "date", indent=3)
    xml += cluster_close(CL_TRANSFER, indent=2)

    xml += cluster_close(CL_ROOT)
    xml += party_stub(PS_OWNER, "Property Owner")
    xml += party_stub(PS_OFFICE, "Property Registry Office")
    xml += xml_footer(CT_ID)
    return xml


def generate():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    count = 0

    # Cast member residences
    for key, c in CAST.items():
        prov = c["province"]
        city = c["city"]
        pc = PROVINCE_CODES[prov]
        cc = CITY_CODES[city]
        prop = {
            "parcel": generate_parcel(pc, cc),
            "addr": c["address"], "addr2": c.get("address2", ""),
            "city": city, "province": prov,
            "prop_type": "Residential",
            "reg_date": random_date(2005, 2020),
            "value": str(random.randint(80000, 350000)),
            "area": str(random.randint(80, 500)),
        }
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
        prop = {
            "parcel": generate_parcel(pc, cc),
            "addr": f"1 {name}", "addr2": "",
            "city": city, "province": prov,
            "prop_type": ptype,
            "reg_date": random_date(1980, 2010),
            "value": str(random.randint(500000, 5000000)),
            "area": str(area),
        }
        xml = build_instance(prop)
        write_xml(os.path.join(OUTPUT_DIR, f"pr-{cuid_generator()}.xml"), xml)
        count += 1

    # Background properties (~7,988 to reach ~8,000 total)
    # Mix: ~65% residential, ~25% commercial, ~10% agricultural/vacant
    bg_prop_types = (
        ["Residential"] * 65 +
        ["Commercial"] * 25 +
        ["Agricultural"] * 7 +
        ["Industrial"] * 3
    )
    for _ in range(7988):
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
        prop = {
            "parcel": generate_parcel(pc, cc),
            "addr": random_address(), "addr2": "",
            "city": city, "province": prov,
            "prop_type": pt,
            "reg_date": random_date(1980, 2024),
            "value": str(value),
            "area": str(area),
        }
        xml = build_instance(prop)
        write_xml(os.path.join(OUTPUT_DIR, f"pr-{cuid_generator()}.xml"), xml)
        count += 1

    print(f"Property Registry: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    generate()
