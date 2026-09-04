"""
Generate Education Record XML instances for CordovaOS demo.

Governance-composed (v2) model: Governed Record wrapper carrying the
Education Record data cluster + Provenance Components cluster, followed by
native subject/provider parties, a modeled System Audit, and attestation.

Elena as faculty, UNC students, some completed credentials.
Output: import_data/education_record/
"""
import os
import random

from shared import (
    NA,
    CAST, PERSONS, PROVINCE_CITIES, CITY_TO_PROVINCE,
    xml_header, xml_preamble, xml_footer, write_xml,
    xdstring, xdtoken, xdtemporal,
    cluster_open, cluster_close, native_partytype,
    make_provenance_values, audit, attestation,
    cuid_generator, _esc,
)

CT_ID = "upq7w1bqbix5v5ss0mu3kq5n"
DM_LABEL = "Education Record"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "sdc4", "import_data", "education_record")

# ─── v2 governance envelope wrappers ─────────────────────────────────────────
GOVERNED_RECORD = "ms-j4t6xb94355k51xg87n8awdl"   # Education Governed Record (Item)
CL_ROOT         = "ms-ifgq7a670csnbv7vcpuiabp0"   # Education Record data cluster
CL_PROV         = "ms-hdhjfg00tngir2txgqyka9cv"   # Provenance Components cluster
SYS_AUDIT       = "ms-fotc5adg15ek2b9ermx2mcih"   # System Audit component

# ─── Data cluster scalars (component, adapter-wrapper) — re-keyed for v2 ──────
W_CID         = ("ms-nj7s1gk45tfgyooxpz0qaha3", "ms-xioyl07fvgh5icdqrcl709tk")
W_STUDENT_ID  = ("ms-khbvruwpu9hnttg8y0mnih6a", "ms-ji7tpm8t62el1thbou5t7oc6")
W_CITY        = ("ms-atdtdfzruh7tya0iv5cz365l", "ms-r5kybrrm4yfh7z02msshfe99")
W_PROVINCE    = ("ms-kv5qqs3o4jwcwz9javgw1pzh", "ms-b2l3dy2sleghrl40w3umgs8c")

# ─── Credential sub-cluster ──────────────────────────────────────────────────
CL_CRED       = "ms-nyf0w3u2hs0svcjnqkb6zzlb"
W_YESNO       = ("ms-ht98owgvxhff3ge85i4h80lp", "ms-w8jk9hv5tdne6wpn27r987gk")
W_FIELD       = ("ms-ouqi09d8kjqeojlr7vnclysj", "ms-a5ptg4s12yqvfs77w3jih15z")
W_CRED_TYPE   = ("ms-sxkjp09cbjb6n13j8a0eg37i", "ms-wsty7lif4bqbsoechcc8ad4e")
W_HONORS      = ("ms-c7qvfjtu0omg4wagiaiy5hej", "ms-zkj6sj2v4vqwqykonvvk6v3r")
W_DATE_AWARD  = ("ms-xi99tao4v75wdrkq0ot02vfd", "ms-gl700lmf3g9l4earvxn7oz0q")

# ─── Enrollment sub-cluster (reuses Field-of-Study adapter W_FIELD) ───────────
CL_ENROLL     = "ms-r97mt4prbpxp04qmdc8iimb8"
W_ENR_STATUS  = ("ms-squd8e2s6pk8xoafu9ec0t9k", "ms-chz6l4lcc856wqm44oy8c3lx")
W_EDU_LEVEL   = ("ms-1ylumrkck2vv635djov01tte4", "ms-o8cuwfpfqa6kx8nvdnzk74d1")
W_ENR_DATE    = ("ms-z72jnzdib9hi311s338zwdog", "ms-gwvuia53itc1xsm8w33r4tw4")
W_EXPECT_DATE = ("ms-g6ntdb41otp1mtwsyb52mez3", "ms-d5aito2h8c31bd9ezti2ynyz")

