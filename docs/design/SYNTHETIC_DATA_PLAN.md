# CordovaOS Synthetic Data Generation Plan

## Overview

Generate realistic synthetic data for the Republic of Cordova: 25,000 people, ~1,500 businesses, and all derived records across 10 domains. Data must support the Contagion narrative and all 7 SPARQL queries.

## Architecture

One Python package (`datagen/`) with a management command: `python manage.py generate_cordova_data`.

The generator runs in phases to respect cross-domain dependencies.

```
datagen/
├── __init__.py
├── management/
│   └── commands/
│       └── generate_cordova_data.py
├── geography.py          # Provinces, cities, area codes
├── population.py         # 25,000 people with demographics
├── families.py           # Family unit generation
├── businesses.py         # 1,500 businesses
├── contagion.py          # Named cast for the scenario
├── generators/
│   ├── __init__.py
│   ├── civil_registry.py
│   ├── vital_statistics.py
│   ├── healthcare.py
│   ├── education.py
│   ├── employment.py
│   ├── business_registry.py
│   ├── property_registry.py
│   ├── tax_revenue.py
│   ├── law_enforcement.py
│   └── maritime.py
└── utils.py              # CID generation, date ranges, faker helpers
```

## Phase 1: Foundation Data

### Geography (geography.py)

```python
PROVINCES = {
    'AL': {'name': 'Aldara', 'capital': 'Porto Sereno',
           'cities': {'01': 'Porto Sereno', '02': 'Vistamar', '03': 'Rioseco'}},
    'BR': {'name': 'Brevina', 'capital': 'Campoluz',
           'cities': {'01': 'Campoluz', '02': 'Tierraverde', '03': 'Montecara'}},
    'CE': {'name': 'Celara', 'capital': 'Novaciudad',
           'cities': {'01': 'Novaciudad', '02': 'Piedrasol', '03': 'Lagunavista'}},
}

AREA_CODES = {
    'Porto Sereno': '100', 'Vistamar': '110', 'Rioseco': '120',
    'Campoluz': '200', 'Tierraverde': '210', 'Montecara': '220',
    'Novaciudad': '300', 'Piedrasol': '310', 'Lagunavista': '320',
}

CITY_POPULATIONS = {
    # Approximate distribution of 25,000
    'Novaciudad': 5500,    # National capital
    'Porto Sereno': 4500,  # Port city
    'Campoluz': 3500,      # University city
    'Vistamar': 2000,
    'Piedrasol': 2000,
    'Tierraverde': 2000,
    'Rioseco': 1800,
    'Montecara': 1800,
    'Lagunavista': 1900,
}
```

### Population (population.py)

Generate 25,000 people with:

| Field | Source |
|-------|--------|
| National ID (CID) | `COR-{province}{city}-{seq:06d}` |
| Given Name | Spanish/Latin American name pool (~200 first names) |
| Surname | Spanish/Latin American surname pool (~150 surnames) |
| Date of Birth | Distributed per age demographics |
| Sex | Male/Female/Intersex (49%/49%/2%) |
| City | Distributed per CITY_POPULATIONS |
| Province | Derived from city |
| Phone | `+99-{area_code}-{NNN}-{NNNN}` |
| Email | `{name}@{provider}.co` (cordomail, novamail, portocorreo) |
| Marital Status | Single/Married/Divorced/Widowed (age-appropriate) |

**Age distribution:**

| Range | % | Count |
|-------|---|-------|
| 0-4 | 4% | 1,000 |
| 5-17 | 12% | 3,000 |
| 18-34 | 18% | 4,500 |
| 35-50 | 24% | 6,000 |
| 51-70 | 26% | 6,500 |
| 71-85 | 12% | 3,000 |
| 86-93 | 4% | 1,000 |

### Families (families.py)

Group people into ~6,000 family units:
- 2-person (young couple, no kids): ~1,500
- 3-4 person (couple + 1-2 kids): ~2,500
- 5-6 person (couple + 3-4 kids or multi-gen): ~1,000
- Single-person: ~1,000 (elderly, young adults)

Relationship types: spouse, parent, child, sibling, grandparent.

Family members share the same city. Some cross-city family links (married person moved).

### Businesses (businesses.py)

Generate ~1,500 businesses:

| Field | Values |
|-------|--------|
| BRN | `BIZ-{seq:06d}` |
| Name | Generated from industry + location |
| Type | sole_proprietor (40%), corporation (30%), partnership (20%), cooperative (10%) |
| Industry | Agriculture, Fishing, Retail, Services, Manufacturing, Education, Healthcare, Transport, Government, Tourism |
| City | Concentrated in Novaciudad (30%) and Porto Sereno (25%) |
| Status | Active (92%), Dissolved (8%) |
| Officers | 1-3 per business, linked to adult population |

**Key named businesses:**
- `BIZ-000847` — Universidad Nacional de Cordova (Campoluz)
- `BIZ-001102` — Transportes del Sur (Porto Sereno, shipping)
- `BIZ-000523` — Porto Sereno General Hospital
- `BIZ-000312` — Government of Cordova (Novaciudad)

### Contagion Cast (contagion.py)

Named characters with fixed CIDs:

| Character | CID | Role |
|-----------|-----|------|
| Carlos Mendoza | COR-AL01-271845 | Patient zero, crew member |
| Elena Mendoza | COR-CE01-271903 | Carlos's sister, teacher at UNC |
| Dr. Isabel Reyes | COR-AL01-284521 | Attending physician |
| Governor Maria Ávila | COR-CE01-100001 | Auditor role |
| Captain Luis Salazar | COR-AL01-195432 | MV Estrella del Sur captain |
| Sgt. Rosa Santos | COR-AL01-312876 | Quarantine enforcement |
| Dr. Fernando Ferrer | COR-BR01-267890 | University epidemiologist |

