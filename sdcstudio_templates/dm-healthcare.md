---
template_version: "4.0.0"
dataset:
  name: "Healthcare Record"
  description: "Basic medical records for persons in the Republic of Cordova — provider assignments, conditions, medications, vaccinations, visits, vitals, and lab results with Restricted:PatientCare access policy"
  domain: "Healthcare"
  creator: "Axius SDC"
  project: "Cordova"
enrichment:
  enable_llm: true
---

# Dataset Overview

Healthcare records in Cordova carry `Restricted:PatientCare` access policy on all clinical cells. This is where the Data Physics proof point becomes visceral: a Healthcare Provider can see clinical data, but if they attempt to compose a restricted cell into a public context, the schema rejects the composition. The failure produces an ExceptionalValue object — structured, governed, and auditable.

In the Contagion scenario, Carlos Mendoza's medical record is created here when he presents at Porto Sereno General Hospital. His diagnosis is visible to the Healthcare Provider role but **redacted** for the Auditor and all other roles. The Auditor can see that a medical record exists, who created it, and when — but not the clinical content.

**Purpose**: Maintain basic medical records for all persons in Cordova.

**Business Context**:
- Primary use: Patient care and clinical documentation
- Secondary use: ExceptionalValue demonstration (out-of-range lab values), privacy constraint demonstration (Restricted:PatientCare)
- Stakeholders: Healthcare providers, patients, public health authority

**Standards Alignment**:
- NIH Common Data Elements (CDE) — reuses vital signs, demographics, and clinical components
- SDC4 Reference Model (SDCRM) — ExceptionalValue handling for out-of-range results
- W3C DPV 2.2 — `dpv:ImproveHealthcare`, `dpv:ProvideHealthcare`
- Legal Basis: `dpv:LegalObligation`, `dpv:Consent`

**Access Control**:
- Full: Healthcare Provider, Citizen (own records)
- Provenance only: Auditor (can see record exists, who created it, when — not clinical content)
- Hidden: All other roles (Law Enforcement, Tax, Port Authority, Civil Registrar, Employer/HR)

---

## Root Cluster: Patient Record

A person's medical record in the Cordova healthcare system.

**Purpose**: Comprehensive medical record for a Cordova resident
**Business Context**: Links to Civil Registry via National ID. All clinical cells carry Restricted:PatientCare policy.

### Column: Patient National ID
**ReuseComponent**: @Cordova:National ID (CID)
**Description**: The patient's Cordova National ID, linking this record to the Civil Registry
**Constraints**:
  - required: true

---

### Column: Medical Record Number
**ReuseComponent**: @NIH_CDE:Medical Record Number
**Description**: Internal medical record number assigned by the healthcare facility
**Constraints**:
  - required: true

---

### Column: Primary Care Provider
**Type**: xdstring
**Description**: Name of the patient's assigned primary care physician
**Constraints**:
  - max_length: 200

---

### Column: Primary Care Facility
**Type**: xdtoken
**Description**: Healthcare facility where the patient receives primary care
**Enumeration**:
  - Porto Sereno General Hospital: Main hospital in Porto Sereno, Aldara
  - Vistamar Medical Clinic: Clinic in Vistamar, Aldara
  - Rioseco Health Center: Health center in Rioseco, Aldara
  - Campoluz University Hospital: Teaching hospital at Universidad Nacional de Cordova, Brevina
  - Tierraverde Rural Clinic: Rural clinic in Tierraverde, Brevina
  - Montecara Community Health: Community health center in Montecara, Brevina
  - Novaciudad Central Hospital: National capital hospital in Novaciudad, Celara
  - Piedrasol Medical Center: Medical center in Piedrasol, Celara
  - Lagunavista Health Clinic: Clinic in Lagunavista, Celara

---

## Sub-Cluster: Allergies and Conditions

Known allergies and chronic conditions.

**Parent**: Patient Record
**Purpose**: Document allergies and ongoing medical conditions for clinical decision-making

### Column: Allergy Description
**Type**: xdstring
**Description**: Description of a known allergy (drug, food, environmental)
**Constraints**:
  - max_length: 300

---

### Column: Allergy Severity
**ReuseComponent**: @NIH_CDE:Severity (3-Point)
**Description**: Severity of allergic reaction — Mild, Moderate, Severe

---

### Column: Chronic Condition
**Type**: xdstring
**Description**: Name or description of a chronic medical condition (e.g., hypertension, diabetes, asthma)
**Constraints**:
  - max_length: 300

---

### Column: Condition Onset Date
**ReuseComponent**: @NIH_CDE:Onset Date
**Description**: Date the condition was first diagnosed or recognized

---

### Column: Condition Status
**Type**: xdtoken
**Description**: Current status of the condition
**Enumeration**:
  - Active: Condition is currently being managed
  - Resolved: Condition has resolved
  - In Remission: Condition is in remission but may recur
