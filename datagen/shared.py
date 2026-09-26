"""
Shared utilities for CordovaOS demo data generation (4.4.0).

Name pools, geography, identifiers, the Contagion cast, and ``record()``: the one
call a generator makes per record. A generator names the values it has by label
path in the published model; the engine (engine.py) fills the model's own instance
template and the schema decides everything else. No generator carries an element
id, an element order or a governance envelope.
"""
import os
import random
import re
from datetime import datetime

from engine import EV, Quantity, Template
from schema import DMLIB, Schema

# Deterministic identifiers. A real CUID2 mixes in the clock, the process id and
# the hostname, so no two runs ever agree, and the README promises the same
# dataset every time. These ids keep the CUID2 shape the schemas require (24
# base-36 characters, leading letter) but are drawn from the module-level
# `random`, which generate_all.py seeds per generator. Same seed, same ids,
# same values, same relationships, on any machine; only record timestamps move.
_ID_ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789"


def cuid_generator():
    return random.choice(_ID_ALPHABET[:26]) + "".join(random.choices(_ID_ALPHABET, k=23))

# Demo-scale switch. Default is the full 25,000-resident dataset (~100K instances).
# Set CORDOVA_DEMO_SCALE=1 to generate a small PoC dataset that loads in minutes.
DEMO_SCALE = os.environ.get("CORDOVA_DEMO_SCALE") == "1"


def scaled(full, demo):
    """Return the demo count when CORDOVA_DEMO_SCALE=1, else the full count."""
    return demo if DEMO_SCALE else full

SDC4_NS = "https://semanticdatacharter.com/ns/sdc4/"
XSI_NS = "http://www.w3.org/2001/XMLSchema-instance"

# ─── Stated absences ─────────────────────────────────────────────────────────
# An absent value is stated, never implied. Where the schema REQUIRES a value and
# the record has none, the generator writes an ISO 21090 null flavor in its place.
# The instance is then invalid on purpose: the value element is mandatory, and
# the Exceptional Value records why it is missing rather than leaving a reader to
# guess. A fact that simply does not apply is left out (the key is not given, or
# its value is None), which is valid and asserts nothing.
ASKR = EV("ASKR")   # asked, and the subject declined to answer
ASKU = EV("ASKU")   # asked, and the answer is not known
MSK = EV("MSK")     # withheld for privacy or policy
NA = EV("NA")       # the field does not apply to this record
NASK = EV("NASK")   # never asked
NAV = EV("NAV")     # applies, exists somewhere, not available here
NI = EV("NI")       # absent, no reason recorded
UNK = EV("UNK")     # applies, and is not known

COR = "COR"   # the Cordova Córdoba; every amount in the models is a quantity in the kept COR units

# ─── Geography ───────────────────────────────────────────────────────────────

PROVINCES = ["Aldara", "Brevina", "Celara"]

# City names MUST match the model's City enum exactly (shared across all domains).
# Enum (from the City component): Porto Sereno, Vistamar, Rioseco (Aldara);
# Campoluz, Tierraverde, Montecara (Brevina); Novaciudad, Piedrasol, Lagunavista (Celara).
PROVINCE_CITIES = {
    "Aldara": ["Porto Sereno", "Vistamar", "Rioseco"],
    "Brevina": ["Campoluz", "Tierraverde", "Montecara"],
    "Celara": ["Novaciudad", "Piedrasol", "Lagunavista"],
}

