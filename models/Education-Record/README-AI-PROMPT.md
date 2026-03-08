# Education Record

**Model ID**: `dm-upq7w1bqbix5v5ss0mu3kq5n`
**Project**: Cordova
**Description**: Track student enrollment and academic credentials at Cordova educational institutions.

### Dublin Core Metadata
- **Language**: en-US
- **Rights**: CC-BY http://creativecommons.org/licenses/by/3.0/
- **Coverage**: Universal

## Package Contents

- `dm-upq7w1bqbix5v5ss0mu3kq5n.xsd` -- XML Schema Definition (data model structure)
- `dm-upq7w1bqbix5v5ss0mu3kq5n.xml` -- XML instance example with sample data
- `dm-upq7w1bqbix5v5ss0mu3kq5n-instance.json` -- JSON instance example (same structure as XML)
- `dm-upq7w1bqbix5v5ss0mu3kq5n.jsonld` -- JSON-LD semantic schema description
- `dm-upq7w1bqbix5v5ss0mu3kq5n.html` -- Human-readable model documentation
- `dm-upq7w1bqbix5v5ss0mu3kq5n_shacl.ttl` -- SHACL shapes for RDF validation
- `dm-upq7w1bqbix5v5ss0mu3kq5n.ttl` -- RDF triples extracted from XSD (Turtle format)
- `dm-upq7w1bqbix5v5ss0mu3kq5n.rdf` -- RDF triples extracted from XSD (RDF/XML format)
- `dm-upq7w1bqbix5v5ss0mu3kq5n.gql` -- GQL CREATE statements for property graph databases
- `SHACL_README.md` -- SHACL usage guide
- `README-AI-PROMPT.md` -- This file

## XML Template Placeholders

The XML instance file (`dm-upq7w1bqbix5v5ss0mu3kq5n.xml`) is a **maximal template** containing every
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
| **Education Record** | Cluster | `ifgq7a670csnbv7vcpuiabp0` | 4 components; 2 sub-cluster(s) |
|   National ID (CID) | XdString | `nj7s1gk45tfgyooxpz0qaha3` | exactLen=16; pattern=`COR-(AL|BR|CE)0[1-3]-[0-9]{6}` |
|   Student ID | XdString | `khbvruwpu9hnttg8y0mnih6a` | minLen=1; maxLen=50 |
|   City | XdToken | `atdtdfzruh7tya0iv5cz365l` | 9 enum(s) |
|   Province | XdToken | `kv5qqs3o4jwcwz9javgw1pzh` | 3 enum(s) |
|   **Credential** | Cluster | `nyf0w3u2hs0svcjnqkb6zzlb` | 5 components |
|     Yes/No | XdBoolean | `ht98owgvxhff3ge85i4h80lp` | -- |
|     Field of Study | XdString | `ouqi09d8kjqeojlr7vnclysj` | minLen=1; maxLen=200 |
|     Credential Type | XdToken | `sxkjp09cbjb6n13j8a0eg37i` | 7 enum(s) |
|     Honors | XdToken | `c7qvfjtu0omg4wagiaiy5hej` | 4 enum(s) |
|     Date Awarded | XdTemporal | `xi99tao4v75wdrkq0ot02vfd` | -- |
|   **Enrollment** | Cluster | `r97mt4prbpxp04qmdc8iimb8` | 1 assert(s); 5 components |
|     Field of Study | XdString | `ouqi09d8kjqeojlr7vnclysj` | minLen=1; maxLen=200 |
|     Enrollment Status | XdToken | `squd8e2s6pk8xoafu9ec0t9k` | 5 enum(s) |
|     Education Level | XdOrdinal | `1ylumrkck2vv635djov01tte4` | -- |
|     Enrollment Date | XdTemporal | `z72jnzdib9hi311s338zwdog` | -- |
|     Expected Completion Date | XdTemporal | `g6ntdb41otp1mtwsyb52mez3` | -- |

## Structural Hierarchy

```
DM: Education Record
  [Cluster] Education Record
    [XdString] National ID (CID)
    [XdString] Student ID
    [XdToken] City
    [XdToken] Province
    [Cluster] Credential
      [XdBoolean] Yes/No
      [XdString] Field of Study
      [XdToken] Credential Type
      [XdToken] Honors
      [XdTemporal] Date Awarded
    [Cluster] Enrollment
      [XdString] Field of Study
      [XdToken] Enrollment Status
      [XdOrdinal] Education Level
      [XdTemporal] Enrollment Date
      [XdTemporal] Expected Completion Date
```

## Semantic Links

