---
template_version: "4.0.0"
dataset:
  name: "Cordova National Components Bundle"
  description: "Republic of Cordova-specific data components for national identifiers, geography, and administrative codes"
  domain: "Government"
  creator: "Axius SDC"
  project: "Cordova"
enrichment:
  enable_llm: true
---

# Dataset Overview

This bundle contains components specific to the Republic of Cordova — a fictional island nation used to demonstrate cross-domain SDC interoperability. These components define national identifiers, geographic codes, and administrative structures unique to Cordova.

**Purpose**: Provide Cordova-specific reusable components that are referenced by all 10 domain Data Models in the Cordova OS demo.

**Business Context**:
- Primary use: National identity, geographic, and administrative components for Cordova demo
- Secondary use: Demonstrate how domain-specific components compose with generic components from Default, NIEM, NIH_CDE, and ProvGov projects
- Stakeholders: Demo audience, investors, SDCStudio evaluation users

**Standards Alignment**:
- SDC4 Reference Model (SDCRM) for structural compliance
- W3C Data Privacy Vocabulary (DPV) 2.2 for access control tagging
- ISO 3166 pattern for national identifier formatting

---

## Root Cluster: Cordova National Components

This cluster contains all Cordova-specific components. After processing, the wrapper data model should be deleted, leaving the individual components available for reuse across all Cordova domain Data Models.

**Purpose**: Container for Cordova national components
**Business Context**: Foundation bundle - components persist after wrapper deletion

---

### Column: National ID (CID)
**Type**: xdstring
**Description**: Cordova National Identity Number. Format: COR-PPCC-NNNNNN where PP is the two-letter province code (AL=Aldara, BR=Brevina, CE=Celara), CC is the two-digit city code (01-03), and NNNNNN is a six-digit sequence number. Issued at birth or naturalization. Required for all government transactions.
**Constraints**:
  - required: true
  - pattern: "COR-[A-Z]{2}[0-9]{2}-[0-9]{6}"
  - max_length: 16
**Examples**: COR-AL01-384721, COR-BR02-001582, COR-CE01-927364

---

### Column: Business Registry Number
**Type**: xdstring
**Description**: Cordova Business Registration Number. Format: BIZ-NNNNNN where NNNNNN is a six-digit sequence number assigned at incorporation. Required for all business filings, tax records, and port authority transactions.
**Constraints**:
  - required: true
  - pattern: "BIZ-[0-9]{6}"
  - max_length: 10
**Examples**: BIZ-001234, BIZ-000017, BIZ-004891

---

### Column: Cordova Phone Number
**Type**: xdstring
**Description**: Cordova national telephone number. Format: +99-PPP-NNN-NNNN where +99 is the country code and PPP is the area code. Area codes: Porto Sereno=100, Vistamar=110, Rioseco=120, Campoluz=200, Tierraverde=210, Montecara=220, Novaciudad=300, Piedrasol=310, Lagunavista=320.
**Constraints**:
  - pattern: "\\+99-[0-9]{3}-[0-9]{3}-[0-9]{4}"
  - max_length: 16
**Examples**: +99-100-555-1234, +99-300-201-8765, +99-200-433-5512

---

### Column: Province
**Type**: xdtoken
**Description**: One of the three provinces of the Republic of Cordova. Used across civil registry, property, tax, and all geographic records.
**Enumeration**:
  - Aldara: Western province. Capital: Porto Sereno. Contains the national port and coastal cities Vistamar and Rioseco.
  - Brevina: Central province. Capital: Campoluz. Agricultural and university region with Tierraverde and Montecara.
  - Celara: Eastern province. Capital: Novaciudad. National capital province and government center with Piedrasol and Lagunavista.
**Examples**: Aldara, Brevina, Celara

---

### Column: City
**Type**: xdtoken
**Description**: One of the nine cities in the Republic of Cordova.
**Enumeration**:
  - Porto Sereno: Capital of Aldara. National port city and sole international port. Area code 100.
  - Vistamar: Coastal city in Aldara. Area code 110.
  - Rioseco: River city in Aldara. Area code 120.
  - Campoluz: Capital of Brevina. Home to Universidad Nacional de Cordova. Area code 200.
  - Tierraverde: Agricultural town in Brevina. Area code 210.
  - Montecara: Mountain town in Brevina. Area code 220.
  - Novaciudad: Capital of Celara and national capital. Government center. Area code 300.
  - Piedrasol: City in Celara. Area code 310.
  - Lagunavista: Lakeside city in Celara. Area code 320.
**Examples**: Porto Sereno, Novaciudad, Campoluz

---

### Column: Area Code
**Type**: xdtoken
**Description**: Cordova telephone area code corresponding to one of the nine cities.
**Enumeration**:
  - "100": Porto Sereno
  - "110": Vistamar
  - "120": Rioseco
  - "200": Campoluz
  - "210": Tierraverde
  - "220": Montecara
  - "300": Novaciudad
  - "310": Piedrasol
  - "320": Lagunavista
**Examples**: 100, 200, 300

---

### Column: Province Code
**Type**: xdtoken
**Description**: Two-letter abbreviation for Cordova provinces, used in the National ID (CID) format.
**Enumeration**:
  - AL: Aldara
  - BR: Brevina
  - CE: Celara
