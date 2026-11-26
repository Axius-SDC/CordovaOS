---
template_version: "4.0.0"
dataset:
  name: "Property Registry"
  description: "Land and property ownership, transfers, liens, and assessed values for the Republic of Cordova — linking parcels to persons, businesses, and tax assessments across domains"
  domain: "Government"
  creator: "Axius SDC"
  project: "Cordova"
enrichment:
  enable_llm: true
---

# Dataset Overview

The Property Registry records every land parcel and property in Cordova. Ownership can be a person (Civil Registry) or a business (Business Registry) — both are valid owner types because they share the same Reference Model structure. Transfer records demonstrate full provenance chains with Attestation (notary). Property assessments link directly to Tax & Revenue for property tax filings.

**Purpose**: Maintain the authoritative registry of land and property ownership in Cordova.

**Business Context**:
- Primary use: Land registration, title verification, property transfers
- Secondary use: Property tax assessment, lien management, economic analysis
- Stakeholders: National Land Registry, Tax Authority, property owners, notaries

**Standards Alignment**:
- SDC4 Reference Model (SDCRM)
- NIEM Core property components
- W3C DPV 2.2 — `dpv:LandRegistration`, `dpv:GovernmentalFinance`
- Legal Basis: `dpv:LegalObligation`

**Access Control**:
- Full: Property Owner, Tax Authority
- Public info (parcel, location, type): All roles
- Financial details (assessed value, liens): Tax Authority, Property Owner
- Provenance only: Auditor
- Hidden: Healthcare Provider

---

## Root Cluster: Property Record

A registered land parcel or property in Cordova.

**Purpose**: Document a property with location, type, and current ownership
**Business Context**: Links to Civil Registry (person owners) and Business Registry (business owners)

### Column: Parcel Number
**ReuseComponent**: @Cordova:Parcel Number
**Description**: Unique land registry identifier for this property
**Constraints**:
  - required: true

---

### Column: Property Type
**ReuseComponent**: @Cordova:Property Type (Cordova)
**Description**: Classification — Residential, Commercial, Agricultural, Government
**Constraints**:
  - required: true

---

### Column: Street Address
**ReuseComponent**: @Default:Address (Line 1)
**Description**: Street address of the property
**Constraints**:
  - required: true

---

### Column: Address Line 2
**ReuseComponent**: @Default:Address (Line 2)
**Description**: Unit, suite, or lot number

---

### Column: City
**ReuseComponent**: @Cordova:City
**Description**: City where the property is located
**Constraints**:
  - required: true

---

### Column: Province
**ReuseComponent**: @Cordova:Province
**Description**: Province where the property is located
**Constraints**:
  - required: true

---

### Column: Property Status
**Type**: xdtoken
**Description**: Current status of the property in the registry
**Enumeration**:
  - Active: Property is registered and in good standing
  - Encumbered: Property has outstanding liens or encumbrances
  - In Transfer: Ownership transfer in progress
  - Government Seized: Property seized by government authority
  - Abandoned: Property declared abandoned
**Constraints**:
  - required: true

---

### Column: Registration Date
**Type**: xdtemporal
**Description**: Date the property was first registered in the land registry
**Constraints**:
  - required: true

---

### Column: Land Area
**Type**: xdquantity
**Description**: Total land area of the property in square meters
**Constraints**:
  - required: true

---

## Sub-Cluster: Current Ownership

Current owner(s) of the property. Owner can be a person or a business entity.

**Parent**: Property Record
**Purpose**: Record current property ownership with link to Civil Registry or Business Registry
**Business Context**: Demonstrates flexible ownership — same Reference Model supports person and business owners
**Rules**:
  - At least one of Owner National ID or Owner Business Registry Number must be present

### Column: Owner National ID
**ReuseComponent**: @Cordova:National ID (CID)
**Description**: National ID of the individual owner. Null for business-owned properties.

---

### Column: Owner Business Registry Number
**ReuseComponent**: @Cordova:Business Registry Number
**Description**: Business Registry Number for business-owned properties. Null for individual owners.

---

### Column: Owner Name
**ReuseComponent**: @NIEM:Person Full Name
**Description**: Full name of the individual or business entity that owns the property
**Constraints**:
  - required: true

---

### Column: Ownership Type
**Type**: xdtoken
**Description**: How the property is owned
**Enumeration**:
  - Sole Owner: Single individual or entity owns the property
  - Joint Owners: Two or more individuals share ownership
  - Business Entity: Owned by a registered business
  - Government: Owned by a government entity
  - Trust: Held in trust
**Constraints**:
  - required: true

---

### Column: Ownership Start Date
**Type**: xdtemporal
**Description**: Date current ownership began
**Constraints**:
  - required: true

---

## Sub-Cluster: Transfer History

Record of property ownership transfers with notary attestation.

**Parent**: Property Record
**Purpose**: Document the provenance chain of property ownership changes
**Business Context**: Demonstrates full Attestation — notary-attested transfers with buyer, seller, and price

### Column: Transfer Date
**Type**: xdtemporal
**Description**: Date the transfer was executed
**Constraints**:
  - required: true

---

### Column: Seller National ID
**ReuseComponent**: @Cordova:National ID (CID)
**Description**: National ID of the selling individual. Null for business sellers.

---

