# Employment Record

**Model ID**: `dm-pm5cks82lnrvyna1xbwpfxic`
**Project**: Cordova
**Description**: Track employment relationships between persons and businesses in Cordova.

### Dublin Core Metadata
- **Language**: en-US
- **Rights**: CC-BY http://creativecommons.org/licenses/by/3.0/
- **Coverage**: Universal

## Package Contents

- `dm-pm5cks82lnrvyna1xbwpfxic.xsd` -- XML Schema Definition (data model structure)
- `dm-pm5cks82lnrvyna1xbwpfxic.xml` -- XML instance example with sample data
- `dm-pm5cks82lnrvyna1xbwpfxic-instance.json` -- JSON instance example (same structure as XML)
- `dm-pm5cks82lnrvyna1xbwpfxic.jsonld` -- JSON-LD semantic schema description
- `dm-pm5cks82lnrvyna1xbwpfxic.html` -- Human-readable model documentation
- `dm-pm5cks82lnrvyna1xbwpfxic_shacl.ttl` -- SHACL shapes for RDF validation
- `dm-pm5cks82lnrvyna1xbwpfxic.ttl` -- RDF triples extracted from XSD (Turtle format)
- `dm-pm5cks82lnrvyna1xbwpfxic.rdf` -- RDF triples extracted from XSD (RDF/XML format)
- `dm-pm5cks82lnrvyna1xbwpfxic.gql` -- GQL CREATE statements for property graph databases
- `SHACL_README.md` -- SHACL usage guide
- `README-AI-PROMPT.md` -- This file

## XML Template Placeholders

The XML instance file (`dm-pm5cks82lnrvyna1xbwpfxic.xml`) is a **maximal template** containing every
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
| **Employment Record** | Cluster | `ablvqv20fp33v8t8c985dlo2` | 1 assert(s); 7 components; 1 sub-cluster(s) |
|   Department | XdString | `bbu03oqjkniydmzb7pqcjg3m` | minLen=1; maxLen=200 |
|   Job Title | XdString | `wfws1oj1kgeaijciw7wkzdi7` | minLen=1; maxLen=200 |
|   City | XdToken | `atdtdfzruh7tya0iv5cz365l` | 9 enum(s) |
|   Employment Status (Cordova) | XdToken | `tb3wwfwects1a6ap4ro7z5s8` | 7 enum(s) |
|   Province | XdToken | `kv5qqs3o4jwcwz9javgw1pzh` | 3 enum(s) |
|   End Date | XdTemporal | `el43lwc0fnamy0v0ocub38t7` | -- |
|   Start Date | XdTemporal | `ghsjyyzudma3eq761dwd4j9p` | -- |
|   **Compensation** | Cluster | `vzabxfc733qk7lo1knaggxfs` | 3 components |
|     Yes/No | XdBoolean | `ht98owgvxhff3ge85i4h80lp` | -- |
|     Pay Frequency | XdToken | `ub0fwihnwu5x1pdv68pjwbeu` | 3 enum(s) |
|     Salary Amount | XdQuantity | `aw74ticc3fnjkz4vk4b03jr6` | min=0.00000; units=Cordova Córdoba (COR) |

## Structural Hierarchy

```
DM: Employment Record
  [Cluster] Employment Record
    [XdString] Department
    [XdString] Job Title
    [XdToken] City
    [XdToken] Employment Status (Cordova)
    [XdToken] Province
    [XdTemporal] End Date
    [XdTemporal] Start Date
    [Cluster] Compensation
      [XdBoolean] Yes/No
      [XdToken] Pay Frequency
      [XdQuantity] Salary Amount
```

## Semantic Links

