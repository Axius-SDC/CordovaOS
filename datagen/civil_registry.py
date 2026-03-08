"""
Generate Civil Registry XML instances for CordovaOS demo.

Produces 25,000 records: 8 Contagion cast + 24,992 background residents.
Output: /home/twcook/GitHub/CordovaOS/app/sdc4/import_data/civil_registry/
"""
import os
import random

from shared import (
    CAST, PERSONS, ALL_CITIES, CITY_TO_PROVINCE, PROVINCE_CODES, CITY_CODES,
    PROVINCE_CITIES, AGE_DISTRIBUTION,
    random_name, random_city_province, random_address, random_dob,
    generate_cid_for_city, generate_phone, generate_email,
    xml_header, xml_preamble, xml_footer, write_xml,
    xdstring, xdtoken, xdtemporal, cluster_open, cluster_close, party_stub,
    _esc, cuid_generator,
)

CT_ID = "uika42uwtj3ijdbegzw2kcwq"
DM_LABEL = "Civil Registry"

OUTPUT_DIR = os.path.join(
    os.path.dirname(__file__),
    "..", "app", "sdc4", "import_data", "civil_registry",
)

# ─── Component → Wrapper mappings (from XML template) ────────────────────────

# Direct children of root cluster ms-bgjt4mvgvkxcn6hurg37u21b
W_NATIONAL_ID   = ("ms-nj7s1gk45tfgyooxpz0qaha3", "ms-sf5d0dzjo5yqp545skp6tmw3")
W_COUNTRY_BIRTH = ("ms-cfg2l8ym4ve833ritrxu765t", "ms-ppatwamypgm2vvl1ixbvbdk8")
W_GIVEN_NAME    = ("ms-kfyzf8u8gdafcpt5kfh2qg3q", "ms-v0yppmgjerq6v83aufxk4bnt")
W_MIDDLE_NAME   = ("ms-oit0ueglhjfcyq80z22kl2z3", "ms-wt8pjkqdkwzuyg68q8eks8rk")
W_SURNAME       = ("ms-v8jgjo2sml12jo7zrb8swoxi", "ms-lquaqukhj8g8jkuxwua9t3f3")
W_CITY          = ("ms-atdtdfzruh7tya0iv5cz365l", "ms-flg3okcdrds65w1twhfdkqj2")
W_MARITAL       = ("ms-vjfgimlbb90ds2xg55tfn941", "ms-xb1lgx6byojidqm8ffdrogah")
W_PROVINCE      = ("ms-kv5qqs3o4jwcwz9javgw1pzh", "ms-yr5nlcn9muub8g69ui0iyrwa")
W_GENDER        = ("ms-cymq16em5zb20whgtfzki6n5", "ms-zah3durtmxt4ssipr5309it9")
W_SEX           = ("ms-mw9qdn71urog8egjbp5t3y00", "ms-kprttn2ok3qk7iqm6l1z1uie")
W_BIRTH_DATE    = ("ms-g3k6bj8su3rvkszg2700dhyh", "ms-jmn2v720qkuydsc5ftpphqrl")

# Contact Information sub-cluster ms-sv48g8am8vqs46nodiugripz
W_EMAIL         = ("ms-x0na649n17if0ukul82cmrx3", "ms-yqxxoehqidrfcbto4s0xdacm")
W_PHONE         = ("ms-nfrvvp87c5imu5h9ups92kgy", "ms-y0vfbpi76tunsfgq8861cpi9")
W_CONTACT_PREF  = ("ms-zlz64jydsmhb5zmytcm2ewyg", "ms-jicqhez3mky3tbtwnmuv1pcd")

# Current Address sub-cluster ms-ytctcqbr30kxsmvx4jk7lae2
W_ADDR1         = ("ms-l338k7nlvnq2am0owa19yxfc", "ms-viugivc8kxgjrpgxyebpgzbs")
W_ADDR2         = ("ms-ek5h6dsqpd9kz0l4mcckmxpt", "ms-drwt9abubt16wo0dtklbe7of")

