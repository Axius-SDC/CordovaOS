"""
Generate Business Registry XML instances for CordovaOS demo.

Governance-composed model (SDC4 v2 envelope): a "Business Registry Governed
Record" wrapper holding the "Business Registry Office" data cluster (4 leaves)
and the "Provenance Components" cluster (7 PROV leaves), followed by the native
governance slots subject / provider / Audit / attestation.

Key businesses from the Contagion narrative + background businesses.
Output: import_data/business_registry/
"""
import os
import random

from shared import (
    scaled,
    random_city_province, random_address, random_date,
    generate_brn, generate_phone, generate_email,
    xml_header, xml_preamble, xml_footer, write_xml,
    xdstring, xdtoken, xdtemporal,
    cluster_open, cluster_close, native_partytype,
    make_provenance_values, audit, attestation,
    cuid_generator, CITY_TO_PROVINCE,
)

CT_ID = "x250838l7oi6l3yavg9twc1i"
DM_LABEL = "Business Registry"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "sdc4", "import_data", "business_registry")

# ─── Governance envelope (from XSD sequence + template instance) ─────────────
# Governed Record wrapper (Item) and the two child clusters.
GOVERNED_RECORD = "ms-og2caskrf2nq0sszcztp3avx"   # "Business Registry Governed Record"
CL_DATA         = "ms-l69byv9b04bedudm59pfclvw"   # "Business Registry Office" (data cluster)
CL_PROV         = "ms-hdhjfg00tngir2txgqyka9cv"   # "Provenance Components"

# Data-cluster leaves (leaf component, adapter wrapper) — re-keyed adapter ids
# for v2, sourced from the template dm-*.xml. Order per mc-l69byv9b04... sequence.
W_ORG_ID    = ("ms-ule5u2z3rjpa9pooaifwj1n3", "ms-xqxyyqzubvs56u8kigibkm0c")  # organization_identifier
W_ORG_NAME  = ("ms-ifw5zfe4oiijbxjn1ylc2wm3", "ms-cr9qfn8vytz4mmlxbcl87ge8")  # organization_name
W_ORG_TYPE  = ("ms-bpqtzla39dwentygpwea8276", "ms-qqz9g2f0t01235xpcyc9pmko")  # organization_type (enum)
W_AGENT     = ("ms-nesxtz8c5o665swc9lhvqkjj", "ms-br3rpp49wxxqze1v0o2wyfi2")  # PROV Agent Type (enum)

# Provenance Components leaves (leaf component, adapter wrapper). Order per
# mc-hdhjfg00... sequence.
P_ACT_DESC  = ("ms-m9xg6e182m1oq77ssrf9iujv", "ms-m97n9nia9v9gh1jnfhmp23nr")  # activity_description
P_ACT_TYPE  = ("ms-ccj1yq2wtwknobszkgzzdbtr", "ms-mk6yzh32rwhv0ciprvli9tef")  # prov_activity_type
P_SYS_ID    = ("ms-bd3s8t23d6m3zizmpwavc32y", "ms-kfuk50puofyygd0q7sc4k0xh")  # system_identifier
P_LOC_ID    = ("ms-zr59goe24qkocprl3feul3mt", "ms-kwlr9oc2a9dxcoajrbf3vw6n")  # system_location_identifier
P_LOC_NAME  = ("ms-fnodzqkbyskwe7nh58rs336k", "ms-lh0gbxrhw64hmtqelr02cvq5")  # system_location_name
P_TS_END    = ("ms-edvvjznmaoibzmfna0uuoo37", "ms-awtmipfy5eyns66da5org50r")  # activity_timestamp_end
P_TS_START  = ("ms-o72s5793973fzho35rnaughs", "ms-t43xb4p92eawh46s02i8bhj0")  # activity_timestamp_start

# System Audit component (substitutionGroup="sdc4:Audit"); all five fixed labels
# match the shared audit() defaults (System Audit / service_account_id /
# System User / Contact and Access / Software Agent Details).
AUDIT_COMPONENT = "ms-fotc5adg15ek2b9ermx2mcih"

WORKFLOW_STATES = ["Registered", "Active", "Suspended", "Dissolved"]

# organization_type enum (fixed by XSD): corporation, government, nonprofit,
# academic, department, vendor.
ORG_TYPES = ["corporation", "government", "nonprofit", "academic", "department", "vendor"]
# PROV Agent Type enum (fixed by XSD): Person, Organization, SoftwareAgent.
# Registered businesses are institutional agents.
AGENT_TYPE_ORG = "Organization"

