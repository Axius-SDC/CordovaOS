# Healthcare Record

**Model ID**: `dm-ftluo2nybgxmn7mawttoos20`
**Project**: Cordova
**Description**: Maintain basic medical records for all persons in Cordova.

### Dublin Core Metadata
- **Language**: en-US
- **Rights**: CC-BY http://creativecommons.org/licenses/by/3.0/
- **Coverage**: Universal

## Package Contents

- `dm-ftluo2nybgxmn7mawttoos20.xsd` -- XML Schema Definition (data model structure)
- `dm-ftluo2nybgxmn7mawttoos20.xml` -- XML instance example with sample data
- `dm-ftluo2nybgxmn7mawttoos20-instance.json` -- JSON instance example (same structure as XML)
- `dm-ftluo2nybgxmn7mawttoos20.jsonld` -- JSON-LD semantic schema description
- `dm-ftluo2nybgxmn7mawttoos20.html` -- Human-readable model documentation
- `dm-ftluo2nybgxmn7mawttoos20_shacl.ttl` -- SHACL shapes for RDF validation
- `dm-ftluo2nybgxmn7mawttoos20.ttl` -- RDF triples extracted from XSD (Turtle format)
- `dm-ftluo2nybgxmn7mawttoos20.rdf` -- RDF triples extracted from XSD (RDF/XML format)
- `dm-ftluo2nybgxmn7mawttoos20.gql` -- GQL CREATE statements for property graph databases
- `SHACL_README.md` -- SHACL usage guide
- `README-AI-PROMPT.md` -- This file

## XML Template Placeholders

The XML instance file (`dm-ftluo2nybgxmn7mawttoos20.xml`) is a **maximal template** containing every
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
| **Patient Record** | Cluster | `ygtbvvmzcw3ukfsg3axqry97` | 2 components; 4 sub-cluster(s) |
|   National ID (CID) | XdString | `nj7s1gk45tfgyooxpz0qaha3` | exactLen=16; pattern=`COR-(AL|BR|CE)0[1-3]-[0-9]{6}` |
|   Medical Record Number | XdString | `jz2hqntyol8lopw6q6zdud78` | minLen=1; maxLen=50 |
|   **Allergies and Conditions** | Cluster | `xplqihmynccwa3o4o8s7gqml` | 5 components |
|     Allergy Description | XdString | `ntk4zsr15bcca2jmocdkcpcc` | minLen=1; maxLen=500 |
|     Chronic Condition | XdString | `cm0nqqnjcylc8vkfph7db2lh` | minLen=1; maxLen=500 |
|     Condition Status | XdToken | `tz13p9d4dpbw3pe9bx51nbou` | 3 enum(s) |
|     Severity (3-Point) | XdOrdinal | `07osold8ovbjsqzvz00f3ked2` | -- |
|     Onset Date | XdTemporal | `p14jkmk8xqs97daq3zvyhrsj` | -- |
|   **Medications** | Cluster | `vhjvhm6vz2om2jfn6b923gw7` | 5 components |
|     Dosage | XdString | `z28bjtjekyybe300ukuyjpi4` | minLen=1; maxLen=200 |
|     Medication Name | XdString | `nomiekce61caq5n9a49d0eu6` | minLen=1; maxLen=200 |
|     Frequency (5-Point) | XdOrdinal | `iprf7jqg9emvm92wo9gkiqcu` | -- |
|     Medication Dosage Amount | XdQuantity | `y7k4p12co0b9v6asll531fhv` | units=Mass/Weight (SI - Metric) |
|     Prescription Date | XdTemporal | `cq6m46w59ouu1cu8tkw1fhib` | -- |
|   **Vaccination History** | Cluster | `eq4h86worv571cl5iiy9unkw` | 3 components |
|     Lot Number | XdString | `td5j1frz2fa8g4uh1hor7w11` | minLen=1; maxLen=200 |
|     Vaccine Name | XdString | `fi1qu4j2zd0801fcqtix35h5` | minLen=1; maxLen=200 |
|     Vaccine Date | XdTemporal | `dyfz05n20jhc1elhozrbjug0` | -- |
|   **Visit Record** | Cluster | `hd9295k8o49j91lvgftul1a0` | 1 assert(s); 12 components |
|     Diagnosis | XdString | `nnu04d5qgrmn1bim8bpu0l65` | minLen=1; maxLen=500 |
|     Facility | XdString | `qvmb5f4xmy56y98q8raelpl9` | minLen=1; maxLen=200 |
|     Reason for Visit | XdString | `qzmcum3kwmskrkj7nhkf8fkm` | minLen=1; maxLen=500 |
|     Clinical Impression | XdString | `cntj1t9t2xjugnux1enpigmf` | minLen=1; maxLen=2000 |
|     Outcome | XdToken | `lccs354vpxmtyo69ba5cu48v` | 5 enum(s) |
|     Visit Type | XdToken | `l9sjn7wj10y5b27ldkv3j8mt` | 6 enum(s) |
|     Body Temperature | XdQuantity | `b5zse0kmvpkj74ggqvgk647l` | units=Temperature (SI - Metric) |
|     Diastolic Blood Pressure | XdQuantity | `lu2w1avj9fic5wrmyftt9fhi` | units=Pressure |
|     Patient Height | XdQuantity | `vh2scyehy68pw7sbvzdg3cn9` | units=Length/Distance (SI - Metric) |
|     Patient Weight | XdQuantity | `s6oo99lbq85kfz0v5nqv9yaf` | units=Mass/Weight (SI - Metric) |
|     Systolic Blood Pressure | XdQuantity | `kokquuk73pm2ohlh4ftnu7wb` | units=Pressure |
|     Visit Date | XdTemporal | `iufcfze52lha16v84kccgxyh` | -- |

