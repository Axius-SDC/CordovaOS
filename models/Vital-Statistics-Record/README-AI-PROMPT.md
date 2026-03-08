# Vital Statistics Record

**Model ID**: `dm-ulzd6pe8072mwkqf7i313bov`
**Project**: Cordova
**Description**: Maintain the authoritative registry of life events in Cordova.

### Dublin Core Metadata
- **Language**: en-US
- **Rights**: CC-BY http://creativecommons.org/licenses/by/3.0/
- **Coverage**: Universal

## Package Contents

- `dm-ulzd6pe8072mwkqf7i313bov.xsd` -- XML Schema Definition (data model structure)
- `dm-ulzd6pe8072mwkqf7i313bov.xml` -- XML instance example with sample data
- `dm-ulzd6pe8072mwkqf7i313bov-instance.json` -- JSON instance example (same structure as XML)
- `dm-ulzd6pe8072mwkqf7i313bov.jsonld` -- JSON-LD semantic schema description
- `dm-ulzd6pe8072mwkqf7i313bov.html` -- Human-readable model documentation
- `dm-ulzd6pe8072mwkqf7i313bov_shacl.ttl` -- SHACL shapes for RDF validation
- `dm-ulzd6pe8072mwkqf7i313bov.ttl` -- RDF triples extracted from XSD (Turtle format)
- `dm-ulzd6pe8072mwkqf7i313bov.rdf` -- RDF triples extracted from XSD (RDF/XML format)
- `dm-ulzd6pe8072mwkqf7i313bov.gql` -- GQL CREATE statements for property graph databases
- `SHACL_README.md` -- SHACL usage guide
- `README-AI-PROMPT.md` -- This file

## XML Template Placeholders

The XML instance file (`dm-ulzd6pe8072mwkqf7i313bov.xml`) is a **maximal template** containing every
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
| **Vital Event** | Cluster | `tard9hhq13m95hinbh4h7k5j` | 1 assert(s); 7 components; 4 sub-cluster(s) |
|   Certificate Number | XdString | `ajfsyoyrz38094hswxh13i3x` | minLen=1; maxLen=50 |
|   City | XdToken | `atdtdfzruh7tya0iv5cz365l` | 9 enum(s) |
|   Event Type | XdToken | `jz7vc6ikueqig8g0lvb2czzr` | 4 enum(s) |
|   Province | XdToken | `kv5qqs3o4jwcwz9javgw1pzh` | 3 enum(s) |
|   Record Status | XdToken | `yri6g628ipi0jqoa0ijnzxxu` | 3 enum(s) |
|   Event Date | XdTemporal | `e3sfb43zh1vjlgceb5guh0mj` | -- |
|   Registration Date | XdTemporal | `vo9jtmexkaaol3y657fm0xn8` | -- |
|   **Birth Record** | Cluster | `az8kem3v58y9zenys7mthqxe` | 3 components |
|     National ID (CID) | XdString | `nj7s1gk45tfgyooxpz0qaha3` | exactLen=16; pattern=`COR-(AL|BR|CE)0[1-3]-[0-9]{6}` |
|     Person Full Name | XdString | `pmw2cq7fioqlbs2ljdh34rkn` | minLen=1; maxLen=100 |
|     Sex | XdToken | `mw9qdn71urog8egjbp5t3y00` | 4 enum(s) |
|   **Death Record** | Cluster | `tdz3pxrf7k6z2df2bfm7ebcp` | 5 components |
|     Cause of Death | XdString | `m3gsphdej7z9csemrrk8uymy` | minLen=1; maxLen=200 |
|     National ID (CID) | XdString | `nj7s1gk45tfgyooxpz0qaha3` | exactLen=16; pattern=`COR-(AL|BR|CE)0[1-3]-[0-9]{6}` |
|     Person Full Name | XdString | `pmw2cq7fioqlbs2ljdh34rkn` | minLen=1; maxLen=100 |
|     Manner of Death | XdToken | `ftuxt5nrrffwjb2vymn80yx2` | 6 enum(s) |
|     Place of Death | XdToken | `dsoyfaplxw8ide1opo5w8fxg` | 3 enum(s) |
|   **Divorce Record** | Cluster | `obybok0oaoa79b11b0ync1zf` | 4 components |
|     Marriage Certificate Number | XdString | `ycujkecjszwwrcd6dhxesk73` | minLen=1; maxLen=50 |
|     National ID (CID) | XdString | `nj7s1gk45tfgyooxpz0qaha3` | exactLen=16; pattern=`COR-(AL|BR|CE)0[1-3]-[0-9]{6}` |
|     Person Full Name | XdString | `pmw2cq7fioqlbs2ljdh34rkn` | minLen=1; maxLen=100 |
|     Decree Date | XdTemporal | `ft4kk6m3r1goxkte0d7wflk8` | -- |
|   **Marriage Record** | Cluster | `chtyne5i6qcwbrby29vbuh2k` | 2 components |
|     National ID (CID) | XdString | `nj7s1gk45tfgyooxpz0qaha3` | exactLen=16; pattern=`COR-(AL|BR|CE)0[1-3]-[0-9]{6}` |
|     Person Full Name | XdString | `pmw2cq7fioqlbs2ljdh34rkn` | minLen=1; maxLen=100 |

