"""
Generate Maritime Port Authority XML instances for CordovaOS demo.

Governance-composed model: MV Estrella del Sur port call + background port
calls, each wrapped in the Maritime Governed Record (data + provenance) with
native subject/provider parties, System Audit and attestation slots.

Output: import_data/maritime_port_authority/
"""
import os
import random

from shared import (
    OMIT,
    xml_header, xml_preamble, xml_footer, write_xml,
    xdstring, xdtoken, xdtemporal, xdquantity, xdcount,
    cluster_open, cluster_close, native_partytype,
    make_provenance_values, audit, attestation, generate_brn,
    cuid_generator, _esc,
)

CT_ID = "md2451x882z5j89g66zb50rw"
DM_LABEL = "Maritime Port Authority"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "sdc4", "import_data", "maritime_port_authority")

# ─── Governance envelope (re-keyed adapter wrappers for v2) ──────────────────
# Item wrapper (Governed Record) + data cluster + provenance cluster.
GOVERNED_RECORD = "ms-haoricee7rjlcybdp70akw9l"   # Maritime Governed Record
CL_ROOT         = "ms-i8cjmvihdces5rqvb2snqwmo"   # Port Call Record (data cluster)
CL_PROV         = "ms-hdhjfg00tngir2txgqyka9cv"   # Provenance Components

# ─── Port Call Record scalar adapters (component, wrapper) ───────────────────
W_FLAG        = ("ms-k7a0poa5c7co38oc65i6jppo", "ms-xfhmav9hjc93poa0bpt6wc1n")
W_PORT_CALL   = ("ms-pbfvurdvio38rt6puifhippe", "ms-hehcff4uuddueau8naw7bube")
W_BERTH       = ("ms-lnjzw0racjo2oxol5w82tp1y", "ms-qv0bs1wolkqffuostwy2mghu")
W_NEXT_PORT   = ("ms-gxt0t3cs4u6v5ob55qkc6ha0", "ms-i63w2j9yeydf98n6dnzafbsf")
W_DEPART_PORT = ("ms-s0qun9zalf98t3ffsefh34rj", "ms-r3c8k3go9pvnr1eo67yssbwk")
W_CALL_SIGN   = ("ms-qlqdwbglcq4v3rg8i8iy7dk0", "ms-m9cb0u7fwwz6sh01adzhovfw")
W_IMO         = ("ms-ycy71t767wlyqma97o82r2m9", "ms-pvu9aqq9gyn92d4mapjjmle4")
W_MMSI        = ("ms-cl1hiqht7tm42a8lh8c4c1hz", "ms-airj580f516kjuxy5gqkwc70")
W_VESSEL_NAME = ("ms-s5zeapfup3xdj6wbqjjkf1nd", "ms-aqmdatfklnbaoke3qypv3igd")
W_VOYAGE_NUM  = ("ms-bmoixtn8r8pu62gbgd1tl8qn", "ms-b6pijumkphk8jxiss0r7t9ob")
W_CARGO_TYPE  = ("ms-bfaa3m23ye8q0qphv0x24if6", "ms-oek61qmf4kvh72ixsaekrzjv")
W_PURPOSE     = ("ms-lyh7y1in5j9ka5cxk2zw2qdj", "ms-xgokjpnwgzaaj6l5r0h3gbe2")
W_CREW_CT     = ("ms-p5qzw565y1dm5f3s6lg2q3ft", "ms-vuhpqduzqkhjh8bslws0xhjl")
W_PAX_CT      = ("ms-x720xrlooqij75bk26pvzrtl", "ms-c2wzf2bgfqgejklruo5fc6ji")
W_DRAFT       = ("ms-xccdfbmuqcy5yzv2n6ef0hrs", "ms-ffk9lh4ly21z4sieskk9oass")
W_GROSS_TON   = ("ms-wtph0sqt244h38lyzf9ot1op", "ms-cwmpa6htkdrrao5wme0qq9nr")
W_LOA         = ("ms-jnxxwzl046rkmkbtm33naueu", "ms-kkru6m6nz06xpamtzw5db6pf")
W_NET_TON     = ("ms-lh0ufebnovngzzgfggud6ae6", "ms-f1k38piyyeyhyh1pczkstikh")
W_ARRIVAL     = ("ms-upvi6l9pyb4f0p4vfunietsw", "ms-v87ycpepejv213lzzi7beane")
W_DEPARTURE   = ("ms-sqpcl9uk7sze8bdqxxqwuqrn", "ms-ipdvc41rklzt2qsuo60t4opz")

