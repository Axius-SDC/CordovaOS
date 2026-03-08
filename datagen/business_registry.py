"""
Generate Business Registry XML instances for CordovaOS demo.

Key businesses from the Contagion narrative + background businesses.
Output: import_data/business_registry/
"""
import os
import random

from shared import (
    random_city_province, random_address, random_date,
    generate_brn, generate_phone, generate_email,
    xml_header, xml_preamble, xml_footer, write_xml,
    xdstring, xdtoken, xdtemporal,
    cluster_open, cluster_close, party_stub,
    cuid_generator, CITY_TO_PROVINCE,
)

CT_ID = "x250838l7oi6l3yavg9twc1i"
DM_LABEL = "Business Registry"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "sdc4", "import_data", "business_registry")

CL_ROOT       = "ms-uv8dwudhyf0gnmzgiyyd1sb1"
W_BRN         = ("ms-l8f0m7op4xhrxqy1jrnvbuly", "ms-iik8wu21w43f197q13uwj5tj")
W_ORG_NAME    = ("ms-uinddfbzfk0jdikmt1jwcq78", "ms-egqz7u61z4r0yn70pzpeawfx")
W_TAX_ID      = ("ms-gu15c6jojx09jy9at1px0ufh", "ms-dst4rs3cigy3hct9gijdahf1")
W_BIZ_TYPE    = ("ms-puz7m7a7rtuehrgp10tm17qn", "ms-zhk32m1ap1kuqnv5yt0lo4f4")
W_INDUSTRY    = ("ms-m0i63npis09ch7ag08ntoneu", "ms-ziymknoa7ci95zdnqbeytn9h")
W_STATUS      = ("ms-cs34ekiq4o9pazzs5baiobis", "ms-wxth7g1d0op9md99qm7441om")
W_REG_DATE    = ("ms-vo9jtmexkaaol3y657fm0xn8", "ms-sxq8qyzr6venrfbc4mqczc5b")

CL_ADDR       = "ms-u8kz7rlfx1jjvkn7kgyao4tw"
W_EMAIL       = ("ms-x0na649n17if0ukul82cmrx3", "ms-bt9jm8o81vgp1d0lp4uqjkzo")
W_PHONE       = ("ms-nfrvvp87c5imu5h9ups92kgy", "ms-rcrcco6ap8fp5f6l0gi7jcsw")
W_ADDR1       = ("ms-l338k7nlvnq2am0owa19yxfc", "ms-fe9vv9dybwtb9jxt3d7q5y92")
W_ADDR2       = ("ms-ek5h6dsqpd9kz0l4mcckmxpt", "ms-og8ysbvvwlw8ndxiih0of8cf")
W_CITY        = ("ms-atdtdfzruh7tya0iv5cz365l", "ms-dg4xea1arkqi12h9dpluz4yg")
W_PROVINCE    = ("ms-kv5qqs3o4jwcwz9javgw1pzh", "ms-c4xrmr6sx6hp779zcq870oh7")

PS_OFFICER    = "ms-d79vg5e2e4nnoxontodl9co7"
PS_OFFICE     = "ms-pndsgg7zczz4bgnmh11g40ka"

# Contagion narrative businesses
BUSINESSES = [
    {"brn": "BIZ-001102", "name": "Pacifico Meridional Shipping S.A.", "tax_id": "TAX-PM-001102",
     "biz_type": "Corporation", "industry": "Maritime Transport",
     "city": "Porto Sereno", "province": "Aldara",
     "addr": "1 Paseo del Puerto", "addr2": "Terminal Building",
     "email": "info@pacifico-meridional.cor", "phone": "+99-100-800-1102"},
    {"brn": "BIZ-000847", "name": "Universidad Nacional de Cordova", "tax_id": "TAX-UNC-000847",
     "biz_type": "Public Institution", "industry": "Higher Education",
     "city": "Campoluz", "province": "Brevina",
     "addr": "100 Avenida Universidad", "addr2": "Main Campus",
     "email": "admin@unc.cor", "phone": "+99-200-800-0847"},
    {"brn": "BIZ-000523", "name": "Porto Sereno General Hospital", "tax_id": "TAX-PSGH-000523",
     "biz_type": "Public Institution", "industry": "Healthcare",
     "city": "Porto Sereno", "province": "Aldara",
     "addr": "50 Boulevard Costero", "addr2": "",
     "email": "admin@psgh.cor", "phone": "+99-100-800-0523"},
    {"brn": "BIZ-000101", "name": "Cordova National Police", "tax_id": "TAX-CNP-000101",
     "biz_type": "Government Agency", "industry": "Law Enforcement",
     "city": "Novaciudad", "province": "Celara",
     "addr": "1 Calle Mayor", "addr2": "National HQ",
     "email": "admin@cnp.cor", "phone": "+99-300-800-0101"},
    {"brn": "BIZ-000205", "name": "Provincial Health Office - Aldara", "tax_id": "TAX-PHO-000205",
     "biz_type": "Government Agency", "industry": "Public Health",
     "city": "Porto Sereno", "province": "Aldara",
     "addr": "15 Avenida Nacional", "addr2": "",
     "email": "health@aldara.gov.cor", "phone": "+99-100-800-0205"},
]

