# Tax and Revenue Record

**Model ID**: `dm-vaw4g2kusit5z0kox5mog54g`
**Project**: Cordova
**Description**: Record all tax filings, assessments, and revenue collection for Cordova.

### Dublin Core Metadata
- **Language**: en-US
- **Rights**: CC-BY http://creativecommons.org/licenses/by/3.0/
- **Coverage**: Universal

## Package Contents

- `dm-vaw4g2kusit5z0kox5mog54g.xsd` -- XML Schema Definition (data model structure)
- `dm-vaw4g2kusit5z0kox5mog54g.xml` -- XML instance example with sample data
- `dm-vaw4g2kusit5z0kox5mog54g-instance.json` -- JSON instance example (same structure as XML)
- `dm-vaw4g2kusit5z0kox5mog54g.jsonld` -- JSON-LD semantic schema description
- `dm-vaw4g2kusit5z0kox5mog54g.html` -- Human-readable model documentation
- `dm-vaw4g2kusit5z0kox5mog54g_shacl.ttl` -- SHACL shapes for RDF validation
- `dm-vaw4g2kusit5z0kox5mog54g.ttl` -- RDF triples extracted from XSD (Turtle format)
- `dm-vaw4g2kusit5z0kox5mog54g.rdf` -- RDF triples extracted from XSD (RDF/XML format)
- `dm-vaw4g2kusit5z0kox5mog54g.gql` -- GQL CREATE statements for property graph databases
- `SHACL_README.md` -- SHACL usage guide
- `README-AI-PROMPT.md` -- This file

## XML Template Placeholders

The XML instance file (`dm-vaw4g2kusit5z0kox5mog54g.xml`) is a **maximal template** containing every
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
| **Tax Filing** | Cluster | `w9v4eo1l0wy5r65tqx5mjyxh` | 4 components; 3 sub-cluster(s) |
|   Filing ID | XdString | `a2yks4n49m6gcgpa7qc9hyg1` | minLen=1; maxLen=50 |
|   Tax Filing Status | XdToken | `hwmy9yj7cbhe94pjnq0n2oo5` | 4 enum(s) |
|   Tax Type | XdToken | `zb956wxcjf1fccvqezivgrv7` | 6 enum(s) |
|   Filing Date | XdTemporal | `cuazcmxeeo8osfybrgdpe9g7` | -- |
|   **Payment** | Cluster | `j4drl0w17dmw49maf3swgi18` | 4 components |
|     Payment Method | XdToken | `fqgaf7s7gkwi6j4hh88meudp` | 4 enum(s) |
|     Payment Status | XdToken | `vt5nh89ol3g5gj0oz35tl6y0` | 3 enum(s) |
|     Payment Amount | XdQuantity | `tzrg36a15rigk48nj20sbw4v` | min=0.00000; units=Cordova Córdoba (COR) |
|     Payment Date | XdTemporal | `xrjzng8dyk9eveyzi03abuhr` | -- |
|   **Source Reference** | Cluster | `kwb0rpk8stxtaitb7k5hahlq` | 2 components |
|     Source Record ID | XdString | `hcfz6urx5c2ayvt8npjl0t4l` | minLen=1; maxLen=50 |
|     Source Domain | XdToken | `hh750k4i187bqzot5md216r1` | 5 enum(s) |
|   **Tax Assessment** | Cluster | `ekmjsthf4vkzcff9pwodqg5n` | 2 components |
|     Taxable Income | XdQuantity | `q1sbdhsdk8glmdr8q1x3mlte` | min=0.00000; units=Cordova Córdoba (COR) |
|     Tax Assessment Amount | XdQuantity | `l5t2s5y0m4ybwom4ryndzaf9` | min=0.00000; units=Cordova Córdoba (COR) |

## Structural Hierarchy

```
DM: Tax and Revenue Record
  [Cluster] Tax Filing
    [XdString] Filing ID
    [XdToken] Tax Filing Status
    [XdToken] Tax Type
    [XdTemporal] Filing Date
    [Cluster] Payment
      [XdToken] Payment Method
      [XdToken] Payment Status
      [XdQuantity] Payment Amount
      [XdTemporal] Payment Date
    [Cluster] Source Reference
      [XdString] Source Record ID
      [XdToken] Source Domain
    [Cluster] Tax Assessment
      [XdQuantity] Taxable Income
      [XdQuantity] Tax Assessment Amount
```

## Semantic Links