## Structural Hierarchy

```
DM: Healthcare Record
  [Cluster] Patient Record
    [XdString] National ID (CID)
    [XdString] Medical Record Number
    [Cluster] Allergies and Conditions
      [XdString] Allergy Description
      [XdString] Chronic Condition
      [XdToken] Condition Status
      [XdOrdinal] Severity (3-Point)
      [XdTemporal] Onset Date
    [Cluster] Medications
      [XdString] Dosage
      [XdString] Medication Name
      [XdOrdinal] Frequency (5-Point)
      [XdQuantity] Medication Dosage Amount
      [XdTemporal] Prescription Date
    [Cluster] Vaccination History
      [XdString] Lot Number
      [XdString] Vaccine Name
      [XdTemporal] Vaccine Date
    [Cluster] Visit Record
      [XdString] Diagnosis
      [XdString] Facility
      [XdString] Reason for Visit
      [XdString] Clinical Impression
      [XdToken] Outcome
      [XdToken] Visit Type
      [XdQuantity] Body Temperature
      [XdQuantity] Diastolic Blood Pressure
      [XdQuantity] Patient Height
      [XdQuantity] Patient Weight
      [XdQuantity] Systolic Blood Pressure
      [XdTemporal] Visit Date
```

## Semantic Links

| Component | Predicate | Object URI |
|-----------|-----------|------------|
| Patient Record | `rdfs:isDefinedBy` | `https://hl7.org/fhir/` |
| Patient Record | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1324077` |
| Patient Record | `skos:broadMatch` | `https://schema.org/ItemList` |
| National ID (CID) | `rdfs:isDefinedBy` | `http://schema.org/identifier` |
| National ID (CID) | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1140371` |
| National ID (CID) | `skos:broadMatch` | `https://schema.org/identifier` |
| Medical Record Number | `rdfs:isDefinedBy` | `https://uts.nlm.nih.gov/uts/umls/concept/C1301894` |
| Medical Record Number | `rdf:type` | `https://schema.org/Text` |
| Allergies and Conditions | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q42982` |
| Allergies and Conditions | `rdfs:isDefinedBy` | `https://hl7.org/fhir/` |
| Allergies and Conditions | `skos:broadMatch` | `https://schema.org/ItemList` |
| Allergy Description | `rdfs:isDefinedBy` | `http://schema.org/description` |
| Allergy Description | `skos:broadMatch` | `https://schema.org/description` |
| Chronic Condition | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q383126` |
| Chronic Condition | `skos:broadMatch` | `https://schema.org/description` |
| Condition Status | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q12136` |
| Condition Status | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Condition Status | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Severity (3-Point) | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Severity (3-Point) | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q10870002` |
| Severity (3-Point) | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Onset Date | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q577` |
| Onset Date | `rdf:type` | `https://schema.org/DateTime` |
| Medications | `rdfs:isDefinedBy` | `https://hl7.org/fhir/` |
| Medications | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q12140` |
| Medications | `skos:broadMatch` | `https://schema.org/ItemList` |
| Dosage | `rdfs:isDefinedBy` | `http://qudt.org/vocab/quantitykind/AmountOfSubstance` |
| Dosage | `skos:broadMatch` | `https://schema.org/description` |
| Medication Name | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q70848614` |
| Medication Name | `skos:broadMatch` | `https://schema.org/name` |
| Frequency (5-Point) | `rdfs:isDefinedBy` | `https://uts.nlm.nih.gov/uts/umls/concept/C0436350` |
| Frequency (5-Point) | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Frequency (5-Point) | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Medication Dosage Amount | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q473420` |
| Medication Dosage Amount | `rdfs:isDefinedBy` | `https://hl7.org/fhir/` |
| Medication Dosage Amount | `skos:exactMatch` | `http://snomed.info/id/398232005` |
| Prescription Date | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q193521` |
| Prescription Date | `skos:broadMatch` | `https://schema.org/DateTime` |
| Vaccination History | `rdfs:isDefinedBy` | `https://www.cdc.gov/vaccines/hcp/imz-schedules/index.html` |
| Vaccination History | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q93623446` |
| Vaccination History | `skos:broadMatch` | `https://schema.org/ItemList` |
| Lot Number | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q28698186` |
| Lot Number | `skos:broadMatch` | `https://schema.org/identifier` |
| Vaccine Name | `skos:broadMatch` | `https://schema.org/Drug` |
| Vaccine Name | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q134808` |
| Vaccine Date | `skos:broadMatch` | `https://schema.org/Date` |
| Vaccine Date | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q192995` |
| Visit Record | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q29182` |
| Visit Record | `rdfs:isDefinedBy` | `https://hl7.org/fhir/` |
| Visit Record | `skos:broadMatch` | `https://schema.org/ItemList` |
| Diagnosis | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q14860489` |
| Diagnosis | `skos:relatedMatch` | `https://schema.org/MedicalCode` |
| Facility | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q9386252` |
| Facility | `skos:broadMatch` | `https://schema.org/name` |
| Reason for Visit | `rdfs:isDefinedBy` | `http://snomed.info/id/409586006` |
| Reason for Visit | `skos:broadMatch` | `https://schema.org/description` |
| Clinical Impression | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q69067902` |
| Clinical Impression | `rdf:type` | `https://schema.org/Text` |
| Outcome | `rdfs:isDefinedBy` | `http://schema.org/result` |
| Outcome | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Outcome | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Visit Type | `rdfs:isDefinedBy` | `https://uts.nlm.nih.gov/uts/umls/concept/C5708072` |
| Visit Type | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Visit Type | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Body Temperature | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1066998` |
| Body Temperature | `rdfs:isDefinedBy` | `https://www.ncbi.nlm.nih.gov/books/NBK331/` |
| Body Temperature | `rdfs:seeAlso` | `https://loinc.org/8310-5/` |
| Body Temperature | `skos:exactMatch` | `http://snomed.info/id/386725007` |
| Diastolic Blood Pressure | `rdfs:isDefinedBy` | `https://professional.heart.org/en/science-news/2017-hypertension-clinical-guidelines` |
| Diastolic Blood Pressure | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q82642` |
| Diastolic Blood Pressure | `skos:exactMatch` | `http://snomed.info/id/271650006` |
| Diastolic Blood Pressure | `rdfs:seeAlso` | `https://loinc.org/8462-4/` |
| Patient Height | `rdfs:seeAlso` | `https://loinc.org/8302-2/` |
| Patient Height | `skos:exactMatch` | `http://snomed.info/id/50373000` |
| Patient Height | `rdfs:isDefinedBy` | `https://www.cdc.gov/nchs/fastats/body-measurements.htm` |
| Patient Height | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q81938` |
| Patient Weight | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q18247` |
| Patient Weight | `rdfs:seeAlso` | `https://loinc.org/29463-7/` |
| Patient Weight | `skos:exactMatch` | `http://snomed.info/id/27113001` |
| Patient Weight | `rdfs:isDefinedBy` | `https://www.cdc.gov/nchs/fastats/body-measurements.htm` |
| Systolic Blood Pressure | `rdfs:isDefinedBy` | `https://professional.heart.org/en/science-news/2017-hypertension-clinical-guidelines` |
| Systolic Blood Pressure | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q82642` |
| Systolic Blood Pressure | `skos:exactMatch` | `http://snomed.info/id/271649006` |
| Systolic Blood Pressure | `rdfs:seeAlso` | `https://loinc.org/8480-6/` |
| Visit Date | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q577` |
| Visit Date | `rdf:type` | `https://schema.org/DateTime` |