**Constraints**:
  - required: true

---

## Sub-Cluster: Medications

Current medication list.

**Parent**: Patient Record
**Purpose**: Track active medications for drug interaction checking and care coordination

### Column: Medication Name
**Type**: xdstring
**Description**: Name of the prescribed medication (generic or brand name)
**Constraints**:
  - required: true
  - max_length: 200

---

### Column: Dosage
**Type**: xdstring
**Description**: Prescribed dosage (e.g., "500mg", "10mg/mL")
**Constraints**:
  - max_length: 100

---

### Column: Frequency
**ReuseComponent**: @NIH_CDE:Frequency (5-Point)
**Description**: How often the medication is taken

---

### Column: Prescriber
**Type**: xdstring
**Description**: Name of the prescribing physician
**Constraints**:
  - max_length: 200

---

### Column: Prescription Date
**Type**: xdtemporal
**Description**: Date the medication was prescribed
**Constraints**:
  - required: true

---

## Sub-Cluster: Vaccination History

Immunization records.

**Parent**: Patient Record
**Purpose**: Track vaccinations for public health compliance and clinical reference

### Column: Vaccine Name
**Type**: xdstring
**Description**: Name of the vaccine administered
**Constraints**:
  - required: true
  - max_length: 200

---

### Column: Vaccine Date
**Type**: xdtemporal
**Description**: Date the vaccine was administered
**Constraints**:
  - required: true

---

### Column: Administering Facility
**Type**: xdstring
**Description**: Healthcare facility where the vaccine was given
**Constraints**:
  - max_length: 200

---

### Column: Dose Number
**ReuseComponent**: @NIH_CDE:Visit Number
**Description**: Dose number in a multi-dose series (e.g., 1 of 2, 2 of 2)

---

### Column: Lot Number
**Type**: xdstring
**Description**: Vaccine lot number for traceability
**Constraints**:
  - max_length: 50

---

## Sub-Cluster: Visit Record

An encounter at a healthcare facility.

**Parent**: Patient Record
**Purpose**: Document each clinical encounter with date, provider, reason, diagnosis, and outcome
**Business Context**: Visit records link to the Contagion scenario — Carlos Mendoza's admission to Porto Sereno General Hospital

### Column: Visit Date
**ReuseComponent**: @NIH_CDE:Visit Date
**Description**: Date of the clinical encounter
**Constraints**:
  - required: true

---

### Column: Visit Type
**ReuseComponent**: @NIH_CDE:Visit Type
**Description**: Type of visit — routine, urgent, emergency, follow-up, screening

---

### Column: Provider Name
**Type**: xdstring
**Description**: Name of the attending physician or provider
**Constraints**:
  - required: true
  - max_length: 200

---

### Column: Facility
**Type**: xdstring
**Description**: Healthcare facility where the visit occurred
**Constraints**:
  - required: true
  - max_length: 200

---

### Column: Reason for Visit
**Type**: xdstring
**Description**: Chief complaint or reason for the clinical encounter
**Constraints**:
  - required: true
  - max_length: 500

---

### Column: Diagnosis
**Type**: xdstring
**Description**: Clinical diagnosis resulting from this visit. This cell carries Restricted:PatientCare policy — it cannot be composed into public reports.
**Constraints**:
  - max_length: 500

---

### Column: Outcome
**Type**: xdtoken
**Description**: Outcome of the visit
**Enumeration**:
  - Treated and Released: Patient treated and released same day
  - Admitted: Patient admitted for inpatient care
  - Referred: Patient referred to specialist or another facility
  - Follow-up Scheduled: Patient to return for follow-up visit
  - No Treatment Required: Observation only, no treatment needed
**Constraints**:
  - required: true

---

### Column: Clinical Impression
**ReuseComponent**: @NIH_CDE:Clinical Impression
**Description**: Provider's overall clinical assessment

---

## Vital Signs (within Visit Record)

Vital signs measured during a clinical encounter. These components are part of the Visit Record cluster (not a separate sub-cluster in the model).

**Purpose**: Record standard vital sign measurements
**Business Context**: Demonstrates reuse of NIH CDE vital sign components — same components used in NIH research forms are used in Cordova clinical records
**Rules**:
  - Systolic Blood Pressure > Diastolic Blood Pressure (when both present)

### Column: Systolic Blood Pressure
**ReuseComponent**: @NIH_CDE:Systolic Blood Pressure
**Description**: Systolic blood pressure in mmHg

---

### Column: Diastolic Blood Pressure
**ReuseComponent**: @NIH_CDE:Diastolic Blood Pressure
**Description**: Diastolic blood pressure in mmHg

---

### Column: Heart Rate
**ReuseComponent**: @NIH_CDE:Heart Rate
**Description**: Heart rate in beats per minute

