"""
Maritime Port Authority 4.4.0: one record per port call.

The model composes the NIEM library's port visit, vessel, voyage, cargo and
person-on-vessel, with Cordova's port call identifier, port fees in the kept COR
units, and the operator's Business Registry Number as the join to the Business
Registry. The MV Estrella del Sur (the Contagion) carries Carlos Mendoza as a
person on the vessel, named by his CID, so the trace from the vessel to the
patient is a join on the CID component. 1 + 5 named + 44 weekly background
port calls = 50 at both scales.
"""
import random
from datetime import date, timedelta

from shared import (
    CAST, COR, Quantity, generate_brn, full_name,
    record, write_record, import_dir,
)

TITLE = "Maritime Port Authority"
SYSTEM = "Cordova Maritime Authority"
OUTPUT_DIR = import_dir("maritime_port_authority")
PORT = "Porto Sereno"
PROVINCE = "Aldara"

# The reservation workflow bound to the model: a cleared port call is a confirmed reservation of the berth.
# "Cleared" (4.3.1) -> ReservationConfirmed; an unpaid fee still being invoiced does not change the berth's state.
STATE_CLEARED = "ReservationConfirmed"

# ISO 3166 alpha-2 flags. Cordova is fictional and has no code: a Cordova-flagged vessel carries the flag as text only.
FLAG_CODES = {"Panama": "PA", "Liberia": "LR", "Marshall Islands": "MH", "Bahamas": "BS", "Malta": "MT",
              "Singapore": "SG", "Hong Kong": "HK", "Greece": "GR", "Cyprus": "CY"}
FEE_TYPES = ["Berth Fee", "Pilotage", "Tug Service", "Cargo Handling", "Customs Processing", "Waste Disposal", "Fresh Water", "Provisions"]
PAYMENT_STATUSES = ["Paid", "Invoiced", "Overdue"]
# UN numbers for the hazardous cargo a tanker or a flagged background call declares: (UN code, chemical, class).
HAZMAT = [("UN1203", "Gasoline", "3"), ("UN1202", "Diesel fuel", "3"), ("UN1075", "Petroleum gases, liquefied", "2.1"), ("UN1830", "Sulfuric acid", "8")]


