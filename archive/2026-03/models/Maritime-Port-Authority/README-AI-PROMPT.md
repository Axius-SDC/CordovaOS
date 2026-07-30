# Maritime Port Authority

**Model ID**: `dm-md2451x882z5j89g66zb50rw`
**Project**: Cordova
**Description**: Record all maritime operations, vessel movements, crew, cargo, and customs at Porto Sereno.

### Dublin Core Metadata
- **Language**: en-US
- **Rights**: CC-BY http://creativecommons.org/licenses/by/3.0/
- **Coverage**: Universal

## Package Contents

- `dm-md2451x882z5j89g66zb50rw.xsd` -- XML Schema Definition (data model structure)
- `dm-md2451x882z5j89g66zb50rw.xml` -- XML instance example with sample data
- `dm-md2451x882z5j89g66zb50rw-instance.json` -- JSON instance example (same structure as XML)
- `dm-md2451x882z5j89g66zb50rw.jsonld` -- JSON-LD semantic schema description
- `dm-md2451x882z5j89g66zb50rw.html` -- Human-readable model documentation
- `dm-md2451x882z5j89g66zb50rw_shacl.ttl` -- SHACL shapes for RDF validation
- `dm-md2451x882z5j89g66zb50rw.ttl` -- RDF triples extracted from XSD (Turtle format)
- `dm-md2451x882z5j89g66zb50rw.rdf` -- RDF triples extracted from XSD (RDF/XML format)
- `dm-md2451x882z5j89g66zb50rw.gql` -- GQL CREATE statements for property graph databases
- `SHACL_README.md` -- SHACL usage guide
- `README-AI-PROMPT.md` -- This file

## XML Template Placeholders

The XML instance file (`dm-md2451x882z5j89g66zb50rw.xml`) is a **maximal template** containing every
element defined in the schema. Placeholder markers indicate where data should go:

- **`_PH_`** -- Required placeholder. This element MUST be replaced with valid data
  matching the schema constraints.
- **`_OPT_PH_`** -- Optional placeholder. This element CAN be replaced with data,
  or the entire enclosing element can be removed from the instance.
- **Fixed values** (labels, language, encoding) are pre-filled from the schema and
  should be kept as-is.

When using this template with an AI assistant, instruct it to:
1. Replace all `_PH_` markers with appropriate data
2. Replace `_OPT_PH_` markers with data or remove the element
3. Keep all fixed values unchanged

## Component Inventory