### Column: Seller Business Registry Number
**ReuseComponent**: @Cordova:Business Registry Number
**Description**: Business Registry Number of the selling business. Null for individual sellers.

---

### Column: Buyer National ID
**ReuseComponent**: @Cordova:National ID (CID)
**Description**: National ID of the buying individual. Null for business buyers.

---

### Column: Buyer Business Registry Number
**ReuseComponent**: @Cordova:Business Registry Number
**Description**: Business Registry Number of the buying business. Null for individual buyers.

---

### Column: Transfer Price
**ReuseComponent**: @NIEM:Amount Value
**Description**: Sale price of the property in Cordova Pesos
**Constraints**:
  - required: true

---

### Column: Notary Name
**ReuseComponent**: @NIEM:Person Full Name
**Description**: Name of the notary who attested the transfer
**Constraints**:
  - required: true

---

### Column: Notary Registration Number
**Type**: xdstring
**Description**: Official registration number of the attesting notary
**Constraints**:
  - required: true
  - max_length: 20

---

## Sub-Cluster: Property Value Assessment

Property value assessment for tax purposes.

**Parent**: Property Record
**Purpose**: Record assessed values that link to Tax & Revenue for property tax filings

### Column: Assessment Year
**Type**: xdcount
**Description**: Calendar year of the assessment
**Constraints**:
  - required: true

---

### Column: Assessed Land Value
**ReuseComponent**: @NIEM:Amount Value
**Description**: Assessed value of the land only
**Constraints**:
  - required: true

---

### Column: Assessed Improvement Value
**ReuseComponent**: @NIEM:Amount Value
**Description**: Assessed value of structures and improvements on the land

---

### Column: Total Assessed Value
**ReuseComponent**: @NIEM:Amount Value
**Description**: Total assessed value (land + improvements) used for property tax calculation
**Constraints**:
  - required: true

---

### Column: Assessment Status
**Type**: xdtoken
**Description**: Status of the assessment
**Enumeration**:
  - Final: Assessment is finalized and accepted
  - Under Appeal: Property owner has appealed the assessment
  - Preliminary: Initial assessment pending review
**Constraints**:
  - required: true

---

## Sub-Cluster: Liens and Encumbrances

Outstanding liens, mortgages, or legal encumbrances on the property.

**Parent**: Property Record
**Purpose**: Record financial and legal claims against the property

### Column: Lien Type
**Type**: xdtoken
**Description**: Type of lien or encumbrance
**Enumeration**:
  - Mortgage: Bank or financial institution mortgage
  - Tax Lien: Government lien for unpaid taxes
  - Judgment Lien: Court-ordered lien from legal judgment
  - Mechanic's Lien: Lien for unpaid construction or repair work
  - Easement: Legal right of way or use restriction
**Constraints**:
  - required: true

---

### Column: Lien Holder
**Type**: xdstring
**Description**: Name of the entity holding the lien
**Constraints**:
  - required: true
  - max_length: 200

---

### Column: Lien Amount
**ReuseComponent**: @NIEM:Amount Value
**Description**: Outstanding amount of the lien in Cordova Pesos

---

### Column: Lien Date
**Type**: xdtemporal
**Description**: Date the lien was recorded
**Constraints**:
  - required: true

---

### Column: Lien Status
**Type**: xdtoken
**Description**: Current status of the lien
**Enumeration**:
  - Active: Lien is currently in effect
  - Satisfied: Lien has been fully paid or resolved
  - Released: Lien has been formally released
**Constraints**:
  - required: true

---

## Governance Components

Components below are SDC4 Reference Model governance structures — Attestation, Participation, and Party — that wrap around the data clusters above.

### Attestation: Property Registry Attestation

Formal governance attestation attached to this Data Model.

- **View**: Property Registry Attested View (XdFile, `application/pdf`, content_mode=`url`) — attested document view
- **Proof**: Digital Signature Proof (XdFile, `application/pgp-signature` + `application/pkcs7-signature`, content_mode=`embed`) — shared cryptographic proof
- **Reason**: Property Registry Attestation Reason (XdString, min_length=1, max_length=500) — free-text reason for attestation

---

### Participation: Transfer Participation

Participation of parties in property ownership transfers.

**Function** (Transfer Party Participation Function):
  - Buyer
  - Seller
  - Notary
  - Witness
  - Other

**Mode** (Transfer Party Participation Mode):
  - In Person
  - By Proxy
  - Electronic Filing
  - By Mail
  - Other

---

### Participation: Lien Holder Participation

Participation of the entity holding a lien on property.

**Function** (Lien Holder Participation Function):
  - Mortgage Holder
  - Tax Lien Authority
  - Judgment Creditor
  - Other

**Mode** (Lien Holder Participation Mode):
  - Electronic Filing
  - By Mail
  - In Person
  - Other

---

### Party: Property Owner

Person or organization that owns a property. W3C PROV-DM Agent with ownership type and start date. Supports both CID (individual) and BRN (corporate) identifiers.

### Party: Transfer Party

Person or organization participating in a property transfer (buyer, seller, or notary). W3C PROV-DM Agent with Cordova national identifiers.

### Party: Lien Holder

Person or organization holding a lien on a property. W3C PROV-DM Agent.

### Party: Property Registry Office

Government office responsible for property records, land titles, and transfer registration. W3C PROV-DM Agent (Organization).