# Family Relationships sub-cluster ms-l9k2fmlc5vn477r3kpi1ufal
W_REL_TYPE      = ("ms-be9apjt8mvjjv86qzycorcjl", "ms-ewvqx9e8k6bmkvagzo5mahrs")
W_REL_END       = ("ms-o7vjxwswi0pxo543hq504jjx", "ms-lvyllvk6q9ojxv90phudd3d9")
W_REL_START     = ("ms-k9ptlhkq3j41p6umlg3tc80x", "ms-dbdmw1sy83yfkqkj6ypqn0ms")

# Cluster IDs
CL_ROOT         = "ms-bgjt4mvgvkxcn6hurg37u21b"
CL_CONTACT      = "ms-sv48g8am8vqs46nodiugripz"
CL_ADDRESS      = "ms-ytctcqbr30kxsmvx4jk7lae2"
CL_FAMILY       = "ms-l9k2fmlc5vn477r3kpi1ufal"

# Party stubs
PS_RELATED      = "ms-avqpyqft9tm22yyink3ltcty"
PS_OFFICE       = "ms-piaz5w21hsuq3hpysyetuvvk"

MARITAL_STATUSES = ["Single", "Married", "Divorced", "Widowed"]
RELATIONSHIP_TYPES = ["Parent", "Spouse", "Sibling", "Child", "Grandparent"]
CONTACT_PREFS = ["Phone", "Email", "Mail"]


def build_birth_date(dob, indent=2):
    """Build Birth Date XdTemporal with all three variant elements."""
    comp_id, wrap_id = W_BIRTH_DATE
    pad = "  " * indent
    # Parse date parts
    year = dob[:4]
    year_month = dob[:7]
    return f"""{pad}<sdc4:{wrap_id}>
{pad}  <sdc4:{comp_id}>
{pad}    <label>Birth Date</label>
{pad}    <xdtemporal-date>{dob}</xdtemporal-date>
{pad}    <xdtemporal-year>{year}</xdtemporal-year>
{pad}    <xdtemporal-year-month>{year_month}</xdtemporal-year-month>
{pad}  </sdc4:{comp_id}>
{pad}</sdc4:{wrap_id}>
"""


def build_instance(person):
    """Build a complete Civil Registry XML instance for one person."""
    xml = xml_header(CT_ID)
    xml += xml_preamble(DM_LABEL)

    # Root cluster open
    xml += cluster_open(CL_ROOT, "Civil Registry Record")

    # Direct components under root cluster
    xml += xdstring(*W_NATIONAL_ID, "National ID (CID)", person["cid"])
    xml += xdstring(*W_COUNTRY_BIRTH, "Country of Birth", person["country_of_birth"])
    xml += xdstring(*W_GIVEN_NAME, "Given Name (Person)", person["given"])
    xml += xdstring(*W_MIDDLE_NAME, "Middle Name (Person)", person["middle"])
    xml += xdstring(*W_SURNAME, "Surname (Person)", person["surname"])
    xml += xdtoken(*W_CITY, "City", person["city"])
    xml += xdtoken(*W_MARITAL, "Marital Status (Cordova)", person["marital_status"])
    xml += xdtoken(*W_PROVINCE, "Province", person["province"])
    xml += xdtoken(*W_GENDER, "Gender Identity", person["gender"])
    xml += xdtoken(*W_SEX, "Sex", person["sex"])
    xml += build_birth_date(person["dob"])

    # Contact Information sub-cluster
    xml += cluster_open(CL_CONTACT, "Contact Information")
    xml += xdstring(*W_EMAIL, "Cordova Email Address", person["email"], indent=3)
    xml += xdstring(*W_PHONE, "Cordova Phone Number", person["phone"], indent=3)
    xml += xdtoken(*W_CONTACT_PREF, "Preferred Contact Method", person["contact_pref"], indent=3)
    xml += cluster_close(CL_CONTACT)

    # Current Address sub-cluster
    xml += cluster_open(CL_ADDRESS, "Current Address")
    xml += xdstring(*W_ADDR1, "Address (Line 1)", person["address"], indent=3)
    xml += xdstring(*W_ADDR2, "Address (Line 2)", person.get("address2", ""), indent=3)
    xml += cluster_close(CL_ADDRESS)

    # Family Relationships sub-cluster
    xml += cluster_open(CL_FAMILY, "Family Relationships")
    xml += xdtoken(*W_REL_TYPE, "Relationship Type", person["rel_type"], indent=3)
    xml += xdtemporal(*W_REL_END, "Relationship End Date", person.get("rel_end", "2099-12-31"), "date", indent=3)
    xml += xdtemporal(*W_REL_START, "Relationship Start Date", person["rel_start"], "date", indent=3)
    xml += cluster_close(CL_FAMILY)

    # Close root cluster
    xml += cluster_close(CL_ROOT)

    # Party stubs (outside root cluster, at root level)
    xml += party_stub(PS_RELATED, "Related Person")
    xml += party_stub(PS_OFFICE, "Civil Registry Office")

    xml += xml_footer(CT_ID)
    return xml


