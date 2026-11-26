---
template_version: "4.0.0"
dataset:
  name: "Law Enforcement Record"
  description: "Incident reports, officer records, and case disposition for the Republic of Cordova — quarantine enforcement, public safety incidents, and misdemeanor case tracking"
  domain: "Justice"
  creator: "Axius SDC"
  project: "Cordova"
enrichment:
  enable_llm: true
---

# Dataset Overview

Cordova is a peaceful island nation with no felony classification — all offenses are misdemeanors. Law Enforcement records cover public safety incidents, quarantine enforcement, traffic violations, and petty crime. In the Contagion scenario, the Provincial Health Authority establishes a quarantine monitoring zone around the port district, and Law Enforcement manages the perimeter and compliance.

This domain heavily reuses NIEM justice components, demonstrating how the same structural definitions work across US federal standards and a fictional island nation.

**Purpose**: Record public safety incidents, charges, and dispositions in Cordova.

**Business Context**:
- Primary use: Police operations, incident documentation, case management
- Secondary use: Quarantine enforcement (Contagion scenario), public safety statistics
- Stakeholders: Cordova National Police, Provincial Health Authority, courts

**Standards Alignment**:
- SDC4 Reference Model (SDCRM)
- NIEM Justice domain (`j:IncidentType`, `j:ArrestType`)
- W3C DPV 2.2 — `dpv:EnforceLaw`, `dpv:PublicSafety`
- Legal Basis: `dpv:OfficialAuthority`, `dpv:LegalObligation`

**Access Control**:
- Full: Law Enforcement, Citizen (own records)
- Identity verification: Civil Registrar
- Provenance only: Auditor
- Hidden: Healthcare Provider, Tax Authority, Port Authority, Employer/HR, Educational Institution

---

## Root Cluster: Incident Report

A single public safety incident recorded by Cordova National Police.

**Purpose**: Document an incident with location, category, involved parties, and outcome
**Business Context**: Links to Civil Registry for person identification

### Column: Incident Report Number
**ReuseComponent**: @NIEM:Incident Report Number
**Description**: Unique identifier for this incident report
**Constraints**:
  - required: true

---

### Column: Incident Category
**ReuseComponent**: @NIEM:Incident Category Code
**Description**: Classification of the incident type
**Constraints**:
  - required: true

---

### Column: Incident Date
**ReuseComponent**: @NIEM:Incident Date
**Description**: Date and time the incident occurred
**Constraints**:
  - required: true

---

### Column: Incident Location Street
**ReuseComponent**: @NIEM:Location Street Full Text
**Description**: Street address where the incident occurred
**Constraints**:
  - required: true

---

### Column: Incident Location City
**ReuseComponent**: @Cordova:City
**Description**: City where the incident occurred
**Constraints**:
  - required: true

---

### Column: Incident Location Province
**ReuseComponent**: @Cordova:Province
**Description**: Province where the incident occurred
**Constraints**:
  - required: true

---

### Column: Incident Summary
**ReuseComponent**: @NIEM:Incident Summary
**Description**: Brief narrative summary of the incident
**Constraints**:
  - required: true

---

### Column: Incident Status
**Type**: xdtoken
**Description**: Current status of the incident
**Enumeration**:
  - Open: Under active investigation
  - Closed: Investigation complete, disposition assigned
  - Pending: Awaiting court action or additional information
**Constraints**:
  - required: true

---

## Sub-Cluster: Incident Reporting Officer

The officer who filed the incident report.

**Parent**: Incident Report
**Purpose**: Identify the reporting officer for accountability and follow-up

### Column: Officer Badge Number
**ReuseComponent**: @NIEM:Officer Badge Number
**Description**: Badge number of the reporting officer
**Constraints**:
  - required: true

---

### Column: Officer Rank
**ReuseComponent**: @NIEM:Officer Rank
**Description**: Rank of the reporting officer

---

### Column: Officer Unit
**ReuseComponent**: @NIEM:Officer Unit
**Description**: Unit or precinct assignment

---

## Sub-Cluster: Incident Involved Person

A person involved in the incident (subject, complainant, or witness).

**Parent**: Incident Report
**Purpose**: Link incident participants to Civil Registry
**Business Context**: Enables cross-domain person queries (incident → person → address → contacts)

