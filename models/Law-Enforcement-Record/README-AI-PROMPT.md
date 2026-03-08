# Law Enforcement Record

**Model ID**: `dm-yh0opq0bnu6y9y56oukg92uf`
**Project**: Cordova
**Description**: Record public safety incidents, charges, and dispositions in Cordova.

### Dublin Core Metadata
- **Language**: en-US
- **Rights**: CC-BY http://creativecommons.org/licenses/by/3.0/
- **Coverage**: Universal

## Package Contents

- `dm-yh0opq0bnu6y9y56oukg92uf.xsd` -- XML Schema Definition (data model structure)
- `dm-yh0opq0bnu6y9y56oukg92uf.xml` -- XML instance example with sample data
- `dm-yh0opq0bnu6y9y56oukg92uf-instance.json` -- JSON instance example (same structure as XML)
- `dm-yh0opq0bnu6y9y56oukg92uf.jsonld` -- JSON-LD semantic schema description
- `dm-yh0opq0bnu6y9y56oukg92uf.html` -- Human-readable model documentation
- `dm-yh0opq0bnu6y9y56oukg92uf_shacl.ttl` -- SHACL shapes for RDF validation
- `dm-yh0opq0bnu6y9y56oukg92uf.ttl` -- RDF triples extracted from XSD (Turtle format)
- `dm-yh0opq0bnu6y9y56oukg92uf.rdf` -- RDF triples extracted from XSD (RDF/XML format)
- `dm-yh0opq0bnu6y9y56oukg92uf.gql` -- GQL CREATE statements for property graph databases
- `SHACL_README.md` -- SHACL usage guide
- `README-AI-PROMPT.md` -- This file

## XML Template Placeholders

The XML instance file (`dm-yh0opq0bnu6y9y56oukg92uf.xml`) is a **maximal template** containing every
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
| **Incident Report** | Cluster | `songhwxr1fp8niqba4fd0yd9` | 8 components; 2 sub-cluster(s) |
|   Incident Report Number | XdString | `yi2189u4pinqitlmm5t6ccrd` | minLen=1; maxLen=50 |
|   Incident Summary | XdString | `rguhpkd7s2d9a51392aon7ir` | minLen=1; maxLen=2000 |
|   Location Street Full Text | XdString | `b6nahtg2we4rh5qsk2j7qfvz` | minLen=1; maxLen=200 |
|   City | XdToken | `atdtdfzruh7tya0iv5cz365l` | 9 enum(s) |
|   Incident Status | XdToken | `e83h36jqgi59dhy1dttp22qm` | 3 enum(s) |
|   Province | XdToken | `kv5qqs3o4jwcwz9javgw1pzh` | 3 enum(s) |
|   Incident Category Code | XdToken | `nc7aq6ofnccavkmczsb2dudy` | 17 enum(s) |
|   Incident Date | XdTemporal | `ohk2uwcomsz8wegfvz0v0yod` | -- |
|   **Charge and Disposition** | Cluster | `c3eoo0vfid9c8riruf7uoyz2` | 1 assert(s); 6 components |
|     Charge Description | XdString | `eoqim4xj9gsxtxrqko1hh55o` | minLen=1; maxLen=200 |
|     Charge Category (Cordova) | XdToken | `hc91pdnj3bb6997l5z4ndchz` | 6 enum(s) |
|     Disposition (Cordova) | XdToken | `rnje7nq6m08vh01g8eg23say` | 4 enum(s) |
|     Fine or Bail Amount | XdQuantity | `yahksk4xc5to981ows7bpp6z` | min=0.00000; units=Cordova Córdoba (COR) |
|     Disposition Date | XdTemporal | `qse1jwofk5lm2wnsrn3f06l0` | -- |
|     Charge Filing Date | XdTemporal | `l0esdclu01pg7qw429oe7kjk` | -- |
|   **Quarantine Enforcement** | Cluster | `avmmc3r38dol0ghko42yeyp4` | 1 assert(s); 5 components |
|     Issuing Authority | XdString | `ixmedhicidzpi7g6g2huqzvv` | minLen=1; maxLen=200 |
|     Quarantine Zone | XdString | `r34gm210y9jifbyxa0fcxy96` | minLen=1; maxLen=200 |
|     Compliance Status | XdToken | `ihoatduhb7fckjw0ezq5u7g1` | 3 enum(s) |
|     Quarantine End Date | XdTemporal | `lohvu07ok3c3xvesa16htf2m` | -- |
|     Quarantine Start Date | XdTemporal | `vq30hd0dl6v59d3ttyyvg6rp` | -- |