# ─── Contagion narrative businesses ──────────────────────────────────────────
BUSINESSES = [
    {"brn": "BIZ-001102", "name": "Pacifico Meridional Shipping S.A.",
     "org_type": "corporation",
     "city": "Porto Sereno", "province": "Aldara"},
    {"brn": "BIZ-000847", "name": "Universidad Nacional de Cordova",
     "org_type": "academic",
     "city": "Campoluz", "province": "Brevina"},
    {"brn": "BIZ-000523", "name": "Porto Sereno General Hospital",
     "org_type": "government",
     "city": "Porto Sereno", "province": "Aldara"},
    {"brn": "BIZ-000101", "name": "Cordova National Police",
     "org_type": "government",
     "city": "Novaciudad", "province": "Celara"},
    {"brn": "BIZ-000205", "name": "Provincial Health Office - Aldara",
     "org_type": "government",
     "city": "Porto Sereno", "province": "Aldara"},
]

BACKGROUND_INDUSTRIES = [
    "Retail", "Agriculture", "Fishing", "Construction", "Tourism",
    "Restaurant", "Manufacturing", "Finance", "Technology", "Legal Services",
    "Real Estate", "Import/Export", "Automotive", "Pharmacy", "Insurance",
    "Education", "Transportation", "Hospitality", "Food Processing",
    "Textiles", "Mining", "Telecommunications", "Media", "Healthcare Services",
    "Consulting", "Architecture", "Environmental Services", "Energy",
    "Security Services", "Veterinary", "Printing", "Logistics",
]

_BIZ_PREFIXES = [
    "Cordova", "Isla", "Costa", "Sierra", "Pacific", "Tropical", "Central",
    "Nacional", "Bahia", "Puerto", "Estrella", "Sol", "Meridional", "Andino",
    "Caribe", "Atlantico", "Norte", "Sur", "Dorado", "Nuevo",
]
_BIZ_SUFFIXES = {
    "Retail": ["Market", "Store", "Tienda", "Bodega", "Boutique"],
    "Agriculture": ["Farms", "Agricola", "Plantation", "Growers", "Harvest"],
    "Fishing": ["Pescadores", "Fishery", "Mariscos", "Seafood Co."],
    "Construction": ["Construction", "Builders", "Constructora", "Engineering"],
    "Tourism": ["Tours", "Travel", "Adventures", "Excursions", "Resort"],
    "Restaurant": ["Restaurant", "Cocina", "Cafe", "Bistro", "Cantina"],
    "Manufacturing": ["Manufacturing", "Industrial", "Products", "Factory"],
    "Finance": ["Finance", "Capital", "Bank", "Credit Union", "Investments"],
    "Technology": ["Tech", "Solutions", "Systems", "Digital", "Software"],
    "Legal Services": ["Legal", "Associates", "Law Group", "Abogados"],
    "Real Estate": ["Real Estate", "Properties", "Inmobiliaria", "Homes"],
    "Import/Export": ["Import/Export", "Trading", "Comercio", "Global Trade"],
    "Automotive": ["Automotive", "Motors", "Auto Parts", "Garage"],
    "Pharmacy": ["Pharmacy", "Farmacia", "Health Supply", "Drugstore"],
    "Insurance": ["Insurance", "Seguros", "Risk Group", "Assurance"],
    "Education": ["Academy", "Institute", "School", "Learning Center"],
    "Transportation": ["Transport", "Logistics", "Carriers", "Express"],
    "Hospitality": ["Hotel", "Inn", "Lodge", "Hospedaje", "Posada"],
    "Food Processing": ["Foods", "Processing", "Alimentos", "Packaging"],
    "Textiles": ["Textiles", "Fabrics", "Clothing", "Fashion"],
    "Mining": ["Mining", "Minerals", "Extraction", "Resources"],
    "Telecommunications": ["Telecom", "Communications", "Networks", "Connect"],
    "Media": ["Media", "Publishing", "Broadcasting", "Press"],
    "Healthcare Services": ["Health", "Medical", "Clinic", "Wellness"],
    "Consulting": ["Consulting", "Advisors", "Strategy", "Partners"],
    "Architecture": ["Architects", "Design Studio", "Urbanism", "Planners"],
    "Environmental Services": ["Environmental", "Green", "Eco Services", "Recycling"],
    "Energy": ["Energy", "Power", "Solar", "Electric"],
    "Security Services": ["Security", "Protection", "Vigilance", "Guard"],
    "Veterinary": ["Veterinary", "Animal Care", "Pet Clinic"],
    "Printing": ["Print", "Graphics", "Press", "Imprenta"],
    "Logistics": ["Logistics", "Freight", "Shipping", "Warehousing"],
}
_ENTITY_TYPES = ["S.A.", "Ltd.", "Co-op", "S.R.L.", "", "", ""]