# ─── Cargo Manifest sub-cluster ─────────────────────────────────────────────
CL_CARGO        = "ms-ibb8e7c8equpeqiv5wxrxxll"
W_CUSTOMS_FILED = ("ms-wxjyv4dmwb0rws14mn5xy3ju", "ms-h6smqocqffasynsgim20ttuk")
W_HAZARDOUS     = ("ms-n7x39orkbwjejdf8r93trlaa", "ms-dru56l57olme5hgyupf9a9mb")
W_BRN           = ("ms-l8f0m7op4xhrxqy1jrnvbuly", "ms-gplgx9ouh0ronqrhvocd2h74")
W_CARGO_DESC    = ("ms-z7zqo56erimvk8dqvl07ihfr", "ms-mclcesn6irh4t7gnmxey1e4e")
W_CARGO_DEST    = ("ms-an9kafb2l1enwh20ngvo1n7y", "ms-kg05e3eichmed24ltqm67zxg")
W_CARGO_ORIG    = ("ms-rt510ljj3vz05fxwcm85i990", "ms-t66adthydob3vtk63zthpzo7")
W_CUSTOMS_REF   = ("ms-dp1dkn09vydj2ss6ho37kyhv", "ms-j4r9laad4rirxgibwboiqpvg")
W_HAZMAT_CLS    = ("ms-gqbvto3l0o5e6uorrgjwdig2", "ms-i1vc2d36wkr3194fec5to2fu")
W_CONTAINER     = ("ms-y5se2qd3r6xx6pz8t7d8cqvf", "ms-qi8ulpm9ktp5eecnv2lp5qrs")
W_CARGO_WT      = ("ms-lqqypwp22ohzb0ud3wq81r9s", "ms-y5x3v5nx01jfbf2x2kj68c9c")

# ─── Port Fees sub-cluster ──────────────────────────────────────────────────
CL_FEES       = "ms-emtr91lypy400ttgzz2ti4et"
W_FEE_TYPE    = ("ms-wvfcfa6u4ers75egrbi25x9l", "ms-ig77r37eczizbojl8pnnhbok")
W_FEE_PAY_ST  = ("ms-vt5nh89ol3g5gj0oz35tl6y0", "ms-tvtb07vks4ai369l6wyvormq")
W_FEE_AMT     = ("ms-e92ud8io69rm826g9b1jrrgh", "ms-mqf57anope4llmpfw8hrz28g")
W_FEE_DATE    = ("ms-zub98dao6k8cbbhsddzoq62w", "ms-ybppe9ht05ivydc8tjmbunmq")

# ─── Provenance Components leaves (component, wrapper) ───────────────────────
P_ACT_DESC = ("ms-m9xg6e182m1oq77ssrf9iujv", "ms-fvj4iipjuaxdr55zonkp16xm")
P_ACT_TYPE = ("ms-ccj1yq2wtwknobszkgzzdbtr", "ms-gdaeo7yt3wq0z38hrypm680l")
P_SYS_ID   = ("ms-bd3s8t23d6m3zizmpwavc32y", "ms-epq45dxx0gqpuj1m42vnzkgl")
P_LOC_ID   = ("ms-zr59goe24qkocprl3feul3mt", "ms-st236fgnq3y8zqj66nlf05di")
P_LOC_NAME = ("ms-fnodzqkbyskwe7nh58rs336k", "ms-slzqqg6gg0lqcd563mdsfsin")
P_TS_END   = ("ms-edvvjznmaoibzmfna0uuoo37", "ms-zq6n3ulnnf26g83et6g0j5wk")
P_TS_START = ("ms-o72s5793973fzho35rnaughs", "ms-j90qiz1y4y4wk4mvt9tuv2n9")