PROVINCE_CODES = {"Aldara": "AL", "Brevina": "BR", "Celara": "CE"}
CITY_CODES = {
    "Porto Sereno": "01", "Vistamar": "02", "Rioseco": "03",
    "Campoluz": "01", "Tierraverde": "02", "Montecara": "03",
    "Novaciudad": "01", "Piedrasol": "02", "Lagunavista": "03",
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
    "Calle de los Heroes", "Avenida Maritima", "Calle Juarez",
    "Boulevard del Norte", "Calle de la Iglesia", "Avenida Republica",
    "Calle Minerva", "Paseo de los Presidentes", "Calle del Molino",
    "Avenida de los Volcanes", "Calle Primavera", "Calle del Mercado",
    "Boulevard de las Palmas", "Avenida de la Constitucion", "Calle Coral",
    "Calle Horizonte", "Paseo de la Sierra", "Calle de los Pescadores",
    "Avenida del Lago", "Calle Magnolia", "Calle de la Bahia",
    "Boulevard Tropical", "Avenida de los Pinos", "Calle Mirador",
    "Calle San Pedro", "Paseo de la Playa", "Calle de la Fuente",
    "Avenida Industrial", "Calle Almendro", "Calle de la Colina",
    "Boulevard San Jose", "Avenida de los Cedros", "Calle Otoño",
    "Calle del Faro", "Paseo de las Gaviotas", "Calle de los Naranjos",
    "Avenida del Sur", "Calle Real", "Calle de la Estacion",
    "Boulevard de la Selva", "Avenida los Andes", "Calle Jazmin",
    "Calle del Bosque", "Paseo de los Laureles", "Calle de los Olivos",
    "Avenida del Este", "Calle Roble", "Calle de la Cumbre",
    "Boulevard de las Aguas", "Avenida de la Marina", "Calle Orquidea",
    "Calle del Valle", "Paseo de las Rosas", "Calle del Muelle",
    "Avenida del Oeste", "Calle Girasol", "Calle de las Palomas",
    "Boulevard del Amanecer", "Avenida de los Manglares", "Calle Ceiba",
    "Calle de los Corales", "Paseo del Atardecer", "Calle del Arroyo",
    "Avenida Panamericana", "Calle Mariposa", "Calle de la Cascada",
    "Boulevard los Flamboyanes", "Avenida de las Islas", "Calle Bamboo",
    "Calle del Puente", "Paseo de los Cocoteros", "Calle de la Cuesta",
    "Avenida de los Tamarindos", "Calle Amapola", "Calle del Tesoro",
    "Boulevard del Caribe", "Avenida de la Reserva",
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
    "Leonardo", "Marco", "Patricio", "Adrian", "Agustin", "Alonso",
    "Alvaro", "Amado", "Angel", "Armando", "Baltazar", "Bautista",
    "Benito", "Bernardo", "Bruno", "Camilo", "Claudio", "Clemente",
    "Cristian", "Dario", "David", "Domingo", "Edgar", "Elias",
    "Ernesto", "Esteban", "Fabian", "Federico", "Felipe", "Felix",
    "Fidel", "Florencio", "Genaro", "Gerardo", "German", "Gilberto",
    "Gonzalo", "Gregorio", "Guillermo", "Hernan", "Hugo", "Ismael",
    "Isidro", "Jaime", "Jesus", "Joel", "Jose", "Juan",
    "Julian", "Julio", "Lazaro", "Leandro", "Lorenzo", "Luciano",
    "Marcelo", "Mario", "Martin", "Mateo", "Matias", "Maximo",
    "Moises", "Nelson", "Nestor", "Norberto", "Octavio", "Omar",
    "Orlando", "Oswaldo", "Paco", "Pascual", "Paulino", "Ramiro",
    "Raul", "Reinaldo", "Rene", "Rigoberto", "Rodolfo", "Rodrigo",
    "Rolando", "Roque", "Rosendo", "Ruben", "Salvador", "Samuel",
    "Santos", "Sebastian", "Silvio", "Simon", "Tadeo", "Teodoro",
    "Timoteo", "Tobias", "Trinidad", "Ulises", "Valentin", "Vicente",
    "Virgilio", "Walter", "Wilfredo", "Xavier", "Yago", "Zacarias",
    "Alfonso", "Benicio", "Carmelo", "Damian", "Efrain", "Fausto",
    "Gael", "Horacio", "Iker", "Jacinto", "Kilian", "Lisandro",
    "Mauro", "Nicanor", "Olegario", "Pancho", "Quintin", "Renato",
    "Sabino", "Thiago", "Urbano", "Ventura", "Wenceslao", "Ximeno",
    "Yanuel", "Zenon", "Abelardo", "Bartolome", "Celestino", "Desiderio",
    "Eugenio", "Fortunato", "Gaspar", "Heriberto", "Ireneo", "Juventino",
    "Ladislao", "Maximino", "Nazario", "Otoniel", "Primitivo", "Reginaldo",
    "Saturnino", "Teofilo", "Ubaldo", "Valerio", "Waldo", "Zeferino",
]