# Map a background industry to a plausible organization_type enum value.
_INDUSTRY_ORG_TYPE = {
    "Education": "academic",
    "Healthcare Services": "nonprofit",
    "Environmental Services": "nonprofit",
    "Public Health": "government",
}

_used_biz_names = set()


def _generate_biz_name(industry, city):
    """Generate a unique business name based on industry and location."""
    for _ in range(20):
        prefix = random.choice(_BIZ_PREFIXES + [city.split()[0]])
        suffixes = _BIZ_SUFFIXES.get(industry, ["Services", "Group", "Company"])
        suffix = random.choice(suffixes)
        entity = random.choice(_ENTITY_TYPES)
        name = f"{prefix} {suffix}"
        if entity:
            name = f"{name} {entity}"
        if name not in _used_biz_names:
            _used_biz_names.add(name)
            return name
    _used_biz_names.add(f"{city} {industry} #{len(_used_biz_names)}")
    return f"{city} {industry} #{len(_used_biz_names)}"


def build_instance(biz):
    """Build a governance-composed Business Registry XML instance for one business."""
    city = biz.get("city") or random_city_province()[0]
    # NB: system_identifier is urn:cordova:system:<slug-of-name> and the leaf
    # caps at 50 chars, so keep the system name short.
    prov = make_provenance_values("Cordova Business Registry", "RecordRegistration", city)
    state = random.choice(WORKFLOW_STATES)

    xml = xml_header(CT_ID)
    xml += xml_preamble(DM_LABEL, current_state=state)

    # Item: Governed Record wrapper.
    xml += cluster_open(GOVERNED_RECORD, "Business Registry Governed Record", indent=1)

    # Data cluster "Business Registry Office" — child order follows the XSD
    # sequence: organization_identifier, organization_name, organization_type,
    # PROV Agent Type.
    xml += cluster_open(CL_DATA, "Business Registry Office", indent=2)
    xml += xdstring(*W_ORG_ID, "organization_identifier", biz["brn"], indent=3)
    xml += xdstring(*W_ORG_NAME, "organization_name", biz["name"], indent=3)
    xml += xdtoken(*W_ORG_TYPE, "organization_type", biz["org_type"], indent=3)
    xml += xdtoken(*W_AGENT, "PROV Agent Type", AGENT_TYPE_ORG, indent=3)
    xml += cluster_close(CL_DATA, indent=2)

    # Provenance Components cluster (sibling of data, inside Governed Record).
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
    xml += native_partytype("subject", "Registered Organization", biz["name"])
    xml += native_partytype("provider", "Business Registry Office",
                            f"{city} Business Registry Office")
    xml += audit(AUDIT_COMPONENT, prov["activity_timestamp_start"],
                 system_id_value=prov["system_identifier"])
    xml += attestation(pending=False,
                       reason="Registration verified by the business registry office",
                       committer="Business Registry Office",
                       committed=prov["activity_timestamp_end"])

    xml += xml_footer(CT_ID)
    return xml


def make_named_businesses():
    """Return the Contagion-narrative businesses ready for build_instance."""
    return [dict(b) for b in BUSINESSES]


def make_background_businesses(count=495):
    """Generate background businesses spread across cities."""
    out = []
    for _ in range(count):
        city, province = random_city_province()
        industry = random.choice(BACKGROUND_INDUSTRIES)
        name = _generate_biz_name(industry, city)
        org_type = _INDUSTRY_ORG_TYPE.get(industry, random.choice(ORG_TYPES))
        out.append({
            "brn": generate_brn(),
            "name": name,
            "org_type": org_type,
            "city": city, "province": province,
        })
    return out


def generate():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    count = 0

    for biz in make_named_businesses() + make_background_businesses(scaled(495, 42)):
        xml = build_instance(biz)
        write_xml(os.path.join(OUTPUT_DIR, f"br-{cuid_generator()}.xml"), xml)
        count += 1

    print(f"Business Registry: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    generate()
