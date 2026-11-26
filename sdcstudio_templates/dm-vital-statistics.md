---
template_version: "4.0.0"
dataset:
  name: "Vital Statistics Record"
  description: "Birth certificates, death certificates, marriage certificates, and divorce decrees for the Republic of Cordova — formal attested life events linking persons, physicians, and legal officials"
  domain: "Government"
  creator: "Axius SDC"
  project: "Cordova"
enrichment:
  enable_llm: true
---

# Dataset Overview

Vital Statistics records formal life events in Cordova — births, deaths, marriages, and divorces. Each record carries a full chain of attestation: who created it, who attested to it, and when. These aren't just data rows; they're governed legal events that demonstrate the Audit and Attestation components of the SDC4 Reference Model. Birth records link to parents (Civil Registry), death records link to certifying physicians (Healthcare), and marriage records link both parties to Civil Registry identities.

**Purpose**: Maintain the authoritative registry of life events in Cordova.

**Business Context**:
- Primary use: Legal documentation of births, deaths, marriages, and divorces
- Secondary use: Demographic statistics, public health (cause of death), identity verification
- Stakeholders: Civil Registrar, Ministry of Health, courts, citizens

**Standards Alignment**:
- SDC4 Reference Model (SDCRM)
- NIEM Core person and justice components
- W3C DPV 2.2 — `dpv:VitalRecords`, `dpv:GovernmentalAdministration`
- Legal Basis: `dpv:LegalObligation`

**Access Control**:
- Full: Citizen (own records), Civil Registrar
- Healthcare context: Healthcare Provider (birth/death certificates)
- Provenance only: Auditor
- Hidden: Port Authority, Tax Authority, Employer/HR, Educational Institution

---

## Root Cluster: Vital Event

A single life event recorded in the Cordova vital statistics registry.

**Purpose**: Common fields shared across all vital event types
**Business Context**: Links to Civil Registry for person identification
**Rules**:
  - Event Date ≤ Registration Date

### Column: Certificate Number
**Type**: xdstring
**Description**: Unique certificate number for this vital record
**Constraints**:
  - required: true
  - max_length: 20

---

### Column: Event Type
**Type**: xdtoken
**Description**: Type of vital event
**Enumeration**:
  - Birth: Birth certificate
  - Death: Death certificate
  - Marriage: Marriage certificate
  - Divorce: Divorce decree
**Constraints**:
  - required: true

---

### Column: Event Date
**Type**: xdtemporal
**Description**: Date the vital event occurred
**Constraints**:
  - required: true

---

### Column: Registration Date
**Type**: xdtemporal
**Description**: Date the event was officially registered
**Constraints**:
  - required: true

---

### Column: Event City
**ReuseComponent**: @Cordova:City
**Description**: City where the event occurred
**Constraints**:
  - required: true

---

### Column: Event Province
**ReuseComponent**: @Cordova:Province
**Description**: Province where the event occurred
**Constraints**:
  - required: true

---

### Column: Record Status
**Type**: xdtoken
**Description**: Status of the vital record
**Enumeration**:
  - Active: Record is current and valid
  - Amended: Record has been officially amended
  - Voided: Record has been voided by court order
**Constraints**:
  - required: true

---

## Sub-Cluster: Birth Record

Details specific to birth certificates.

**Parent**: Vital Event
**Purpose**: Document a birth with parents, attending physician, and location
**Business Context**: Links newborn and parents to Civil Registry, physician to Healthcare

### Column: Child National ID
**ReuseComponent**: @Cordova:National ID (CID)
**Description**: National ID assigned to the newborn at birth registration
**Constraints**:
  - required: true

---

### Column: Child Name
**ReuseComponent**: @NIEM:Person Full Name
**Description**: Full legal name of the child as registered
**Constraints**:
  - required: true

---

### Column: Child Sex
**ReuseComponent**: @NIH_CDE:Sex
**Description**: Biological sex of the child at birth
**Constraints**:
  - required: true

---

### Column: Mother National ID
**ReuseComponent**: @Cordova:National ID (CID)
**Description**: National ID of the mother, linking to Civil Registry
**Constraints**:
  - required: true

---

### Column: Father National ID
**ReuseComponent**: @Cordova:National ID (CID)
**Description**: National ID of the father, linking to Civil Registry

---

### Column: Attending Physician Name
**ReuseComponent**: @NIEM:Person Full Name
**Description**: Name of the physician or midwife who attended the birth