## Using This Model with AI Assistants

### Quick Start Prompt

Copy and customize this prompt for your AI assistant:

```
I have an SDC4-compliant data model called "Healthcare Record" and need help
creating a data entry application.

**Attached Files:**
- XML Schema (dm-ftluo2nybgxmn7mawttoos20.xsd)
- Example instance (dm-ftluo2nybgxmn7mawttoos20.xml)
- HTML documentation (dm-ftluo2nybgxmn7mawttoos20.html)

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
"Healthcare Record" SDC4 schema (dm-ftluo2nybgxmn7mawttoos20.xsd).
Include CSV import, SQLite storage, forms with validation, and a data browser.
Use the sdcvalidator library for full SDC4 XML validation.
```

**React/Next.js Web App:**
```
Build a React/Next.js application with a REST API backend for the
"Healthcare Record" schema (dm-ftluo2nybgxmn7mawttoos20.xsd).
Frontend: data entry forms and browser using the schema structure.
Backend: Node.js/Express with PostgreSQL for storage.
```

**Django Admin Interface:**
```
Generate Django models from the "Healthcare Record" SDC4 schema (dm-ftluo2nybgxmn7mawttoos20.xsd)
with a custom admin interface.
Each cluster should be a Django model with appropriate field types.
Include CSV import/export via Django admin actions.
```

**REST API Only:**
```
Create a FastAPI REST API for the "Healthcare Record" data model (dm-ftluo2nybgxmn7mawttoos20.xsd).
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
validator = SDC4Validator('dm-ftluo2nybgxmn7mawttoos20.xsd')

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
validator = SDC4Validator('dm-ftluo2nybgxmn7mawttoos20.xsd')
recovered_tree = validator.validate_with_recovery('data.xml')
validator.save_recovered_xml('recovered_data.xml', 'data.xml')
```

**Note**: XML validation is completely optional. You can build applications
using only JSON, implement custom validation, or add sdcvalidator later.

## GQL Graph Database Usage

The `dm-ftluo2nybgxmn7mawttoos20.gql` file contains GQL CREATE statements for property
graph databases (e.g., Neo4j, Amazon Neptune, TigerGraph).

### Loading into Neo4j

```cypher
// Load the GQL file content
// Copy the CREATE statements from dm-ftluo2nybgxmn7mawttoos20.gql into the Neo4j browser
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

The `dm-ftluo2nybgxmn7mawttoos20.html` file contains human-readable descriptions,
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
