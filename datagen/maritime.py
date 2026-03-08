"""
Generate Maritime Port Authority XML instances for CordovaOS demo.

MV Estrella del Sur port call + background port calls.
Output: import_data/maritime_port_authority/
"""
import os
import random

from shared import (
    xml_header, xml_preamble, xml_footer, write_xml,
    xdstring, xdtoken, xdtemporal, xdquantity, xdcount, xdboolean_stub,
    cluster_open, cluster_close, party_stub,
    cuid_generator,
)

CT_ID = "md2451x882z5j89g66zb50rw"
DM_LABEL = "Maritime Port Authority"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "app", "sdc4", "import_data", "maritime_port_authority")

CL_ROOT       = "ms-i8cjmvihdces5rqvb2snqwmo"
W_FLAG        = ("ms-k7a0poa5c7co38oc65i6jppo", "ms-gtcewfnuiwxk88o2f6kyq2qq")
W_PORT_CALL   = ("ms-pbfvurdvio38rt6puifhippe", "ms-datw526rgr3c7qnctl29ii3t")
W_BERTH       = ("ms-lnjzw0racjo2oxol5w82tp1y", "ms-q3edmk68p18r5hmooj9fnq7v")
W_NEXT_PORT   = ("ms-gxt0t3cs4u6v5ob55qkc6ha0", "ms-qbb98735oa0d7awuuvx546e4")
W_DEPART_PORT = ("ms-s0qun9zalf98t3ffsefh34rj", "ms-gscwer0gabezbmujxqunvdnt")
W_CALL_SIGN   = ("ms-qlqdwbglcq4v3rg8i8iy7dk0", "ms-hs7iau3fhhsavr8g0xse1lim")
W_IMO         = ("ms-ycy71t767wlyqma97o82r2m9", "ms-rhufsyscux1xajt2jghz07aj")
W_MMSI        = ("ms-cl1hiqht7tm42a8lh8c4c1hz", "ms-m8xnwdo3vyqsylawsjo52rkr")
W_VESSEL_NAME = ("ms-s5zeapfup3xdj6wbqjjkf1nd", "ms-totmylcmt56sn688wgya36jl")
W_VOYAGE_NUM  = ("ms-bmoixtn8r8pu62gbgd1tl8qn", "ms-anx5yec6ztqaqof19hi222ji")
W_CARGO_TYPE  = ("ms-bfaa3m23ye8q0qphv0x24if6", "ms-yivkkq6trtjamqyxn685g8dd")
W_PURPOSE     = ("ms-lyh7y1in5j9ka5cxk2zw2qdj", "ms-pjl8qxlaqzixw9uuim6388wr")
W_CREW_CT     = ("ms-p5qzw565y1dm5f3s6lg2q3ft", "ms-cqcbdkc6skdvo641ssae9bmk")
W_PAX_CT      = ("ms-x720xrlooqij75bk26pvzrtl", "ms-p7rywz55higp9awhqd9451v0")
W_DRAFT       = ("ms-xccdfbmuqcy5yzv2n6ef0hrs", "ms-t4db94419qggktbt84irn5s9")
W_GROSS_TON   = ("ms-wtph0sqt244h38lyzf9ot1op", "ms-w1xcrfj28hldeu3s5cw3fkr1")
W_LOA         = ("ms-jnxxwzl046rkmkbtm33naueu", "ms-cv05cfjraxexftvbff52vqyq")
W_NET_TON     = ("ms-lh0ufebnovngzzgfggud6ae6", "ms-lfb485gxtowvj3iuh7mwmb4o")
W_ARRIVAL     = ("ms-upvi6l9pyb4f0p4vfunietsw", "ms-jxhqlk89vh1uyz4w6fsn4tgb")
W_DEPARTURE   = ("ms-sqpcl9uk7sze8bdqxxqwuqrn", "ms-f6f41zs72e5bddz7l1butw8w")