**MV Estrella del Sur:**
- IMO: 9847321
- Flag State: Panama
- Port Call ID: PS-2026-0142
- Arrival: 2026-01-14T06:30:00
- 18 crew members (Carlos + 17 others)

## Phase 2: Domain Record Generation

Each generator creates Django model instances using the generated app's models.

### Civil Registry (civil_registry.py)
- **Records**: 25,000 (one per person)
- **Key fields**: National ID, name, DOB, sex, address, phone, email, marital status
- **Sub-clusters**: Current Address (street, city, province), Contact Information (phone, email), Family Relationships (relationship type, related person CID)

### Vital Statistics (vital_statistics.py)
- **Birth certificates**: 25,000 (one per person, linked to parents)
- **Death certificates**: ~1,200 (4.8% mortality, mostly elderly)
- **Marriage certificates**: ~4,000 (married couples)
- **Divorce decrees**: ~800 (divorced persons)
- Attestation: registrar name, office, date

### Healthcare (healthcare.py)
- **Patient records**: ~22,000 (88% of population have at least one record)
- **Visits**: ~60,000 (avg 2.7 visits per patient)
- **Allergies**: ~3,000 people (12%)
- **Chronic conditions**: ~4,000 people (16%, skewed to older)
- **Medications**: ~5,000 active prescriptions
- **Vaccinations**: ~50,000 records (avg 2 per person with records)
- **Lab results**: ~15,000 (blood type for all patients + panels)
- Carlos Mendoza: tropical disease presentation, restricted medical record

### Education (education.py)
- **Current enrollment**: ~4,000 (school age + university)
- **Completed records**: ~15,000 (adults with education history)
- **Credentials**: ~8,000 (degrees, certifications)
- Elena Mendoza: Professor at Universidad Nacional de Cordova
- ~312 students currently enrolled at UNC (for Contagion contact count)

### Employment (employment.py)
- **Current employment**: ~12,000 (adults 18-70, ~70% employment rate)
- **Historical records**: ~20,000 (including past jobs)
- **Unemployment**: ~8% of working-age adults
- Elena Mendoza: employed at UNC (employer BRN: BIZ-000847)
- 26 coworkers at UNC (for Contagion contact count)

### Business Registry (business_registry.py)
- **Records**: ~1,500 businesses
- **Officers**: ~3,000 officer records (1-3 per business)
- Transportes del Sur (BIZ-001102): shipping company, vessel operator

### Property Registry (property_registry.py)
- **Properties**: ~8,000
- **Type distribution**: Residential 65%, Commercial 15%, Agricultural 15%, Government 5%
- **Ownership**: ~80% of adults own/co-own at least one property
- **Transfer history**: ~2,000 transfers in last 5 years
- **Liens**: ~800 active liens

### Tax and Revenue (tax_revenue.py)
- **Annual filings**: ~30,000 (multiple years for working adults)
- **Tax types**: Income Tax, Business Tax, Property Tax, Port Fee, Fine Collection, Import Duty
- **Cross-references**: Employment income, property assessments, business filings, port fees
- Payment status distribution: Paid (85%), Overdue (8%), Payment Plan (5%), Waived (2%)

### Law Enforcement (law_enforcement.py)
- **Incident reports**: ~2,000
- **Offenders**: ~1,500 unique people (5-8% of adults)
- **Charges**: petty theft, public intoxication, trespassing, disorderly conduct, traffic violations, minor vandalism
- **Quarantine records**: 3-5 (including Contagion quarantine zone around Porto Sereno port district)
- Sgt. Santos: reporting officer for quarantine enforcement

### Maritime (maritime.py)
- **Vessels**: ~200
- **Port calls**: ~2,000 per year (generate 1 year of data)
- **Cargo manifests**: ~5,000 (multiple cargo types per port call)
- **Crew records**: ~3,000 (mix of Cordovan nationals and foreign)
- MV Estrella del Sur: Port Call PS-2026-0142, 18 crew including Carlos

## Phase 3: RDF Triple Emission

After Django model instances are created, each app's RDF emitter extracts triples to the GraphDB triplestore. This uses the generated apps' built-in `rdf_emitter.py` functionality.

```bash
python manage.py generate_cordova_data   # Phase 1+2: create Django records
python manage.py emit_rdf --all          # Phase 3: extract RDF triples to GraphDB
```

## Data Integrity Constraints

Cross-domain consistency requirements:

1. Every person in Civil Registry gets a birth certificate in Vital Statistics
2. Every employed person's employer exists in Business Registry
3. Every property owner exists in Civil Registry (person) or Business Registry (company)
4. Every tax filing references a valid CID or BRN
5. Every port call vessel operator exists in Business Registry
6. Every crew member exists in Civil Registry
7. Every student/teacher's institution exists in Business Registry
8. Every law enforcement incident involves a person in Civil Registry
9. Family relationships are symmetric (if A is parent of B, B is child of A)
10. Contagion cast members have complete records across all relevant domains

## Output Format

Data is loaded directly into Django models via the ORM. Additionally, export to:
- **JSON fixtures** (`datagen/fixtures/`) — for portable demo distribution
- **CSV files** (`datagen/exports/`) — for data inspection and debugging

## Dependencies

- `faker` — name/address/date generation with Spanish locale
- `cuid2` — for generating CUID2 instance IDs
- Standard library `random`, `datetime`, `csv`, `json`