FEMALE_GIVEN = [
    "Elena", "Isabel", "Maria", "Lucia", "Ana", "Carmen", "Sofia",
    "Valentina", "Gabriela", "Natalia", "Camila", "Daniela", "Laura",
    "Mariana", "Paula", "Rosa", "Teresa", "Victoria", "Andrea",
    "Catalina", "Diana", "Eva", "Fernanda", "Gloria", "Helena",
    "Julia", "Lorena", "Monica", "Patricia", "Sandra", "Alicia",
    "Beatriz", "Clara", "Dolores", "Esperanza", "Francisca",
    "Ines", "Julieta", "Liliana", "Marta", "Adriana", "Agustina",
    "Alejandra", "Amelia", "Amparo", "Angela", "Antonia", "Araceli",
    "Aurora", "Barbara", "Belen", "Bianca", "Blanca", "Brenda",
    "Carla", "Carolina", "Cecilia", "Celeste", "Claudia", "Consuelo",
    "Cristina", "Dalia", "Debora", "Delfina", "Dora", "Edith",
    "Elisa", "Emilia", "Estela", "Eugenia", "Fabiola", "Fatima",
    "Felicia", "Flor", "Florencia", "Frida", "Gisela", "Graciela",
    "Guadalupe", "Hortensia", "Irene", "Iris", "Ivonne", "Jacinta",
    "Jimena", "Josefina", "Juana", "Karla", "Karina", "Leonor",
    "Leticia", "Lilia", "Lina", "Luisa", "Lourdes", "Luz",
    "Magdalena", "Manuela", "Marcela", "Margarita", "Marina", "Marisol",
    "Mercedes", "Milagros", "Miriam", "Nadia", "Nelly", "Nerea",
    "Nilda", "Noemi", "Norma", "Olga", "Paloma", "Pamela",
    "Paz", "Perla", "Pilar", "Priscila", "Rafaela", "Raquel",
    "Rebeca", "Regina", "Renata", "Rocio", "Romina", "Ruth",
    "Sabrina", "Sara", "Selena", "Silvia", "Soledad", "Sonia",
    "Susana", "Tamara", "Tatiana", "Vanessa", "Veronica", "Violeta",
    "Virginia", "Viviana", "Ximena", "Yolanda", "Zara", "Zoila",
    "Alba", "Alma", "Benita", "Candelaria", "Dina", "Elvira",
    "Fermina", "Gertrudis", "Herminia", "Iliana", "Justina", "Lidia",
    "Matilde", "Natividad", "Ofelia", "Pastora", "Remedios", "Rosalia",
    "Salvadora", "Teodora", "Ursula", "Venancia", "Wanda", "Zulema",
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
    "Pena", "Rios", "Acosta", "Aguirre", "Alarcon", "Alvarado",
    "Amaya", "Arce", "Arellano", "Arias", "Ayala", "Barrera",
    "Barrientos", "Bautista", "Becerra", "Benavides", "Bermudez", "Bravo",
    "Brito", "Bustamante", "Caballero", "Calderon", "Camacho", "Cano",
    "Carrillo", "Carvajal", "Castellanos", "Cervantes", "Chavez", "Cisneros",
    "Contreras", "Cordero", "Coronado", "Cortes", "Crespo", "Cuevas",
    "Davila", "Dominguez", "Duarte", "Duran", "Echeverria", "Escalante",
    "Escobar", "Esquivel", "Estrada", "Fajardo", "Figueroa", "Franco",
    "Galarza", "Gallardo", "Gallegos", "Garay", "Garrido", "Gimenez",
    "Godoy", "Gomez", "Gracia", "Guzman", "Heredia", "Herrera",
    "Hurtado", "Ibarra", "Iglesias", "Jaramillo", "Lara", "Ledesma",
    "Lira", "Lizarraga", "Llanos", "Luna", "Machado", "Maldonado",
    "Marin", "Marquez", "Mata", "Mejia", "Mena", "Miranda",
    "Molina", "Montalvo", "Montero", "Montoya", "Mora", "Moya",
    "Munoz", "Murillo", "Naranjo", "Narvaez", "Nava", "Nieto",
    "Ochoa", "Ojeda", "Olivares", "Olvera", "Orozco", "Orrego",
    "Osorio", "Otero", "Pacheco", "Padilla", "Palacios", "Pantoja",
    "Parra", "Paz", "Peralta", "Pimentel", "Pineda", "Pinzon",
    "Ponce", "Portillo", "Posada", "Prado", "Prieto", "Puentes",
    "Quevedo", "Quintana", "Quintero", "Quiroga", "Rangel", "Rendon",
    "Restrepo", "Rincon", "Rivas", "Robledo", "Rocha", "Roman",
    "Rosado", "Rosales", "Rubio", "Rueda", "Ruiz", "Saavedra",
    "Salas", "Saldana", "Sambrano", "Sandoval", "Santana", "Segura",
    "Serrano", "Sierra", "Silva", "Solano", "Solis", "Soriano",
    "Suarez", "Tapia", "Tejada", "Tellez", "Tirado", "Tovar",
    "Trejo", "Trevino", "Trujillo", "Uribe", "Urrutia", "Valdes",
    "Valencia", "Valenzuela", "Vallejo", "Vasquez", "Velasco", "Velasquez",
    "Velez", "Vera", "Vergara", "Vidal", "Villalobos", "Villanueva",
    "Villarreal", "Villegas", "Yanez", "Zambrano", "Zamora", "Zapata",
    "Zarate", "Zavala", "Zelaya", "Zepeda", "Zuniga", "Araya",
    "Balderas", "Barajas", "Barrios", "Batista", "Blanco", "Bonilla",
    "Borrego", "Canales", "Carmona", "Casanova", "Casas", "Centeno",
    "Cerda", "Chacon", "Cifuentes", "Colon", "Conde", "Corona",
    "Curiel", "Delvalle", "Enriquez", "Farias", "Ferreira", "Fierro",
    "Gaitan", "Galindo", "Gamboa", "Granados", "Grijalva", "Guevara",
    "Guillen", "Hinojosa", "Huerta", "Izquierdo", "Jurado", "Leal",
    "Leiva", "Linares", "Loaiza", "Lomeli", "Lozada", "Lozano",
    "Macias", "Madrigal", "Magana", "Manzano", "Marmol", "Melendez",
    "Mercado", "Mesa", "Montes", "Murrieta", "Noriega", "Oliva",
]