| Component | Predicate | Object URI |
|-----------|-----------|------------|
| Tax Filing | `rdfs:isDefinedBy` | `https://niemopen.org/` |
| Tax Filing | `skos:broadMatch` | `https://schema.org/ItemList` |
| Tax Filing | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q2861384` |
| Filing ID | `rdfs:isDefinedBy` | `http://release.niem.gov/niem/niem-core/5.0/niem-core.owl#IdentificationType` |
| Filing ID | `skos:broadMatch` | `https://schema.org/identifier` |
| Tax Filing Status | `skos:relatedMatch` | `https://www.wikidata.org/wiki/Q5448453` |
| Tax Type | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Tax Type | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Tax Type | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q130109687` |
| Filing Date | `skos:broadMatch` | `https://schema.org/Date` |
| Filing Date | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q107296042` |
| Payment | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1148747` |
| Payment | `skos:broadMatch` | `https://schema.org/ItemList` |
| Payment Method | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1912682` |
| Payment Method | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Payment Method | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Payment Status | `rdfs:isDefinedBy` | `http://schema.org/PaymentStatusType` |
| Payment Status | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Payment Status | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Payment Amount | `rdfs:isDefinedBy` | `https://schema.org/MonetaryAmount` |
| Payment Amount | `skos:broadMatch` | `http://qudt.org/vocab/quantitykind/Currency` |
| Payment Amount | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1148747` |
| Payment Date | `rdfs:isDefinedBy` | `http://release.niem.gov/niem/niem-core/5.0/#PaymentDate` |
| Payment Date | `skos:broadMatch` | `https://schema.org/Date` |
| Source Reference | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1713` |
| Source Reference | `skos:broadMatch` | `https://schema.org/ItemList` |
| Source Record ID | `rdfs:isDefinedBy` | `http://www.w3.org/ns/prov#hadPrimaryId` |
| Source Record ID | `skos:broadMatch` | `https://schema.org/identifier` |
| Source Domain | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q7363` |
| Source Domain | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Source Domain | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Tax Assessment | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q851176` |
| Tax Assessment | `skos:broadMatch` | `https://schema.org/ItemList` |
| Taxable Income | `rdfs:isDefinedBy` | `https://schema.org/MonetaryAmount` |
| Taxable Income | `skos:broadMatch` | `http://qudt.org/vocab/quantitykind/Currency` |
| Taxable Income | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q786825` |
| Tax Assessment Amount | `rdfs:isDefinedBy` | `https://schema.org/MonetaryAmount` |
| Tax Assessment Amount | `skos:broadMatch` | `http://qudt.org/vocab/quantitykind/Currency` |
| Tax Assessment Amount | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q7688416` |

## Using This Model with AI Assistants

### Quick Start Prompt

Copy and customize this prompt for your AI assistant:

```
I have an SDC4-compliant data model called "Tax and Revenue Record" and need help
creating a data entry application.

**Attached Files:**
- XML Schema (dm-vaw4g2kusit5z0kox5mog54g.xsd)
- Example instance (dm-vaw4g2kusit5z0kox5mog54g.xml)
- HTML documentation (dm-vaw4g2kusit5z0kox5mog54g.html)

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
"Tax and Revenue Record" SDC4 schema (dm-vaw4g2kusit5z0kox5mog54g.xsd).
Include CSV import, SQLite storage, forms with validation, and a data browser.
Use the sdcvalidator library for full SDC4 XML validation.
```

**React/Next.js Web App:**
```
Build a React/Next.js application with a REST API backend for the
"Tax and Revenue Record" schema (dm-vaw4g2kusit5z0kox5mog54g.xsd).
Frontend: data entry forms and browser using the schema structure.
Backend: Node.js/Express with PostgreSQL for storage.
```

**Django Admin Interface:**
```
Generate Django models from the "Tax and Revenue Record" SDC4 schema (dm-vaw4g2kusit5z0kox5mog54g.xsd)
with a custom admin interface.
Each cluster should be a Django model with appropriate field types.
Include CSV import/export via Django admin actions.
```

**REST API Only:**
```
Create a FastAPI REST API for the "Tax and Revenue Record" data model (dm-vaw4g2kusit5z0kox5mog54g.xsd).
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
validator = SDC4Validator('dm-vaw4g2kusit5z0kox5mog54g.xsd')

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
validator = SDC4Validator('dm-vaw4g2kusit5z0kox5mog54g.xsd')
recovered_tree = validator.validate_with_recovery('data.xml')
validator.save_recovered_xml('recovered_data.xml', 'data.xml')
```

**Note**: XML validation is completely optional. You can build applications
using only JSON, implement custom validation, or add sdcvalidator later.

## GQL Graph Database Usage

The `dm-vaw4g2kusit5z0kox5mog54g.gql` file contains GQL CREATE statements for property
graph databases (e.g., Neo4j, Amazon Neptune, TigerGraph).

### Loading into Neo4j

```cypher
// Load the GQL file content
// Copy the CREATE statements from dm-vaw4g2kusit5z0kox5mog54g.gql into the Neo4j browser
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

The `dm-vaw4g2kusit5z0kox5mog54g.html` file contains human-readable descriptions,
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