def build_instance(pc):
    """One Maritime Port Authority record for one port call."""
    brn = pc.get("brn") or generate_brn()
    flag_code = FLAG_CODES.get(pc["flag"])
    values = {
        "Port Call Record/Port Call ID": pc["port_call_id"],
        "Port Call Record/Crew Count": Quantity(str(pc["crew"]), "persons"),
        "Port Call Record/Passenger Count": Quantity(str(pc["pax"]), "persons"),
        "Vessel/Vessel Name": pc["vessel_name"],
        "Vessel/Vessel IMO Number": pc["imo"],
        "Vessel/Vessel MMSI": pc["mmsi"],
        "Vessel/Vessel Call Sign": pc["call_sign"],
        "Vessel/Vessel National Flag": pc["flag"],
        "Vessel/Vessel National Flag ISO3166 Alpha2 (iso_3166)/Vessel National Flag ISO3166 Alpha2 Code (iso_3166)": flag_code,
        "Vessel/Vessel National Flag ISO3166 Alpha2 (iso_3166)/Code Display Text": pc["flag"] if flag_code else None,
        "Vessel/Vessel Cargo Category": pc["cargo_type"],
        "Vessel/Vessel Gross Tonnage Value": Quantity(str(pc["gross_ton"]), "ratio"),   # gross tonnage is a dimensionless index; the Default unitless symbol
        "Vessel/Vessel Net Tonnage Volume": Quantity(f"{int(pc['net_ton']) * 2.8317:.1f}", "m3"),   # NIEM carries net tonnage as a volume: 1 register ton = 100 ft³ = 2.8317 m³
        "Vessel/Vessel Overall Length": Quantity(str(pc["loa"]), "m"),
        "Vessel/Vessel Draft": Quantity(str(pc["draft"]), "m"),
        "Vessel/Vessel Operator Reference": f"urn:cordova:brn:{brn}",
        "Vessel/Vessel Cargo On Board Indicator": True,
        "Port Visit/Port/Port Name": f"Port of {PORT}",
        "Port Visit/Port/City Name": PORT,
        "Port Visit/Port/Region Name": PROVINCE,
        "Port Visit/Visit Anchorage": pc["berth"],
        "Port Visit/Visit Receiving Facility Name": f"{PORT} Commercial Terminal",
        "Port Visit/Visit Actual Arrival Date Time": pc["arrival"],
        "Port Visit/Visit Actual Departure Date Time": pc["departure"],
        "Voyage/Voyage Identification": pc["voyage"],
        "Voyage/Voyage Category": pc["purpose"],
        "Voyage/Voyage Summary": f"From {pc['depart_port']} to {PORT}, onward to {pc['next_port']}",
        "Voyage/Voyage Destination Location Reference": "urn:cordova:port:" + pc["next_port"].split(",")[0].lower().replace(" ", "-"),
        "Voyage/Voyage End Date Time": pc["arrival"],
        "Cargo Manifest/Business Registry Number": brn,
        "Cargo Manifest/Container Count": Quantity(str(pc.get("containers", 0)), "TEU"),
        "Cargo Manifest/Cargo/Item Description": pc["cargo_desc"],
        "Cargo Manifest/Cargo/Cargo Category": pc["cargo_type"],
        "Cargo Manifest/Cargo/Cargo Gross Weight": Quantity(str(pc.get("cargo_wt", 0)), "t"),
        "Cargo Manifest/Cargo/Cargo Identification": pc.get("customs_ref") or None,
        "Cargo Manifest/Cargo/Cargo Origin Location Reference": "urn:cordova:port:" + pc["cargo_orig"].split(",")[0].lower().replace(" ", "-"),
        "Cargo Manifest/Cargo/Cargo Destination Location Reference": f"urn:cordova:port:{PORT.lower().replace(' ', '-')}",
        "Cargo Manifest/Cargo/Cargo Hazardous Material Indicator": bool(pc.get("hazardous")),
        "Port Fees/Fee Type": pc.get("fee_type", "Berth Fee"),
        "Port Fees/Payment Status": pc.get("payment_status", "Paid"),
        "Port Fees/Port Fee Amount": Quantity(str(pc.get("fee_amt", 5000)), COR),
        "Port Fees/Fee Date": pc["arrival"][:10],
    }
    if pc.get("hazardous"):
        un, chemical, hz_class = pc.get("hazmat") or HAZMAT[0]
        values.update({
            "Cargo Manifest/Cargo/Hazmat Declaration/Hazmat Declaration UN Hazmat (hazmat)/Hazmat Declaration UN Hazmat Code (hazmat)": un,
            "Cargo Manifest/Cargo/Hazmat Declaration/Hazmat Declaration UN Hazmat (hazmat)/Code Display Text": chemical,
            "Cargo Manifest/Cargo/Hazmat Declaration/Hazmat Declaration Chemical Common Name": chemical,
            "Cargo Manifest/Cargo/Hazmat Declaration/Hazmat Declaration Hazmat Class": hz_class,
        })
    for person in pc.get("persons", []):   # crew or passengers named on the manifest, by CID
        values.update({
            "Person on Vessel/Person (Demographics)/Full Name (Person)/Given Name (Person)": person["given"],
            "Person on Vessel/Person (Demographics)/Full Name (Person)/Surname (Person)": person["surname"],
            "Person on Vessel/Person (Demographics)/Administrative Gender": person["sex"].lower(),
            "Person on Vessel/Person (Demographics)/Date of Birth": person["dob"],
            "Person on Vessel/Crew Role Code": person["role"],
            "Person on Vessel/Crew Role": person["role"],
            "Person on Vessel/Person Embarkation Date": person["embarked"],
            "Person on Vessel/Person Debarkation Date": person["debarked"],
            "Person on Vessel/Person Embarkation Location Reference": "urn:cordova:port:" + person["embarked_at"].lower().replace(" ", "-"),
            "Person on Vessel/Person Debarkation Location Reference": f"urn:cordova:port:{PORT.lower().replace(' ', '-')}",
            "Person on Vessel/Person Cabin Number": person.get("cabin"),
        })
    operator = pc.get("operator", f"{pc['vessel_name']} Shipping Co.")
    return record(TITLE, values, state=STATE_CLEARED, system=SYSTEM, activity_type="PortCallRegistration", when=pc["arrival"],
                  city=PORT, province=PROVINCE, cid=(pc.get("persons") or [{}])[0].get("cid"),
                  subject=("Vessel Owner/Operator", operator), provider=("Port Authority", f"{PORT} Port Authority"),
                  attestation_reason="Port call cleared by the port authority", committer=f"{PORT} Port Authority")


