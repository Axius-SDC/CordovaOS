# Plan: Build CordovaOS Demo Data for Bulk Import

## Context

CordovaOS is a cross-domain interoperability demo for SDC4 — a fictional island nation (Republic of Cordova) with 10 government domains. The demo's centerpiece is "The Contagion," a 7-beat crisis narrative showing how SDC4 enables cross-domain queries with zero integration code. Data will be created as XML instance files and bulk-imported into each app via `/import_data/{app_name}/` directories.

**Prerequisite**: All 10 data models must be regenerated in SDCStudio, downloaded, and the CordovaOS project rebuilt before data generation begins. The XML template files (`dm-{ct_id}.xml`) from each app's `mediafiles/dmlib/` define the exact structure each XML instance must follow.

## Data Generation Sequence

### Phase 1: Foundation Data (Civil Registry + Vital Statistics)

Everything else depends on people existing first.

**1a. Civil Registry** — `/import_data/civil_registry/`
- Contagion cast with fixed CIDs (Carlos, Elena, Dr. Reyes, Governor Avila, Dr. Ferrer)
- ~200 additional named residents to support contact tracing (UNC faculty/staff, building neighbors, port workers)
- Family relationships linking cast members and key contacts
- Sources: `the-contagion.md` cast list, `dm-civil-registry.md` template

**1b. Vital Statistics** — `/import_data/vital_statistics/`
- Birth certificates for all civil registry persons
- Marriage certificates for married couples (Carlos's parents, etc.)
- Sources: `dm-vital-statistics.md` template

### Phase 2: Institutional Data (Businesses, Property, Education)

These establish the organizations and places the cast interacts with.

**2a. Business Registry** — `/import_data/business_registry/`
- Pacifico Meridional Shipping S.A. (BIZ-001102) — vessel operator
- Universidad Nacional de Cordova (BIZ-000847) — Elena's employer
- Porto Sereno General Hospital
- ~20 additional businesses for economic context
- Sources: `dm-business-registry.md` template

**2b. Property Registry** — `/import_data/property_registry/`
- Carlos's residence (Porto Sereno)
- Elena's residence (Campoluz)
- Hospital property, university campus, port facility
- ~30 additional properties
- Sources: `dm-property-registry.md` template

**2c. Education** — `/import_data/education_record/`
- Elena as faculty at UNC
- ~50 current UNC students (subset of the 312 for contact tracing)
- A few completed enrollments for cast members
- Sources: `dm-education.md` template

### Phase 3: Economic Data (Employment, Tax)

**3a. Employment** — `/import_data/employment_record/`
- Carlos — employed by Pacifico Meridional Shipping
- Elena — Associate Professor, UNC
- Dr. Reyes — Porto Sereno General Hospital
- Dr. Ferrer — Provincial Health Officer, Aldara
- Sgt. Santos — Cordova National Police
- ~30 additional employment records (UNC staff, port workers)
- Sources: `dm-employment.md` template

**3b. Tax & Revenue** — `/import_data/tax_revenue/`
- Tax filings for key cast members and businesses
- ~30 filings to demonstrate cross-domain tax-to-employment links
- Sources: `dm-tax-revenue.md` template

### Phase 4: Operational Data (Maritime, Healthcare, Law Enforcement)

These are the domains where the Contagion narrative plays out.

**4a. Maritime** — `/import_data/maritime/`
- MV Estrella del Sur (IMO 9847321) port call PC-2026-0142
- 18 crew manifest entries (Carlos + 17 crew)
- Cargo manifest entries
- Captain Rodrigo Salazar (foreign national, no CID)
- ~5 additional recent port calls for context
- Sources: `dm-maritime-port.md` template, `the-contagion.md` Beat 1

**4b. Healthcare** — `/import_data/healthcare_record/`
- Carlos's patient record with visit on Jan 14, 2026 (the symptomatic presentation)
- Vitals, lab results for Carlos
- Elena's patient record (baseline, no symptoms)
- Dr. Reyes as provider
- ~20 additional patient records
- Sources: `dm-healthcare.md` template, `the-contagion.md` Beats 3-5

**4c. Law Enforcement** — `/import_data/law_enforcement/`
- Quarantine enforcement records (Beat 5)
- Sgt. Santos as reporting officer
- Quarantine zone records for the port area
- ~5 routine incident reports for context
- Sources: `dm-law-enforcement.md` template, `the-contagion.md` Beat 5

### Phase 5: Verification

After bulk import of all apps:
1. Run each of the 7 SPARQL queries from `/home/twcook/GitHub/CordovaOS/sparql/`
2. Verify Query 07 (Contagion Contact Tracing) returns the expected contact tiers
3. Verify Query 01 (Complete Government Profile) for Carlos shows records across all domains
4. Spot-check cross-domain joins via shared National ID ct_id

## Data Scale

**Demo-appropriate scale** (~400-500 XML files total), not the full 25,000-person synthetic population from `SYNTHETIC_DATA_PLAN.md`. Enough to:
- Tell the Contagion story convincingly
- Make SPARQL queries return meaningful multi-hop results
- Show each domain app with realistic content
- Keep generation and import fast

The full 25,000-person dataset can be a follow-up effort once the demo narrative is validated.

## Implementation Approach

For each app:
1. Read the app's XML template file (`dm-{ct_id}.xml`) to get the exact XML structure
2. Write a Python script that generates XML instances conforming to that schema
3. Each instance gets a unique `instance_id` (i-{cuid2}) and `creation_timestamp`
4. Output files to `/import_data/{app_name}/`
5. Bulk import via each app's admin UI

Scripts will live in a `datagen/` directory in the CordovaOS repo, one module per domain, with shared utilities for CID generation, name generation, and date handling.

## Key Reference Documents

- Cast & narrative: `/home/twcook/GitHub/SDC_Demo/design/the-contagion.md`
- Domain templates: `/home/twcook/GitHub/SDC_Demo/templates/dm-*.md`
- Cordova components: `/home/twcook/GitHub/SDC_Demo/templates/01-cordova-bundle.md`
- SPARQL queries: `/home/twcook/GitHub/CordovaOS/sparql/*.rq`
- Data plan (reference): `/home/twcook/GitHub/CordovaOS/design/SYNTHETIC_DATA_PLAN.md`