**Examples**: AL, BR, CE

---

### Column: City Code
**Type**: xdtoken
**Description**: Two-digit city code within a province, used in the National ID (CID) format. 01 = provincial capital, 02 and 03 = other cities.
**Enumeration**:
  - "01": Provincial capital (Porto Sereno, Campoluz, or Novaciudad)
  - "02": Second city (Vistamar, Tierraverde, or Piedrasol)
  - "03": Third city (Rioseco, Montecara, or Lagunavista)
**Examples**: 01, 02, 03

---

### Column: Cordova Email Address
**Type**: xdstring
**Description**: Email address using one of the Cordova national email providers. Providers: cordomail.co, novamail.co, portocorreo.co
**Constraints**:
  - max_length: 100
**Examples**: carlos.mendoza@cordomail.co, elena.mendoza@novamail.co, portmaster@portocorreo.co

---

### Column: Relationship Type
**Type**: xdtoken
**Description**: Familial or legal relationship between two persons in the Cordova Civil Registry.
**Enumeration**:
  - Spouse: Married partner
  - Parent: Biological or adoptive parent
  - Child: Biological or adopted child
  - Sibling: Brother or sister (biological, half, or adoptive)
  - Grandparent: Paternal or maternal grandparent
  - Grandchild: Child of one's child
  - Guardian: Legal guardian (non-parent)
**Examples**: Spouse, Parent, Child, Sibling

---

### Column: Marital Status (Cordova)
**Type**: xdtoken
**Description**: Marital status as recorded in the Cordova Civil Registry. Aligned with vital statistics records.
**Enumeration**:
  - Single: Never married
  - Married: Currently in a legal marriage
  - Divorced: Marriage legally dissolved
  - Widowed: Spouse deceased
  - Separated: Legally separated but not divorced
**Examples**: Single, Married, Divorced

---

### Column: Property Type (Cordova)
**Type**: xdtoken
**Description**: Classification of real property in the Cordova Property Registry.
**Enumeration**:
  - Residential: Single-family home, apartment, or multi-family dwelling
  - Commercial: Office, retail, warehouse, or mixed-use commercial property
  - Agricultural: Farmland, ranch, or agricultural production facility
  - Government: Government-owned buildings, facilities, and land
  - Industrial: Manufacturing, processing, or industrial facility
**Examples**: Residential, Commercial, Agricultural

---

### Column: Tax Filing Status
**Type**: xdtoken
**Description**: Filing status for annual Cordova tax returns.
**Enumeration**:
  - Individual: Single person filing
  - Joint: Married couple filing jointly
  - Business: Business entity filing (sole proprietor, partnership, corporation)
  - Estate: Estate or trust filing
**Examples**: Individual, Joint, Business

---

### Column: Business Type (Cordova)
**Type**: xdtoken
**Description**: Legal structure of a business entity in the Cordova Business Registry.
**Enumeration**:
  - Sole Proprietor: Single-owner business
  - Partnership: Two or more owners
  - Corporation: Incorporated entity with shareholders
  - Cooperative: Member-owned cooperative enterprise
**Examples**: Sole Proprietor, Corporation, Cooperative

---

### Column: Employment Status (Cordova)
**Type**: xdtoken
**Description**: Employment classification in Cordova employment records.
**Enumeration**:
  - Full-Time: 40+ hours per week, permanent position
  - Part-Time: Less than 40 hours per week
  - Contract: Fixed-term or project-based employment
  - Self-Employed: Independent business owner or freelancer
  - Unemployed: Not currently employed, seeking work
  - Retired: No longer in active employment
  - Student: Full-time student, may have part-time work
**Examples**: Full-Time, Part-Time, Self-Employed

---

### Column: Parcel Number
**Type**: xdstring
**Description**: Cordova property parcel identifier. Format: PP-CC-NNNNNN where PP is the province code, CC is the city code, and NNNNNN is a parcel sequence number.
**Constraints**:
  - pattern: "[A-Z]{2}-[0-9]{2}-[0-9]{6}"
  - max_length: 12
**Examples**: AL-01-000142, CE-01-003891, BR-02-000017

---

### Column: Charge Category (Cordova)
**Type**: xdtoken
**Description**: Categories of misdemeanor offenses in Cordova law enforcement records. Cordova has no felony classification — all criminal matters are misdemeanor-level.
**Enumeration**:
  - Petty Theft: Theft of property valued under 500 pesos
  - Public Intoxication: Intoxication in a public space causing disturbance
  - Trespassing: Unauthorized entry onto private or restricted property
  - Disorderly Conduct: Behavior that disturbs public peace
  - Traffic Violation: Moving or parking violations
  - Minor Vandalism: Damage to property valued under 500 pesos
**Examples**: Petty Theft, Traffic Violation, Disorderly Conduct

---

### Column: Disposition (Cordova)
**Type**: xdtoken
**Description**: Outcome of a law enforcement case in Cordova.
**Enumeration**:
  - Fine: Monetary penalty assessed
  - Community Service: Ordered community service hours
  - Case Dismissed: Charges dropped or dismissed
  - Pending: Case awaiting disposition
**Examples**: Fine, Community Service, Pending
