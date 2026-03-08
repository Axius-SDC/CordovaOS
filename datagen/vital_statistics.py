"""
Generate Vital Statistics XML instances for CordovaOS demo.

Birth certificates for all persons, marriages for some, a few deaths.
Output: import_data/vital_statistics_record/
"""
import os
import random

from shared import (
    CAST, PERSONS, random_date, generate_cid_for_city, CITY_TO_PROVINCE,
    xml_header, xml_preamble, xml_footer, write_xml,
    xdstring, xdtoken, xdtemporal, xdtemporal_multi,
    cluster_open, cluster_close, party_stub,
    cuid_generator, _esc,
)

CT_ID = "ulzd6pe8072mwkqf7i313bov"
DM_LABEL = "Vital Statistics Record"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "sdc4", "import_data", "vital_statistics_record")

# Wrapper mappings from template
# Root cluster: ms-tard9hhq13m95hinbh4h7k5j (Vital Event)
CL_ROOT = "ms-tard9hhq13m95hinbh4h7k5j"
W_CERT_NUM    = ("ms-ajfsyoyrz38094hswxh13i3x", "ms-d8058sqjlnbdru4fvnbf8iq7")
W_CITY        = ("ms-atdtdfzruh7tya0iv5cz365l", "ms-zc8k83nwlgf2spscql8ucgxh")
W_EVENT_TYPE  = ("ms-jz7vc6ikueqig8g0lvb2czzr", "ms-qfn1rbp54e6m97gdqa5lyxry")
W_PROVINCE    = ("ms-kv5qqs3o4jwcwz9javgw1pzh", "ms-t853xugvamhcb20hge069enq")
W_STATUS      = ("ms-yri6g628ipi0jqoa0ijnzxxu", "ms-f8z9rmp13zn1idj95tc87otv")
W_EVENT_DATE  = ("ms-e3sfb43zh1vjlgceb5guh0mj", "ms-d554vcjrk26dz9ym7eg77n1v")  # date + year-month
W_REG_DATE    = ("ms-vo9jtmexkaaol3y657fm0xn8", "ms-rleuc13sdyflkzco9owr4wic")

# Birth Record sub-cluster: ms-az8kem3v58y9zenys7mthqxe
CL_BIRTH      = "ms-az8kem3v58y9zenys7mthqxe"
W_B_CID       = ("ms-nj7s1gk45tfgyooxpz0qaha3", "ms-wxnkqtvtkoxd1oj0v187q9ow")
W_B_NAME      = ("ms-pmw2cq7fioqlbs2ljdh34rkn", "ms-rr7nywto5dyqhpg7g9pw90y0")
W_B_SEX       = ("ms-mw9qdn71urog8egjbp5t3y00", "ms-xejs3hs8xnoa12g4x5wyz7a4")

# Death Record sub-cluster: ms-tdz3pxrf7k6z2df2bfm7ebcp
CL_DEATH      = "ms-tdz3pxrf7k6z2df2bfm7ebcp"
W_D_CAUSE     = ("ms-m3gsphdej7z9csemrrk8uymy", "ms-nazyew1acpjrop7p0edsshz3")
W_D_MANNER    = ("ms-ftuxt5nrrffwjb2vymn80yx2", "ms-dv9sctsindynzoppt6auf9p9")
W_D_PLACE     = ("ms-dsoyfaplxw8ide1opo5w8fxg", "ms-p1u860zehqb1ltrtd9hwrtnw")

# Divorce Record sub-cluster: ms-obybok0oaoa79b11b0ync1zf
CL_DIVORCE    = "ms-obybok0oaoa79b11b0ync1zf"
W_DV_CERT     = ("ms-ycujkecjszwwrcd6dhxesk73", "ms-yflzlkllbvjg6gz2eu931eye")
W_DV_DATE     = ("ms-ft4kk6m3r1goxkte0d7wflk8", "ms-nvyvn3lr8s2nr8w2mwyoh2sz")

# Marriage Record sub-cluster: ms-chtyne5i6qcwbrby29vbuh2k (empty cluster)
CL_MARRIAGE   = "ms-chtyne5i6qcwbrby29vbuh2k"

# Party stubs
PS_SUBJECT    = "ms-qcofdwdb4hrmxeby89g8sjl1"
PS_OFFICE     = "ms-xqhxjh5kzvgrzu0u87v3fxb2"

_cert_counter = 0


def next_cert():
    global _cert_counter
    _cert_counter += 1
    return f"VS-{_cert_counter:06d}"