# ─── Provenance Components leaves (component, adapter-wrapper) ────────────────
P_ACT_DESC    = ("ms-m9xg6e182m1oq77ssrf9iujv", "ms-u1dfkfg8zf63ondcionqow46")
P_ACT_TYPE    = ("ms-ccj1yq2wtwknobszkgzzdbtr", "ms-kdnqrut5deijmrkio64dxxns")
P_SYS_ID      = ("ms-bd3s8t23d6m3zizmpwavc32y", "ms-s3tg6tidg3dlhy2hw4sh08yi")
P_LOC_ID      = ("ms-zr59goe24qkocprl3feul3mt", "ms-a1mc2y0227aneigwj81g7vpq")
P_LOC_NAME    = ("ms-fnodzqkbyskwe7nh58rs336k", "ms-dnyj6nl5h0dmm6utk5lp7j1m")
P_TS_END      = ("ms-edvvjznmaoibzmfna0uuoo37", "ms-z7gbl0l5borca9iob2mnwab9")
P_TS_START    = ("ms-o72s5793973fzho35rnaughs", "ms-dj93716fknpyq6smydh17tez")

# ─── Domain enums (must match the model's own enumeration components) ─────────
FIELDS = [
    "Marine Biology", "Environmental Science", "Computer Science",
    "Economics", "Political Science", "Engineering", "Medicine",
    "Literature", "History", "Chemistry", "Physics", "Mathematics",
    "Nursing", "Public Health", "Business Administration",
]
HONORS = ["None", "Cum Laude", "Magna Cum Laude", "Summa Cum Laude"]

# Education Level XdOrdinal: (ordinal, symbol) pairs from the model's enum.
EDU_LEVEL = {
    "primary":    ("0", "Less than high school"),
    "secondary":  ("1", "High school diploma/GED"),
    "associate":  ("3", "Associate degree"),
    "bachelor":   ("4", "Bachelor's degree"),
    "master":     ("5", "Master's degree"),
    "doctorate":  ("6", "Doctoral degree"),
}
# Credential Type XdToken enum, keyed by tier.
CRED_TYPE = {
    "primary":    "Primary Certificate",
    "secondary":  "Secondary Diploma",
    "associate":  "Associate Degree",
    "bachelor":   "Bachelor's Degree",
    "master":     "Master's Degree",
    "doctorate":  "Doctoral Degree",
}

_sid_counter = 0


def next_sid():
    global _sid_counter
    _sid_counter += 1
    return f"UNC-{_sid_counter:06d}"


# ─── Local component builders (types the shared stubs don't cover) ────────────

def _xdany_leaf(pad, comp_id, wrap_id, label, tail):
    """Common XdAny leaf body (label + optional act..longitude) plus `tail`."""
    return (f"{pad}<sdc4:{wrap_id}>\n"
            f"{pad}  <sdc4:{comp_id}>\n"
            f"{pad}    <label>{_esc(label)}</label>\n"
            f"{pad}    <act></act>\n"
            f"{pad}    <vtb>2020-01-01T00:00:00</vtb>\n"
            f"{pad}    <vte>9999-12-31T23:59:59</vte>\n"
            f"{pad}    <tr>2020-01-01T00:00:00</tr>\n"
            f"{pad}    <modified>2020-01-01T00:00:00</modified>\n"
            f"{pad}    <latitude>0.0</latitude>\n"
            f"{pad}    <longitude>0.0</longitude>\n"
            f"{tail}"
            f"{pad}  </sdc4:{comp_id}>\n"
            f"{pad}</sdc4:{wrap_id}>\n")


def xdboolean_choice(comp_id, wrap_id, label, is_true, indent=2):
    """XdBoolean with the required true-value/false-value choice (enum Yes/No)."""
    pad = "  " * indent
    if is_true:
        tail = f"{pad}    <true-value>Yes</true-value>\n"
    else:
        tail = f"{pad}    <false-value>No</false-value>\n"
    return _xdany_leaf(pad, comp_id, wrap_id, label, tail)


