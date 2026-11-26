---
template_version: "4.0.0"
dataset:
  name: "Maritime Port Authority"
  description: "Ship traffic, cargo manifests, crew lists, customs declarations, and port operations for Porto Sereno — the sole international port of the Republic of Cordova"
  domain: "Maritime"
  creator: "Axius SDC"
  project: "Cordova"
enrichment:
  enable_llm: true
---

# Dataset Overview

Porto Sereno is Cordova's only international port. This domain captures vessel arrivals, cargo movements, crew identity, customs declarations, and port fees. It is the entry point for the Contagion scenario — a sick crew member arriving on MV Estrella del Sur triggers cross-domain contact tracing through Civil Registry, Healthcare, Employment, and Education.

**Purpose**: Record all maritime operations, vessel movements, crew, cargo, and customs at Porto Sereno.

**Business Context**:
- Primary use: Port authority operations, customs enforcement, vessel tracking
- Secondary use: Supply chain provenance queries (cargo → business → tax), contagion contact tracing
- Stakeholders: Port Authority, Customs, Coast Guard, Business Registry (shipping companies)

**Standards Alignment**:
- NIEM Maritime domain (`m:VesselArrivalType`) — reuses NIEM vessel and crew components
- IMO FAL Convention for vessel arrival reporting
- SDC4 Reference Model (SDCRM) for structural compliance
- W3C DPV 2.2 — `dpv:RegulatoryCompliance`, `dpv:CustomsDeclaration`
- Legal Basis: `dpv:OfficialAuthority`, `dpv:LegalObligation`

**Access Control**:
- Full: Port Authority, Citizen (own records)
- Crew lists: Law Enforcement
- Port fees: Tax Authority
- Provenance only: Auditor
- Hidden: Healthcare, Civil Registrar, Employer/HR

---

## Root Cluster: Port Call Record

A single port call — one vessel arriving at and departing from Porto Sereno.

**Purpose**: Document a vessel's visit to Porto Sereno with all associated records
**Business Context**: Primary operational record for port authority. Links to cargo, crew, fees, and customs.
**Rules**:
  - Arrival Date/Time ≤ Departure Date/Time

### Column: Port Call ID
**Type**: xdstring
**Description**: Unique identifier for this port call record. Assigned by Porto Sereno Port Authority.
**Constraints**:
  - required: true
  - max_length: 20

---

### Column: Vessel Name
**ReuseComponent**: @NIEM:Vessel Name
**Description**: The official registered name of the vessel
**Constraints**:
  - required: true

---

### Column: Vessel IMO Number
**ReuseComponent**: @NIEM:Vessel IMO Number
**Description**: International Maritime Organization 7-digit ship identification number
**Constraints**:
  - required: true

---

### Column: Vessel Call Sign
**ReuseComponent**: @NIEM:Vessel Call Sign
**Description**: Radio call sign assigned to the vessel

---

### Column: Vessel MMSI
**ReuseComponent**: @NIEM:Vessel MMSI
**Description**: Maritime Mobile Service Identity number (9 digits)

---

### Column: Flag State
**Type**: xdstring
**Description**: Country of vessel registration (flag state)
**Constraints**:
  - required: true
  - max_length: 100

---

### Column: Vessel Type
**ReuseComponent**: @NIEM:Cargo Type
**Description**: Type of vessel — cargo, tanker, bulk carrier, fishing, passenger, cruise
**Constraints**:
  - required: true

---

### Column: Gross Tonnage
**ReuseComponent**: @NIEM:Vessel Gross Tonnage
**Description**: Vessel gross tonnage (GT) as per International Tonnage Certificate

---

### Column: Net Tonnage
**ReuseComponent**: @NIEM:Vessel Net Tonnage
**Description**: Vessel net tonnage (NT)

---

### Column: Vessel Length
**ReuseComponent**: @NIEM:Vessel Length
**Description**: Overall length of vessel in meters

---

### Column: Vessel Draft
**ReuseComponent**: @NIEM:Vessel Draft
**Description**: Current draft of vessel in meters

---

### Column: Arrival Date/Time
**Type**: xdtemporal
**Description**: Date and time the vessel arrived at Porto Sereno
**Constraints**:
  - required: true

---

