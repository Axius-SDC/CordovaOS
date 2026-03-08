"""
Shared utilities for CordovaOS demo data generation.

Provides XML element builders, name pools, geography, and the Contagion cast.
"""
import random
from datetime import datetime, date
from cuid2 import cuid_wrapper

cuid_generator = cuid_wrapper()

SDC4_NS = "https://semanticdatacharter.com/ns/sdc4/"
XSI_NS = "http://www.w3.org/2001/XMLSchema-instance"

# ─── Geography ───────────────────────────────────────────────────────────────

PROVINCES = ["Aldara", "Brevina", "Celara"]

PROVINCE_CITIES = {
    "Aldara": ["Porto Sereno", "Montecalvo", "Bahia Linda"],
    "Brevina": ["Campoluz", "Sierra Verde", "Tierra Roja"],
    "Celara": ["Novaciudad", "Costa Brava", "Lago Azul"],
}

PROVINCE_CODES = {"Aldara": "AL", "Brevina": "BR", "Celara": "CE"}
CITY_CODES = {
    "Porto Sereno": "01", "Montecalvo": "02", "Bahia Linda": "03",
    "Campoluz": "01", "Sierra Verde": "02", "Tierra Roja": "03",
    "Novaciudad": "01", "Costa Brava": "02", "Lago Azul": "03",
}

ALL_CITIES = [c for cities in PROVINCE_CITIES.values() for c in cities]

CITY_TO_PROVINCE = {}
for prov, cities in PROVINCE_CITIES.items():
    for city in cities:
        CITY_TO_PROVINCE[city] = prov


def random_city_province():
    """Return (city, province) tuple."""
    prov = random.choice(PROVINCES)
    city = random.choice(PROVINCE_CITIES[prov])
    return city, prov


# ─── Street Names ────────────────────────────────────────────────────────────

STREET_NAMES = [
    "Calle de las Flores", "Avenida Universidad", "Calle Mayor",
    "Paseo del Puerto", "Calle del Mar", "Avenida Libertad",
    "Calle San Martin", "Boulevard Costero", "Calle de la Paz",
    "Avenida Nacional", "Calle del Sol", "Paseo de la Luna",
    "Calle Victoria", "Avenida del Parque", "Calle Comercio",
    "Calle Bolivar", "Avenida de la Costa", "Calle Independencia",
    "Paseo de las Americas", "Calle Esperanza", "Calle del Rio",
    "Avenida Central", "Calle Nueva", "Calle Progreso",
]


def random_address():
    """Return a street address string."""
    number = random.randint(1, 200)
    street = random.choice(STREET_NAMES)
    return f"{number} {street}"


# ─── Name Pools ──────────────────────────────────────────────────────────────

MALE_GIVEN = [
    "Carlos", "Alejandro", "Diego", "Fernando", "Gabriel", "Hector",
    "Ivan", "Javier", "Luis", "Manuel", "Nicolas", "Oscar", "Pablo",
    "Rafael", "Santiago", "Tomas", "Victor", "Andres", "Eduardo",
    "Francisco", "Ricardo", "Antonio", "Miguel", "Jorge", "Roberto",
    "Daniel", "Pedro", "Ramon", "Sergio", "Alberto", "Enrique",
    "Arturo", "Cesar", "Emilio", "Gustavo", "Ignacio", "Joaquin",
    "Leonardo", "Marco", "Patricio",
]

FEMALE_GIVEN = [
    "Elena", "Isabel", "Maria", "Lucia", "Ana", "Carmen", "Sofia",
    "Valentina", "Gabriela", "Natalia", "Camila", "Daniela", "Laura",
    "Mariana", "Paula", "Rosa", "Teresa", "Victoria", "Andrea",
    "Catalina", "Diana", "Eva", "Fernanda", "Gloria", "Helena",
    "Julia", "Lorena", "Monica", "Patricia", "Sandra", "Alicia",
    "Beatriz", "Clara", "Dolores", "Esperanza", "Francisca",
    "Ines", "Julieta", "Liliana", "Marta",
]

