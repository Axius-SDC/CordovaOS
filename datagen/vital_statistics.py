"""
Generate Vital Statistics Record XML instances for CordovaOS demo.

Governance-composed (v2) model: a Governed Record Item wrapping the
Provenance Components cluster and the Vital Event data cluster, followed by
the DM's native subject / provider / Audit / attestation slots.

Birth certificates for all persons, marriages for married cast/adults, and a
small number of deaths.
Output: app/sdc4/import_data/vital_statistics_record/
"""
import os
import random

from shared import (
    CAST, PERSONS, random_date,
    xml_header, xml_preamble, xml_footer, write_xml,
    xdstring, xdtoken, xdtemporal,
    cluster_open, cluster_close, native_partytype,
    make_provenance_values, audit, attestation,
    cuid_generator,
)

CT_ID = "ulzd6pe8072mwkqf7i313bov"
DM_LABEL = "Vital Statistics Record"
OUTPUT_DIR = os.path.join(
    os.path.dirname(__file__),
    "..", "app", "sdc4", "import_data", "vital_statistics_record",
)

# ─── Governance envelope (re-keyed for v2 from YOUR template) ─────────────────
GOVERNED_RECORD = "ms-r2g662g70dx34eq12v9n4ng7"   # Vital Statistics Governed Record
CL_PROV         = "ms-hdhjfg00tngir2txgqyka9cv"   # Provenance Components
CL_EVENT        = "ms-tard9hhq13m95hinbh4h7k5j"   # Vital Event (data cluster)

# System Audit component (substitutionGroup="sdc4:Audit") — same id as civil.
SYSTEM_AUDIT    = "ms-fotc5adg15ek2b9ermx2mcih"

# ─── Provenance Components leaves (component, wrapper) ────────────────────────
# XSD sequence order of the Provenance Components cluster.
P_ACT_DESC      = ("ms-m9xg6e182m1oq77ssrf9iujv", "ms-dasx4perkgzp4c9l9uivth98")
P_ACT_TYPE      = ("ms-ccj1yq2wtwknobszkgzzdbtr", "ms-ivhnosqylq91bk0tjwe5ud4w")
P_SYS_ID        = ("ms-bd3s8t23d6m3zizmpwavc32y", "ms-oneyra7z219t8gekdsmhf5sx")
P_LOC_ID        = ("ms-zr59goe24qkocprl3feul3mt", "ms-z18ro4pi293x28724jjy1hn3")
P_LOC_NAME      = ("ms-fnodzqkbyskwe7nh58rs336k", "ms-mokdt6eh429r1xygju89ks8q")
P_TS_END        = ("ms-edvvjznmaoibzmfna0uuoo37", "ms-goytsnnd3og57suhh9lfphxm")
P_TS_START      = ("ms-o72s5793973fzho35rnaughs", "ms-hh2ggqxoo5mh1nddnag0tkf8")

# ─── Vital Event scalars (component, wrapper) ────────────────────────────────
W_CERT_NUM      = ("ms-ajfsyoyrz38094hswxh13i3x", "ms-k83op4asfdj45cf1p9jjal6p")
W_CITY          = ("ms-atdtdfzruh7tya0iv5cz365l", "ms-bfvwsejckb1dzg8d406qs4qk")
W_EVENT_TYPE    = ("ms-jz7vc6ikueqig8g0lvb2czzr", "ms-f58b8g7vv8qopqk3wl9kqdjy")
W_PROVINCE      = ("ms-kv5qqs3o4jwcwz9javgw1pzh", "ms-as91flr2x5cft82ggbkgs683")
W_STATUS        = ("ms-yri6g628ipi0jqoa0ijnzxxu", "ms-p2lxki4xdkdttefc8v7ut2mw")
W_EVENT_DATE    = ("ms-e3sfb43zh1vjlgceb5guh0mj", "ms-skwgla9yoeu9dwhp4zugu74m")
W_REG_DATE      = ("ms-vo9jtmexkaaol3y657fm0xn8", "ms-xkwh4shwsjoaxf3ciicazga0")