| Label | Type | CT ID | Constraints |
|-------|------|-------|-------------|
| **Port Call Record** | Cluster | `i8cjmvihdces5rqvb2snqwmo` | 1 assert(s); 20 components; 2 sub-cluster(s) |
|   Flag State | XdString | `k7a0poa5c7co38oc65i6jppo` | minLen=1; maxLen=200 |
|   Port Call ID | XdString | `pbfvurdvio38rt6puifhippe` | minLen=1; maxLen=50 |
|   Berth Assignment | XdString | `lnjzw0racjo2oxol5w82tp1y` | minLen=1; maxLen=200 |
|   Next Port of Call | XdString | `gxt0t3cs4u6v5ob55qkc6ha0` | minLen=1; maxLen=200 |
|   Port of Departure | XdString | `s0qun9zalf98t3ffsefh34rj` | minLen=1; maxLen=200 |
|   Vessel Call Sign | XdString | `qlqdwbglcq4v3rg8i8iy7dk0` | minLen=1; maxLen=50 |
|   Vessel IMO Number | XdString | `ycy71t767wlyqma97o82r2m9` | exactLen=7; pattern=`\d{7}` |
|   Vessel MMSI | XdString | `cl1hiqht7tm42a8lh8c4c1hz` | exactLen=9; pattern=`\d{9}` |
|   Vessel Name | XdString | `s5zeapfup3xdj6wbqjjkf1nd` | minLen=1; maxLen=200 |
|   Voyage Number | XdString | `bmoixtn8r8pu62gbgd1tl8qn` | minLen=1; maxLen=50 |
|   Cargo Type | XdToken | `bfaa3m23ye8q0qphv0x24if6` | 8 enum(s) |
|   Purpose of Call | XdToken | `lyh7y1in5j9ka5cxk2zw2qdj` | 9 enum(s) |
|   Crew Count | XdCount | `p5qzw565y1dm5f3s6lg2q3ft` | units=Persons |
|   Passenger Count | XdCount | `x720xrlooqij75bk26pvzrtl` | units=Persons |
|   Vessel Draft | XdQuantity | `xccdfbmuqcy5yzv2n6ef0hrs` | units=Length/Distance (SI - Metric) |
|   Vessel Gross Tonnage | XdQuantity | `wtph0sqt244h38lyzf9ot1op` | units=Gross Tonnage |
|   Vessel Length Overall | XdQuantity | `jnxxwzl046rkmkbtm33naueu` | units=Length/Distance (SI - Metric) |
|   Vessel Net Tonnage | XdQuantity | `lh0ufebnovngzzgfggud6ae6` | units=Net Tonnage |
|   Arrival Date/Time | XdTemporal | `upvi6l9pyb4f0p4vfunietsw` | -- |
|   Departure Date/Time | XdTemporal | `sqpcl9uk7sze8bdqxxqwuqrn` | -- |
|   **Cargo Manifest** | Cluster | `ibb8e7c8equpeqiv5wxrxxll` | 1 assert(s); 11 components |
|     Customs Declaration Filed | XdBoolean | `wxjyv4dmwb0rws14mn5xy3ju` | -- |
|     Hazardous Cargo | XdBoolean | `n7x39orkbwjejdf8r93trlaa` | -- |
|     Business Registry Number | XdString | `l8f0m7op4xhrxqy1jrnvbuly` | exactLen=10; pattern=`BIZ-[0-9]{6}` |
|     Cargo Description | XdString | `z7zqo56erimvk8dqvl07ihfr` | minLen=1; maxLen=200 |
|     Cargo Destination | XdString | `an9kafb2l1enwh20ngvo1n7y` | minLen=1; maxLen=200 |
|     Cargo Origin | XdString | `rt510ljj3vz05fxwcm85i990` | minLen=1; maxLen=200 |
|     Customs Reference Number | XdString | `dp1dkn09vydj2ss6ho37kyhv` | minLen=1; maxLen=50 |
|     Cargo Type | XdToken | `bfaa3m23ye8q0qphv0x24if6` | 8 enum(s) |
|     Hazmat Class | XdToken | `gqbvto3l0o5e6uorrgjwdig2` | 1 enum(s) |
|     Container Count | XdCount | `y5se2qd3r6xx6pz8t7d8cqvf` | units=Twenty-foot Equivalent Units (TEU) |
|     Cargo Weight | XdQuantity | `lqqypwp22ohzb0ud3wq81r9s` | min=0.00000; units=Mass/Weight (SI - Metric) |
|   **Port Fees** | Cluster | `emtr91lypy400ttgzz2ti4et` | 4 components |
|     Fee Type | XdToken | `wvfcfa6u4ers75egrbi25x9l` | 8 enum(s) |
|     Payment Status | XdToken | `vt5nh89ol3g5gj0oz35tl6y0` | 3 enum(s) |
|     Port Fee Amount | XdQuantity | `e92ud8io69rm826g9b1jrrgh` | min=0.00000; units=Cordova Córdoba (COR) |
|     Fee Date | XdTemporal | `zub98dao6k8cbbhsddzoq62w` | -- |

## Structural Hierarchy

```
DM: Maritime Port Authority
  [Cluster] Port Call Record
    [XdString] Flag State
    [XdString] Port Call ID
    [XdString] Berth Assignment
    [XdString] Next Port of Call
    [XdString] Port of Departure
    [XdString] Vessel Call Sign
    [XdString] Vessel IMO Number
    [XdString] Vessel MMSI
    [XdString] Vessel Name
    [XdString] Voyage Number
    [XdToken] Cargo Type
    [XdToken] Purpose of Call
    [XdCount] Crew Count
    [XdCount] Passenger Count
    [XdQuantity] Vessel Draft
    [XdQuantity] Vessel Gross Tonnage
    [XdQuantity] Vessel Length Overall
    [XdQuantity] Vessel Net Tonnage
    [XdTemporal] Arrival Date/Time
    [XdTemporal] Departure Date/Time
    [Cluster] Cargo Manifest
      [XdBoolean] Customs Declaration Filed
      [XdBoolean] Hazardous Cargo
      [XdString] Business Registry Number
      [XdString] Cargo Description
      [XdString] Cargo Destination
      [XdString] Cargo Origin
      [XdString] Customs Reference Number
      [XdToken] Cargo Type
      [XdToken] Hazmat Class
      [XdCount] Container Count
      [XdQuantity] Cargo Weight
    [Cluster] Port Fees
      [XdToken] Fee Type
      [XdToken] Payment Status
      [XdQuantity] Port Fee Amount
      [XdTemporal] Fee Date
```