CL_CARGO      = "ms-ibb8e7c8equpeqiv5wxrxxll"
W_CUSTOMS_FILED = ("ms-wxjyv4dmwb0rws14mn5xy3ju", "ms-gobeymr1af857fpihaugr8ec")
W_HAZARDOUS   = ("ms-n7x39orkbwjejdf8r93trlaa", "ms-p756taj6vfy2ry7i01wcacni")
W_BRN         = ("ms-l8f0m7op4xhrxqy1jrnvbuly", "ms-u85l66fzbj3xfi0tcqw6lced")
W_CARGO_DESC  = ("ms-z7zqo56erimvk8dqvl07ihfr", "ms-zztr4vcn6y7jsouka5ib9wk8")
W_CARGO_DEST  = ("ms-an9kafb2l1enwh20ngvo1n7y", "ms-esn0jhpiw0nkb3xo6ypp27h7")
W_CARGO_ORIG  = ("ms-rt510ljj3vz05fxwcm85i990", "ms-jr4zmv9evt3noil7fxfb0rv2")
W_CUSTOMS_REF = ("ms-dp1dkn09vydj2ss6ho37kyhv", "ms-uin35nzyd95nrf8rby5ejeaz")
W_HAZMAT_CLS  = ("ms-gqbvto3l0o5e6uorrgjwdig2", "ms-wybr587b5dmwqrat5awx7ptj")
W_CONTAINER   = ("ms-y5se2qd3r6xx6pz8t7d8cqvf", "ms-tgo730zvr0uzoen62l55g7e2")
W_CARGO_WT    = ("ms-lqqypwp22ohzb0ud3wq81r9s", "ms-yd4axcokjgbanidq1a2z8lkm")

CL_FEES       = "ms-emtr91lypy400ttgzz2ti4et"
W_FEE_TYPE    = ("ms-wvfcfa6u4ers75egrbi25x9l", "ms-zco7ycjig3qczebhn5keg4bi")
W_FEE_PAY_ST  = ("ms-vt5nh89ol3g5gj0oz35tl6y0", "ms-o829bhh23n90ghd0moacjyp2")
W_FEE_AMT     = ("ms-e92ud8io69rm826g9b1jrrgh", "ms-y56t342e4l7bfqnh7ont6lcq")
W_FEE_DATE    = ("ms-zub98dao6k8cbbhsddzoq62w", "ms-ge5vvcmifjc1sx9fy9uq4w09")

PS_OPERATOR   = "ms-i2e1qhvmkvbnkt0le7rczw5x"
PS_AUTHORITY  = "ms-l29wc96z6g1a432bhcxxo7dy"


def build_instance(pc):
    xml = xml_header(CT_ID)
    xml += xml_preamble(DM_LABEL)
    xml += cluster_open(CL_ROOT, "Port Call Record")

    xml += xdstring(*W_FLAG, "Flag State", pc["flag"])
    xml += xdstring(*W_PORT_CALL, "Port Call ID", pc["port_call_id"])
    xml += xdstring(*W_BERTH, "Berth Assignment", pc["berth"])
    xml += xdstring(*W_NEXT_PORT, "Next Port of Call", pc["next_port"])
    xml += xdstring(*W_DEPART_PORT, "Port of Departure", pc["depart_port"])
    xml += xdstring(*W_CALL_SIGN, "Vessel Call Sign", pc["call_sign"])
    xml += xdstring(*W_IMO, "Vessel IMO Number", pc["imo"])
    xml += xdstring(*W_MMSI, "Vessel MMSI", pc["mmsi"])
    xml += xdstring(*W_VESSEL_NAME, "Vessel Name", pc["vessel_name"])
    xml += xdstring(*W_VOYAGE_NUM, "Voyage Number", pc["voyage"])
    xml += xdtoken(*W_CARGO_TYPE, "Cargo Type", pc["cargo_type"])
    xml += xdtoken(*W_PURPOSE, "Purpose of Call", pc["purpose"])
    xml += xdcount(*W_CREW_CT, "Crew Count", str(pc["crew"]), "Persons")
    xml += xdcount(*W_PAX_CT, "Passenger Count", str(pc["pax"]), "Persons")
    xml += xdquantity(*W_DRAFT, "Vessel Draft", str(pc["draft"]), "Length/Distance (SI - Metric)")
    xml += xdquantity(*W_GROSS_TON, "Vessel Gross Tonnage", str(pc["gross_ton"]), "Gross Tonnage")
    xml += xdquantity(*W_LOA, "Vessel Length Overall", str(pc["loa"]), "Length/Distance (SI - Metric)")
    xml += xdquantity(*W_NET_TON, "Vessel Net Tonnage", str(pc["net_ton"]), "Net Tonnage")
    xml += xdtemporal(*W_ARRIVAL, "Arrival Date/Time", pc["arrival"], "datetime")
    xml += xdtemporal(*W_DEPARTURE, "Departure Date/Time", pc["departure"], "datetime")

    # Cargo Manifest
    xml += cluster_open(CL_CARGO, "Cargo Manifest", indent=2)
    xml += xdboolean_stub(*W_CUSTOMS_FILED, "Customs Declaration Filed", indent=3)
    xml += xdboolean_stub(*W_HAZARDOUS, "Hazardous Cargo", indent=3)
    xml += xdstring(*W_BRN, "Business Registry Number", pc.get("brn", "N/A"), indent=3)
    xml += xdstring(*W_CARGO_DESC, "Cargo Description", pc["cargo_desc"], indent=3)
    xml += xdstring(*W_CARGO_DEST, "Cargo Destination", pc["cargo_dest"], indent=3)
    xml += xdstring(*W_CARGO_ORIG, "Cargo Origin", pc["cargo_orig"], indent=3)
    xml += xdstring(*W_CUSTOMS_REF, "Customs Reference Number", pc.get("customs_ref", "N/A"), indent=3)
    xml += xdtoken(*W_HAZMAT_CLS, "Hazmat Class", pc.get("hazmat", "None"), indent=3)
    xml += xdcount(*W_CONTAINER, "Container Count", str(pc.get("containers", 0)),
                    "Twenty-foot Equivalent Units (TEU)", indent=3)
    xml += xdquantity(*W_CARGO_WT, "Cargo Weight", str(pc.get("cargo_wt", 0)),
                       "Mass/Weight (SI - Metric)", indent=3)
    xml += cluster_close(CL_CARGO, indent=2)

    # Port Fees
    xml += cluster_open(CL_FEES, "Port Fees", indent=2)
    xml += xdtoken(*W_FEE_TYPE, "Fee Type", pc.get("fee_type", "Docking"), indent=3)
    xml += xdtoken(*W_FEE_PAY_ST, "Payment Status", "Paid", indent=3)
    xml += xdquantity(*W_FEE_AMT, "Port Fee Amount", str(pc.get("fee_amt", 5000)),
                       "Cordova Córdoba (COR)", indent=3)
    xml += xdtemporal(*W_FEE_DATE, "Fee Date", pc["arrival"][:10], "date", indent=3)
    xml += cluster_close(CL_FEES, indent=2)

    xml += cluster_close(CL_ROOT)
    xml += party_stub(PS_OPERATOR, "Vessel Owner/Operator")
    xml += party_stub(PS_AUTHORITY, "Port Authority")
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
    "brn": "BIZ-001102",
    "cargo_desc": "Mixed general cargo - agricultural equipment, building materials",
    "cargo_dest": "Porto Sereno, Republic of Cordova",
    "cargo_orig": "Buenaventura, Colombia",
    "customs_ref": "CUS-2026-0142-001",
    "containers": 45, "cargo_wt": 2340,
    "fee_type": "Docking", "fee_amt": 12500,
}