## Structural Hierarchy

```
DM: Vital Statistics Record
  [Cluster] Vital Event
    [XdString] Certificate Number
    [XdToken] City
    [XdToken] Event Type
    [XdToken] Province
    [XdToken] Record Status
    [XdTemporal] Event Date
    [XdTemporal] Registration Date
    [Cluster] Birth Record
      [XdString] National ID (CID)
      [XdString] Person Full Name
      [XdToken] Sex
    [Cluster] Death Record
      [XdString] Cause of Death
      [XdString] National ID (CID)
      [XdString] Person Full Name
      [XdToken] Manner of Death
      [XdToken] Place of Death
    [Cluster] Divorce Record
      [XdString] Marriage Certificate Number
      [XdString] National ID (CID)
      [XdString] Person Full Name
      [XdTemporal] Decree Date
    [Cluster] Marriage Record
      [XdString] National ID (CID)
      [XdString] Person Full Name
```

## Semantic Links

| Component | Predicate | Object URI |
|-----------|-----------|------------|
| Vital Event | `skos:relatedMatch` | `https://www.wikidata.org/wiki/Q97211668` |
| Vital Event | `skos:broadMatch` | `https://schema.org/ItemList` |
| Vital Event | `skos:exactMatch` | `https://www.wikidata.org/wiki/Q18562479` |
| Vital Event | `skos:broadMatch` | `https://www.wikidata.org/wiki/Q1131372` |
| Vital Event | `rdfs:isDefinedBy` | `https://www.who.int/data/data-collection-tools/civil-registration-and-vital-statistics-(crvs)` |
| Certificate Number | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q108891191` |
| Certificate Number | `skos:broadMatch` | `https://schema.org/identifier` |
| City | `rdfs:isDefinedBy` | `http://schema.org/City` |
| City | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| City | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Event Type | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q108586636` |
| Event Type | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Event Type | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Province | `rdfs:isDefinedBy` | `http://schema.org/AdministrativeArea` |
| Province | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Province | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Province | `rdfs:isDefinedBy` | `https://schema.org/State` |
| Record Status | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q65720124` |
| Record Status | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Record Status | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Event Date | `skos:broadMatch` | `https://schema.org/Date` |
| Event Date | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q7911665` |
| Registration Date | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q137375576` |
| Registration Date | `skos:broadMatch` | `https://schema.org/Date` |
| Birth Record | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q83900` |
| Birth Record | `skos:broadMatch` | `https://schema.org/ItemList` |
| Birth Record | `rdfs:isDefinedBy` | `https://www.who.int/data/data-collection-tools/civil-registration-and-vital-statistics-(crvs)` |
| National ID (CID) | `rdfs:isDefinedBy` | `http://schema.org/identifier` |
| National ID (CID) | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1140371` |
| National ID (CID) | `skos:broadMatch` | `https://schema.org/identifier` |
| Person Full Name | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1071027` |
| Person Full Name | `rdf:type` | `https://schema.org/Text` |
| Sex | `rdfs:isDefinedBy` | `https://uts.nlm.nih.gov/uts/umls/concept/C5236503` |
| Sex | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Sex | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Death Record | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q708653` |
| Death Record | `skos:broadMatch` | `https://schema.org/ItemList` |
| Death Record | `rdfs:isDefinedBy` | `https://www.who.int/data/data-collection-tools/civil-registration-and-vital-statistics-(crvs)` |
| Cause of Death | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1931388` |
| Cause of Death | `skos:broadMatch` | `https://schema.org/description` |
| National ID (CID) | `rdfs:isDefinedBy` | `http://schema.org/identifier` |
| National ID (CID) | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1140371` |
| National ID (CID) | `skos:broadMatch` | `https://schema.org/identifier` |
| Person Full Name | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1071027` |
| Person Full Name | `rdf:type` | `https://schema.org/Text` |
| Manner of Death | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q2438541` |
| Manner of Death | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Manner of Death | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Place of Death | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q18658526` |
| Place of Death | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Place of Death | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Divorce Record | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q131460403` |
| Divorce Record | `skos:broadMatch` | `https://schema.org/ItemList` |
| Divorce Record | `rdfs:isDefinedBy` | `https://www.who.int/data/data-collection-tools/civil-registration-and-vital-statistics-(crvs)` |
| Marriage Certificate Number | `skos:broadMatch` | `https://www.wikidata.org/wiki/Q820655` |
| Marriage Certificate Number | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1299632` |
| National ID (CID) | `rdfs:isDefinedBy` | `http://schema.org/identifier` |
| National ID (CID) | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1140371` |
| National ID (CID) | `skos:broadMatch` | `https://schema.org/identifier` |
| Person Full Name | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1071027` |
| Person Full Name | `rdf:type` | `https://schema.org/Text` |
| Decree Date | `rdfs:isDefinedBy` | `http://release.niem.gov/niem/niem-core/5.0/DocumentIssueDate` |
| Decree Date | `skos:broadMatch` | `https://schema.org/Date` |
| Marriage Record | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1299632` |
| Marriage Record | `skos:broadMatch` | `https://schema.org/ItemList` |
| Marriage Record | `rdfs:isDefinedBy` | `https://www.who.int/data/data-collection-tools/civil-registration-and-vital-statistics-(crvs)` |
| National ID (CID) | `rdfs:isDefinedBy` | `http://schema.org/identifier` |
| National ID (CID) | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1140371` |
| National ID (CID) | `skos:broadMatch` | `https://schema.org/identifier` |
| Person Full Name | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1071027` |
| Person Full Name | `rdf:type` | `https://schema.org/Text` |