### Column: Person National ID
**ReuseComponent**: @Cordova:National ID (CID)
**Description**: National ID of the involved person, linking to Civil Registry
**Constraints**:
  - required: true

---

### Column: Person Name
**ReuseComponent**: @NIEM:Person Full Name
**Description**: Full name of the involved person
**Constraints**:
  - required: true

---

### Column: Involvement Type
**Type**: xdtoken
**Description**: How the person is involved in the incident
**Enumeration**:
  - Subject: Person of interest or suspected offender
  - Complainant: Person who reported the incident
  - Witness: Person who observed the incident
**Constraints**:
  - required: true

---

### Column: Person Statement
**ReuseComponent**: @NIEM:Witness Statement
**Description**: Statement provided by the involved person

---

## Sub-Cluster: Charge and Disposition

Charges filed and case outcome. Cordova has misdemeanor-level offenses only.

**Parent**: Incident Report
**Purpose**: Record charges and their disposition
**Rules**:
  - If Disposition is "Fine", Fine Amount must be present

### Column: Charge Category
**ReuseComponent**: @Cordova:Charge Category (Cordova)
**Description**: Category of the misdemeanor charge
**Constraints**:
  - required: true

---

### Column: Charge Description
**ReuseComponent**: @NIEM:Charge Description
**Description**: Detailed description of the charge

---

### Column: Charge Date
**ReuseComponent**: @NIEM:Charge Filing Date
**Description**: Date the charge was filed

---

### Column: Disposition
**ReuseComponent**: @Cordova:Disposition (Cordova)
**Description**: Outcome of the case — Fine, Community Service, Case Dismissed, Pending

---

### Column: Disposition Date
**Type**: xdtemporal
**Description**: Date the disposition was recorded

---

### Column: Fine Amount
**ReuseComponent**: @NIEM:Amount Value
**Description**: Amount of fine assessed, if applicable. Links to Tax & Revenue for collection.

---

## Sub-Cluster: Quarantine Enforcement

Special sub-cluster for public health quarantine orders. Used in the Contagion scenario.

**Parent**: Incident Report
**Purpose**: Document quarantine zone establishment and compliance monitoring
**Business Context**: Links Law Enforcement to Healthcare domain through quarantine orders
**Rules**:
  - Quarantine Start Date ≤ Quarantine End Date

### Column: Quarantine Zone
**Type**: xdstring
**Description**: Description of the geographic area under quarantine (e.g., "Porto Sereno Port District, Berths 1-12")
**Constraints**:
  - max_length: 500

---

### Column: Quarantine Start Date
**Type**: xdtemporal
**Description**: Date the quarantine order took effect
**Constraints**:
  - required: true

---

### Column: Quarantine End Date
**Type**: xdtemporal
**Description**: Date the quarantine order was lifted. Null if still active.

---

### Column: Issuing Authority
**Type**: xdstring
**Description**: The authority that issued the quarantine order (e.g., "Provincial Health Authority, Aldara")
**Constraints**:
  - required: true
  - max_length: 200

---

### Column: Compliance Status
**Type**: xdtoken
**Description**: Whether the quarantine is being complied with
**Enumeration**:
  - Compliant: All persons and entities within the zone are complying
  - Violation Detected: One or more violations of the quarantine order detected
  - Under Review: Compliance status being assessed
**Constraints**:
  - required: true

---

## Governance Components

Components below are SDC4 Reference Model governance structures — Attestation, Participation, and Party — that wrap around the data clusters above.

### Attestation: Law Enforcement Attestation

Formal governance attestation attached to this Data Model.

- **View**: Law Enforcement Attested View (XdFile, `application/pdf`, content_mode=`url`) — attested document view
- **Proof**: Digital Signature Proof (XdFile, `application/pgp-signature` + `application/pkcs7-signature`, content_mode=`embed`) — shared cryptographic proof
- **Reason**: Law Enforcement Attestation Reason (XdString, min_length=1, max_length=500) — free-text reason for attestation

---

### Party: Reporting Officer

The law enforcement officer who filed the incident report. W3C PROV-DM Agent (Person) with badge number as identifier.

### Party: Involved Person

Person involved in a law enforcement incident (suspect, victim, witness). W3C PROV-DM Agent (Person) with involvement classification.
