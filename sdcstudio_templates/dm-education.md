---
template_version: "4.0.0"
dataset:
  name: "Education Record"
  description: "Student enrollment, academic programs, and credentials at educational institutions in the Republic of Cordova — linking persons to campuses for contact tracing and workforce qualification"
  domain: "Government"
  creator: "Axius SDC"
  project: "Cordova"
enrichment:
  enable_llm: true
---

# Dataset Overview

Education records connect persons to educational institutions. In the Contagion scenario, Elena Mendoza is a teacher at Universidad Nacional de Cordova in Campoluz — the contact tracing chain reaches the university campus through this domain combined with Employment. Students and staff at the campus can be identified through enrollment and employment records.

**Purpose**: Track student enrollment and academic credentials at Cordova educational institutions.

**Business Context**:
- Primary use: Ministry of Education enrollment management, credential verification
- Secondary use: Contact tracing (campus-level), workforce qualification verification
- Stakeholders: Ministry of Education, educational institutions, employers (credential verification)

**Standards Alignment**:
- SDC4 Reference Model (SDCRM)
- NIEM Core education components
- W3C DPV 2.2 — `dpv:AcademicResearch`, `dpv:ProvideEducation`
- Legal Basis: `dpv:LegalObligation`, `dpv:PublicInterest`

**Access Control**:
- Full: Citizen (own records), Educational Institution (own students)
- Credential verification: Employer/HR
- Enrollment data: Civil Registrar
- Provenance only: Auditor
- Hidden: Healthcare Provider, Port Authority, Tax Authority

---

## Root Cluster: Education Record

A student's enrollment or completed credential at an educational institution.

**Purpose**: Document academic enrollment, program, and credential attainment
**Business Context**: Links persons to campuses and academic programs

### Column: Student National ID
**ReuseComponent**: @Cordova:National ID (CID)
**Description**: The student's Cordova National ID, linking to Civil Registry
**Constraints**:
  - required: true

---

### Column: Student ID
**Type**: xdstring
**Description**: Institution-assigned student identifier
**Constraints**:
  - required: true
  - max_length: 20

---

### Column: Institution Name
**ReuseComponent**: @NIEM:Educational Institution
**Description**: Name of the educational institution
**Constraints**:
  - required: true

---

### Column: Institution City
**ReuseComponent**: @Cordova:City
**Description**: City where the institution is located
**Constraints**:
  - required: true

---

### Column: Institution Province
**ReuseComponent**: @Cordova:Province
**Description**: Province where the institution is located
**Constraints**:
  - required: true

---

### Column: Institution Type
**Type**: xdtoken
**Description**: Classification of the educational institution
**Enumeration**:
  - Primary School: Elementary / primary education (ages 6-12)
  - Secondary School: Middle and high school education (ages 12-18)
  - University: Four-year university or college
  - Technical Institute: Vocational or technical training institution
  - Graduate School: Post-graduate degree programs
**Constraints**:
  - required: true

---

## Sub-Cluster: Enrollment

Current or historical enrollment in an academic program.

**Parent**: Education Record
**Purpose**: Track enrollment period and program details
**Rules**:
  - Enrollment Date ≤ Expected Completion Date

### Column: Program Name
**ReuseComponent**: @NIEM:Field of Study
**Description**: Academic program or field of study (e.g., "Medicine", "Civil Engineering", "Marine Biology")
**Constraints**:
  - required: true

---

### Column: Enrollment Date
**Type**: xdtemporal
**Description**: Date the student enrolled in the program
**Constraints**:
  - required: true

---

### Column: Expected Completion Date
**Type**: xdtemporal
**Description**: Expected date of program completion

---

### Column: Enrollment Status
**Type**: xdtoken
**Description**: Current enrollment status
**Enumeration**:
  - Active: Currently enrolled and attending
  - Graduated: Successfully completed the program
  - Withdrawn: Voluntarily withdrew from the program
  - Suspended: Enrollment temporarily suspended
  - On Leave: Approved leave of absence
**Constraints**:
  - required: true

---

### Column: Education Level
**ReuseComponent**: @NIH_CDE:Education Level
**Description**: Level of education being pursued

---

## Sub-Cluster: Credential

Academic degree, diploma, or certificate earned.

**Parent**: Education Record
**Purpose**: Record awarded credentials for verification and workforce qualification

### Column: Credential Type
**Type**: xdtoken
**Description**: Type of academic credential awarded
**Enumeration**:
  - Primary Certificate: Primary school completion certificate
  - Secondary Diploma: Secondary school diploma
  - Associate Degree: Two-year associate degree
  - Bachelor's Degree: Four-year undergraduate degree
  - Master's Degree: Graduate-level master's degree
  - Doctoral Degree: Doctoral or PhD degree
  - Professional Certificate: Professional or vocational certification
**Constraints**:
  - required: true

---

### Column: Field of Study
**ReuseComponent**: @NIEM:Field of Study
**Description**: Major or field of study for the credential
**Constraints**:
  - required: true

---

### Column: Date Awarded
**Type**: xdtemporal
**Description**: Date the credential was officially awarded
**Constraints**:
  - required: true

---

### Column: Honors
**Type**: xdtoken
**Description**: Academic honors received, if any
**Enumeration**:
  - None: No honors designation
  - Cum Laude: With honors
  - Magna Cum Laude: With great honors
  - Summa Cum Laude: With highest honors

---

### Column: Credential Verified
**ReuseComponent**: @NIH_CDE:Yes/No
**Description**: Whether the credential has been independently verified

---

## Governance Components

Components below are SDC4 Reference Model governance structures — Attestation, Participation, and Party — that wrap around the data clusters above.

### Attestation: Education Record Attestation

Formal governance attestation attached to this Data Model.

- **View**: Education Record Attested View (XdFile, `application/pdf`, content_mode=`url`) — attested document view
- **Proof**: Digital Signature Proof (XdFile, `application/pgp-signature` + `application/pkcs7-signature`, content_mode=`embed`) — shared cryptographic proof
- **Reason**: Education Record Attestation Reason (XdString, min_length=1, max_length=500) — free-text reason for attestation

---

### Party: Educational Institution

Educational institution (university, college, school, etc.) granting credentials. W3C PROV-DM Agent (Organization) with Cordova institution classification.

### Party: Student

Person enrolled in an educational program. W3C PROV-DM Agent (Person) with Cordova CID.