BG_VESSELS = [
    ("MV Pacifica Corriente", "Panama", "9823456", "352823456", "HPPAC", "Tanker", "Fuel Discharge", 22, "2026-01-05"),
    ("MV Costa Linda", "Republic of Cordova", "9812345", "370812345", "HCCL", "Container", "Cargo Discharge", 15, "2026-01-08"),
    ("MV Atlantico Sur", "Liberia", "9834567", "636834567", "D5AS", "Bulk Carrier", "Cargo Loading", 19, "2026-01-15"),
    ("MV Isla Bonita", "Republic of Cordova", "9845678", "370845678", "HCIB", "General Cargo", "Cargo Discharge", 12, "2025-12-28"),
    ("MV Porto Express", "Marshall Islands", "9856789", "538856789", "V7PE", "Container", "Cargo Discharge", 20, "2025-12-20"),
]


def generate():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    count = 0

    # MV Estrella del Sur
    xml = build_instance(ESTRELLA)
    write_xml(os.path.join(OUTPUT_DIR, f"mp-{cuid_generator()}.xml"), xml)
    count += 1

    # Background port calls
    for name, flag, imo, mmsi, csign, ctype, purpose, crew, arr_date in BG_VESSELS:
        pc = {
            "flag": flag, "port_call_id": f"PC-2026-{random.randint(100,999):03d}",
            "berth": f"Berth {random.randint(1,12)}, Porto Sereno Commercial Terminal",
            "next_port": random.choice(["Cartagena", "Panama City", "Guayaquil", "Callao"]),
            "depart_port": random.choice(["Houston", "Santos", "Buenaventura", "Balboa"]),
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
            "containers": random.randint(10, 100),
            "cargo_wt": random.randint(500, 5000),
            "fee_amt": random.randint(5000, 25000),
        }
        xml = build_instance(pc)
        write_xml(os.path.join(OUTPUT_DIR, f"mp-{cuid_generator()}.xml"), xml)
        count += 1

    print(f"Maritime Port Authority: generated {count} XML files in {OUTPUT_DIR}")


if __name__ == "__main__":
    generate()