## Semantic Links

| Component | Predicate | Object URI |
|-----------|-----------|------------|
| Port Call Record | `rdfs:isDefinedBy` | `https://www.imo.org/en/about/conventions/pages/international-convention-on-tonnage-measurement-of-ships.aspx` |
| Port Call Record | `rdfs:isDefinedBy` | `http://schema.org/Report` |
| Port Call Record | `skos:broadMatch` | `https://schema.org/ItemList` |
| Flag State | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q3591841` |
| Flag State | `skos:broadMatch` | `https://schema.org/name` |
| Port Call ID | `rdfs:isDefinedBy` | `http://purl.obolibrary.org/obo/BFO_0000009` |
| Port Call ID | `skos:broadMatch` | `https://schema.org/identifier` |
| Berth Assignment | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q57964937` |
| Berth Assignment | `rdf:type` | `https://schema.org/Text` |
| Next Port of Call | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q119382961` |
| Next Port of Call | `rdf:type` | `https://schema.org/Text` |
| Port of Departure | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q76455346` |
| Port of Departure | `rdf:type` | `https://schema.org/Text` |
| Vessel Call Sign | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q23581925` |
| Vessel Call Sign | `rdf:type` | `https://schema.org/Text` |
| Vessel IMO Number | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1970938` |
| Vessel IMO Number | `rdf:type` | `https://schema.org/Text` |
| Vessel MMSI | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1795701` |
| Vessel MMSI | `rdf:type` | `https://schema.org/Text` |
| Vessel Name | `rdf:type` | `https://schema.org/Text` |
| Vessel Name | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q56351075` |
| Voyage Number | `rdf:type` | `https://schema.org/Text` |
| Voyage Number | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q130365988` |
| Cargo Type | `skos:relatedMatch` | `https://www.wikidata.org/wiki/Q319224` |
| Cargo Type | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Cargo Type | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Purpose of Call | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q20729393` |
| Purpose of Call | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Purpose of Call | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Crew Count | `rdf:type` | `https://schema.org/Integer` |
| Crew Count | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q2513968` |
| Passenger Count | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q319604` |
| Passenger Count | `rdf:type` | `https://schema.org/Integer` |
| Vessel Draft | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q863247` |
| Vessel Draft | `rdfs:isDefinedBy` | `https://www.imo.org/en/about/conventions/pages/international-convention-on-tonnage-measurement-of-ships.aspx` |
| Vessel Draft | `rdf:type` | `https://schema.org/Number` |
| Vessel Gross Tonnage | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q217792` |
| Vessel Gross Tonnage | `rdfs:isDefinedBy` | `https://www.imo.org/en/about/conventions/pages/international-convention-on-tonnage-measurement-of-ships.aspx` |
| Vessel Gross Tonnage | `rdf:type` | `https://schema.org/Number` |
| Vessel Length Overall | `rdfs:isDefinedBy` | `https://www.imo.org/en/about/conventions/pages/international-convention-on-tonnage-measurement-of-ships.aspx` |
| Vessel Length Overall | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1424988` |
| Vessel Length Overall | `rdf:type` | `https://schema.org/Number` |
| Vessel Net Tonnage | `rdfs:isDefinedBy` | `https://www.imo.org/en/about/conventions/pages/international-convention-on-tonnage-measurement-of-ships.aspx` |
| Vessel Net Tonnage | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q756933` |
| Vessel Net Tonnage | `rdf:type` | `https://schema.org/Number` |
| Arrival Date/Time | `rdfs:isDefinedBy` | `http://release.niem.gov/niem/niem-core/5.0/niem-core.owl#ArrivalDateTime` |
| Arrival Date/Time | `skos:broadMatch` | `https://schema.org/Date` |
| Arrival Date/Time | `skos:broadMatch` | `https://schema.org/DateTime` |
| Departure Date/Time | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q52943` |
| Departure Date/Time | `skos:broadMatch` | `https://schema.org/Date` |
| Departure Date/Time | `skos:broadMatch` | `https://schema.org/DateTime` |
| Cargo Manifest | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q105851048` |
| Cargo Manifest | `rdfs:isDefinedBy` | `https://www.imo.org/en/about/conventions/pages/international-convention-on-tonnage-measurement-of-ships.aspx` |
| Cargo Manifest | `skos:broadMatch` | `https://schema.org/ItemList` |
| Customs Declaration Filed | `skos:relatedMatch` | `https://www.wikidata.org/wiki/Q847595` |
| Customs Declaration Filed | `rdf:type` | `https://schema.org/Boolean` |
| Hazardous Cargo | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q13537426` |
| Hazardous Cargo | `rdf:type` | `https://schema.org/Boolean` |
| Business Registry Number | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q12047291` |
| Business Registry Number | `rdfs:isDefinedBy` | `http://schema.org/identifier` |
| Business Registry Number | `skos:broadMatch` | `https://schema.org/identifier` |
| Cargo Description | `rdfs:isDefinedBy` | `http://release.niem.gov/niem/niem-core/6.0/niem-core.owl#CargoDescriptionText` |
| Cargo Description | `skos:broadMatch` | `https://schema.org/description` |
| Cargo Destination | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q5254083` |
| Cargo Destination | `skos:broadMatch` | `https://schema.org/description` |
| Cargo Origin | `skos:broadMatch` | `https://schema.org/description` |
| Cargo Origin | `rdfs:isDefinedBy` | `http://schema.org/shippingOrigin` |
| Customs Reference Number | `rdfs:isDefinedBy` | `http://schema.org/identifier` |
| Customs Reference Number | `rdf:type` | `https://schema.org/Text` |
| Cargo Type | `skos:relatedMatch` | `https://www.wikidata.org/wiki/Q319224` |
| Cargo Type | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Cargo Type | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Container Count | `skos:broadMatch` | `https://www.wikidata.org/wiki/Q380340` |
| Container Count | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1366867` |
| Cargo Weight | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q319224` |
| Cargo Weight | `rdfs:isDefinedBy` | `https://www.imo.org/en/about/conventions/pages/international-convention-on-tonnage-measurement-of-ships.aspx` |
| Cargo Weight | `rdf:type` | `https://schema.org/Number` |
| Port Fees | `rdfs:isDefinedBy` | `http://release.niem.gov/niem/niem-core/5.0/niem-core.owl#Fee` |
| Port Fees | `rdfs:isDefinedBy` | `https://www.imo.org/en/about/conventions/pages/international-convention-on-tonnage-measurement-of-ships.aspx` |
| Port Fees | `skos:broadMatch` | `https://schema.org/ItemList` |
| Fee Type | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1912682` |
| Fee Type | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Fee Type | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Payment Status | `rdfs:isDefinedBy` | `http://schema.org/PaymentStatusType` |
| Payment Status | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Payment Status | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Port Fee Amount | `rdfs:isDefinedBy` | `https://schema.org/MonetaryAmount` |
| Port Fee Amount | `skos:broadMatch` | `http://qudt.org/vocab/quantitykind/Currency` |
| Port Fee Amount | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1194642` |
| Fee Date | `rdfs:isDefinedBy` | `http://release.niem.gov/niem/niem-core/6.0/AssessmentDate` |
| Fee Date | `skos:broadMatch` | `https://schema.org/Date` |

