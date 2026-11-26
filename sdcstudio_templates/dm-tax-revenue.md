---
template_version: "4.0.0"
dataset:
  name: "Tax and Revenue Record"
  description: "Individual and business tax filings, port fees, property assessments, and fine collections for the Republic of Cordova — linking income, property, and commerce across domains"
  domain: "Government"
  creator: "Axius SDC"
  project: "Cordova"
enrichment:
  enable_llm: true
---

# Dataset Overview

Tax & Revenue is the financial nexus of Cordova. It collects and records individual income tax (linked to Employment), business tax (linked to Business Registry), property tax (linked to Property Registry), port fees (linked to Maritime), and fine collections (linked to Law Enforcement). Cross-domain SPARQL queries through this domain answer questions like: "Which businesses in Porto Sereno owe port fees and also have outstanding tax filings?"

**Purpose**: Record all tax filings, assessments, and revenue collection for Cordova.

**Business Context**:
- Primary use: Tax administration, revenue collection, fiscal reporting
- Secondary use: Cross-domain financial queries (income → employer → port fees → cargo)
- Stakeholders: Cordova Tax Authority, Ministry of Finance, taxpayers

**Standards Alignment**:
- SDC4 Reference Model (SDCRM)
- NIEM Core financial components
- W3C DPV 2.2 — `dpv:CollectTaxes`, `dpv:GovernmentalFinance`
- Legal Basis: `dpv:LegalObligation`

**Access Control**:
- Full: Tax Authority, Citizen (own records)
- Revenue totals: Port Authority (port fee reconciliation)
- Fine collection: Law Enforcement
- Provenance only: Auditor
- Hidden: Healthcare Provider, Employer/HR, Educational Institution

---

## Root Cluster: Tax Filing

A single tax filing for an individual or business.

**Purpose**: Document a tax filing with type, period, amounts, and payment status
**Business Context**: Links to Civil Registry (individual) or Business Registry (business)

### Column: Filing ID
**Type**: xdstring
**Description**: Unique identifier for this tax filing
**Constraints**:
  - required: true
  - max_length: 20

---

### Column: Taxpayer National ID
**ReuseComponent**: @Cordova:National ID (CID)
**Description**: National ID of the individual taxpayer. Null for business filings.

---

### Column: Taxpayer Business Registry Number
**ReuseComponent**: @Cordova:Business Registry Number
**Description**: Business Registry Number for business filings. Null for individual filings.

---

### Column: Filing Status
**ReuseComponent**: @Cordova:Tax Filing Status
**Description**: Filing type — Individual, Joint, Business, Estate
**Constraints**:
  - required: true

---

### Column: Tax Year
**Type**: xdcount
**Description**: Calendar year for this tax filing (e.g., 2025, 2026)
**Constraints**:
  - required: true

---

### Column: Tax Type
**Type**: xdtoken
**Description**: Category of tax being filed
**Enumeration**:
  - Income Tax: Individual or joint income tax
  - Business Tax: Corporate or business entity tax
  - Property Tax: Real property tax assessment
  - Port Fee: Maritime port service fees
  - Fine Collection: Collection of law enforcement fines
  - Import Duty: Customs duty on imported cargo
**Constraints**:
  - required: true

---

### Column: Filing Date
**Type**: xdtemporal
**Description**: Date the filing was submitted
**Constraints**:
  - required: true

---

## Sub-Cluster: Tax Assessment

Tax amounts assessed and due.

**Parent**: Tax Filing
**Purpose**: Record the financial details of the tax assessment

### Column: Gross Amount
**ReuseComponent**: @NIEM:Amount Value
**Description**: Total gross amount subject to tax (income, property value, cargo value, etc.)
**Constraints**:
  - required: true

---

### Column: Deductions
**ReuseComponent**: @NIEM:Amount Value
**Description**: Total deductions applied

---

### Column: Tax Owed
**ReuseComponent**: @NIEM:Amount Value
**Description**: Net tax amount owed after deductions and credits
**Constraints**:
  - required: true

---

## Sub-Cluster: Payment

Payment records for the tax filing.

**Parent**: Tax Filing
**Purpose**: Track payments against tax assessments

### Column: Payment Amount
**ReuseComponent**: @NIEM:Amount Value
**Description**: Amount paid
**Constraints**:
  - required: true

---

### Column: Payment Date
**Type**: xdtemporal
**Description**: Date payment was received
**Constraints**:
  - required: true

---

### Column: Payment Method
**Type**: xdtoken
**Description**: How the payment was made
**Enumeration**:
  - Bank Transfer: Electronic bank transfer
  - Check: Paper check
  - Cash: Cash payment at tax office
  - Payroll Deduction: Withheld from employer payroll
**Constraints**:
  - required: true

---

### Column: Payment Status
**Type**: xdtoken
**Description**: Current payment status
**Enumeration**:
  - Paid in Full: All amounts owed have been paid
  - Partial Payment: Some but not all amounts have been paid
  - Overdue: Payment is past due date
  - Payment Plan: Taxpayer is on an approved installment plan
  - Waived: Amount has been waived or forgiven
**Constraints**:
  - required: true

---

## Sub-Cluster: Source Reference

Links this tax filing to its originating domain record.

**Parent**: Tax Filing
**Purpose**: Trace the provenance of tax revenue back to the originating transaction
**Business Context**: Enables graph queries from tax revenue back to the source domain

### Column: Source Domain
**Type**: xdtoken
**Description**: The domain that generated this tax obligation
**Enumeration**:
  - Employment: Income from employment records
  - Business Registry: Business entity tax filing
  - Property Registry: Property tax from property records
  - Maritime: Port fees from port call records
  - Law Enforcement: Fine collection from incident dispositions
**Constraints**:
  - required: true

---

### Column: Source Record ID
**Type**: xdstring
**Description**: Identifier of the originating record in the source domain (e.g., Port Call ID, Parcel Number, Incident Report Number)
**Constraints**:
  - max_length: 30

---

## Governance Components

Components below are SDC4 Reference Model governance structures — Attestation, Participation, and Party — that wrap around the data clusters above.

### Attestation: Tax Record Attestation

Formal governance attestation attached to this Data Model.

- **View**: Tax Record Attested View (XdFile, `application/pdf`, content_mode=`url`) — attested document view
- **Proof**: Digital Signature Proof (XdFile, `application/pgp-signature` + `application/pkcs7-signature`, content_mode=`embed`) — shared cryptographic proof
- **Reason**: Tax Record Attestation Reason (XdString, min_length=1, max_length=500) — free-text reason for attestation

---

### Party: Taxpayer

Person or organization filing taxes. W3C PROV-DM Agent with Cordova CID (individual) and BRN (corporate) identifiers.

### Party: Tax Authority

Government tax and revenue authority responsible for tax collection and compliance. W3C PROV-DM Agent (Organization).