## Structural Hierarchy

```
DM: Law Enforcement Record
  [Cluster] Incident Report
    [XdString] Incident Report Number
    [XdString] Incident Summary
    [XdString] Location Street Full Text
    [XdToken] City
    [XdToken] Incident Status
    [XdToken] Province
    [XdToken] Incident Category Code
    [XdTemporal] Incident Date
    [Cluster] Charge and Disposition
      [XdString] Charge Description
      [XdToken] Charge Category (Cordova)
      [XdToken] Disposition (Cordova)
      [XdQuantity] Fine or Bail Amount
      [XdTemporal] Disposition Date
      [XdTemporal] Charge Filing Date
    [Cluster] Quarantine Enforcement
      [XdString] Issuing Authority
      [XdString] Quarantine Zone
      [XdToken] Compliance Status
      [XdTemporal] Quarantine End Date
      [XdTemporal] Quarantine Start Date
```

## Semantic Links

| Component | Predicate | Object URI |
|-----------|-----------|------------|
| Incident Report | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q6014597` |
| Incident Report | `rdfs:isDefinedBy` | `https://niemopen.org/` |
| Incident Report | `skos:broadMatch` | `https://schema.org/ItemList` |
| Incident Report Number | `rdf:type` | `https://schema.org/Text` |
| Incident Report Number | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q111653916` |
| Incident Summary | `rdfs:isDefinedBy` | `http://schema.org/description` |
| Incident Summary | `rdf:type` | `https://schema.org/Text` |
| Location Street Full Text | `rdf:type` | `https://schema.org/Text` |
| Location Street Full Text | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q24574749` |
| City | `rdfs:isDefinedBy` | `http://schema.org/City` |
| City | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| City | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Incident Status | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Incident Status | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Incident Status | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q2443992` |
| Province | `rdfs:isDefinedBy` | `http://schema.org/AdministrativeArea` |
| Province | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Province | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Province | `rdfs:isDefinedBy` | `https://schema.org/State` |
| Incident Category Code | `rdfs:isDefinedBy` | `http://www.w3.org/2004/02/skos/core#Concept` |
| Incident Category Code | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Incident Category Code | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Incident Date | `rdfs:isDefinedBy` | `http://purl.obolibrary.org/obo/BFO_0000015` |
| Incident Date | `rdf:type` | `https://schema.org/DateTime` |
| Charge and Disposition | `rdfs:isDefinedBy` | `http://release.niem.gov/niem/niem-core/6.0/#Charge` |
| Charge and Disposition | `rdfs:isDefinedBy` | `https://niemopen.org/` |
| Charge and Disposition | `skos:broadMatch` | `https://schema.org/ItemList` |
| Charge Description | `rdfs:isDefinedBy` | `http://schema.org/name` |
| Charge Description | `rdf:type` | `https://schema.org/Text` |
| Charge Category (Cordova) | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1752346` |
| Charge Category (Cordova) | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Charge Category (Cordova) | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Disposition (Cordova) | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q2972905` |
| Disposition (Cordova) | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Disposition (Cordova) | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Fine or Bail Amount | `skos:broadMatch` | `https://www.wikidata.org/wiki/Q313614` |
| Fine or Bail Amount | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q186361` |
| Fine or Bail Amount | `rdfs:isDefinedBy` | `https://schema.org/MonetaryAmount` |
| Disposition Date | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q117195543` |
| Disposition Date | `skos:broadMatch` | `https://schema.org/Date` |
| Charge Filing Date | `rdfs:isDefinedBy` | `http://schema.org/datePublished` |
| Charge Filing Date | `rdf:type` | `https://schema.org/DateTime` |
| Quarantine Enforcement | `rdfs:isDefinedBy` | `https://www.imo.org/en/about/conventions/pages/international-convention-on-tonnage-measurement-of-ships.aspx` |
| Quarantine Enforcement | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q186588` |
| Quarantine Enforcement | `skos:broadMatch` | `https://schema.org/ItemList` |
| Issuing Authority | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q136462915` |
| Issuing Authority | `skos:broadMatch` | `https://schema.org/name` |
| Quarantine Zone | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q356936` |
| Quarantine Zone | `skos:broadMatch` | `https://schema.org/description` |
| Compliance Status | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q752476` |
| Compliance Status | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Compliance Status | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Quarantine End Date | `rdfs:isDefinedBy` | `http://schema.org/endDate` |
| Quarantine End Date | `skos:broadMatch` | `https://schema.org/Date` |
| Quarantine Start Date | `skos:broadMatch` | `https://schema.org/Date` |
| Quarantine Start Date | `rdfs:isDefinedBy` | `http://schema.org/startDate` |