| Component | Predicate | Object URI |
|-----------|-----------|------------|
| Employment Record | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q627374` |
| Employment Record | `rdfs:isDefinedBy` | `https://niemopen.org/` |
| Employment Record | `skos:broadMatch` | `https://schema.org/ItemList` |
| Department | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q2366457` |
| Department | `skos:broadMatch` | `https://schema.org/description` |
| Job Title | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q828803` |
| Job Title | `rdf:type` | `https://schema.org/Text` |
| City | `rdfs:isDefinedBy` | `http://schema.org/City` |
| City | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| City | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Employment Status (Cordova) | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q126734850` |
| Employment Status (Cordova) | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Employment Status (Cordova) | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Province | `rdfs:isDefinedBy` | `http://schema.org/AdministrativeArea` |
| Province | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Province | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Province | `rdfs:isDefinedBy` | `https://schema.org/State` |
| End Date | `skos:broadMatch` | `https://schema.org/Date` |
| End Date | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q121875611` |
| Start Date | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q5347252` |
| Start Date | `skos:broadMatch` | `https://schema.org/Date` |
| Compensation | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q21127747` |
| Compensation | `rdfs:isDefinedBy` | `https://niemopen.org/` |
| Compensation | `skos:broadMatch` | `https://schema.org/ItemList` |
| Yes/No | `skos:relatedMatch` | `https://www.wikidata.org/wiki/Q113518417` |
| Yes/No | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Yes/No | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Pay Frequency | `rdfs:isDefinedBy` | `http://release.niem.gov/niem/niem-core/6.0/niem-core.owl#PayPeriodFrequencyCode` |
| Pay Frequency | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Pay Frequency | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Salary Amount | `rdfs:isDefinedBy` | `https://schema.org/MonetaryAmount` |
| Salary Amount | `skos:broadMatch` | `http://qudt.org/vocab/quantitykind/Currency` |
| Salary Amount | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q178848` |

## Using This Model with AI Assistants

### Quick Start Prompt

Copy and customize this prompt for your AI assistant:

```
I have an SDC4-compliant data model called "Employment Record" and need help
creating a data entry application.

**Attached Files:**
- XML Schema (dm-pm5cks82lnrvyna1xbwpfxic.xsd)
- Example instance (dm-pm5cks82lnrvyna1xbwpfxic.xml)
- HTML documentation (dm-pm5cks82lnrvyna1xbwpfxic.html)

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
"Employment Record" SDC4 schema (dm-pm5cks82lnrvyna1xbwpfxic.xsd).
Include CSV import, SQLite storage, forms with validation, and a data browser.
Use the sdcvalidator library for full SDC4 XML validation.
```

**React/Next.js Web App:**
```
Build a React/Next.js application with a REST API backend for the
"Employment Record" schema (dm-pm5cks82lnrvyna1xbwpfxic.xsd).
Frontend: data entry forms and browser using the schema structure.
Backend: Node.js/Express with PostgreSQL for storage.
```

**Django Admin Interface:**
```
Generate Django models from the "Employment Record" SDC4 schema (dm-pm5cks82lnrvyna1xbwpfxic.xsd)
with a custom admin interface.
Each cluster should be a Django model with appropriate field types.
Include CSV import/export via Django admin actions.
```

**REST API Only:**
```
Create a FastAPI REST API for the "Employment Record" data model (dm-pm5cks82lnrvyna1xbwpfxic.xsd).
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
validator = SDC4Validator('dm-pm5cks82lnrvyna1xbwpfxic.xsd')

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
validator = SDC4Validator('dm-pm5cks82lnrvyna1xbwpfxic.xsd')
recovered_tree = validator.validate_with_recovery('data.xml')
validator.save_recovered_xml('recovered_data.xml', 'data.xml')
```

**Note**: XML validation is completely optional. You can build applications
using only JSON, implement custom validation, or add sdcvalidator later.

## GQL Graph Database Usage

The `dm-pm5cks82lnrvyna1xbwpfxic.gql` file contains GQL CREATE statements for property
graph databases (e.g., Neo4j, Amazon Neptune, TigerGraph).

### Loading into Neo4j

```cypher
// Load the GQL file content
// Copy the CREATE statements from dm-pm5cks82lnrvyna1xbwpfxic.gql into the Neo4j browser
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

The `dm-pm5cks82lnrvyna1xbwpfxic.html` file contains human-readable descriptions,
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
