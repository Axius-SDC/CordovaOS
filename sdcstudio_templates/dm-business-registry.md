---
template_version: "4.0.0"
dataset:
  name: "Business Registry"
  description: "Legal registration, officers, and classification for all business entities in the Republic of Cordova — linking employers to people, port cargo to receiving companies, and businesses to tax filings"
  domain: "Government"
  creator: "Axius SDC"
  project: "Cordova"
enrichment:
  enable_llm: true
---

# Dataset Overview

The Business Registry records every legal business entity in Cordova. It connects to Employment (employer identity), Maritime (shipping companies and cargo receivers), Tax & Revenue (business tax filings), and Property Registry (commercial property ownership). In the Contagion scenario, the vessel operator and the cargo receiving company are both identified through this domain.

**Purpose**: Maintain the authoritative registry of business entities in Cordova.

**Business Context**:
- Primary use: Business incorporation, licensing, and compliance
- Secondary use: Supply chain provenance (cargo → receiving business → tax filings)
- Stakeholders: Ministry of Commerce, Tax Authority, Port Authority, business owners

**Standards Alignment**:
- SDC4 Reference Model (SDCRM)
- NIEM Core organization components
- W3C DPV 2.2 — `dpv:CommercialRegistration`, `dpv:RegulatoryCompliance`
- Legal Basis: `dpv:LegalObligation`

**Access Control**:
- Full: Business Owner, Tax Authority
- Public info (name, type, status): All roles
- Financial details: Tax Authority only
- Provenance only: Auditor
- Hidden: Healthcare Provider

---

## Root Cluster: Business Entity

A registered business in the Republic of Cordova.

**Purpose**: Complete business registration record
**Business Context**: Links to Employment, Maritime, Tax, and Property domains

### Column: Business Registry Number
**ReuseComponent**: @Cordova:Business Registry Number
**Description**: Unique Cordova business registration identifier
**Constraints**:
  - required: true

---

### Column: Business Name
**ReuseComponent**: @NIEM:Organization Name
**Description**: Legal name of the business entity
**Constraints**:
  - required: true

---

### Column: Business Type
**ReuseComponent**: @Cordova:Business Type (Cordova)
**Description**: Legal structure — Sole Proprietor, Partnership, Corporation, Cooperative
**Constraints**:
  - required: true

---

### Column: Industry
**Type**: xdtoken
**Description**: Primary industry classification
**Enumeration**:
  - Agriculture: Farming, ranching, forestry, fishing
  - Manufacturing: Production and processing of goods
  - Shipping: Maritime transport, logistics, freight forwarding
  - Retail: Consumer goods sales
  - Healthcare: Medical services, clinics, pharmacies
  - Education: Schools, universities, training providers
  - Technology: Software, IT services, telecommunications
  - Construction: Building, infrastructure, real estate development
  - Finance: Banking, insurance, accounting
  - Government Services: Public sector contracting, consulting
  - Hospitality: Hotels, restaurants, tourism
**Constraints**:
  - required: true

---

### Column: Registration Date
**Type**: xdtemporal
**Description**: Date the business was officially registered in Cordova
**Constraints**:
  - required: true

---

### Column: Status
**Type**: xdtoken
**Description**: Current registration status
**Enumeration**:
  - Active: Business is currently operating
  - Suspended: Registration temporarily suspended
  - Dissolved: Business has been legally dissolved
**Constraints**:
  - required: true

---

### Column: Tax ID
**ReuseComponent**: @NIEM:Organization Tax ID
**Description**: Tax identification number assigned by Cordova Tax Authority

---

## Sub-Cluster: Registered Address

Official business address on file with the registry.

**Parent**: Business Entity
**Purpose**: Legal address for service and correspondence

### Column: Street Address
**ReuseComponent**: @Default:Address (Line 1)
**Description**: Business street address
**Constraints**:
  - required: true

---

### Column: Address Line 2
**ReuseComponent**: @Default:Address (Line 2)
**Description**: Suite, floor, or unit number

---

### Column: City
**ReuseComponent**: @Cordova:City
**Description**: City where the business is registered
**Constraints**:
  - required: true

---

### Column: Province
**ReuseComponent**: @Cordova:Province
**Description**: Province where the business is registered
**Constraints**:
  - required: true

---

### Column: Phone
**ReuseComponent**: @Cordova:Cordova Phone Number
**Description**: Business telephone number

---

### Column: Email
**ReuseComponent**: @Cordova:Cordova Email Address
**Description**: Business email address

---

## Sub-Cluster: Officers

Persons associated with the business as owners, directors, or officers. Links to Civil Registry.

**Parent**: Business Entity
**Purpose**: Record the persons legally responsible for the business
**Business Context**: Enables person → business → tax chain queries in the graph
**Rules**:
  - Appointment Date ≤ Resignation Date

### Column: Officer National ID
**ReuseComponent**: @Cordova:National ID (CID)
**Description**: National ID of the business officer, linking to Civil Registry
**Constraints**:
  - required: true

---

### Column: Officer Name
**ReuseComponent**: @NIEM:Person Full Name
**Description**: Full name of the officer
**Constraints**:
  - required: true

---

### Column: Officer Role
**Type**: xdtoken
**Description**: Role of the person in the business
**Enumeration**:
  - Owner: Business owner or majority shareholder
  - Director: Board member or director
  - Manager: General manager or managing partner
  - Secretary: Corporate secretary
  - Treasurer: Financial officer or treasurer
**Constraints**:
  - required: true

---

### Column: Appointment Date
**Type**: xdtemporal
**Description**: Date the officer was appointed to their role
**Constraints**:
  - required: true

---

### Column: Resignation Date
**Type**: xdtemporal
**Description**: Date the officer resigned or was removed. Null for current officers.

---

## Governance Components

Components below are SDC4 Reference Model governance structures — Attestation, Participation, and Party — that wrap around the data clusters above.

### Attestation: Business Registry Attestation

Formal governance attestation attached to this Data Model.

- **View**: Business Registry Attested View (XdFile, `application/pdf`, content_mode=`url`) — attested document view
- **Proof**: Digital Signature Proof (XdFile, `application/pgp-signature` + `application/pkcs7-signature`, content_mode=`embed`) — shared cryptographic proof
- **Reason**: Business Registry Attestation Reason (XdString, min_length=1, max_length=500) — free-text reason for attestation

---

### Party: Business Officer

Person acting as an officer of a business entity (director, secretary, etc.). W3C PROV-DM Agent (Person) with appointment lifecycle.

### Party: Business Registry Office

Government office responsible for maintaining the national business registry. W3C PROV-DM Agent (Organization).
