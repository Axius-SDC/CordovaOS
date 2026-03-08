# Business Registry

**Model ID**: `dm-x250838l7oi6l3yavg9twc1i`
**Project**: Cordova
**Description**: Maintain the authoritative registry of business entities in Cordova.

### Dublin Core Metadata
- **Language**: en-US
- **Rights**: CC-BY http://creativecommons.org/licenses/by/3.0/
- **Coverage**: Universal

## Package Contents

- `dm-x250838l7oi6l3yavg9twc1i.xsd` -- XML Schema Definition (data model structure)
- `dm-x250838l7oi6l3yavg9twc1i.xml` -- XML instance example with sample data
- `dm-x250838l7oi6l3yavg9twc1i-instance.json` -- JSON instance example (same structure as XML)
- `dm-x250838l7oi6l3yavg9twc1i.jsonld` -- JSON-LD semantic schema description
- `dm-x250838l7oi6l3yavg9twc1i.html` -- Human-readable model documentation
- `dm-x250838l7oi6l3yavg9twc1i_shacl.ttl` -- SHACL shapes for RDF validation
- `dm-x250838l7oi6l3yavg9twc1i.ttl` -- RDF triples extracted from XSD (Turtle format)
- `dm-x250838l7oi6l3yavg9twc1i.rdf` -- RDF triples extracted from XSD (RDF/XML format)
- `dm-x250838l7oi6l3yavg9twc1i.gql` -- GQL CREATE statements for property graph databases
- `SHACL_README.md` -- SHACL usage guide
- `README-AI-PROMPT.md` -- This file

## XML Template Placeholders

The XML instance file (`dm-x250838l7oi6l3yavg9twc1i.xml`) is a **maximal template** containing every
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
| **Business Entity** | Cluster | `uv8dwudhyf0gnmzgiyyd1sb1` | 7 components; 1 sub-cluster(s) |
|   Business Registry Number | XdString | `l8f0m7op4xhrxqy1jrnvbuly` | exactLen=10; pattern=`BIZ-[0-9]{6}` |
|   Organization Name | XdString | `uinddfbzfk0jdikmt1jwcq78` | minLen=1; maxLen=200 |
|   Organization Tax ID | XdString | `gu15c6jojx09jy9at1px0ufh` | minLen=1; maxLen=50 |
|   Business Type (Cordova) | XdToken | `puz7m7a7rtuehrgp10tm17qn` | 4 enum(s) |
|   Industry | XdToken | `m0i63npis09ch7ag08ntoneu` | 11 enum(s) |
|   Status | XdToken | `cs34ekiq4o9pazzs5baiobis` | 3 enum(s) |
|   Registration Date | XdTemporal | `vo9jtmexkaaol3y657fm0xn8` | -- |
|   **Registered Address** | Cluster | `u8kz7rlfx1jjvkn7kgyao4tw` | 6 components |
|     Cordova Email Address | XdString | `x0na649n17if0ukul82cmrx3` | minLen=5; maxLen=254; pattern=`[-a-zA-Z0-9._%+]+@(cordomail|novamail|portocorreo)\.co` |
|     Cordova Phone Number | XdString | `nfrvvp87c5imu5h9ups92kgy` | exactLen=16; pattern=`\+99-[123][012]0-[0-9]{3}-[0-9]{4}` |
|     Address (Line 1) | XdString | `l338k7nlvnq2am0owa19yxfc` | maxLen=200 |
|     Address (Line 2) | XdString | `ek5h6dsqpd9kz0l4mcckmxpt` | maxLen=200 |
|     City | XdToken | `atdtdfzruh7tya0iv5cz365l` | 9 enum(s) |
|     Province | XdToken | `kv5qqs3o4jwcwz9javgw1pzh` | 3 enum(s) |

## Structural Hierarchy

```
DM: Business Registry
  [Cluster] Business Entity
    [XdString] Business Registry Number
    [XdString] Organization Name
    [XdString] Organization Tax ID
    [XdToken] Business Type (Cordova)
    [XdToken] Industry
    [XdToken] Status
    [XdTemporal] Registration Date
    [Cluster] Registered Address
      [XdString] Cordova Email Address
      [XdString] Cordova Phone Number
      [XdString] Address (Line 1)
      [XdString] Address (Line 2)
      [XdToken] City
      [XdToken] Province
```

## Semantic Links