### Column: Departure Date/Time
**Type**: xdtemporal
**Description**: Date and time the vessel departed Porto Sereno. Null if vessel is currently in port.

---

### Column: Berth Assignment
**ReuseComponent**: @NIEM:Berth Assignment
**Description**: Assigned berth number or designation at Porto Sereno

---

### Column: Purpose of Call
**ReuseComponent**: @NIEM:Purpose of Call
**Description**: Reason for the port call — cargo discharge, cargo loading, bunkering, repairs, crew change, passenger embarkation
**Constraints**:
  - required: true

---

### Column: Last Port of Departure
**ReuseComponent**: @NIEM:Port of Departure
**Description**: The port the vessel departed from before arriving at Porto Sereno
**Constraints**:
  - required: true

---

### Column: Next Port of Call
**ReuseComponent**: @NIEM:Next Port of Call
**Description**: The vessel's next scheduled port after departing Porto Sereno

---

### Column: Voyage Number
**ReuseComponent**: @NIEM:Voyage Number
**Description**: The shipping company's voyage or rotation number

---

## Sub-Cluster: Port Call Vessel Owner

The company that owns or operates the vessel. Links to Business Registry.

**Parent**: Port Call Record
**Purpose**: Identify the responsible shipping company for regulatory and financial purposes

### Column: Company Name
**ReuseComponent**: @NIEM:Organization Name
**Description**: Name of the vessel owner or operating company
**Constraints**:
  - required: true

---

### Column: Business Registry Number
**ReuseComponent**: @Cordova:Business Registry Number
**Description**: Cordova Business Registry Number if the company is registered in Cordova. Null for foreign companies.

---

### Column: Company Contact
**ReuseComponent**: @NIEM:Contact Telephone Number
**Description**: Contact telephone for the shipping company or local agent

---

### Column: Local Agent
**Type**: xdstring
**Description**: Name of the local shipping agent representing the vessel in Porto Sereno
**Constraints**:
  - max_length: 200

---

## Sub-Cluster: Cargo Manifest

Cargo loaded or discharged during this port call.

**Parent**: Port Call Record
**Purpose**: Record cargo movements for customs, safety, and tax purposes
**Rules**:
  - If Hazardous Cargo is true, Hazmat Class must be present

### Column: Cargo Type
**ReuseComponent**: @NIEM:Cargo Type
**Description**: Classification of cargo — container, bulk, liquid, break-bulk, vehicles, livestock, hazardous
**Constraints**:
  - required: true

---

### Column: Cargo Description
**Type**: xdstring
**Description**: Description of cargo contents
**Constraints**:
  - required: true
  - max_length: 500

---

### Column: Cargo Weight
**ReuseComponent**: @NIEM:Total Cargo Weight
**Description**: Total weight of this cargo item in metric tons
**Constraints**:
  - required: true

---

### Column: Cargo Origin
**Type**: xdstring
**Description**: Port or country of origin for this cargo
**Constraints**:
  - max_length: 200

---

### Column: Cargo Destination
**Type**: xdstring
**Description**: Final destination for this cargo (may be Porto Sereno or transshipment)
**Constraints**:
  - max_length: 200

---

### Column: Customs Reference
**ReuseComponent**: @NIEM:Customs Reference Number
**Description**: Customs declaration reference number for this cargo item

---

### Column: Customs Declaration Filed
**ReuseComponent**: @NIEM:Customs Declaration Filed
**Description**: Whether a customs declaration has been filed for this cargo

---

### Column: Hazardous Cargo
**ReuseComponent**: @NIEM:Hazardous Cargo
**Description**: Whether the cargo is classified as hazardous materials

---

### Column: Hazmat Class
**ReuseComponent**: @NIEM:Hazmat Class
**Description**: IMO hazardous materials classification, if applicable

---

### Column: Receiving Business
**ReuseComponent**: @Cordova:Business Registry Number
**Description**: Cordova Business Registry Number of the company receiving this cargo. Links to Business Registry and Tax domains.

---

## Sub-Cluster: Crew List

Persons aboard the vessel. Links to Civil Registry for Cordovan nationals.

**Parent**: Port Call Record
**Purpose**: Record crew identity for immigration, health screening, and contact tracing
**Business Context**: Critical for the Contagion scenario — crew member Carlos Mendoza is identified here
**Rules**:
  - If Medical Assistance Required is true, Shore Leave Requested cannot be true