SURNAMES = [
    "Mendoza", "Reyes", "Avila", "Santos", "Ferrer", "Gutierrez",
    "Lucero", "Salazar", "Rodriguez", "Garcia", "Martinez", "Lopez",
    "Gonzalez", "Hernandez", "Perez", "Sanchez", "Ramirez", "Torres",
    "Flores", "Rivera", "Cruz", "Morales", "Ortiz", "Castillo",
    "Nunez", "Romero", "Diaz", "Alvarez", "Vargas", "Delgado",
    "Vega", "Moreno", "Jimenez", "Ramos", "Medina", "Guerrero",
    "Castro", "Soto", "Paredes", "Espinoza", "Cardenas", "Rojas",
    "Aguilar", "Cabrera", "Campos", "Fuentes", "Leon", "Navarro",
    "Pena", "Rios",
]

MIDDLE_NAMES = [
    "Antonio", "Maria", "Jose", "Rosa", "Luis", "Teresa", "Angel",
    "Carmen", "Francisco", "Isabel", "Manuel", "Lucia", "Alberto",
    "Elena", "Eduardo", "Gloria", "Ricardo", "Alicia", "Ernesto",
    "Patricia",
]


def random_name(sex="Male"):
    """Return (given, middle, surname) tuple."""
    pool = MALE_GIVEN if sex == "Male" else FEMALE_GIVEN
    given = random.choice(pool)
    middle = random.choice(MIDDLE_NAMES)
    surname = random.choice(SURNAMES)
    return given, middle, surname


# ─── CID Generation ──────────────────────────────────────────────────────────

_cid_counter = {}


def generate_cid(province_code, city_code):
    """Generate a National ID in format COR-PP99-NNNNNN."""
    key = f"{province_code}{city_code}"
    if key not in _cid_counter:
        _cid_counter[key] = random.randint(100000, 399999)
    _cid_counter[key] += 1
    return f"COR-{province_code}{city_code}-{_cid_counter[key]:06d}"


def generate_cid_for_city(city):
    """Generate a CID for a given city."""
    prov = CITY_TO_PROVINCE[city]
    return generate_cid(PROVINCE_CODES[prov], CITY_CODES[city])


# ─── Phone / Email ───────────────────────────────────────────────────────────

AREA_CODES = {
    "Porto Sereno": "100", "Montecalvo": "102", "Bahia Linda": "104",
    "Campoluz": "200", "Sierra Verde": "202", "Tierra Roja": "204",
    "Novaciudad": "300", "Costa Brava": "302", "Lago Azul": "304",
}


def generate_phone(city):
    """Generate Cordova phone: +99-PPP-NNN-NNNN."""
    area = AREA_CODES.get(city, "100")
    n1 = random.randint(100, 999)
    n2 = random.randint(1000, 9999)
    return f"+99-{area}-{n1}-{n2}"


def generate_email(given, surname):
    """Generate a .cor email address."""
    return f"{given.lower()}.{surname.lower()}@mail.cor"


# ─── Business Registry Numbers ───────────────────────────────────────────────

_brn_counter = 0


def generate_brn():
    """Generate BIZ-NNNNNN."""
    global _brn_counter
    _brn_counter += 1
    return f"BIZ-{_brn_counter:06d}"


# ─── Parcel Numbers ──────────────────────────────────────────────────────────

_parcel_counter = {}


def generate_parcel(province_code, city_code):
    """Generate PP-CC-NNNNNN."""
    key = f"{province_code}-{city_code}"
    if key not in _parcel_counter:
        _parcel_counter[key] = random.randint(100000, 199999)
    _parcel_counter[key] += 1
    return f"{province_code}-{city_code}-{_parcel_counter[key]:06d}"


# ─── Date Helpers ────────────────────────────────────────────────────────────

def random_dob(min_age=18, max_age=75):
    """Return a random date of birth as YYYY-MM-DD string."""
    year = 2026 - random.randint(min_age, max_age)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{year:04d}-{month:02d}-{day:02d}"


def random_date(start_year=2020, end_year=2025):
    """Return a random date as YYYY-MM-DD string."""
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{year:04d}-{month:02d}-{day:02d}"


def now_iso():
    """Return current UTC timestamp as ISO string."""
    return datetime.utcnow().isoformat()