# ─── Sub-cluster ids and their leaves ────────────────────────────────────────
# Birth Record
CL_BIRTH        = "ms-az8kem3v58y9zenys7mthqxe"
W_B_CID         = ("ms-nj7s1gk45tfgyooxpz0qaha3", "ms-aoa6q4uhjljlzfxd70094nfr")
W_B_NAME        = ("ms-pmw2cq7fioqlbs2ljdh34rkn", "ms-opnt8x5td0xqo1k3ho5hhle5")
W_B_SEX         = ("ms-mw9qdn71urog8egjbp5t3y00", "ms-sligxuomjlg4173o34za8huj")

# Death Record (XSD order: Cause, [CID], [Name], Manner, Place — CID/Name are
# the shared adapters reused from Birth Record)
CL_DEATH        = "ms-tdz3pxrf7k6z2df2bfm7ebcp"
W_D_CAUSE       = ("ms-m3gsphdej7z9csemrrk8uymy", "ms-p8l8hnsuoiqhepssfvcghc36")
W_D_MANNER      = ("ms-ftuxt5nrrffwjb2vymn80yx2", "ms-ujx5pv7v1p6m8f2t1ewa4rh9")
W_D_PLACE       = ("ms-dsoyfaplxw8ide1opo5w8fxg", "ms-elfbh7mvkcrbnip8z6ufa6kv")

# Divorce Record (XSD order: Marriage Cert, [CID], [Name], Decree Date)
CL_DIVORCE      = "ms-obybok0oaoa79b11b0ync1zf"
W_DV_CERT       = ("ms-ycujkecjszwwrcd6dhxesk73", "ms-t9cr97ufkpvqk0d4obid275k")
W_DV_DATE       = ("ms-ft4kk6m3r1goxkte0d7wflk8", "ms-on7zvdpycerrdugizgeoj60t")

# Marriage Record (XSD order: [CID], [Name] — both reuse the Birth adapters)
CL_MARRIAGE     = "ms-chtyne5i6qcwbrby29vbuh2k"

# ─── Domain enums (must conform to XSD enumerations) ─────────────────────────
# Event Type:  Birth | Death | Marriage | Divorce
# Record Status: Active | Amended | Voided
# Sex: Male | Female | Intersex | Unknown
# Manner of Death: Natural | Accident | Homicide | Suicide | Undetermined
#                  | Pending Investigation
# Place of Death: Hospital | Residence | Other
WORKFLOW_STATES = ["Active", "Amended"]
MANNERS = ["Natural", "Accident", "Undetermined"]
PLACES = ["Hospital", "Residence", "Other"]
CAUSES = [
    "Cardiovascular disease", "Respiratory failure", "Cerebrovascular accident",
    "Malignant neoplasm", "Sepsis", "Renal failure", "Trauma",
]

_cert_counter = 0


def next_cert():
    global _cert_counter
    _cert_counter += 1
    return f"VS-{_cert_counter:06d}"


def _full_name(person):
    return f"{person['given']} {person.get('middle', '')} {person['surname']}".replace("  ", " ").strip()


# ─── Sub-cluster builders (emit empty label-only cluster when not relevant) ───

def _birth_cluster(person=None, indent=3):
    out = cluster_open(CL_BIRTH, "Birth Record", indent=indent)
    if person is not None:
        out += xdstring(*W_B_CID, "National ID (CID)", person["cid"], indent=indent + 1)
        out += xdstring(*W_B_NAME, "Person Full Name", _full_name(person), indent=indent + 1)
        out += xdtoken(*W_B_SEX, "Sex", person["sex"], indent=indent + 1)
    out += cluster_close(CL_BIRTH, indent=indent)
    return out


def _death_cluster(person=None, cause=None, manner=None, place=None, indent=3):
    out = cluster_open(CL_DEATH, "Death Record", indent=indent)
    if person is not None:
        out += xdstring(*W_D_CAUSE, "Cause of Death", cause, indent=indent + 1)
        out += xdstring(*W_B_CID, "National ID (CID)", person["cid"], indent=indent + 1)
        out += xdstring(*W_B_NAME, "Person Full Name", _full_name(person), indent=indent + 1)
        out += xdtoken(*W_D_MANNER, "Manner of Death", manner, indent=indent + 1)
        out += xdtoken(*W_D_PLACE, "Place of Death", place, indent=indent + 1)
    out += cluster_close(CL_DEATH, indent=indent)
    return out