### Column: Crew Member Name
**ReuseComponent**: @NIEM:Person Full Name
**Description**: Full name of the crew member
**Constraints**:
  - required: true

---

### Column: Crew Member National ID
**ReuseComponent**: @Cordova:National ID (CID)
**Description**: Cordova National ID if the crew member is a Cordovan national. Null for foreign nationals. Links to Civil Registry.

---

### Column: Passport Number
**ReuseComponent**: @NIEM:Passport Number
**Description**: Passport number for identity verification
**Constraints**:
  - required: true

---

### Column: Nationality
**ReuseComponent**: @NIEM:Country Code
**Description**: Country of citizenship
**Constraints**:
  - required: true

---

### Column: Rank/Position
**ReuseComponent**: @NIEM:Job Title
**Description**: Crew member's rank or position aboard the vessel (Captain, First Officer, Engineer, Deck Hand, Cook, etc.)
**Constraints**:
  - required: true

---

### Column: Date of Birth
**ReuseComponent**: @NIH_CDE:Birth Date
**Description**: Crew member's date of birth for identity verification

---

### Column: Shore Leave Requested
**ReuseComponent**: @NIEM:Crew Shore Leave Requested
**Description**: Whether the crew member has requested shore leave in Porto Sereno

---

### Column: Medical Flag
**ReuseComponent**: @NIEM:Medical Assistance Required
**Description**: Whether the crew member requires medical assistance. If true, triggers Healthcare domain linkage.

---

## Sub-Cluster: Port Fees

Financial charges for this port call. Links to Tax & Revenue domain.

**Parent**: Port Call Record
**Purpose**: Record port fees for billing, tax reporting, and financial auditing

### Column: Fee Type
**Type**: xdtoken
**Description**: Type of port fee assessed
**Enumeration**:
  - Berth Fee: Daily charge for berth occupancy
  - Pilotage: Pilot services for harbor entry/exit
  - Tug Service: Tugboat assistance charges
  - Cargo Handling: Stevedore and cargo handling fees
  - Customs Processing: Customs inspection and processing fee
  - Waste Disposal: Ship waste removal charges
  - Fresh Water: Potable water supply charges
  - Provisions: Ship provisioning charges
**Constraints**:
  - required: true

---

### Column: Fee Amount
**ReuseComponent**: @NIEM:Amount Value
**Description**: Amount charged in Cordova Pesos
**Constraints**:
  - required: true

---

### Column: Fee Date
**Type**: xdtemporal
**Description**: Date the fee was assessed
**Constraints**:
  - required: true

---

### Column: Payment Status
**Type**: xdtoken
**Description**: Whether the fee has been paid
**Enumeration**:
  - Paid: Payment received
  - Invoiced: Invoice issued, awaiting payment
  - Overdue: Payment past due date
**Constraints**:
  - required: true

---

## Governance Components

Components below are SDC4 Reference Model governance structures — Attestation, Participation, and Party — that wrap around the data clusters above.

### Attestation: Maritime Attestation

Formal governance attestation attached to this Data Model.

- **View**: Maritime Attested View (XdFile, `application/pdf`, content_mode=`url`) — attested document view
- **Proof**: Digital Signature Proof (XdFile, `application/pgp-signature` + `application/pkcs7-signature`, content_mode=`embed`) — shared cryptographic proof
- **Reason**: Maritime Attestation Reason (XdString, min_length=1, max_length=500) — free-text reason for attestation

---

### Participation: Crew Participation

Participation of crew members aboard the vessel.

**Function** (Crew Participation Function):
  - Bridge Officer
  - Engineer
  - Deck Officer
  - Radio Officer
  - Medical Officer
  - Other

**Mode** (Crew Participation Mode):
  - On Board
  - Shore-Based Remote
  - Port Authority Liaison
  - Other

---

### Party: Vessel Owner/Operator

The organization that owns or operates the vessel. W3C PROV-DM Agent (Organization) with registry number as identifier.

### Party: Crew Member

Person serving as crew member aboard a vessel. W3C PROV-DM Agent (Person) with passport, nationality, and operational status.

### Party: Port Authority

Maritime port authority managing vessel traffic, arrivals, and departures. W3C PROV-DM Agent (Organization).