# System Audit ms- component (substitutionGroup="sdc4:Audit"); labels match
# the shared audit() civil-registry defaults exactly (confirmed against XSD).
AUDIT_COMPONENT = "ms-fotc5adg15ek2b9ermx2mcih"

# ─── Domain enum mappings (values must match XSD enumerations) ───────────────
# Cargo Type (xdtoken): containers, bulk_dry, bulk_liquid, vehicles,
#   general_cargo, refrigerated, livestock, none
CARGO_TYPE_MAP = {
    "Container": "containers", "Containers": "containers",
    "Bulk Carrier": "bulk_dry", "Bulk": "bulk_dry",
    "Tanker": "bulk_liquid",
    "General Cargo": "general_cargo",
    "Ro-Ro": "vehicles", "RoRo": "vehicles",
    "Reefer": "refrigerated", "Refrigerated": "refrigerated",
    "Livestock": "livestock",
}
# Purpose of Call (xdtoken): load_cargo, discharge_cargo, load_discharge,
#   refuel, provisions, repairs, crew_change, emergency, other
PURPOSE_MAP = {
    "Cargo Discharge": "discharge_cargo",
    "Cargo Loading": "load_cargo",
    "Fuel Discharge": "refuel", "Fuel Bunkering": "refuel",
    "Crew Change": "crew_change",
}
# Fee Type (xdtoken): exact enumeration values
FEE_TYPES = ["Berth Fee", "Pilotage", "Tug Service", "Cargo Handling",
             "Customs Processing", "Waste Disposal", "Fresh Water", "Provisions"]
FEE_TYPE_MAP = {"Docking": "Berth Fee"}
# Payment Status (xdtoken): Paid, Invoiced, Overdue
PAYMENT_STATUSES = ["Paid", "Invoiced", "Overdue"]
# Hazmat Class (xdtoken): the model carries a single combined enumeration value.
HAZMAT_CLASS_VALUE = ("1-explosives,2-gases,3-flammable-liquids,4-flammable-solids,"
                      "5-oxidizers,6-toxic,7-radioactive,8-corrosives,9-misc")


def _cargo_type(v):
    return CARGO_TYPE_MAP.get(v, "general_cargo")


def _purpose(v):
    return PURPOSE_MAP.get(v, "other")


def _fee_type(v):
    return FEE_TYPE_MAP.get(v, v if v in FEE_TYPES else "Berth Fee")


def xdboolean_yn(component_id, wrapper_id, label, value, indent=2):
    """XdBoolean leaf: full XdAny optional sequence + the required true/false
    choice (enumerated Yes/No, per the model)."""
    pad = "  " * indent
    tag = "true-value" if value else "false-value"
    val = "Yes" if value else "No"
    return f'''{pad}<sdc4:{wrapper_id}>
{pad}  <sdc4:{component_id}>
{pad}    <label>{_esc(label)}</label>
{pad}    <act></act>
{pad}    <vtb>2020-01-01T00:00:00</vtb>
{pad}    <vte>9999-12-31T23:59:59</vte>
{pad}    <tr>2020-01-01T00:00:00</tr>
{pad}    <modified>2020-01-01T00:00:00</modified>
{pad}    <latitude>0.0</latitude>
{pad}    <longitude>0.0</longitude>
{pad}    <{tag}>{val}</{tag}>
{pad}  </sdc4:{component_id}>
{pad}</sdc4:{wrapper_id}>
'''