def xdordinal(comp_id, wrap_id, label, ordinal, symbol, indent=2):
    """XdOrdinal with the required ordinal (decimal) + symbol (enum) values."""
    pad = "  " * indent
    tail = (f"{pad}    <ordinal>{ordinal}</ordinal>\n"
            f"{pad}    <symbol>{_esc(symbol)}</symbol>\n")
    return _xdany_leaf(pad, comp_id, wrap_id, label, tail)


def build_instance(rec):
    """Build a governance-composed Education Record instance for one record."""
    prov = make_provenance_values("Cordova Education Registry",
                                  "RecordRegistration", rec["city"])
    completed = rec["enr_status"] == "Graduated"

    xml = xml_header(CT_ID)
    xml += xml_preamble(DM_LABEL, current_state=rec["enr_status"])

    # Item: Governed Record wrapper
    xml += cluster_open(GOVERNED_RECORD, "Education Governed Record", indent=1)

    # Data cluster. The XSD sequence lists the sub-clusters (Credential,
    # Enrollment) BEFORE the scalar adapters (CID, Student ID, City, Province).
    xml += cluster_open(CL_ROOT, "Education Record", indent=2)

    # Credential sub-cluster
    xml += cluster_open(CL_CRED, "Credential", indent=3)
    xml += xdboolean_choice(*W_YESNO, "Yes/No", completed, indent=4)
    xml += xdstring(*W_FIELD, "Field of Study", rec["field"], indent=4)
    xml += xdtoken(*W_CRED_TYPE, "Credential Type", rec["cred_type"], indent=4)
    xml += xdtoken(*W_HONORS, "Honors", rec.get("honors", "None"), indent=4)
    xml += xdtemporal(*W_DATE_AWARD, "Date Awarded",
                      rec.get("date_awarded", NA), "date", indent=4)
    xml += cluster_close(CL_CRED, indent=3)

    # Enrollment sub-cluster (Field of Study adapter reused as first child)
    xml += cluster_open(CL_ENROLL, "Enrollment", indent=3)
    xml += xdstring(*W_FIELD, "Field of Study", rec["field"], indent=4)
    xml += xdtoken(*W_ENR_STATUS, "Enrollment Status", rec["enr_status"], indent=4)
    xml += xdordinal(*W_EDU_LEVEL, "Education Level",
                     rec["edu_ordinal"], rec["edu_symbol"], indent=4)
    xml += xdtemporal(*W_ENR_DATE, "Enrollment Date", rec["enr_date"], "date", indent=4)
    xml += xdtemporal(*W_EXPECT_DATE, "Expected Completion Date",
                      rec["expect_date"], "date", indent=4)
    xml += cluster_close(CL_ENROLL, indent=3)

    # Scalars (after the sub-clusters, per XSD sequence)
    xml += xdstring(*W_CID, "National ID (CID)", rec["cid"], indent=3)
    xml += xdstring(*W_STUDENT_ID, "Student ID", rec["student_id"], indent=3)
    xml += xdtoken(*W_CITY, "City", rec["city"], indent=3)
    xml += xdtoken(*W_PROVINCE, "Province", rec["province"], indent=3)
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
    xml += native_partytype("subject", "Student", rec.get("student_name", "Student"))
    xml += native_partytype("provider", "Educational Institution", rec["institution"])
    xml += audit(SYS_AUDIT, prov["activity_timestamp_start"],
                 system_id_value=prov["system_identifier"])
    xml += attestation(pending=not completed,
                       reason="Enrollment verified by the registrar's office",
                       committer=rec["institution"],
                       committed=prov["activity_timestamp_end"])

    xml += xml_footer(CT_ID)
    return xml


# ─── Institutions (valid enum cities only) ───────────────────────────────────

UNIVERSITY = ("Universidad Nacional de Cordova", "Campoluz", "Brevina")


