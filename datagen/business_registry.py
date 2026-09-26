"""
Business Registry 4.4.0: one record per registered organisation.

The model composes the NIEM library's organization (name, category, status,
established and incorporation dates, contact information, location) beside
Cordova's own Business Registry Number, the join every other domain uses for an
employer, a taxpayer or a vessel operator. The five Contagion-narrative
businesses keep their fixed BRNs; background businesses fill the nine cities
(495 full, 42 demo).
"""
import random

from shared import (
    scaled, random_city_province, random_address, random_date,
    generate_brn, generate_phone, generate_email,
    record, write_record, import_dir,
)

TITLE = "Business Registry"
SYSTEM = "Cordova Business Registry"
OUTPUT_DIR = import_dir("business_registry")

# The 4.3.1 organization types map onto the NIEM organization category code list.
ORG_TYPES = ["corporation", "government", "nonprofit", "academic", "department", "vendor"]
ND_EX_CODE = {"corporation": "BUSINESS", "government": "GOVERNMENT", "nonprofit": "CHARITY",
              "academic": "EDUCATION", "department": "GOVERNMENT", "vendor": "BUSINESS"}
# The asset-status workflow: a registration that is complete and in force, still being processed, or withdrawn.
# 4.3.1 states Registered/Active -> Completed, Suspended -> UnderDevelopment (under review), Dissolved -> Withdrawn.
STATE_OF = {"Registered": "Completed", "Active": "Completed", "Suspended": "UnderDevelopment", "Dissolved": "Withdrawn"}
STATUSES = ["Registered", "Active", "Active", "Active", "Suspended", "Dissolved"]

# ─── Contagion narrative businesses ──────────────────────────────────────────
BUSINESSES = [
    {"brn": "BIZ-001102", "name": "Pacifico Meridional Shipping S.A.", "org_type": "corporation",
     "industry": "Logistics", "city": "Porto Sereno", "province": "Aldara", "established": "1998-04-12"},
    {"brn": "BIZ-000847", "name": "Universidad Nacional de Cordova", "org_type": "academic",
     "industry": "Education", "city": "Campoluz", "province": "Brevina", "established": "1952-03-01"},
    {"brn": "BIZ-000523", "name": "Porto Sereno General Hospital", "org_type": "government",
     "industry": "Healthcare Services", "city": "Porto Sereno", "province": "Aldara", "established": "1961-09-15"},
    {"brn": "BIZ-000101", "name": "Cordova National Police", "org_type": "government",
     "industry": "Security Services", "city": "Novaciudad", "province": "Celara", "established": "1946-01-10"},
    {"brn": "BIZ-000205", "name": "Provincial Health Office - Aldara", "org_type": "government",
     "industry": "Public Health", "city": "Porto Sereno", "province": "Aldara", "established": "1972-06-30"},
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

# Map a background industry to a plausible organization type.
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


def _email_for(name):
    slug = "".join(ch for ch in name.lower().replace(" ", "") if ch.isalnum())[:24] or "office"
    return f"info@{slug}.co"


def build_instance(biz):
    """One Business Registry record for one organisation."""
    city, province = biz["city"], biz["province"]
    status = biz["status"]
    incorporated = biz["org_type"] in ("corporation", "vendor")
    values = {
        "Business Registry Office/Business Registry Number": biz["brn"],
        "Organization (NIEM)/Organization Name": biz["name"],
        "Organization (NIEM)/Organization Identification": biz["brn"],
        "Organization (NIEM)/Organization Category": biz["industry"],
        "Organization (NIEM)/Organization Category ND Ex Code": ND_EX_CODE[biz["org_type"]],
        "Organization (NIEM)/Organization Status": status,
        "Organization (NIEM)/Organization Active Indicator": status != "Dissolved",
        "Organization (NIEM)/Organization Incorporated Indicator": incorporated,
        "Organization (NIEM)/Organization Established Date": biz["established"],
        "Organization (NIEM)/Organization Incorporation Date": biz["established"] if incorporated else None,
        "Organization (NIEM)/Organization Termination Date": biz.get("terminated"),
        "Organization (NIEM)/Organization Jurisdiction Reference": f"urn:cordova:province:{province.lower()}",
        "Contact Information (NIEM)/Contact Point/Phone Number": biz["phone"],
        "Contact Information (NIEM)/Contact Point/Email Address": biz["email"],
        "Contact Information (NIEM)/Contact Point/Contact Method": "phone",
        "Contact Information (NIEM)/Contact Point/Contact Use": "work",
        "Contact Information (NIEM)/Address (NIEM)/Address Category Code": "registered office",
        "Contact Information (NIEM)/Address (NIEM)/International Address/Address (Line 1)": biz["address"],
        "Contact Information (NIEM)/Address (NIEM)/International Address/City Name": city,
        "Contact Information (NIEM)/Address (NIEM)/International Address/Region Name": province,
        "Contact Information (NIEM)/Address (NIEM)/International Address/Address Use": "work",
        "Location (NIEM)/Location Name": city,
        "Location (NIEM)/Location Category": "Registered office",
    }
    return record(TITLE, values, state=STATE_OF[status], system=SYSTEM, activity_type="RecordRegistration",
                  when=biz["registered"], city=city, province=province,
                  subject=("Registered Organization", biz["name"]), provider=("Business Registry Office", f"{city} Business Registry Office"),
                  attestation_reason="Registration verified by the business registry office", committer="Business Registry Office")


# Every business this generator wrote, in order. Employment reads it so that an
# employer is a registered organisation with a BRN rather than a free-text name.
REGISTERED = []


def employer_roster():
    """Businesses available as employers, or [] if the registry has not run."""
    return REGISTERED


def _complete(biz):
    """The contact and registration facts every record carries."""
    biz.setdefault("address", random_address())
    biz.setdefault("phone", generate_phone(biz["city"]))
    biz.setdefault("email", _email_for(biz["name"]))
    biz.setdefault("status", "Active")
    biz.setdefault("registered", biz["established"])
    if biz["status"] == "Dissolved":
        biz.setdefault("terminated", random_date(2022, 2025))
    return biz


def make_named_businesses():
    """The Contagion-narrative businesses ready for build_instance; all of them are active."""
    return [_complete(dict(b)) for b in BUSINESSES]


def make_background_businesses(count=495):
    """Generate background businesses spread across cities."""
    out = []
    for _ in range(count):
        city, province = random_city_province()
        industry = random.choice(BACKGROUND_INDUSTRIES)
        name = _generate_biz_name(industry, city)
        org_type = _INDUSTRY_ORG_TYPE.get(industry, random.choice(ORG_TYPES))
        out.append(_complete({
            "brn": generate_brn(), "name": name, "org_type": org_type, "industry": industry,
            "city": city, "province": province,
            "established": random_date(1985, 2024), "status": random.choice(STATUSES),
        }))
    return out


def generate():
    count = 0
    for biz in make_named_businesses() + make_background_businesses(scaled(495, 42)):
        write_record(OUTPUT_DIR, "br", build_instance(biz))
        REGISTERED.append(dict(biz))
        count += 1
    print(f"Business Registry: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    random.seed("cordovaos:Business Registry")
    generate()