## Using This Model with AI Assistants

### Quick Start Prompt

Copy and customize this prompt for your AI assistant:

```
I have an SDC4-compliant data model called "Law Enforcement Record" and need help
creating a data entry application.

**Attached Files:**
- XML Schema (dm-yh0opq0bnu6y9y56oukg92uf.xsd)
- Example instance (dm-yh0opq0bnu6y9y56oukg92uf.xml)
- HTML documentation (dm-yh0opq0bnu6y9y56oukg92uf.html)

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
"Law Enforcement Record" SDC4 schema (dm-yh0opq0bnu6y9y56oukg92uf.xsd).
Include CSV import, SQLite storage, forms with validation, and a data browser.
Use the sdcvalidator library for full SDC4 XML validation.
```

**React/Next.js Web App:**
```
Build a React/Next.js application with a REST API backend for the
"Law Enforcement Record" schema (dm-yh0opq0bnu6y9y56oukg92uf.xsd).
Frontend: data entry forms and browser using the schema structure.
Backend: Node.js/Express with PostgreSQL for storage.
```

**Django Admin Interface:**
```
Generate Django models from the "Law Enforcement Record" SDC4 schema (dm-yh0opq0bnu6y9y56oukg92uf.xsd)
with a custom admin interface.
Each cluster should be a Django model with appropriate field types.
Include CSV import/export via Django admin actions.
```

**REST API Only:**
```
Create a FastAPI REST API for the "Law Enforcement Record" data model (dm-yh0opq0bnu6y9y56oukg92uf.xsd).
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
validator = SDC4Validator('dm-yh0opq0bnu6y9y56oukg92uf.xsd')

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
validator = SDC4Validator('dm-yh0opq0bnu6y9y56oukg92uf.xsd')
recovered_tree = validator.validate_with_recovery('data.xml')
validator.save_recovered_xml('recovered_data.xml', 'data.xml')
```

**Note**: XML validation is completely optional. You can build applications
using only JSON, implement custom validation, or add sdcvalidator later.

## GQL Graph Database Usage

The `dm-yh0opq0bnu6y9y56oukg92uf.gql` file contains GQL CREATE statements for property
graph databases (e.g., Neo4j, Amazon Neptune, TigerGraph).

### Loading into Neo4j

```cypher
// Load the GQL file content
// Copy the CREATE statements from dm-yh0opq0bnu6y9y56oukg92uf.gql into the Neo4j browser
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

The `dm-yh0opq0bnu6y9y56oukg92uf.html` file contains human-readable descriptions,
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