def make_cast_persons():
    """Convert CAST dict entries to person records with relationship data."""
    persons = []
    for key, c in CAST.items():
        p = dict(c)  # copy
        p["key"] = key
        p["country_of_birth"] = c.get("country_of_birth", "Republic of Cordova")

        # Assign family relationships for known cast
        if key == "carlos":
            p["rel_type"] = "Sibling"
            p["rel_start"] = "1994-11-22"  # Elena's birth
            p["rel_end"] = "2099-12-31"
        elif key == "elena":
            p["rel_type"] = "Sibling"
            p["rel_start"] = "1991-08-14"  # Carlos's birth
            p["rel_end"] = "2099-12-31"
        elif key in ("dr_reyes", "dr_ferrer", "governor_avila", "dr_gutierrez", "prof_lucero"):
            p["rel_type"] = "Spouse"
            p["rel_start"] = random_dob(min_age=10, max_age=30)
            p["rel_end"] = "2099-12-31"
        else:
            p["rel_type"] = "Parent"
            p["rel_start"] = p["dob"]
            p["rel_end"] = "2099-12-31"

        persons.append(p)
    return persons


def make_background_persons(count=24992):
    """Generate background residents spread across cities."""
    persons = []
    for i in range(count):
        sex = random.choice(["Male", "Female"])
        given, middle, surname = random_name(sex)
        city, province = random_city_province()
        cid = generate_cid_for_city(city)
        dob = random_dob(distribution=AGE_DISTRIBUTION)
        # Children are single; adults get random marital status
        age = 2026 - int(dob[:4])
        marital = "Single" if age < 18 else random.choice(MARITAL_STATUSES)
        addr = random_address()
        addr2 = random.choice(["", "", "", f"Apt {random.randint(1, 50)}",
                                f"Unit {random.randint(1, 20)}"])
        phone = generate_phone(city)
        email = generate_email(given, surname)
        contact_pref = random.choice(CONTACT_PREFS)

        rel_type = random.choice(RELATIONSHIP_TYPES)
        rel_start = random_dob(min_age=0, max_age=50)

        persons.append({
            "key": f"bg_{i:05d}",
            "cid": cid,
            "given": given, "middle": middle, "surname": surname,
            "sex": sex, "gender": sex, "dob": dob,
            "city": city, "province": province,
            "address": addr, "address2": addr2,
            "country_of_birth": "Republic of Cordova",
            "marital_status": marital,
            "phone": phone, "email": email,
            "contact_pref": contact_pref,
            "rel_type": rel_type,
            "rel_start": rel_start,
            "rel_end": "2099-12-31",
        })
    return persons


def generate():
    """Generate all Civil Registry XML files."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    cast_persons = make_cast_persons()
    bg_persons = make_background_persons(24992)
    all_persons = cast_persons + bg_persons

    # Populate shared PERSONS list for other domain generators
    PERSONS.clear()
    PERSONS.extend(all_persons)

    count = 0
    for person in all_persons:
        xml = build_instance(person)
        filename = f"cr-{cuid_generator()}.xml"
        filepath = os.path.join(OUTPUT_DIR, filename)
        write_xml(filepath, xml)
        count += 1

    print(f"Civil Registry: generated {count} XML files in {OUTPUT_DIR}")
    return all_persons


if __name__ == "__main__":
    generate()