BACKGROUND_TYPES = ["Corporation", "Sole Proprietorship", "Partnership", "Cooperative", "NGO"]
BACKGROUND_INDUSTRIES = [
    "Retail", "Agriculture", "Fishing", "Construction", "Tourism",
    "Restaurant", "Manufacturing", "Finance", "Technology", "Legal Services",
    "Real Estate", "Import/Export", "Automotive", "Pharmacy", "Insurance",
]
BACKGROUND_NAMES = [
    "Cordova Coffee Exporters", "Isla Verde Farms", "Costa Azul Tours",
    "Mendoza Construction S.A.", "Bahia Pescadores Coop",
    "Sierra Tech Solutions", "Novaciudad Legal Associates",
    "Campoluz Agricultural Supply", "Porto Sereno Fish Market",
    "Estrella Insurance Group", "Rios Pharmacy Chain",
    "Cardenas Real Estate", "Montecalvo Automotive",
    "Lago Azul Resort", "Tierra Roja Mining Co.",
    "Cordova National Bank", "Central Market Co-op",
    "Pacific Telecommunications", "Isla Import/Export Ltd.",
    "Brevina Textiles S.A.",
]


def build_instance(biz):
    xml = xml_header(CT_ID)
    xml += xml_preamble(DM_LABEL)
    xml += cluster_open(CL_ROOT, "Business Entity")
    xml += xdstring(*W_BRN, "Business Registry Number", biz["brn"])
    xml += xdstring(*W_ORG_NAME, "Organization Name", biz["name"])
    xml += xdstring(*W_TAX_ID, "Organization Tax ID", biz["tax_id"])
    xml += xdtoken(*W_BIZ_TYPE, "Business Type (Cordova)", biz["biz_type"])
    xml += xdtoken(*W_INDUSTRY, "Industry", biz["industry"])
    xml += xdtoken(*W_STATUS, "Status", "Active")
    xml += xdtemporal(*W_REG_DATE, "Registration Date", biz["reg_date"], "date")

    xml += cluster_open(CL_ADDR, "Registered Address", indent=2)
    xml += xdstring(*W_EMAIL, "Cordova Email Address", biz["email"], indent=3)
    xml += xdstring(*W_PHONE, "Cordova Phone Number", biz["phone"], indent=3)
    xml += xdstring(*W_ADDR1, "Address (Line 1)", biz["addr"], indent=3)
    xml += xdstring(*W_ADDR2, "Address (Line 2)", biz.get("addr2", ""), indent=3)
    xml += xdtoken(*W_CITY, "City", biz["city"], indent=3)
    xml += xdtoken(*W_PROVINCE, "Province", biz["province"], indent=3)
    xml += cluster_close(CL_ADDR, indent=2)

    xml += cluster_close(CL_ROOT)
    xml += party_stub(PS_OFFICER, "Business Officer")
    xml += party_stub(PS_OFFICE, "Business Registry Office")
    xml += xml_footer(CT_ID)
    return xml


def generate():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    count = 0

    # Named businesses
    for biz in BUSINESSES:
        biz["reg_date"] = random_date(1990, 2020)
        xml = build_instance(biz)
        write_xml(os.path.join(OUTPUT_DIR, f"br-{cuid_generator()}.xml"), xml)
        count += 1

    # Background businesses
    for i, name in enumerate(BACKGROUND_NAMES):
        city, province = random_city_province()
        brn = generate_brn()
        biz = {
            "brn": brn, "name": name,
            "tax_id": f"TAX-{brn}",
            "biz_type": random.choice(BACKGROUND_TYPES),
            "industry": random.choice(BACKGROUND_INDUSTRIES),
            "city": city, "province": province,
            "addr": random_address(), "addr2": "",
            "email": f"info@{name.lower().replace(' ', '-')[:20]}.cor",
            "phone": generate_phone(city),
            "reg_date": random_date(1995, 2023),
        }
        xml = build_instance(biz)
        write_xml(os.path.join(OUTPUT_DIR, f"br-{cuid_generator()}.xml"), xml)
        count += 1

    print(f"Business Registry: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    generate()