def _divorce_cluster(person=None, cert=None, decree_date=None, indent=3):
    out = cluster_open(CL_DIVORCE, "Divorce Record", indent=indent)
    if person is not None:
        out += xdstring(*W_DV_CERT, "Marriage Certificate Number", cert, indent=indent + 1)
        out += xdstring(*W_B_CID, "National ID (CID)", person["cid"], indent=indent + 1)
        out += xdstring(*W_B_NAME, "Person Full Name", _full_name(person), indent=indent + 1)
        out += xdtemporal(*W_DV_DATE, "Decree Date", decree_date, "date", indent=indent + 1)
    out += cluster_close(CL_DIVORCE, indent=indent)
    return out


def _marriage_cluster(person=None, indent=3):
    out = cluster_open(CL_MARRIAGE, "Marriage Record", indent=indent)
    if person is not None:
        out += xdstring(*W_B_CID, "National ID (CID)", person["cid"], indent=indent + 1)
        out += xdstring(*W_B_NAME, "Person Full Name", _full_name(person), indent=indent + 1)
    out += cluster_close(CL_MARRIAGE, indent=indent)
    return out


def build_instance(record):
    """Build a governance-composed Vital Statistics Record instance.

    `record` is a dict describing a vital event:
      event_type: "Birth" | "Death" | "Marriage" | "Divorce"
      person:     primary subject person dict (given/middle/surname/cid/sex)
      city, province, event_date, reg_date
      (death)  cause, manner, place
      (divorce) marriage_cert, decree_date
    """
    event_type = record["event_type"]
    person = record["person"]
    city = record["city"]
    province = record["province"]
    activity = {
        "Birth": "BirthRegistration", "Death": "DeathRegistration",
        "Marriage": "MarriageRegistration", "Divorce": "DivorceRegistration",
    }[event_type]
    prov = make_provenance_values("Cordova Vital Statistics System", activity, city)
    state = random.choice(WORKFLOW_STATES)

    xml = xml_header(CT_ID)
    xml += xml_preamble(DM_LABEL, current_state=state)

    # Item: Governed Record wrapper
    xml += cluster_open(GOVERNED_RECORD, "Vital Statistics Governed Record", indent=1)

    # (1) Provenance Components cluster FIRST (per this DM's Governed Record XSD).
    xml += cluster_open(CL_PROV, "Provenance Components", indent=2)
    xml += xdstring(*P_ACT_DESC, "activity_description", prov["activity_description"], indent=3)
    xml += xdstring(*P_ACT_TYPE, "prov_activity_type", prov["prov_activity_type"], indent=3)
    xml += xdstring(*P_SYS_ID, "system_identifier", prov["system_identifier"], indent=3)
    xml += xdstring(*P_LOC_ID, "system_location_identifier", prov["system_location_identifier"], indent=3)
    xml += xdstring(*P_LOC_NAME, "system_location_name", prov["system_location_name"], indent=3)
    xml += xdtemporal(*P_TS_END, "activity_timestamp_end", prov["activity_timestamp_end"], "datetime", indent=3)
    xml += xdtemporal(*P_TS_START, "activity_timestamp_start", prov["activity_timestamp_start"], "datetime", indent=3)
    xml += cluster_close(CL_PROV, indent=2)

    # (2) Vital Event data cluster. XSD sequence: sub-clusters BEFORE scalars.
    xml += cluster_open(CL_EVENT, "Vital Event", indent=2)

    xml += _birth_cluster(person if event_type == "Birth" else None)
    xml += _death_cluster(
        person if event_type == "Death" else None,
        cause=record.get("cause"), manner=record.get("manner"), place=record.get("place"))
    xml += _divorce_cluster(
        person if event_type == "Divorce" else None,
        cert=record.get("marriage_cert"), decree_date=record.get("decree_date"))
    xml += _marriage_cluster(person if event_type == "Marriage" else None)

    xml += xdstring(*W_CERT_NUM, "Certificate Number", record["cert_num"], indent=3)
    xml += xdtoken(*W_CITY, "City", city, indent=3)
    xml += xdtoken(*W_EVENT_TYPE, "Event Type", event_type, indent=3)
    xml += xdtoken(*W_PROVINCE, "Province", province, indent=3)
    xml += xdtoken(*W_STATUS, "Record Status", record.get("status", "Active"), indent=3)
    xml += xdtemporal(*W_EVENT_DATE, "Event Date", record["event_date"], "date", indent=3)
    xml += xdtemporal(*W_REG_DATE, "Registration Date", record["reg_date"], "date", indent=3)
    xml += cluster_close(CL_EVENT, indent=2)

    xml += cluster_close(GOVERNED_RECORD, indent=1)

    # Native governance slots, DM order: subject, provider, Audit, attestation.
    xml += native_partytype("subject", "Vital Record Subject", _full_name(person))
    xml += native_partytype("provider", "Vital Statistics Office",
                            f"{city} Vital Statistics Office")
    xml += audit(SYSTEM_AUDIT, prov["activity_timestamp_start"],
                 system_id_value=prov["system_identifier"])
    xml += attestation(pending=False,
                       reason=f"{event_type} record certified by the vital statistics office",
                       committer="Vital Statistics Office",
                       committed=prov["activity_timestamp_end"])

    xml += xml_footer(CT_ID)
    return xml


