---
template_version: "4.0.0"
dataset:
  name: "Civil Registry"
  description: "The authoritative source of identity for every person in the Republic of Cordova — births, addresses, family relationships, and national identification"
  domain: "Government"
  creator: "Axius SDC"
  project: "Cordova"
enrichment:
  enable_llm: true
---

# Dataset Overview

The Civil Registry is the anchor domain in Cordova OS. Every other domain — Healthcare, Maritime, Law Enforcement, Tax, Employment — references Person cells from this registry. The Person cell appears identically across all ten domains because they share the same SDCRM type. No mapping. No reconciliation. No ETL.

**Purpose**: Maintain the authoritative identity record for every person in Cordova.

**Business Context**:
- Primary use: Government identity management and vital records linkage
- Secondary use: Cross-domain identity reference for all other Cordova domains
- Stakeholders: Civil Registrar, all government agencies, citizens

**Standards Alignment**:
- SDC4 Reference Model (SDCRM) — Person cell structure
- W3C DPV 2.2 — `dpv:IdentityVerification`, `dpv:MaintainCivilRegistry`
- Legal Basis: `dpv:OfficialAuthority`

**Access Control**:
- Full: Citizen (own records), Civil Registrar
- Identity only: Law Enforcement, Tax Authority
- Crew ID: Port Authority
- Verify: Employer/HR
- Provenance only: Auditor

---

## Root Cluster: Civil Registry Record

A complete civil registry entry for one person. This is the anchor node in the Cordova graph — the Person cell that every other domain references.

**Purpose**: Complete identity record for a Cordova resident
**Business Context**: Authoritative source of truth for all government identity verification

### Column: National ID
**ReuseComponent**: @Cordova:National ID (CID)
**Description**: The person's Cordova National Identity Number (CID)
**Constraints**:
  - required: true

---

### Column: Given Name
**ReuseComponent**: @Default:Given Name (Person)
**Description**: The person's first/given name
**Constraints**:
  - required: true

---

### Column: Middle Name
**ReuseComponent**: @Default:Middle Name (Person)
**Description**: The person's middle name, if any

---

### Column: Surname
**ReuseComponent**: @Default:Surname (Person)
**Description**: The person's family/last name
**Constraints**:
  - required: true

---

### Column: Date of Birth
**ReuseComponent**: @NIH_CDE:Birth Date
**Description**: The person's date of birth
**Constraints**:
  - required: true

---

### Column: Sex
**ReuseComponent**: @NIH_CDE:Sex
**Description**: Biological sex as recorded on the birth certificate
**Constraints**:
  - required: true

---

### Column: Gender Identity
**ReuseComponent**: @NIH_CDE:Gender Identity
**Description**: Self-reported gender identity

---

### Column: Place of Birth City
**ReuseComponent**: @Cordova:City
**Description**: City of birth within Cordova. Null if born outside Cordova.

---

### Column: Place of Birth Province
**ReuseComponent**: @Cordova:Province
**Description**: Province of birth within Cordova. Null if born outside Cordova.

---

### Column: Country of Birth
**ReuseComponent**: @NIH_CDE:Country of Birth
**Description**: Country of birth. "Cordova" for nationals, ISO country name for foreign-born residents.
**Constraints**:
  - required: true

---

### Column: Marital Status
**ReuseComponent**: @Cordova:Marital Status (Cordova)
**Description**: Current marital status as recorded in the Civil Registry

---

## Sub-Cluster: Current Address

The person's current residential address within Cordova.

**Parent**: Civil Registry Record
**Purpose**: Current residential address for correspondence and jurisdiction determination

### Column: Street Address
**ReuseComponent**: @Default:Address (Line 1)
**Description**: Street address line 1
**Constraints**:
  - required: true

---

### Column: Address Line 2
**ReuseComponent**: @Default:Address (Line 2)
**Description**: Apartment, suite, or unit number

---

### Column: City
**ReuseComponent**: @Cordova:City
**Description**: City of residence
**Constraints**:
  - required: true

---

### Column: Province
**ReuseComponent**: @Cordova:Province
**Description**: Province of residence
**Constraints**:
  - required: true

---

## Sub-Cluster: Contact Information

Phone, email, and preferred contact method for the person.

**Parent**: Civil Registry Record
**Purpose**: Enable government communication with the person

### Column: Phone Number
**ReuseComponent**: @Cordova:Cordova Phone Number
**Description**: Primary telephone number

---

### Column: Email Address
**ReuseComponent**: @Cordova:Cordova Email Address
**Description**: Primary email address

---

### Column: Preferred Contact Method
**ReuseComponent**: @NIH_CDE:Preferred Contact Method
**Description**: How the person prefers to be contacted

---

## Sub-Cluster: Family Relationships

Links between persons in the Civil Registry. Each relationship record connects two National IDs.

**Parent**: Civil Registry Record
**Purpose**: Record familial and legal relationships between persons
**Business Context**: Enables cross-person queries (family units, next of kin, guardianship)
**Rules**:
  - Relationship Start Date ≤ Relationship End Date

### Column: Related Person National ID
**ReuseComponent**: @Cordova:National ID (CID)
**Description**: The National ID (CID) of the related person
**Constraints**:
  - required: true

---

### Column: Relationship Type
**ReuseComponent**: @Cordova:Relationship Type
**Description**: The type of relationship to the related person (Spouse, Parent, Child, Sibling, Grandparent, Grandchild, Guardian)
**Constraints**:
  - required: true

---

### Column: Relationship Start Date
**Type**: xdtemporal
**Description**: Date the relationship was established or recorded (e.g., marriage date, birth date of child, guardianship order date)

---

### Column: Relationship End Date
**Type**: xdtemporal
**Description**: Date the relationship ended, if applicable (e.g., divorce date, death date). Null for active relationships.

---

## Governance Components

Components below are SDC4 Reference Model governance structures — Attestation, Participation, and Party — that wrap around the data clusters above.

### Attestation: Civil Registry Attestation

Formal governance attestation attached to this Data Model.

- **View**: Civil Registry Attested View (XdFile, `application/pdf`, content_mode=`url`) — attested document view
- **Proof**: Digital Signature Proof (XdFile, `application/pgp-signature` + `application/pkcs7-signature`, content_mode=`embed`) — shared cryptographic proof
- **Reason**: Civil Registry Attestation Reason (XdString, min_length=1, max_length=500) — free-text reason for attestation

---

### Party: Related Person

Person related to the civil registry subject via family relationship (parent, child, spouse, etc.). W3C PROV-DM Agent (Person) with Cordova CID.

### Party: Civil Registry Office

Government office responsible for civil registry records (births, marriages, deaths, name changes). W3C PROV-DM Agent (Organization).