def _school(prefix, city, province):
    return (f"{prefix} {city}", city, province)


def _random_city_province():
    prov = random.choice(list(PROVINCE_CITIES.keys()))
    city = random.choice(PROVINCE_CITIES[prov])
    return city, prov


def _make_record(person, tier, field, enr_status, enr_year, expect_year,
                 institution, city, province):
    ordinal, symbol = EDU_LEVEL[tier]
    honors = "None"
    date_awarded = NA
    if enr_status == "Graduated":
        honors = random.choice(HONORS)
        date_awarded = f"{expect_year}-{random.randint(5,6):02d}-{random.randint(1,28):02d}"
    return {
        "cid": person["cid"],
        "student_id": next_sid(),
        "student_name": f"{person.get('given','')} {person.get('surname','')}".strip(),
        "institution": institution,
        "city": city, "province": province,
        "field": field,
        "cred_type": CRED_TYPE[tier],
        "edu_ordinal": ordinal, "edu_symbol": symbol,
        "honors": honors, "date_awarded": date_awarded,
        "enr_status": enr_status,
        "enr_date": f"{enr_year}-09-01",
        "expect_date": f"{expect_year}-{random.randint(5,6):02d}-15",
    }


def generate():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    count = 0

    # Cast: completed doctorates, now faculty/professionals
    cast_specs = [
        ("elena",    "Marine Biology", 2016, 2022),
        ("dr_reyes", "Medicine",       1998, 2004),
        ("dr_ferrer","Public Health",  1994, 2000),
    ]
    for key, field, enr_year, expect_year in cast_specs:
        person = CAST[key]
        rec = _make_record(person, "doctorate", field, "Graduated",
                           enr_year, expect_year, *UNIVERSITY)
        write_xml(os.path.join(OUTPUT_DIR, f"ed-{cuid_generator()}.xml"), build_instance(rec))
        count += 1

    # School-age and recent graduates from the background population
    if not PERSONS:
        from civil_registry import generate as gen_cr
        gen_cr()

    eligible = [p for p in PERSONS if p.get("key", "").startswith("bg_")
                and 5 <= (2026 - int(p["dob"][:4])) <= 30]

    for p in eligible:
        age = 2026 - int(p["dob"][:4])
        if age <= 11:
            tier = "primary"
            city, province = _random_city_province()
            institution = f"Escuela Primaria {city}"
            enr_status = "Active"
            field = "General Education"
            enr_year = max(2020, 2026 - (age - 5))
            expect_year = enr_year + 6
        elif age <= 17:
            tier = "secondary"
            city, province = _random_city_province()
            institution = random.choice([f"Liceo Nacional {city}", f"Colegio Tecnico {city}"])
            enr_status = random.choice(["Active", "Active", "Active", "On Leave"])
            field = random.choice(["General Studies", "Science Track",
                                    "Humanities Track", "Technical Track"])
            enr_year = max(2020, 2026 - (age - 12))
            expect_year = enr_year + 6
        elif age <= 25:
            institution, city, province = UNIVERSITY
            tier = random.choice(["bachelor", "bachelor", "bachelor", "master"])
            enr_status = random.choice(["Active", "Active", "Active", "On Leave", "Graduated"])
            field = random.choice(FIELDS)
            enr_year = random.randint(2018, 2024)
            expect_year = enr_year + (4 if tier == "bachelor" else 2)
        else:
            institution, city, province = UNIVERSITY
            tier = random.choice(["bachelor", "master", "master"])
            enr_status = "Graduated"
            field = random.choice(FIELDS)
            enr_year = random.randint(2014, 2020)
            expect_year = enr_year + (4 if tier == "bachelor" else 2)

        rec = _make_record(p, tier, field, enr_status, enr_year, expect_year,
                           institution, city, province)
        write_xml(os.path.join(OUTPUT_DIR, f"ed-{cuid_generator()}.xml"), build_instance(rec))
        count += 1

    print(f"Education Record: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    generate()