def build_birth(person):
    """Build a birth certificate instance."""
    city = person["city"]
    province = person["province"]
    dob = person["dob"]
    reg_date = dob  # registered on birth date
    full_name = f"{person['given']} {person['middle']} {person['surname']}"

    xml = xml_header(CT_ID)
    xml += xml_preamble(DM_LABEL)
    xml += cluster_open(CL_ROOT, "Vital Event")
    xml += xdstring(*W_CERT_NUM, "Certificate Number", next_cert())
    xml += xdtoken(*W_CITY, "City", city)
    xml += xdtoken(*W_EVENT_TYPE, "Event Type", "Birth")
    xml += xdtoken(*W_PROVINCE, "Province", province)
    xml += xdtoken(*W_STATUS, "Record Status", "Active")
    xml += xdtemporal_multi(*W_EVENT_DATE, "Event Date", dob, ("date", "year-month"))
    xml += xdtemporal(*W_REG_DATE, "Registration Date", reg_date, "date")

    # Birth Record
    xml += cluster_open(CL_BIRTH, "Birth Record", indent=2)
    xml += xdstring(*W_B_CID, "National ID (CID)", person["cid"], indent=3)
    xml += xdstring(*W_B_NAME, "Person Full Name", full_name, indent=3)
    xml += xdtoken(*W_B_SEX, "Sex", person["sex"], indent=3)
    xml += cluster_close(CL_BIRTH, indent=2)

    # Death Record (empty for living persons)
    xml += cluster_open(CL_DEATH, "Death Record", indent=2)
    xml += xdstring(*W_D_CAUSE, "Cause of Death", "N/A", indent=3)
    xml += xdtoken(*W_D_MANNER, "Manner of Death", "N/A", indent=3)
    xml += xdtoken(*W_D_PLACE, "Place of Death", "N/A", indent=3)
    xml += cluster_close(CL_DEATH, indent=2)

    # Divorce Record (empty)
    xml += cluster_open(CL_DIVORCE, "Divorce Record", indent=2)
    xml += xdstring(*W_DV_CERT, "Marriage Certificate Number", "N/A", indent=3)
    xml += xdtemporal(*W_DV_DATE, "Decree Date", "1900-01-01", "date", indent=3)
    xml += cluster_close(CL_DIVORCE, indent=2)

    # Marriage Record (empty cluster)
    xml += cluster_open(CL_MARRIAGE, "Marriage Record", indent=2)
    xml += cluster_close(CL_MARRIAGE, indent=2)

    xml += cluster_close(CL_ROOT)
    xml += party_stub(PS_SUBJECT, "Vital Record Subject")
    xml += party_stub(PS_OFFICE, "Vital Statistics Office")
    xml += xml_footer(CT_ID)
    return xml


def build_marriage(person1, person2, marriage_date, city, province):
    """Build a marriage certificate instance."""
    xml = xml_header(CT_ID)
    xml += xml_preamble(DM_LABEL)
    xml += cluster_open(CL_ROOT, "Vital Event")
    xml += xdstring(*W_CERT_NUM, "Certificate Number", next_cert())
    xml += xdtoken(*W_CITY, "City", city)
    xml += xdtoken(*W_EVENT_TYPE, "Event Type", "Marriage")
    xml += xdtoken(*W_PROVINCE, "Province", province)
    xml += xdtoken(*W_STATUS, "Record Status", "Active")
    xml += xdtemporal_multi(*W_EVENT_DATE, "Event Date", marriage_date, ("date", "year-month"))
    xml += xdtemporal(*W_REG_DATE, "Registration Date", marriage_date, "date")

    # Birth Record (N/A for marriage)
    xml += cluster_open(CL_BIRTH, "Birth Record", indent=2)
    xml += xdstring(*W_B_CID, "National ID (CID)", person1["cid"], indent=3)
    name1 = f"{person1['given']} {person1['middle']} {person1['surname']}"
    xml += xdstring(*W_B_NAME, "Person Full Name", name1, indent=3)
    xml += xdtoken(*W_B_SEX, "Sex", person1["sex"], indent=3)
    xml += cluster_close(CL_BIRTH, indent=2)

    xml += cluster_open(CL_DEATH, "Death Record", indent=2)
    xml += xdstring(*W_D_CAUSE, "Cause of Death", "N/A", indent=3)
    xml += xdtoken(*W_D_MANNER, "Manner of Death", "N/A", indent=3)
    xml += xdtoken(*W_D_PLACE, "Place of Death", "N/A", indent=3)
    xml += cluster_close(CL_DEATH, indent=2)

    xml += cluster_open(CL_DIVORCE, "Divorce Record", indent=2)
    xml += xdstring(*W_DV_CERT, "Marriage Certificate Number", "N/A", indent=3)
    xml += xdtemporal(*W_DV_DATE, "Decree Date", "1900-01-01", "date", indent=3)
    xml += cluster_close(CL_DIVORCE, indent=2)

    xml += cluster_open(CL_MARRIAGE, "Marriage Record", indent=2)
    xml += cluster_close(CL_MARRIAGE, indent=2)

    xml += cluster_close(CL_ROOT)
    xml += party_stub(PS_SUBJECT, "Vital Record Subject")
    xml += party_stub(PS_OFFICE, "Vital Statistics Office")
    xml += xml_footer(CT_ID)
    return xml


def generate():
    """Generate Vital Statistics XML files."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Need PERSONS populated from civil_registry first
    if not PERSONS:
        from civil_registry import generate as gen_cr
        gen_cr()

    count = 0

    # Birth certificates for all persons
    for person in PERSONS:
        xml = build_birth(person)
        write_xml(os.path.join(OUTPUT_DIR, f"vs-{cuid_generator()}.xml"), xml)
        count += 1

    # Marriage certificates for married cast members
    married_cast = [k for k, v in CAST.items() if v["marital_status"] == "Married"]
    for key in married_cast:
        c = CAST[key]
        marriage_date = random_date(2000, 2015)
        xml = build_marriage(c, c, marriage_date, c["city"], c["province"])
        write_xml(os.path.join(OUTPUT_DIR, f"vs-{cuid_generator()}.xml"), xml)
        count += 1

    print(f"Vital Statistics: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    generate()