def build_instance(pc):
    """Build a governance-composed Maritime Port Authority XML instance."""
    # Keep system_name short: it seeds system_identifier (urn:...), which the
    # model caps at 50 chars.
    prov = make_provenance_values(
        "Cordova Maritime Authority", "PortCallRegistration",
        city="Porto Sereno")

    customs_filed = pc.get("customs_filed", True)
    hazardous = pc.get("hazardous", False)
    brn = pc.get("brn") or generate_brn()

    xml = xml_header(CT_ID)
    xml += xml_preamble(DM_LABEL, current_state="Cleared")

    # Item: Maritime Governed Record wrapper
    xml += cluster_open(GOVERNED_RECORD, "Maritime Governed Record", indent=1)

    # Data cluster (Port Call Record). Per the XSD sequence the two sub-clusters
    # (Cargo Manifest, Port Fees) precede the scalar adapters, so emit them first.
    xml += cluster_open(CL_ROOT, "Port Call Record", indent=2)

    # Cargo Manifest sub-cluster
    xml += cluster_open(CL_CARGO, "Cargo Manifest", indent=3)
    xml += xdboolean_yn(*W_CUSTOMS_FILED, "Customs Declaration Filed", customs_filed, indent=4)
    xml += xdboolean_yn(*W_HAZARDOUS, "Hazardous Cargo", hazardous, indent=4)
    xml += xdstring(*W_BRN, "Business Registry Number", brn, indent=4)
    xml += xdstring(*W_CARGO_DESC, "Cargo Description", pc["cargo_desc"], indent=4)
    xml += xdstring(*W_CARGO_DEST, "Cargo Destination", pc["cargo_dest"], indent=4)
    xml += xdstring(*W_CARGO_ORIG, "Cargo Origin", pc["cargo_orig"], indent=4)
    xml += xdstring(*W_CUSTOMS_REF, "Customs Reference Number", pc.get("customs_ref", OMIT), indent=4)
    if hazardous:
        xml += xdtoken(*W_HAZMAT_CLS, "Hazmat Class", HAZMAT_CLASS_VALUE, indent=4)
    xml += xdcount(*W_CONTAINER, "Container Count", str(pc.get("containers", 0)),
                   "Twenty-foot Equivalent Units (TEU)", indent=4)
    xml += xdquantity(*W_CARGO_WT, "Cargo Weight", str(pc.get("cargo_wt", 0)),
                      "Mass/Weight (SI - Metric)", indent=4)
    xml += cluster_close(CL_CARGO, indent=3)

    # Port Fees sub-cluster
    xml += cluster_open(CL_FEES, "Port Fees", indent=3)
    xml += xdtoken(*W_FEE_TYPE, "Fee Type", _fee_type(pc.get("fee_type", "Berth Fee")), indent=4)
    xml += xdtoken(*W_FEE_PAY_ST, "Payment Status", pc.get("payment_status", "Paid"), indent=4)
    xml += xdquantity(*W_FEE_AMT, "Port Fee Amount", str(pc.get("fee_amt", 5000)),
                      "Cordova Córdoba (COR)", indent=4)
    xml += xdtemporal(*W_FEE_DATE, "Fee Date", pc["arrival"][:10], "date", indent=4)
    xml += cluster_close(CL_FEES, indent=3)

    # Scalar adapters (XSD sequence order)
    xml += xdstring(*W_FLAG, "Flag State", pc["flag"], indent=3)
    xml += xdstring(*W_PORT_CALL, "Port Call ID", pc["port_call_id"], indent=3)
    xml += xdstring(*W_BERTH, "Berth Assignment", pc["berth"], indent=3)
    xml += xdstring(*W_NEXT_PORT, "Next Port of Call", pc["next_port"], indent=3)
    xml += xdstring(*W_DEPART_PORT, "Port of Departure", pc["depart_port"], indent=3)
    xml += xdstring(*W_CALL_SIGN, "Vessel Call Sign", pc["call_sign"], indent=3)
    xml += xdstring(*W_IMO, "Vessel IMO Number", pc["imo"], indent=3)
    xml += xdstring(*W_MMSI, "Vessel MMSI", pc["mmsi"], indent=3)
    xml += xdstring(*W_VESSEL_NAME, "Vessel Name", pc["vessel_name"], indent=3)
    xml += xdstring(*W_VOYAGE_NUM, "Voyage Number", pc["voyage"], indent=3)
    xml += xdtoken(*W_CARGO_TYPE, "Cargo Type", _cargo_type(pc["cargo_type"]), indent=3)
    xml += xdtoken(*W_PURPOSE, "Purpose of Call", _purpose(pc["purpose"]), indent=3)
    xml += xdcount(*W_CREW_CT, "Crew Count", str(pc["crew"]), "Persons", indent=3)
    xml += xdcount(*W_PAX_CT, "Passenger Count", str(pc["pax"]), "Persons", indent=3)
    xml += xdquantity(*W_DRAFT, "Vessel Draft", str(pc["draft"]), "Length/Distance (SI - Metric)", indent=3)
    xml += xdquantity(*W_GROSS_TON, "Vessel Gross Tonnage", str(pc["gross_ton"]), "Gross Tonnage", indent=3)
    xml += xdquantity(*W_LOA, "Vessel Length Overall", str(pc["loa"]), "Length/Distance (SI - Metric)", indent=3)
    xml += xdquantity(*W_NET_TON, "Vessel Net Tonnage", str(pc["net_ton"]), "Net Tonnage", indent=3)
    xml += xdtemporal(*W_ARRIVAL, "Arrival Date/Time", pc["arrival"], "datetime", indent=3)
    xml += xdtemporal(*W_DEPARTURE, "Departure Date/Time", pc["departure"], "datetime", indent=3)
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

    # Native governance slots, DM order: subject, provider(s), Audit, attestation.
    xml += native_partytype("subject", "Subject Vessel", pc["vessel_name"])
    xml += native_partytype("provider", "Vessel Owner/Operator",
                            pc.get("operator", f"{pc['vessel_name']} Shipping Co."))
    xml += native_partytype("provider", "Port Authority",
                            "Porto Sereno Port Authority")
    xml += audit(AUDIT_COMPONENT, prov["activity_timestamp_start"],
                 system_id_value=prov["system_identifier"])
    xml += attestation(pending=False,
                       reason="Port call cleared by the port authority",
                       committer="Porto Sereno Port Authority",
                       committed=prov["activity_timestamp_end"])

    xml += xml_footer(CT_ID)
    return xml