# The Contagion: MV Estrella del Sur, with Carlos Mendoza (CID COR-AL01-271845) on the crew manifest.
ESTRELLA = {
    "flag": "Republic of Cordova", "port_call_id": "PC-2026-0142",
    "berth": "Berth 7, Porto Sereno Commercial Terminal",
    "next_port": "Cartagena, Colombia", "depart_port": "Buenaventura, Colombia",
    "call_sign": "HCES", "imo": "9847321", "mmsi": "370847321",
    "vessel_name": "MV Estrella del Sur", "voyage": "VOY-2026-ES-008",
    "cargo_type": "General Cargo", "purpose": "Cargo Discharge",
    "crew": 18, "pax": 0,
    "draft": "7.2", "gross_ton": "12847", "loa": "142.5", "net_ton": "7693",
    "arrival": "2026-01-11T06:30:00", "departure": "2026-01-13T18:00:00",
    "brn": "BIZ-001102", "customs_filed": True, "hazardous": False,
    "cargo_desc": "Mixed general cargo - agricultural equipment, building materials",
    "cargo_dest": "Porto Sereno, Republic of Cordova",
    "cargo_orig": "Buenaventura, Colombia",
    "customs_ref": "CUS-2026-0142-001",
    "containers": 45, "cargo_wt": 2340,
    "fee_type": "Berth Fee", "fee_amt": 12500,
    "operator": "Estrella Maritime Lines S.A.",
    "persons": [{**CAST["carlos"], "role": "Able Seaman", "embarked": "2026-01-04", "debarked": "2026-01-13", "embarked_at": "Buenaventura", "cabin": "C-12"}],
}

BG_VESSELS = [
    ("MV Pacifica Corriente", "Panama", "9823456", "352823456", "HPPAC", "Tanker", "Fuel Discharge", 22, "2026-01-05"),
    ("MV Costa Linda", "Republic of Cordova", "9812345", "370812345", "HCCL", "Container", "Cargo Discharge", 15, "2026-01-08"),
    ("MV Atlantico Sur", "Liberia", "9834567", "636834567", "D5AS", "Bulk Carrier", "Cargo Loading", 19, "2026-01-15"),
    ("MV Isla Bonita", "Republic of Cordova", "9845678", "370845678", "HCIB", "General Cargo", "Cargo Discharge", 12, "2025-12-28"),
    ("MV Porto Express", "Marshall Islands", "9856789", "538856789", "V7PE", "Container", "Cargo Discharge", 20, "2025-12-20"),
]

_VESSEL_PREFIXES = ["MV", "MT", "MV", "MV", "SS"]
_VESSEL_NAMES = [
    "Bahia Dorada", "Caribe Sol", "Luna del Sur", "Onda Tropical",
    "Viento Norte", "Mar Sereno", "Delfin Azul", "Coral Blanco",
    "Sierra Marina", "Horizonte", "Estrella Polar", "Rio Grande",
    "Condor Andino", "Pelicano", "Gaviota", "Barracuda",
    "Mariposa del Mar", "Orion Pacific", "Neptune Star", "Ocean Pearl",
    "Golden Tide", "Silver Wave", "Blue Meridian", "Red Coral",
    "Tropic Wind", "Iron Hull", "Crystal Bay", "Thunder Sea",
    "Morning Star", "Evening Light", "Southern Cross", "Northern Dawn",
    "Emerald Coast", "Sapphire Seas", "Diamond Reef", "Amber Sun",
    "Jade Current", "Ivory Mist", "Bronze Anchor", "Copper Ridge",
    "Falcon Crest", "Eagle Point", "Hawk Bay", "Osprey",
]
_FLAGS = ["Panama", "Liberia", "Marshall Islands", "Republic of Cordova", "Bahamas", "Malta", "Singapore", "Hong Kong", "Greece", "Cyprus"]
_CARGO_TYPES = ["Container", "Bulk Carrier", "Tanker", "General Cargo", "Ro-Ro", "Reefer"]
_PURPOSES = ["Cargo Discharge", "Cargo Loading", "Fuel Bunkering", "Crew Change", "Cargo Discharge"]
_DEPARTURE_PORTS = [
    "Houston, USA", "Santos, Brazil", "Buenaventura, Colombia", "Balboa, Panama",
    "Callao, Peru", "Guayaquil, Ecuador", "Kingston, Jamaica", "Colon, Panama",
    "Cartagena, Colombia", "Veracruz, Mexico", "Havana, Cuba", "Limon, Costa Rica",
]
_NEXT_PORTS = [
    "Cartagena, Colombia", "Panama City, Panama", "Guayaquil, Ecuador",
    "Callao, Peru", "Kingston, Jamaica", "Santos, Brazil", "Havana, Cuba",
    "Miami, USA", "Houston, USA", "Colon, Panama",
]
_MMSI_PREFIX = {"Panama": "352", "Liberia": "636", "Marshall Islands": "538", "Republic of Cordova": "370", "Bahamas": "311",
                "Malta": "249", "Singapore": "563", "Hong Kong": "477", "Greece": "240", "Cyprus": "212"}