# ─── Record builders ─────────────────────────────────────────────────────────

def make_birth_record(person):
    return {
        "event_type": "Birth", "person": person,
        "city": person["city"], "province": person["province"],
        "event_date": person["dob"], "reg_date": person["dob"],
        "cert_num": next_cert(), "status": "Active",
    }


def make_marriage_record(person, marriage_date, city, province):
    return {
        "event_type": "Marriage", "person": person,
        "city": city, "province": province,
        "event_date": marriage_date, "reg_date": marriage_date,
        "cert_num": next_cert(), "status": "Active",
    }


def make_death_record(person, death_date):
    return {
        "event_type": "Death", "person": person,
        "city": person["city"], "province": person["province"],
        "event_date": death_date, "reg_date": death_date,
        "cert_num": next_cert(), "status": "Active",
        "cause": random.choice(CAUSES),
        "manner": random.choice(MANNERS),
        "place": random.choice(PLACES),
    }


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
        xml = build_instance(make_birth_record(person))
        write_xml(os.path.join(OUTPUT_DIR, f"vs-{cuid_generator()}.xml"), xml)
        count += 1

    # Marriage certificates for married cast members
    married_cast = [k for k, v in CAST.items() if v.get("marital_status") == "Married"]
    for key in married_cast:
        c = dict(CAST[key])
        marriage_date = random_date(2000, 2015)
        xml = build_instance(make_marriage_record(c, marriage_date, c["city"], c["province"]))
        write_xml(os.path.join(OUTPUT_DIR, f"vs-{cuid_generator()}.xml"), xml)
        count += 1

    # Background marriages: pair up married adults (~up to 500 marriages)
    adults = [p for p in PERSONS if p.get("key", "").startswith("bg_")
              and (2026 - int(p["dob"][:4])) >= 18
              and p.get("marital_status") == "Married"]
    random.shuffle(adults)
    num_pairs = min(len(adults) // 2, 500)
    for i in range(num_pairs):
        p1 = adults[i * 2]
        marriage_date = random_date(2005, 2024)
        xml = build_instance(make_marriage_record(p1, marriage_date, p1["city"], p1["province"]))
        write_xml(os.path.join(OUTPUT_DIR, f"vs-{cuid_generator()}.xml"), xml)
        count += 1

    # A small number of deaths among older adults
    elders = [p for p in PERSONS if p.get("key", "").startswith("bg_")
              and (2026 - int(p["dob"][:4])) >= 70]
    random.shuffle(elders)
    for p in elders[:200]:
        death_date = random_date(2020, 2025)
        xml = build_instance(make_death_record(p, death_date))
        write_xml(os.path.join(OUTPUT_DIR, f"vs-{cuid_generator()}.xml"), xml)
        count += 1

    print(f"Vital Statistics: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    generate()