| Component | Predicate | Object URI |
|-----------|-----------|------------|
| Business Entity | `rdfs:isDefinedBy` | `https://niemopen.org/` |
| Business Entity | `skos:broadMatch` | `https://schema.org/ItemList` |
| Business Entity | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1269299` |
| Business Registry Number | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q12047291` |
| Business Registry Number | `rdfs:isDefinedBy` | `http://schema.org/identifier` |
| Business Registry Number | `skos:broadMatch` | `https://schema.org/identifier` |
| Organization Name | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q168678` |
| Organization Name | `rdf:type` | `https://schema.org/Text` |
| Organization Tax ID | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q2397748` |
| Organization Tax ID | `rdf:type` | `https://schema.org/Text` |
| Business Type (Cordova) | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Business Type (Cordova) | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Business Type (Cordova) | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1058914` |
| Industry | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q2976602` |
| Industry | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Industry | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Status | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Status | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Status | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q856698` |
| Registration Date | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q137375576` |
| Registration Date | `skos:broadMatch` | `https://schema.org/Date` |
| Registered Address | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q65616986` |
| Registered Address | `skos:broadMatch` | `https://schema.org/ItemList` |
| Cordova Email Address | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1273217` |
| Cordova Email Address | `skos:broadMatch` | `https://schema.org/name` |
| Cordova Phone Number | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q214995` |
| Cordova Phone Number | `skos:relatedMatch` | `https://www.wikidata.org/wiki/Q214995` |
| Address (Line 1) | `rdf:type` | `https://schema.org/Text` |
| Address (Line 1) | `rdfs:isDefinedBy` | `https://schema.org/streetAddress` |
| Address (Line 2) | `rdf:type` | `https://schema.org/Text` |
| Address (Line 2) | `rdfs:isDefinedBy` | `https://schema.org/streetAddress` |
| City | `rdfs:isDefinedBy` | `http://schema.org/City` |
| City | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| City | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Province | `rdfs:isDefinedBy` | `http://schema.org/AdministrativeArea` |
| Province | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Province | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Province | `rdfs:isDefinedBy` | `https://schema.org/State` |

## Using This Model with AI Assistants

### Quick Start Prompt

Copy and customize this prompt for your AI assistant:

```
I have an SDC4-compliant data model called "Business Registry" and need help
creating a data entry application.

**Attached Files:**
- XML Schema (dm-x250838l7oi6l3yavg9twc1i.xsd)
- Example instance (dm-x250838l7oi6l3yavg9twc1i.xml)
- HTML documentation (dm-x250838l7oi6l3yavg9twc1i.html)

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
"Business Registry" SDC4 schema (dm-x250838l7oi6l3yavg9twc1i.xsd).
Include CSV import, SQLite storage, forms with validation, and a data browser.
Use the sdcvalidator library for full SDC4 XML validation.
```

**React/Next.js Web App:**
```
Build a React/Next.js application with a REST API backend for the
"Business Registry" schema (dm-x250838l7oi6l3yavg9twc1i.xsd).
Frontend: data entry forms and browser using the schema structure.
Backend: Node.js/Express with PostgreSQL for storage.
```

**Django Admin Interface:**
```
Generate Django models from the "Business Registry" SDC4 schema (dm-x250838l7oi6l3yavg9twc1i.xsd)
with a custom admin interface.
Each cluster should be a Django model with appropriate field types.
Include CSV import/export via Django admin actions.
```

**REST API Only:**
```
Create a FastAPI REST API for the "Business Registry" data model (dm-x250838l7oi6l3yavg9twc1i.xsd).
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
validator = SDC4Validator('dm-x250838l7oi6l3yavg9twc1i.xsd')

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
validator = SDC4Validator('dm-x250838l7oi6l3yavg9twc1i.xsd')
recovered_tree = validator.validate_with_recovery('data.xml')
validator.save_recovered_xml('recovered_data.xml', 'data.xml')
```

**Note**: XML validation is completely optional. You can build applications
using only JSON, implement custom validation, or add sdcvalidator later.

## GQL Graph Database Usage

The `dm-x250838l7oi6l3yavg9twc1i.gql` file contains GQL CREATE statements for property
graph databases (e.g., Neo4j, Amazon Neptune, TigerGraph).

### Loading into Neo4j

```cypher
// Load the GQL file content
// Copy the CREATE statements from dm-x250838l7oi6l3yavg9twc1i.gql into the Neo4j browser
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

The `dm-x250838l7oi6l3yavg9twc1i.html` file contains human-readable descriptions,
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