---

### Column: Respiratory Rate
**ReuseComponent**: @NIH_CDE:Respiratory Rate
**Description**: Respiratory rate in breaths per minute

---

### Column: Temperature (Celsius)
**ReuseComponent**: @NIH_CDE:Temperature (Celsius)
**Description**: Body temperature in degrees Celsius

---

### Column: Oxygen Saturation
**ReuseComponent**: @NIH_CDE:Oxygen Saturation
**Description**: Blood oxygen saturation percentage (SpO2)

---

### Column: Height (cm)
**ReuseComponent**: @NIH_CDE:Height (cm)
**Description**: Patient height in centimeters

---

### Column: Weight (kg)
**ReuseComponent**: @NIH_CDE:Weight (kg)
**Description**: Patient weight in kilograms

---

### Column: BMI
**ReuseComponent**: @NIH_CDE:BMI
**Description**: Calculated Body Mass Index

---

## Lab Results (within Visit Record)

Basic laboratory test results. Out-of-range values demonstrate ExceptionalValue handling. These components are part of the Visit Record cluster (not a separate sub-cluster in the model).

**Purpose**: Record laboratory test results with reference range validation
**Business Context**: Lab results with values outside reference ranges produce ExceptionalValue objects — structured, governed records of the anomaly rather than silent data loss

### Column: Test Name
**Type**: xdstring
**Description**: Name of the laboratory test performed
**Constraints**:
  - required: true
  - max_length: 200

---

### Column: Test Date
**Type**: xdtemporal
**Description**: Date the lab test was performed
**Constraints**:
  - required: true

---

### Column: Result Value
**Type**: xdstring
**Description**: The test result value. If this value falls outside the reference range, the system generates an ExceptionalValue object containing the out-of-range value, the validation error, and the clinical context — preserving the data for review rather than discarding it.
**Constraints**:
  - required: true
  - max_length: 100

---

### Column: Result Units
**Type**: xdstring
**Description**: Unit of measurement for the result (e.g., mg/dL, mmol/L, cells/uL)
**Constraints**:
  - max_length: 50

---

### Column: Reference Range Low
**Type**: xdstring
**Description**: Lower bound of the normal reference range
**Constraints**:
  - max_length: 50

---

### Column: Reference Range High
**Type**: xdstring
**Description**: Upper bound of the normal reference range
**Constraints**:
  - max_length: 50

---

### Column: Abnormal Flag
**ReuseComponent**: @NIH_CDE:Data Quality Flag
**Description**: Whether the result is flagged as abnormal (outside reference range). Abnormal results trigger ExceptionalValue processing.

---

### Column: Blood Type
**Type**: xdtoken
**Description**: ABO blood type and Rh factor. Recorded once per patient.
**Enumeration**:
  - A+: A positive
  - A-: A negative
  - B+: B positive
  - B-: B negative
  - AB+: AB positive
  - AB-: AB negative
  - O+: O positive
  - O-: O negative

---

## Governance Components

Components below are SDC4 Reference Model governance structures — Attestation, Participation, and Party — that wrap around the data clusters above.

### Attestation: Healthcare Record Attestation

Formal governance attestation attached to this Data Model.

- **View**: Healthcare Record Attested View (XdFile, `application/pdf`, content_mode=`url`) — attested document view
- **Proof**: Digital Signature Proof (XdFile, `application/pgp-signature` + `application/pkcs7-signature`, content_mode=`embed`) — shared cryptographic proof
- **Reason**: Healthcare Record Attestation Reason (XdString, min_length=1, max_length=500) — free-text reason for attestation

---

### Participation: Prescriber Participation

Participation of the prescribing physician.

**Function** (Prescriber Participation Function):
  - Attending Physician
  - Consulting Physician
  - Resident
  - Nurse Practitioner
  - Other

**Mode** (Prescriber Participation Mode):
  - In Person
  - Telehealth
  - Electronic Order
  - By Telephone
  - Other

---

### Participation: Vaccination Facility Participation

Participation of the facility administering vaccinations.

**Function** (Vaccination Facility Participation Function):
  - Administering Site
  - Storage Facility
  - Distribution Center
  - Other

**Mode** (Vaccination Facility Participation Mode):
  - In Person
  - Mobile Clinic
  - Drive-Through
  - Other

---

### Party: Healthcare Provider

Healthcare provider (facility and/or clinician) delivering care. W3C PROV-DM Agent supporting both Person and Organization types.

### Party: Prescriber

Physician who prescribed medication. W3C PROV-DM Agent (Person).

### Party: Administering Facility

Healthcare facility that administered a vaccination. W3C PROV-DM Agent (Organization).

### Party: Primary Care Assignment

Patient's assigned primary care provider and facility. W3C PROV-DM Agent supporting Person (clinician) and Organization (facility).