| Component | Predicate | Object URI |
|-----------|-----------|------------|
| Education Record | `rdfs:isDefinedBy` | `https://niemopen.org/` |
| Education Record | `skos:broadMatch` | `https://schema.org/ItemList` |
| Education Record | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q131156977` |
| National ID (CID) | `rdfs:isDefinedBy` | `http://schema.org/identifier` |
| National ID (CID) | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1140371` |
| National ID (CID) | `skos:broadMatch` | `https://schema.org/identifier` |
| Student ID | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q906630` |
| Student ID | `skos:broadMatch` | `https://schema.org/identifier` |
| City | `rdfs:isDefinedBy` | `http://schema.org/City` |
| City | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| City | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Province | `rdfs:isDefinedBy` | `http://schema.org/AdministrativeArea` |
| Province | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Province | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Province | `rdfs:isDefinedBy` | `https://schema.org/State` |
| Credential | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q16861606` |
| Credential | `rdfs:isDefinedBy` | `https://niemopen.org/` |
| Credential | `skos:broadMatch` | `https://schema.org/ItemList` |
| Yes/No | `skos:relatedMatch` | `https://www.wikidata.org/wiki/Q113518417` |
| Yes/No | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Yes/No | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Field of Study | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1047113` |
| Field of Study | `rdf:type` | `https://schema.org/Text` |
| Credential Type | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Credential Type | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Credential Type | `rdfs:isDefinedBy` | `https://www.w3.org/2018/credentials#type` |
| Honors | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q11415564` |
| Honors | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Honors | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Date Awarded | `rdfs:isDefinedBy` | `http://purl.org/dc/terms/issued` |
| Date Awarded | `skos:broadMatch` | `https://schema.org/Date` |
| Enrollment | `rdfs:isDefinedBy` | `https://www.cdc.gov/vaccines/hcp/imz-schedules/index.html` |
| Enrollment | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q102252225` |
| Enrollment | `skos:broadMatch` | `https://schema.org/ItemList` |
| Field of Study | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1047113` |
| Field of Study | `rdf:type` | `https://schema.org/Text` |
| Enrollment Status | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q76649493` |
| Enrollment Status | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Enrollment Status | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Education Level | `rdfs:isDefinedBy` | `https://uts.nlm.nih.gov/uts/umls/concept/C2030935` |
| Education Level | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Education Level | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Enrollment Date | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q137375576` |
| Enrollment Date | `skos:broadMatch` | `https://schema.org/Date` |
| Expected Completion Date | `rdfs:isDefinedBy` | `http://release.niem.gov/niem/niem-core/6.0/ProgramPlannedEndDate` |
| Expected Completion Date | `skos:broadMatch` | `https://schema.org/Date` |

## Using This Model with AI Assistants

### Quick Start Prompt

Copy and customize this prompt for your AI assistant:

```
I have an SDC4-compliant data model called "Education Record" and need help
creating a data entry application.

**Attached Files:**
- XML Schema (dm-upq7w1bqbix5v5ss0mu3kq5n.xsd)
- Example instance (dm-upq7w1bqbix5v5ss0mu3kq5n.xml)
- HTML documentation (dm-upq7w1bqbix5v5ss0mu3kq5n.html)

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
"Education Record" SDC4 schema (dm-upq7w1bqbix5v5ss0mu3kq5n.xsd).
Include CSV import, SQLite storage, forms with validation, and a data browser.
Use the sdcvalidator library for full SDC4 XML validation.
```

**React/Next.js Web App:**
```
Build a React/Next.js application with a REST API backend for the
"Education Record" schema (dm-upq7w1bqbix5v5ss0mu3kq5n.xsd).
Frontend: data entry forms and browser using the schema structure.
Backend: Node.js/Express with PostgreSQL for storage.
```

**Django Admin Interface:**
```
Generate Django models from the "Education Record" SDC4 schema (dm-upq7w1bqbix5v5ss0mu3kq5n.xsd)
with a custom admin interface.
Each cluster should be a Django model with appropriate field types.
Include CSV import/export via Django admin actions.
```

**REST API Only:**
```
Create a FastAPI REST API for the "Education Record" data model (dm-upq7w1bqbix5v5ss0mu3kq5n.xsd).
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
validator = SDC4Validator('dm-upq7w1bqbix5v5ss0mu3kq5n.xsd')

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
validator = SDC4Validator('dm-upq7w1bqbix5v5ss0mu3kq5n.xsd')
recovered_tree = validator.validate_with_recovery('data.xml')
validator.save_recovered_xml('recovered_data.xml', 'data.xml')
```

**Note**: XML validation is completely optional. You can build applications
using only JSON, implement custom validation, or add sdcvalidator later.

## GQL Graph Database Usage

The `dm-upq7w1bqbix5v5ss0mu3kq5n.gql` file contains GQL CREATE statements for property
graph databases (e.g., Neo4j, Amazon Neptune, TigerGraph).

### Loading into Neo4j

```cypher
// Load the GQL file content
// Copy the CREATE statements from dm-upq7w1bqbix5v5ss0mu3kq5n.gql into the Neo4j browser
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

The `dm-upq7w1bqbix5v5ss0mu3kq5n.html` file contains human-readable descriptions,
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