MIDDLE_NAMES = [
    "Antonio", "Maria", "Jose", "Rosa", "Luis", "Teresa", "Angel",
    "Carmen", "Francisco", "Isabel", "Manuel", "Lucia", "Alberto",
    "Elena", "Eduardo", "Gloria", "Ricardo", "Alicia", "Ernesto",
    "Patricia", "Alejandro", "Beatriz", "Carlos", "Dolores", "Emilio",
    "Fernanda", "Guillermo", "Helena", "Ignacio", "Josefina", "Leonardo",
    "Margarita", "Nicolas", "Olga", "Pedro", "Raquel", "Santiago",
    "Valentina", "Victor", "Andrea", "Benito", "Catalina", "Diego",
    "Esperanza", "Felipe", "Gabriela", "Horacio", "Ines", "Javier",
    "Lourdes", "Miguel", "Natalia", "Oscar", "Pilar", "Rafael",
    "Silvia", "Tomas", "Ursula", "Xavier", "Yolanda", "Andres",
    "Blanca", "Cesar", "Diana", "Esteban", "Florencia", "Gerardo",
    "Irene", "Julian", "Lorena", "Marcos", "Norberto", "Orlando",
    "Paloma", "Roberto", "Susana", "Teodoro", "Virginia", "Armando",
    "Cecilia", "Damian", "Estela", "Fabian", "Graciela", "Hernan",
    "Ivonne", "Joaquin", "Laura", "Marisol", "Nadia", "Pablo",
    "Remedios", "Salvador", "Tatiana", "Ulises", "Violeta", "Waldo",
    "Ximena", "Zacarias",
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

# Area codes MUST satisfy the Cordova Phone Number pattern \+99-[123][012]0-...
# i.e. the three digits are [123][012]0 (matches the City enum's documented codes).
AREA_CODES = {
    "Porto Sereno": "100", "Vistamar": "110", "Rioseco": "120",
    "Campoluz": "200", "Tierraverde": "210", "Montecara": "220",
    "Novaciudad": "300", "Piedrasol": "310", "Lagunavista": "320",
}


def generate_phone(city):
    """Generate Cordova phone: +99-AAA-NNN-NNNN (area AAA = [123][012]0)."""
    area = AREA_CODES.get(city, "100")
    n1 = random.randint(100, 999)
    n2 = random.randint(1000, 9999)
    return f"+99-{area}-{n1}-{n2}"


def generate_email(given, surname):
    """Generate a .cor email address."""
    return f"{given.lower()}.{surname.lower()}@{random.choice(['cordomail','novamail','portocorreo'])}.co"


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

def random_dob(min_age=18, max_age=75, distribution=None):
    """Return a random date of birth as YYYY-MM-DD string.

    distribution: optional dict mapping (min_age, max_age) -> weight for
    realistic age pyramids. If None, uniform between min_age and max_age.
    """
    if distribution:
        ranges, weights = zip(*distribution.items())
        chosen = random.choices(ranges, weights=weights, k=1)[0]
        age = random.randint(chosen[0], chosen[1])
    else:
        age = random.randint(min_age, max_age)
    year = 2026 - age
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{year:04d}-{month:02d}-{day:02d}"


# Realistic age distribution for Cordova's 25,000 population
AGE_DISTRIBUTION = {
    (0, 17): 22,     # children 22%
    (18, 35): 28,    # young adults 28%
    (36, 55): 25,    # middle-age 25%
    (56, 75): 18,    # older 18%
    (76, 95): 7,     # elderly 7%
}


def random_date(start_year=2020, end_year=2025):
    """Return a random date as YYYY-MM-DD string."""
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{year:04d}-{month:02d}-{day:02d}"


def now_iso():
    """Return current UTC timestamp as ISO string."""
    return datetime.utcnow().isoformat()




# ─── Models ──────────────────────────────────────────────────────────────────
# A generator names its model by title. The ct_id comes from the published schema
# the app carries, so a republished model needs no generator change.

_MODELS: dict[str, str] = {}


def model_ct(title: str) -> str:
    """The ct_id of the published model whose title starts with ``title``."""
    if not _MODELS:
        for name in sorted(os.listdir(DMLIB)):
            m = re.match(r"dm-([a-z0-9]{24})\.xsd$", name)
            if m:
                s = Schema.for_dm(m.group(1))
                _MODELS[s.label.get(s.dm, "")] = m.group(1)
    hits = [ct for t, ct in _MODELS.items() if t.startswith(title)]
    assert len(hits) == 1, (title, hits)
    return hits[0]


def template(title: str) -> Template:
    return Template.for_dm(model_ct(title))


# ─── Governance ──────────────────────────────────────────────────────────────
# Every 4.4.0 model composes the same governance envelope from the ProvGov library
# (PROV Activity, PROV Agent, Audit Event) beside the domain's data cluster, and
# binds the Cordova System Audit in the DM's audit slot. record() fills them all
# from a handful of facts about the record and the system that handled it.

SOFTWARE_VERSION = open(os.path.join(os.path.dirname(__file__), "..", "app", "sdc4", "VERSION"), encoding="utf-8").read().strip()

_activity_counter = 0
_audit_counter = 0


def _slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def governance(system: str, activity_type: str, when: str, city: str, cid: str | None = None, agent_org: str = "Government of the Republic of Cordova") -> dict:
    """Values for the PROV Activity, PROV Agent and Audit Event clusters of one record.

    ``system`` is the domain's handling system ("Cordova Civil Registry System"); ``when`` the
    day the record was made (YYYY-MM-DD) or a full timestamp; ``city`` where the system ran.
    """
    global _activity_counter, _audit_counter
    _activity_counter += 1
    _audit_counter += 1
    start = when if "T" in when else f"{when}T08:00:00"
    end = when if "T" in when else f"{when}T08:00:05"
    agent = f"urn:cordova:system:{_slug(system)}"
    values = {
        "PROV Activity/Activity Identifier": f"urn:cordova:activity:{_slug(system)}:{_activity_counter:07d}",
        "PROV Activity/Activity Label": activity_type,
        "PROV Activity/Activity Type": activity_type,
        "PROV Activity/Activity Description": f"{activity_type} performed in the {system}",
        "PROV Activity/Activity Status": "ActivityCompleted",
        "PROV Activity/Activity Location": city,
        "PROV Activity/Started At": start,
        "PROV Activity/Ended At": end,
        "PROV Activity/Was Associated With Reference": agent,
        "PROV Agent/Agent Identifier": agent,
        "PROV Agent/Agent Name": system,
        "PROV Agent/PROV Agent Type": "SoftwareAgent",
        "PROV Agent/Software Name": "CordovaOS",
        "PROV Agent/Software Version": SOFTWARE_VERSION,
        "PROV Agent/Agent Organization Name": agent_org,
        "Audit Event/Audit Event Identifier": f"urn:cordova:audit:{_slug(system)}:{_audit_counter:07d}",
        "Audit Event/Audit Event Action": "C",
        "Audit Event/Audit Event Outcome": "0",
        "Audit Event/Audit Recorded At": end,
        "Audit Event/Audit Agent Reference": agent,
        "Audit Event/Purpose of Use": "HOPERAT",
        "Audit Event/Confidentiality": "N",
        "Audit Event/Provenance Agent Type": "enterer",
        "Audit Event/System Identifier": agent,
        "Audit Event/System Location Name": f"{city} Data Center",
    }
    if cid:
        values["Audit Event/Data Subject Reference"] = f"urn:cordova:cid:{cid}"
    return values


def record(title: str, values: dict, *, state: str, system: str, activity_type: str, when: str, city: str, province: str,
           subject: tuple[str, str], provider: tuple[str, str], attestation_reason: str, committer: str, cid: str | None = None,
           instance_id: str | None = None) -> str:
    """One validated-shape instance of the model titled ``title``, as XML text.

    ``values`` maps label paths in the model to values (a string, a Quantity, a bool, an
    EV, or None to leave the fact out). Everything else is the governance every record
    carries: the PROV activity and agent, the audit event, the Cordova System Audit
    (system, city, province), the subject and provider parties, and the attestation.
    """
    t = template(title)
    vals = {k: v for k, v in values.items() if v is not None}
    vals.update(governance(system, activity_type, when, city, cid))
    end = when if "T" in when else f"{when}T08:00:05"
    return t.instance(vals, instance_id=instance_id or cuid_generator(), current_state=state, timestamp=now_iso(),
                      subject=subject, provider=provider,
                      audit={"system_id": f"urn:cordova:system:{_slug(system)}", "user": system, "timestamp": end,
                             "values": {"Cordova System Audit/City": city, "Cordova System Audit/Province": province}},
                      attestation={"reason": attestation_reason, "committer": committer, "committed": end, "pending": False})


def write_record(directory: str, prefix: str, xml: str) -> str:
    """Write one instance as ``<prefix>-<cuid>.xml`` with the XML declaration, and return the path."""
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, f"{prefix}-{cuid_generator()}.xml")
    with open(path, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write(xml)
    return path


IMPORT_ROOT = os.environ.get("CORDOVA_IMPORT_DIR") or os.path.join(os.path.dirname(__file__), "..", "app", "sdc4", "import_data")


def import_dir(app: str) -> str:
    """Where a domain's records are written: app/sdc4/import_data/<app>, or under CORDOVA_IMPORT_DIR."""
    return os.path.join(IMPORT_ROOT, app)


def full_name(person: dict) -> str:
    return f"{person['given']} {person['surname']}"


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
        "phone": "+99-100-555-1845", "email": "carlos.mendoza@cordomail.co",
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
        "phone": "+99-300-555-1903", "email": "elena.mendoza@cordomail.co",
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
        "phone": "+99-100-555-5322", "email": "isabel.reyes@novamail.co",
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
        "phone": "+99-300-555-4287", "email": "tomas.avila@cordomail.co",
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
        "phone": "+99-100-555-3847", "email": "maria.santos@novamail.co",
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
        "phone": "+99-100-555-8934", "email": "lucia.ferrer@portocorreo.co",
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
        "phone": "+99-200-555-4201", "email": "ramon.gutierrez@cordomail.co",
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
        "phone": "+99-200-555-8744", "email": "ana.lucero@novamail.co",
        "contact_pref": "Email",
    },
}

# Persons list: all cast + generated background persons
# This will be populated by civil_registry generator and reused by other domains
PERSONS = []