---

### Column: Birth Facility
**Type**: xdstring
**Description**: Name of the hospital or facility where birth occurred
**Constraints**:
  - max_length: 200

---

## Sub-Cluster: Death Record

Details specific to death certificates.

**Parent**: Vital Event
**Purpose**: Document a death with cause, certifying physician, and circumstances
**Business Context**: Links to Healthcare (certifying physician), enables public health statistics

### Column: Deceased National ID
**ReuseComponent**: @Cordova:National ID (CID)
**Description**: National ID of the deceased person
**Constraints**:
  - required: true

---

### Column: Deceased Name
**ReuseComponent**: @NIEM:Person Full Name
**Description**: Full name of the deceased
**Constraints**:
  - required: true

---

### Column: Cause of Death
**Type**: xdstring
**Description**: Primary cause of death as determined by certifying physician
**Constraints**:
  - required: true
  - max_length: 500

---

### Column: Manner of Death
**Type**: xdtoken
**Description**: Manner in which death occurred
**Enumeration**:
  - Natural: Death from natural causes or disease
  - Accident: Unintentional death from external cause
  - Homicide: Death caused by another person
  - Suicide: Self-inflicted death
  - Undetermined: Manner could not be determined
  - Pending Investigation: Under active investigation
**Constraints**:
  - required: true

---

### Column: Certifying Physician Name
**ReuseComponent**: @NIEM:Person Full Name
**Description**: Name of the physician who certified the death
**Constraints**:
  - required: true

---

### Column: Certifying Physician License
**Type**: xdstring
**Description**: Medical license number of the certifying physician
**Constraints**:
  - max_length: 20

---

### Column: Place of Death
**Type**: xdtoken
**Description**: Type of location where death occurred
**Enumeration**:
  - Hospital: In a medical facility
  - Residence: At the deceased's home
  - Other: Other location (workplace, public area, etc.)
**Constraints**:
  - required: true

---

## Sub-Cluster: Marriage Record

Details specific to marriage certificates.

**Parent**: Vital Event
**Purpose**: Document a marriage with both parties, officiant, and witnesses
**Business Context**: Links both parties to Civil Registry identities

### Column: Spouse 1 National ID
**ReuseComponent**: @Cordova:National ID (CID)
**Description**: National ID of the first spouse
**Constraints**:
  - required: true

---

### Column: Spouse 1 Name
**ReuseComponent**: @NIEM:Person Full Name
**Description**: Full name of the first spouse
**Constraints**:
  - required: true

---

### Column: Spouse 2 National ID
**ReuseComponent**: @Cordova:National ID (CID)
**Description**: National ID of the second spouse
**Constraints**:
  - required: true

---

### Column: Spouse 2 Name
**ReuseComponent**: @NIEM:Person Full Name
**Description**: Full name of the second spouse
**Constraints**:
  - required: true

---

### Column: Officiant Name
**ReuseComponent**: @NIEM:Person Full Name
**Description**: Name of the person who officiated the marriage ceremony
**Constraints**:
  - required: true

---

### Column: Officiant Title
**Type**: xdstring
**Description**: Title or capacity of the officiant (e.g., "Judge", "Minister", "Civil Registrar")
**Constraints**:
  - required: true
  - max_length: 100

---

### Column: Witness 1 Name
**ReuseComponent**: @NIEM:Person Full Name
**Description**: Name of the first witness

---

### Column: Witness 2 Name
**ReuseComponent**: @NIEM:Person Full Name
**Description**: Name of the second witness

---

## Sub-Cluster: Divorce Record

Details specific to divorce decrees.

**Parent**: Vital Event
**Purpose**: Document a divorce with both parties and court details

### Column: Party 1 National ID
**ReuseComponent**: @Cordova:National ID (CID)
**Description**: National ID of the first party to the divorce
**Constraints**:
  - required: true

---

### Column: Party 1 Name
**ReuseComponent**: @NIEM:Person Full Name
**Description**: Full name of the first party
**Constraints**:
  - required: true

---

### Column: Party 2 National ID
**ReuseComponent**: @Cordova:National ID (CID)
**Description**: National ID of the second party to the divorce
**Constraints**:
  - required: true

---

### Column: Party 2 Name
**ReuseComponent**: @NIEM:Person Full Name
**Description**: Full name of the second party
**Constraints**:
  - required: true

---