# ─── XML Builders ────────────────────────────────────────────────────────────

def xml_header(ct_id):
    """Return the XML declaration and root opening tag."""
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<sdc4:dm-{ct_id}
  xmlns:xsi="{XSI_NS}"
  xmlns:sdc4="{SDC4_NS}"
  xsi:schemaLocation="{SDC4_NS} https://semanticdatacharter.com/dmlib/dm-{ct_id}.xsd">
'''


def xml_preamble(dm_label, instance_id=None):
    """Return dm-label through current-state elements."""
    iid = instance_id or cuid_generator()
    ts = now_iso()
    return f'''  <dm-label>{dm_label}</dm-label>
  <dm-language>en-US</dm-language>
  <dm-encoding>utf-8</dm-encoding>
  <creation_timestamp>{ts}</creation_timestamp>
  <instance_id>{iid}</instance_id>
  <instance_version>1</instance_version>
  <source_instance_id/>
  <source_version_id/>
  <current-state/>
'''


def xml_footer(ct_id):
    """Return root closing tag."""
    return f'</sdc4:dm-{ct_id}>\n'


def xdstring(component_id, wrapper_id, label, value, indent=2):
    """Build an XdString component XML fragment."""
    pad = "  " * indent
    return f'''{pad}<sdc4:{wrapper_id}>
{pad}  <sdc4:{component_id}>
{pad}    <label>{label}</label>
{pad}    <xdstring-value>{_esc(value)}</xdstring-value>
{pad}  </sdc4:{component_id}>
{pad}</sdc4:{wrapper_id}>
'''


def xdtoken(component_id, wrapper_id, label, value, indent=2):
    """Build an XdToken component XML fragment."""
    pad = "  " * indent
    return f'''{pad}<sdc4:{wrapper_id}>
{pad}  <sdc4:{component_id}>
{pad}    <label>{label}</label>
{pad}    <xdtoken-value>{_esc(value)}</xdtoken-value>
{pad}  </sdc4:{component_id}>
{pad}</sdc4:{wrapper_id}>
'''


def xdtemporal(component_id, wrapper_id, label, value, variant="date", indent=2):
    """Build an XdTemporal component XML fragment."""
    pad = "  " * indent
    return f'''{pad}<sdc4:{wrapper_id}>
{pad}  <sdc4:{component_id}>
{pad}    <label>{label}</label>
{pad}    <xdtemporal-{variant}>{value}</xdtemporal-{variant}>
{pad}  </sdc4:{component_id}>
{pad}</sdc4:{wrapper_id}>
'''


def xdcount(component_id, wrapper_id, label, value, units_label, units_value=None, indent=2):
    """Build an XdCount component XML fragment.

    units_label: the label inside xdcount-units (e.g. "Persons")
    units_value: the xdstring-value inside xdcount-units (defaults to units_label)
    """
    pad = "  " * indent
    uv = _esc(units_value or units_label)
    return f'''{pad}<sdc4:{wrapper_id}>
{pad}  <sdc4:{component_id}>
{pad}    <label>{label}</label>
{pad}    <xdcount-value>{value}</xdcount-value>
{pad}    <xdcount-units>
{pad}      <label>{_esc(units_label)}</label>
{pad}      <xdstring-value>{uv}</xdstring-value>
{pad}    </xdcount-units>
{pad}  </sdc4:{component_id}>
{pad}</sdc4:{wrapper_id}>
'''


def xdquantity(component_id, wrapper_id, label, value, units_label, units_value=None, indent=2):
    """Build an XdQuantity component XML fragment.

    units_label: the label inside xdquantity-units (e.g. "Cordova Córdoba (COR)")
    units_value: the xdstring-value inside xdquantity-units (defaults to units_label)
    """
    pad = "  " * indent
    uv = _esc(units_value or units_label)
    return f'''{pad}<sdc4:{wrapper_id}>
{pad}  <sdc4:{component_id}>
{pad}    <label>{label}</label>
{pad}    <xdquantity-value>{value}</xdquantity-value>
{pad}    <xdquantity-units>
{pad}      <label>{_esc(units_label)}</label>
{pad}      <xdstring-value>{uv}</xdstring-value>
{pad}    </xdquantity-units>
{pad}  </sdc4:{component_id}>
{pad}</sdc4:{wrapper_id}>
'''


def xdboolean(component_id, wrapper_id, label, value, indent=2):
    """Build an XdBoolean component XML fragment."""
    pad = "  " * indent
    val = "true" if value else "false"
    return f'''{pad}<sdc4:{wrapper_id}>
{pad}  <sdc4:{component_id}>
{pad}    <label>{label}</label>
{pad}    <xdboolean-value>{val}</xdboolean-value>
{pad}  </sdc4:{component_id}>
{pad}</sdc4:{wrapper_id}>
'''


def xdtemporal_multi(component_id, wrapper_id, label, date_val, variants=("date", "year", "year-month"), indent=2):
    """Build an XdTemporal with multiple variant elements derived from a date string."""
    pad = "  " * indent
    parts = [f"{pad}<sdc4:{wrapper_id}>", f"{pad}  <sdc4:{component_id}>", f"{pad}    <label>{label}</label>"]
    for v in variants:
        if v == "date":
            parts.append(f"{pad}    <xdtemporal-date>{date_val}</xdtemporal-date>")
        elif v == "year":
            parts.append(f"{pad}    <xdtemporal-year>{date_val[:4]}</xdtemporal-year>")
        elif v == "year-month":
            parts.append(f"{pad}    <xdtemporal-year-month>{date_val[:7]}</xdtemporal-year-month>")
        elif v == "datetime":
            parts.append(f"{pad}    <xdtemporal-datetime>{date_val}</xdtemporal-datetime>")
    parts.append(f"{pad}  </sdc4:{component_id}>")
    parts.append(f"{pad}</sdc4:{wrapper_id}>")
    return "\n".join(parts) + "\n"


def xdboolean_stub(component_id, wrapper_id, label, indent=2):
    """Build an XdBoolean stub (true-value/false-value not yet implemented)."""
    pad = "  " * indent
    return f'''{pad}<sdc4:{wrapper_id}>
{pad}  <sdc4:{component_id}>
{pad}    <label>{label}</label>
{pad}    <!-- Element true-value not yet implemented -->
{pad}    <!-- Element false-value not yet implemented -->
{pad}  </sdc4:{component_id}>
{pad}</sdc4:{wrapper_id}>
'''


def xdordinal_stub(component_id, wrapper_id, label, indent=2):
    """Build an XdOrdinal stub (ordinal/symbol not yet implemented)."""
    pad = "  " * indent
    return f'''{pad}<sdc4:{wrapper_id}>
{pad}  <sdc4:{component_id}>
{pad}    <label>{label}</label>
{pad}    <!-- Element ordinal not yet implemented -->
{pad}    <!-- Element symbol not yet implemented -->
{pad}  </sdc4:{component_id}>
{pad}</sdc4:{wrapper_id}>
'''


def cluster_open(cluster_id, label, indent=1):
    """Open a cluster element."""
    pad = "  " * indent
    return f'{pad}<sdc4:{cluster_id}>\n{pad}  <label>{label}</label>\n'


def cluster_close(cluster_id, indent=1):
    """Close a cluster element."""
    pad = "  " * indent
    return f'{pad}</sdc4:{cluster_id}>\n'


def party_stub(cluster_id, label, indent=1):
    """Return a party-details stub cluster."""
    pad = "  " * indent
    return f'''{pad}<sdc4:{cluster_id}>
{pad}  <label>{label}</label>
{pad}    <!-- Element party-details not yet implemented -->
{pad}</sdc4:{cluster_id}>
'''


def write_xml(filepath, content):
    """Write XML content to file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def _esc(text):
    """Escape XML special characters."""
    if text is None:
        return ""
    s = str(text)
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


# ─── Contagion Cast ──────────────────────────────────────────────────────────

CAST = {
    "carlos": {
        "cid": "COR-AL01-271845",
        "given": "Carlos", "middle": "Antonio", "surname": "Mendoza",
        "sex": "Male", "gender": "Male", "dob": "1991-08-14",
        "city": "Porto Sereno", "province": "Aldara",
        "address": "42 Calle de las Flores", "address2": "Apt 3B",
        "country_of_birth": "Republic of Cordova",
        "marital_status": "Single",
        "phone": "+99-100-555-1845", "email": "carlos.mendoza@mail.cor",
        "contact_pref": "Phone",
    },
    "elena": {
        "cid": "COR-CE01-271903",
        "given": "Elena", "middle": "Maria", "surname": "Mendoza",
        "sex": "Female", "gender": "Female", "dob": "1994-11-22",
        "city": "Novaciudad", "province": "Celara",
        "address": "18 Avenida Universidad", "address2": "Unit 12",
        "country_of_birth": "Republic of Cordova",
        "marital_status": "Single",
        "phone": "+99-300-555-1903", "email": "elena.mendoza@mail.cor",
        "contact_pref": "Email",
    },
    "dr_reyes": {
        "cid": "COR-AL01-195322",
        "given": "Isabel", "middle": "Carmen", "surname": "Reyes",
        "sex": "Female", "gender": "Female", "dob": "1978-03-05",
        "city": "Porto Sereno", "province": "Aldara",
        "address": "7 Boulevard Costero", "address2": "",
        "country_of_birth": "Republic of Cordova",
        "marital_status": "Married",
        "phone": "+99-100-555-5322", "email": "isabel.reyes@mail.cor",
        "contact_pref": "Email",
    },
    "governor_avila": {
        "cid": "COR-CE01-104287",
        "given": "Tomas", "middle": "Eduardo", "surname": "Avila",
        "sex": "Male", "gender": "Male", "dob": "1965-06-18",
        "city": "Novaciudad", "province": "Celara",
        "address": "1 Avenida Nacional", "address2": "Governor's Residence",
        "country_of_birth": "Republic of Cordova",
        "marital_status": "Married",
        "phone": "+99-300-555-4287", "email": "tomas.avila@gov.cor",
        "contact_pref": "Phone",
    },
    "sgt_santos": {
        "cid": "COR-AL01-203847",
        "given": "Maria", "middle": "Rosa", "surname": "Santos",
        "sex": "Female", "gender": "Female", "dob": "1985-01-30",
        "city": "Porto Sereno", "province": "Aldara",
        "address": "55 Calle San Martin", "address2": "",
        "country_of_birth": "Republic of Cordova",
        "marital_status": "Single",
        "phone": "+99-100-555-3847", "email": "maria.santos@cnp.cor",
        "contact_pref": "Phone",
    },
    "dr_ferrer": {
        "cid": "COR-AL01-188934",
        "given": "Lucia", "middle": "Teresa", "surname": "Ferrer",
        "sex": "Female", "gender": "Female", "dob": "1972-09-12",
        "city": "Porto Sereno", "province": "Aldara",
        "address": "23 Avenida Libertad", "address2": "",
        "country_of_birth": "Republic of Cordova",
        "marital_status": "Married",
        "phone": "+99-100-555-8934", "email": "lucia.ferrer@health.cor",
        "contact_pref": "Email",
    },
    "dr_gutierrez": {
        "cid": "COR-BR01-334201",
        "given": "Ramon", "middle": "Luis", "surname": "Gutierrez",
        "sex": "Male", "gender": "Male", "dob": "1980-04-19",
        "city": "Campoluz", "province": "Brevina",
        "address": "10 Calle del Sol", "address2": "",
        "country_of_birth": "Republic of Cordova",
        "marital_status": "Married",
        "phone": "+99-200-555-4201", "email": "ramon.gutierrez@unc.cor",
        "contact_pref": "Email",
    },
    "prof_lucero": {
        "cid": "COR-BR01-298744",
        "given": "Ana", "middle": "Patricia", "surname": "Lucero",
        "sex": "Female", "gender": "Female", "dob": "1976-12-03",
        "city": "Campoluz", "province": "Brevina",
        "address": "34 Avenida del Parque", "address2": "",
        "country_of_birth": "Republic of Cordova",
        "marital_status": "Married",
        "phone": "+99-200-555-8744", "email": "ana.lucero@unc.cor",
        "contact_pref": "Email",
    },
}

# Persons list: all cast + generated background persons
# This will be populated by civil_registry generator and reused by other domains
PERSONS = []