# The Contagion: MV Estrella del Sur
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
}

BG_VESSELS = [
    ("MV Pacifica Corriente", "Panama", "9823456", "352823456", "HPPAC", "Tanker", "Fuel Discharge", 22, "2026-01-05"),
    ("MV Costa Linda", "Republic of Cordova", "9812345", "370812345", "HCCL", "Container", "Cargo Discharge", 15, "2026-01-08"),
    ("MV Atlantico Sur", "Liberia", "9834567", "636834567", "D5AS", "Bulk Carrier", "Cargo Loading", 19, "2026-01-15"),
    ("MV Isla Bonita", "Republic of Cordova", "9845678", "370845678", "HCIB", "General Cargo", "Cargo Discharge", 12, "2025-12-28"),
    ("MV Porto Express", "Marshall Islands", "9856789", "538856789", "V7PE", "Container", "Cargo Discharge", 20, "2025-12-20"),
]

# Generate additional background vessels for weekly port calls across 2025-2026
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
_FLAGS = [
    "Panama", "Liberia", "Marshall Islands", "Republic of Cordova",
    "Bahamas", "Malta", "Singapore", "Hong Kong", "Greece", "Cyprus",
]
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


def generate():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    count = 0

    # MV Estrella del Sur
    xml = build_instance(ESTRELLA)
    write_xml(os.path.join(OUTPUT_DIR, f"mp-{cuid_generator()}.xml"), xml)
    count += 1

    # Named background port calls (5 original vessels)
    for name, flag, imo, mmsi, csign, ctype, purpose, crew, arr_date in BG_VESSELS:
        pc = {
            "flag": flag, "port_call_id": f"PC-2026-{random.randint(100,999):03d}",
            "berth": f"Berth {random.randint(1,12)}, Porto Sereno Commercial Terminal",
            "next_port": random.choice(_NEXT_PORTS),
            "depart_port": random.choice(_DEPARTURE_PORTS),
            "call_sign": csign, "imo": imo, "mmsi": mmsi,
            "vessel_name": name, "voyage": f"VOY-2026-{random.randint(1,99):02d}",
            "cargo_type": ctype, "purpose": purpose,
            "crew": crew, "pax": 0,
            "draft": f"{random.uniform(5, 10):.1f}",
            "gross_ton": str(random.randint(8000, 30000)),
            "loa": f"{random.uniform(100, 200):.1f}",
            "net_ton": str(random.randint(4000, 18000)),
            "arrival": f"{arr_date}T{random.randint(4,20):02d}:00:00",
            "departure": f"{arr_date[:8]}{int(arr_date[8:10])+2:02d}T{random.randint(6,22):02d}:00:00",
            "cargo_desc": f"{ctype} shipment",
            "cargo_dest": "Porto Sereno, Republic of Cordova",
            "cargo_orig": "International",
            "customs_filed": True,
            "hazardous": ctype == "Tanker",
            "containers": random.randint(10, 100),
            "cargo_wt": random.randint(500, 5000),
            "fee_type": random.choice(FEE_TYPES),
            "payment_status": random.choice(PAYMENT_STATUSES),
            "fee_amt": random.randint(5000, 25000),
        }
        xml = build_instance(pc)
        write_xml(os.path.join(OUTPUT_DIR, f"mp-{cuid_generator()}.xml"), xml)
        count += 1

    # Generated background port calls (44 more, total ~50 with Estrella)
    # Spread across 2025-2026 calendar (roughly weekly)
    from datetime import date, timedelta
    start_date = date(2025, 1, 6)
    mmsi_pfx = {"Panama": "352", "Liberia": "636", "Marshall Islands": "538",
                "Republic of Cordova": "370", "Bahamas": "311", "Malta": "249",
                "Singapore": "563", "Hong Kong": "477", "Greece": "240", "Cyprus": "212"}
    for i in range(44):
        # Roughly weekly arrivals
        arr = start_date + timedelta(weeks=i)
        arr_str = arr.strftime("%Y-%m-%d")
        dep = arr + timedelta(days=random.randint(1, 4))
        dep_str = dep.strftime("%Y-%m-%d")
        vname = f"{random.choice(_VESSEL_PREFIXES)} {_VESSEL_NAMES[i % len(_VESSEL_NAMES)]}"
        flag = random.choice(_FLAGS)
        imo_num = str(9800000 + random.randint(1000, 99999))
        mmsi_num = mmsi_pfx.get(flag, "370") + f"{random.randint(0, 999999):06d}"
        csign = f"{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=4))}"
        ctype = random.choice(_CARGO_TYPES)

        pc = {
            "flag": flag,
            "port_call_id": f"PC-{arr.year}-{100 + i + 10:04d}",
            "berth": f"Berth {random.randint(1,12)}, Porto Sereno Commercial Terminal",
            "next_port": random.choice(_NEXT_PORTS),
            "depart_port": random.choice(_DEPARTURE_PORTS),
            "call_sign": csign, "imo": imo_num, "mmsi": mmsi_num,
            "vessel_name": vname,
            "voyage": f"VOY-{arr.year}-{random.randint(1,999):03d}",
            "cargo_type": ctype,
            "purpose": random.choice(_PURPOSES),
            "crew": random.randint(10, 28), "pax": 0,
            "draft": f"{random.uniform(4.5, 11):.1f}",
            "gross_ton": str(random.randint(5000, 45000)),
            "loa": f"{random.uniform(90, 250):.1f}",
            "net_ton": str(random.randint(3000, 25000)),
            "arrival": f"{arr_str}T{random.randint(4,20):02d}:{random.choice(['00','30'])}:00",
            "departure": f"{dep_str}T{random.randint(6,22):02d}:{random.choice(['00','30'])}:00",
            "cargo_desc": f"{ctype} shipment - miscellaneous goods",
            "cargo_dest": "Porto Sereno, Republic of Cordova",
            "cargo_orig": random.choice(_DEPARTURE_PORTS),
            "customs_filed": random.random() > 0.1,
            "hazardous": random.random() < 0.12,
            "containers": random.randint(0, 150) if ctype == "Container" else random.randint(0, 10),
            "cargo_wt": random.randint(200, 8000),
            "fee_type": random.choice(FEE_TYPES),
            "payment_status": random.choice(PAYMENT_STATUSES),
            "fee_amt": random.randint(3000, 30000),
        }
        xml = build_instance(pc)
        write_xml(os.path.join(OUTPUT_DIR, f"mp-{cuid_generator()}.xml"), xml)
        count += 1

    print(f"Maritime Port Authority: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    generate()
