---
template_version: "4.0.0"
dataset:
  name: "Employment Record"
  description: "Employment history and current positions for persons in the Republic of Cordova — employer, role, dates, and compensation linked to Civil Registry and Business Registry"
  domain: "Government"
  creator: "Axius SDC"
  project: "Cordova"
enrichment:
  enable_llm: true
---

# Dataset Overview

Employment records connect persons (Civil Registry) to businesses (Business Registry) through employment relationships. In the Contagion scenario, Elena Mendoza's employment at Universidad Nacional de Cordova in Campoluz is discovered through this domain — enabling contact tracing from the Maritime crew list to the university campus.

**Purpose**: Track employment relationships between persons and businesses in Cordova.

**Business Context**:
- Primary use: Government labor records, social security, workforce statistics
- Secondary use: Cross-domain identity enrichment (person → employer → location), contact tracing
- Stakeholders: Ministry of Labor, Tax Authority, employers, employees

**Standards Alignment**:
- SDC4 Reference Model (SDCRM)
- NIEM Core employment components
- W3C DPV 2.2 — `dpv:PersonnelManagement`, `dpv:SocialSecurityAdministration`
- Legal Basis: `dpv:LegalObligation`

**Access Control**:
- Full: Citizen (own records), Employer/HR (own staff)
- Employment verification: Civil Registrar, Law Enforcement
- Income data: Tax Authority
- Provenance only: Auditor
- Hidden: Healthcare Provider, Port Authority

---

## Root Cluster: Employment Record

A single employment relationship between a person and an employer.

**Purpose**: Document an employment position with dates, role, and compensation
**Business Context**: Links Civil Registry persons to Business Registry entities
**Rules**:
  - Start Date ≤ End Date

### Column: Employee National ID
**ReuseComponent**: @Cordova:National ID (CID)
**Description**: The employee's Cordova National ID, linking to Civil Registry
**Constraints**:
  - required: true

---

### Column: Employer Business Registry Number
**ReuseComponent**: @Cordova:Business Registry Number
**Description**: The employer's Cordova Business Registry Number, linking to Business Registry
**Constraints**:
  - required: true

---

### Column: Employer Name
**ReuseComponent**: @NIEM:Organization Name
**Description**: Name of the employing organization
**Constraints**:
  - required: true

---

### Column: Job Title
**ReuseComponent**: @NIEM:Job Title
**Description**: The employee's job title or position
**Constraints**:
  - required: true

---

### Column: Department
**Type**: xdstring
**Description**: Department or division within the employer organization
**Constraints**:
  - max_length: 200

---

### Column: Employment Status
**ReuseComponent**: @Cordova:Employment Status (Cordova)
**Description**: Current employment classification (Full-Time, Part-Time, Contract, Self-Employed, etc.)
**Constraints**:
  - required: true

---

### Column: Start Date
**Type**: xdtemporal
**Description**: Date employment began
**Constraints**:
  - required: true

---

### Column: End Date
**Type**: xdtemporal
**Description**: Date employment ended. Null for current positions.

---

### Column: Work Location City
**ReuseComponent**: @Cordova:City
**Description**: City where the employee primarily works

---

### Column: Work Location Province
**ReuseComponent**: @Cordova:Province
**Description**: Province where the employee primarily works

---

## Sub-Cluster: Compensation

Salary and benefits information. Restricted to Tax Authority and Employer/HR roles.

**Parent**: Employment Record
**Purpose**: Record compensation for tax reporting and labor statistics

### Column: Annual Salary
**Type**: xdcount
**Description**: Annual gross salary in Cordova Pesos. This cell carries restricted access — visible only to Tax Authority, Employer/HR, and the employee.
**Constraints**:
  - required: true

---

### Column: Pay Frequency
**Type**: xdtoken
**Description**: How often the employee is paid
**Enumeration**:
  - Monthly: Paid once per month
  - Bi-Weekly: Paid every two weeks
  - Weekly: Paid every week
**Constraints**:
  - required: true

---

### Column: Benefits Enrolled
**ReuseComponent**: @NIH_CDE:Yes/No
**Description**: Whether the employee is enrolled in employer-provided benefits

---

## Governance Components

Components below are SDC4 Reference Model governance structures — Attestation, Participation, and Party — that wrap around the data clusters above.

### Attestation: Employment Record Attestation

Formal governance attestation attached to this Data Model.

- **View**: Employment Record Attested View (XdFile, `application/pdf`, content_mode=`url`) — attested document view
- **Proof**: Digital Signature Proof (XdFile, `application/pgp-signature` + `application/pkcs7-signature`, content_mode=`embed`) — shared cryptographic proof
- **Reason**: Employment Record Attestation Reason (XdString, min_length=1, max_length=500) — free-text reason for attestation

---

### Party: Employer

Organization employing the person. W3C PROV-DM Agent (Organization) with Cordova BRN.

### Party: Employee

Person employed by an organization. W3C PROV-DM Agent (Person) with Cordova CID.