## Using This Model with AI Assistants

### Quick Start Prompt

Copy and customize this prompt for your AI assistant:

```
I have an SDC4-compliant data model called "Maritime Port Authority" and need help
creating a data entry application.

**Attached Files:**
- XML Schema (dm-md2451x882z5j89g66zb50rw.xsd)
- Example instance (dm-md2451x882z5j89g66zb50rw.xml)
- HTML documentation (dm-md2451x882z5j89g66zb50rw.html)

**What I Need:**
I need a [specify framework: Python Reflex / React / Django / etc.] application that:

1. **Data Import**: Import data from CSV files
2. **Data Storage**: Store in [SQLite / PostgreSQL / MySQL / etc.] database
3. **Data Entry**: Forms for creating/editing records with validation
4. **Data Browser**: View, filter, and search records
5. **Export**: Export data back to CSV or XML

**Database Design:**
Each SDC4 Cluster in the schema should map to a database table with
appropriate relationships.

**My Specific Requirements:**
[Add your specific needs here]

Please analyze the schema and propose an application architecture.
```

### Example Use Cases

**Python Reflex Data Entry App:**
```
Create a Python Reflex application for data entry based on the
"Maritime Port Authority" SDC4 schema (dm-md2451x882z5j89g66zb50rw.xsd).
Include CSV import, SQLite storage, forms with validation, and a data browser.
Use the sdcvalidator library for full SDC4 XML validation.
```

**React/Next.js Web App:**
```
Build a React/Next.js application with a REST API backend for the
"Maritime Port Authority" schema (dm-md2451x882z5j89g66zb50rw.xsd).
Frontend: data entry forms and browser using the schema structure.
Backend: Node.js/Express with PostgreSQL for storage.
```