### Column: Decree Date
**Type**: xdtemporal
**Description**: Date the divorce decree was issued by the court
**Constraints**:
  - required: true

---

### Column: Court Name
**Type**: xdstring
**Description**: Name of the court that issued the decree
**Constraints**:
  - required: true
  - max_length: 200

---

### Column: Marriage Certificate Number
**Type**: xdstring
**Description**: Certificate number of the original marriage being dissolved
**Constraints**:
  - max_length: 20

---

## Sub-Cluster: Attestation

Formal attestation chain for the vital record — who created, verified, and registered it.

**Parent**: Vital Event
**Purpose**: Document the governance chain for legal accountability
**Business Context**: Demonstrates SDC4 Attestation — the Auditor role sees only this sub-cluster

### Column: Registrar Name
**ReuseComponent**: @NIEM:Person Full Name
**Description**: Name of the civil registrar who recorded the event
**Constraints**:
  - required: true

---

### Column: Registrar Office
**Type**: xdstring
**Description**: Office or jurisdiction of the registrar (e.g., "Civil Registry, Porto Sereno")
**Constraints**:
  - required: true
  - max_length: 200

---

### Column: Attestation Date
**Type**: xdtemporal
**Description**: Date the record was formally attested and sealed
**Constraints**:
  - required: true

---

### Column: Attestation Method
**Type**: xdtoken
**Description**: How the record was attested
**Enumeration**:
  - In Person: Attested with parties present at registrar office
  - Hospital Report: Attested based on hospital report (births, deaths)
  - Court Order: Attested based on court decree (divorces, amendments)
**Constraints**:
  - required: true

---

## Governance Components

Components below are SDC4 Reference Model governance structures — Attestation, Participation, and Party — that wrap around the data clusters above. They were created during pipeline improvements and define who participates, how records are attested, and which organizational roles are involved.

### Attestation: Vital Record Attestation

Formal governance attestation attached to this Data Model.

- **View**: Vital Record Attested View (XdFile, `application/pdf`, content_mode=`url`) — attested document view
- **Proof**: Digital Signature Proof (XdFile, `application/pgp-signature` + `application/pkcs7-signature`, content_mode=`embed`) — shared cryptographic proof
- **Reason**: Vital Record Attestation Reason (XdString, min_length=1, max_length=500) — free-text reason for attestation

---

### Participation: Birth Facility Participation

Participation of the facility where a birth was recorded.

**Function** (Birth Facility Participation Function):
  - Delivering Hospital
  - Birth Center
  - Home Birth Attendant
  - Other

**Mode** (Birth Facility Participation Mode):
  - In Person
  - Electronic Filing
  - Other

---

### Participation: Certifying Physician Participation

Participation of the physician certifying a death.

**Function** (Certifying Physician Participation Function):
  - Attending Physician
  - Medical Examiner
  - Coroner
  - Other

**Mode** (Certifying Physician Participation Mode):
  - In Person
  - Electronic Certification
  - By Proxy
  - Other

---

### Participation: Court Participation

Participation of the court issuing a divorce decree.

**Function** (Court Participation Function):
  - Presiding Court
  - Filing Court
  - Issuing Court
  - Other

**Mode** (Court Participation Mode):
  - In Person
  - Electronic Filing
  - By Mail
  - Other

---

### Participation: Officiant Participation

Participation of the person officiating a marriage.

**Function** (Officiant Participation Function):
  - Religious Officiant
  - Civil Officiant
  - Judge
  - Other

**Mode** (Officiant Participation Mode):
  - In Person
  - By Proxy
  - Other

---

### Party: Vital Record Attestor

The person who formally attests to the vital record — registrar, officiant, or certifying authority. W3C PROV-DM Agent pattern.

### Party: Vital Record Subject

Person who is the subject of a vital statistics record (birth, death, marriage, divorce). W3C PROV-DM Agent (Person) with Cordova CID.

### Party: Birth Facility

Healthcare facility where a birth was recorded. W3C PROV-DM Agent (Organization).

### Party: Certifying Physician

Physician certifying a death record. W3C PROV-DM Agent (Person) with license identifier.

### Party: Court

Court that issued a divorce decree. W3C PROV-DM Agent (Organization).

### Party: Officiant

Person officiating a marriage ceremony (judge, clergy, etc.). W3C PROV-DM Agent (Person).

### Party: Vital Statistics Office

Government office responsible for recording and certifying vital events. W3C PROV-DM Agent (Organization).