## Using This Model with AI Assistants

### Quick Start Prompt

Copy and customize this prompt for your AI assistant:

```
I have an SDC4-compliant data model called "Vital Statistics Record" and need help
creating a data entry application.

**Attached Files:**
- XML Schema (dm-ulzd6pe8072mwkqf7i313bov.xsd)
- Example instance (dm-ulzd6pe8072mwkqf7i313bov.xml)
- HTML documentation (dm-ulzd6pe8072mwkqf7i313bov.html)

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
"Vital Statistics Record" SDC4 schema (dm-ulzd6pe8072mwkqf7i313bov.xsd).
Include CSV import, SQLite storage, forms with validation, and a data browser.
Use the sdcvalidator library for full SDC4 XML validation.
```

**React/Next.js Web App:**
```
Build a React/Next.js application with a REST API backend for the
"Vital Statistics Record" schema (dm-ulzd6pe8072mwkqf7i313bov.xsd).
Frontend: data entry forms and browser using the schema structure.
Backend: Node.js/Express with PostgreSQL for storage.
```

**Django Admin Interface:**
```
Generate Django models from the "Vital Statistics Record" SDC4 schema (dm-ulzd6pe8072mwkqf7i313bov.xsd)
with a custom admin interface.
Each cluster should be a Django model with appropriate field types.
Include CSV import/export via Django admin actions.
```

**REST API Only:**
```
Create a FastAPI REST API for the "Vital Statistics Record" data model (dm-ulzd6pe8072mwkqf7i313bov.xsd).
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
validator = SDC4Validator('dm-ulzd6pe8072mwkqf7i313bov.xsd')

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
validator = SDC4Validator('dm-ulzd6pe8072mwkqf7i313bov.xsd')
recovered_tree = validator.validate_with_recovery('data.xml')
validator.save_recovered_xml('recovered_data.xml', 'data.xml')
```

**Note**: XML validation is completely optional. You can build applications
using only JSON, implement custom validation, or add sdcvalidator later.

## GQL Graph Database Usage

The `dm-ulzd6pe8072mwkqf7i313bov.gql` file contains GQL CREATE statements for property
graph databases (e.g., Neo4j, Amazon Neptune, TigerGraph).

### Loading into Neo4j

```cypher
// Load the GQL file content
// Copy the CREATE statements from dm-ulzd6pe8072mwkqf7i313bov.gql into the Neo4j browser
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

The `dm-ulzd6pe8072mwkqf7i313bov.html` file contains human-readable descriptions,
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