def generate():
    count = 0

    write_record(OUTPUT_DIR, "mp", build_instance(ESTRELLA))
    count += 1

    # Named background port calls (5 vessels)
    for name, flag, imo, mmsi, csign, ctype, purpose, crew, arr_date in BG_VESSELS:
        hazardous = ctype == "Tanker"
        pc = {
            "flag": flag, "port_call_id": f"PC-2026-{random.randint(100, 999):03d}",
            "berth": f"Berth {random.randint(1, 12)}, Porto Sereno Commercial Terminal",
            "next_port": random.choice(_NEXT_PORTS), "depart_port": random.choice(_DEPARTURE_PORTS),
            "call_sign": csign, "imo": imo, "mmsi": mmsi,
            "vessel_name": name, "voyage": f"VOY-2026-{random.randint(1, 99):02d}",
            "cargo_type": ctype, "purpose": purpose,
            "crew": crew, "pax": 0,
            "draft": f"{random.uniform(5, 10):.1f}", "gross_ton": str(random.randint(8000, 30000)),
            "loa": f"{random.uniform(100, 200):.1f}", "net_ton": str(random.randint(4000, 18000)),
            "arrival": f"{arr_date}T{random.randint(4, 20):02d}:00:00",
            "departure": f"{arr_date[:8]}{int(arr_date[8:10]) + 2:02d}T{random.randint(6, 22):02d}:00:00",
            "cargo_desc": f"{ctype} shipment", "cargo_dest": "Porto Sereno, Republic of Cordova", "cargo_orig": "International",
            "customs_filed": True, "hazardous": hazardous, "hazmat": random.choice(HAZMAT[:2]) if hazardous else None,
            "containers": random.randint(10, 100), "cargo_wt": random.randint(500, 5000),
            "fee_type": random.choice(FEE_TYPES), "payment_status": random.choice(PAYMENT_STATUSES), "fee_amt": random.randint(5000, 25000),
        }
        write_record(OUTPUT_DIR, "mp", build_instance(pc))
        count += 1

    # Generated background port calls (44, roughly weekly across 2025-2026)
    start_date = date(2025, 1, 6)
    for i in range(44):
        arr = start_date + timedelta(weeks=i)
        dep = arr + timedelta(days=random.randint(1, 4))
        vname = f"{random.choice(_VESSEL_PREFIXES)} {_VESSEL_NAMES[i % len(_VESSEL_NAMES)]}"
        flag = random.choice(_FLAGS)
        imo_num = str(9800000 + random.randint(1000, 99999))
        mmsi_num = _MMSI_PREFIX.get(flag, "370") + f"{random.randint(0, 999999):06d}"
        csign = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=4))
        ctype = random.choice(_CARGO_TYPES)
        hazardous = random.random() < 0.12
        pc = {
            "flag": flag, "port_call_id": f"PC-{arr.year}-{100 + i + 10:04d}",
            "berth": f"Berth {random.randint(1, 12)}, Porto Sereno Commercial Terminal",
            "next_port": random.choice(_NEXT_PORTS), "depart_port": random.choice(_DEPARTURE_PORTS),
            "call_sign": csign, "imo": imo_num, "mmsi": mmsi_num,
            "vessel_name": vname, "voyage": f"VOY-{arr.year}-{random.randint(1, 999):03d}",
            "cargo_type": ctype, "purpose": random.choice(_PURPOSES),
            "crew": random.randint(10, 28), "pax": 0,
            "draft": f"{random.uniform(4.5, 11):.1f}", "gross_ton": str(random.randint(5000, 45000)),
            "loa": f"{random.uniform(90, 250):.1f}", "net_ton": str(random.randint(3000, 25000)),
            "arrival": f"{arr.isoformat()}T{random.randint(4, 20):02d}:{random.choice(['00', '30'])}:00",
            "departure": f"{dep.isoformat()}T{random.randint(6, 22):02d}:{random.choice(['00', '30'])}:00",
            "cargo_desc": f"{ctype} shipment - miscellaneous goods", "cargo_dest": "Porto Sereno, Republic of Cordova",
            "cargo_orig": random.choice(_DEPARTURE_PORTS),
            "customs_filed": random.random() > 0.1, "hazardous": hazardous, "hazmat": random.choice(HAZMAT) if hazardous else None,
            "containers": random.randint(0, 150) if ctype == "Container" else random.randint(0, 10),
            "cargo_wt": random.randint(200, 8000),
            "fee_type": random.choice(FEE_TYPES), "payment_status": random.choice(PAYMENT_STATUSES), "fee_amt": random.randint(3000, 30000),
        }
        write_record(OUTPUT_DIR, "mp", build_instance(pc))
        count += 1

    print(f"Maritime Port Authority: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    random.seed("cordovaos:Maritime")
    generate()