**Django Admin Interface:**
```
Generate Django models from the "Maritime Port Authority" SDC4 schema (dm-md2451x882z5j89g66zb50rw.xsd)
with a custom admin interface.
Each cluster should be a Django model with appropriate field types.
Include CSV import/export via Django admin actions.
```

**REST API Only:**
```
Create a FastAPI REST API for the "Maritime Port Authority" data model (dm-md2451x882z5j89g66zb50rw.xsd).
Endpoints for CRUD operations on each cluster.
Include XML validation using sdcvalidator.
Return both JSON and XML responses.
```

## SDC4 Validation (Optional but Recommended)

For full SDC4 compliance with XML validation, use the `sdcvalidator` Python library.

### Installation

```bash
pip install sdcvalidator
```

### Basic Usage

```python
from sdcvalidator import SDC4Validator

# Initialize validator with your SDC4 data model schema
validator = SDC4Validator('dm-md2451x882z5j89g66zb50rw.xsd')

# Validate and get a detailed report
report = validator.validate_and_report('data.xml')

if report['valid']:
    print('Valid SDC4 XML instance')
else:
    print('Validation errors:')
    for error in report['errors']:
        print(f"  - {error['xpath']}: {error['reason']}")
```

### ExceptionalValue Recovery

When validation errors occur, sdcvalidator can quarantine invalid data
with ISO 21090 ExceptionalValue elements:

```python
validator = SDC4Validator('dm-md2451x882z5j89g66zb50rw.xsd')
recovered_tree = validator.validate_with_recovery('data.xml')
validator.save_recovered_xml('recovered_data.xml', 'data.xml')
```

**Note**: XML validation is completely optional. You can build applications
using only JSON, implement custom validation, or add sdcvalidator later.

## GQL Graph Database Usage

The `dm-md2451x882z5j89g66zb50rw.gql` file contains GQL CREATE statements for property
graph databases (e.g., Neo4j, Amazon Neptune, TigerGraph).

### Loading into Neo4j

```cypher
// Load the GQL file content
// Copy the CREATE statements from dm-md2451x882z5j89g66zb50rw.gql into the Neo4j browser
```

### Example Queries

```cypher
// Find all components in this data model
MATCH (n:ModelComponent) RETURN n.label, n.sdcType

// Show the structural hierarchy
MATCH (dm:DataModel)-[:HAS_ROOT_CLUSTER]->(c:Cluster)-[:CONTAINS_COMPONENT]->(comp)
RETURN dm.label, c.label, comp.label, comp.sdcType

// Find components with specific constraints
MATCH (n:ModelComponent) WHERE n.minLength IS NOT NULL
RETURN n.label, n.minLength, n.maxLength
```

## Tips for Working with AI Assistants

### 1. Start with Architecture Discussion

Before asking for code, ask the AI to:
- Analyze the schema structure
- Identify complex relationships
- Recommend database design
- Suggest appropriate frameworks

### 2. Iterate in Phases

- **Phase 1**: Basic data models and storage
- **Phase 2**: Data entry forms
- **Phase 3**: Data browser and search
- **Phase 4**: CSV import/export
- **Phase 5**: Advanced features (auth, reporting, etc.)

### 3. Leverage the Documentation

The `dm-md2451x882z5j89g66zb50rw.html` file contains human-readable descriptions,
constraint definitions, business rules, and semantic links.
Share this with the AI for better understanding.

### 4. Database Schema Mapping

**Option 1: Normalized Tables (Traditional)**
```
Cluster -> Database Table
Sub-Cluster -> Separate Table with Foreign Key
Component -> Table Column
```

**Option 2: JSON Embedding (Simpler)**
```
Main Cluster -> Table
Sub-Clusters -> JSON Column
Components -> Mixed (simple types as columns, complex as JSON)
```

Ask your AI assistant which approach fits your use case.

## Additional Resources

**SDC4 Specification:**
- [Semantic Data Charter](https://semanticdatacharter.org)

**sdcvalidator Documentation:**
- [PyPI Package](https://pypi.org/project/sdcvalidator/)

**Framework Documentation:**
- [Python Reflex](https://reflex.dev)
- [Django](https://www.djangoproject.com)
- [React](https://react.dev)
- [FastAPI](https://fastapi.tiangolo.com)

---

**Generated by SDCStudio** -- Your SDC4-compliant data modeling platform
