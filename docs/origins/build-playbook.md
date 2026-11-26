# Build Playbook — Cordova OS

The phase-by-phase execution plan for building the Republic of Cordova demo, from template authoring through deployed demo with dashboards.

**Companion documents:**
- `concepts.md` — Architecture, domains, RBAC, proof points (the *what*)
- `the-contagion.md` — Demo narrative and presentation script (the *story*)
- `build-playbook.md` — This document: execution workflow (the *how*)

---

## The Positioning Narrative: "Vibe Coding for Enterprise"

"Vibe coding" — using AI to generate entire applications — normally fails in the enterprise because the AI hallucinates the data model. It creates spaghetti code where `Customer_ID` is a string in one table and an integer in another. There are no guardrails.

SDCStudio changes this equation:

> "We used SDCStudio to lock down the **Data Physics** (the hard part). Once the structure was compiled, we let the AI 'vibe code' the **Interface** (the easy part)."

This positions SDCStudio as **guardrails for Generative Engineering** — the tool that makes AI-assisted development safe for enterprise data.

### The Three Phases

| Phase | Analogy | Who Does It | What Happens |
|-------|---------|-------------|-------------|
| **1. Constitution** | Writing the laws | Human (Tim) in SDCStudio | Import templates, compose components, publish data models |
| **2. Enforcement** | Compiling the laws | SDCStudio App Generator | Generates Django apps with models, forms, validation, RDF emission |
| **3. Paint** | Decorating the building | Claude + Graphwise team | Synthetic data, styled UI, SPARQL queries, dashboards |

**The key insight:** Phase 1 is the only phase that requires domain expertise. Phase 2 is deterministic (compiler output). Phase 3 is where AI shines — because the data model is already locked down, the AI can't corrupt the structure. It can only make it prettier.

### SDCStudio as Developer Tool, Not No-Code Wizard

SDCStudio generates **scaffolding**: Django apps with models, forms, basic views, validation logic, and RDF triple emission. The generated UI is intentionally generic.

This is a feature, not a limitation:

- **If SDCStudio generated "perfect" custom UIs**, it would look like a black-box app builder (which investors hate because it feels rigid and vendor-locked).
- **By generating scaffolding**, SDCStudio is a **Developer Tool** that writes the boring boilerplate and lets developers (or AI) handle the frontend.

The pitch: *"SDCStudio writes the sheet music so the AI can play the piano."*

---

## Phase 1: Constitution — Template Authoring

**Goal:** Define all 10 domain data models in SDCStudio using the template import system.

**Who:** Tim Cook, in the SDCStudio web interface.

**Duration:** This is the "2 hours defining the laws of the Republic of Cordova" narrative beat.

### Step 1.1: Import the Cordova Bundle

Import `templates/01-cordova-bundle.md` first. This creates the **Cordova** project in SDCStudio and defines the 18 Cordova-specific components:

| Component | Type | Purpose |
|-----------|------|---------|
| National ID (CID) | xdstring | Identity anchor (COR-PPCC-NNNNNN format) |
| Business Registry Number | xdstring | Business identifier (BIZ-NNNNNN) |
| Cordova Phone Number | xdstring | +99-PPP-NNN-NNNN format |
| Province | xdtoken | 3 provinces (Aldara, Brevina, Celara) |
| City | xdtoken | 9 cities |
| Area Code | xdtoken | 9 area codes |
| Province Code | xdtoken | AL, BR, CE |
| City Code | xdtoken | 01-03 per province |
| Cordova Email Address | xdstring | @cordomail.co / @novamail.co / @portocorreo.co |
| Relationship Type | xdtoken | Spouse, Parent, Child, Sibling, Grandparent |
| Marital Status | xdtoken | Single, Married, Divorced, Widowed |
| Property Type (Cordova) | xdtoken | Residential, Commercial, Agricultural, Government |
| Tax Filing Status | xdtoken | Individual, Joint, Business, Estate |
| Business Type (Cordova) | xdtoken | Sole Proprietor, Partnership, Corporation, Cooperative |
| Employment Status (Cordova) | xdtoken | Full-Time, Part-Time, Contract, etc. |
| Parcel Number | xdstring | Land registry identifier |
| Charge Category (Cordova) | xdtoken | Misdemeanor categories |
| Disposition (Cordova) | xdtoken | Fine, Community Service, Case Dismissed, Pending |

**Prerequisite:** The Default, NIEM, and NIH_CDE projects must already exist in SDCStudio with their component libraries. These are populated from the existing template repositories:
- `/home/twcook/GitHub/CDEs/SDCTemplates/` (NIH CDE bundles)
- `/home/twcook/GitHub/niem-model/SDCTemplates/` (NIEM bundles)

### Step 1.2: Import Domain Templates

Import the 10 domain data model templates in any order (the bundle must be imported first):

| Template | Domain | Clusters | Reuses From |
|----------|--------|----------|-------------|
| `dm-civil-registry.md` | Civil Registry | 4 | Cordova, Default, NIH_CDE |
| `dm-maritime-port.md` | Maritime / Port | 5 | NIEM, Cordova, NIH_CDE |
| `dm-healthcare.md` | Healthcare | 7 | NIH_CDE, Cordova |
| `dm-employment.md` | Employment | 2 | Cordova, NIEM, NIH_CDE |
| `dm-business-registry.md` | Business Registry | 3 | Cordova, NIEM, Default |
| `dm-education.md` | Education | 3 | Cordova, NIEM, NIH_CDE |
| `dm-law-enforcement.md` | Law Enforcement | 5 | NIEM, Cordova |
| `dm-tax-revenue.md` | Tax & Revenue | 4 | Cordova, NIEM |
| `dm-property-registry.md` | Property Registry | 5 | Cordova, NIEM, Default |
| `dm-vital-statistics.md` | Vital Statistics | 6 | Cordova, NIEM, NIH_CDE |

**Total:** 44 clusters across 10 data models.

### Step 1.3: Review and Publish

For each imported data model:
1. Review the component mappings in SDCStudio (verify all `@ProjectName:Component` references resolved)
2. Add any `act` (access control) metadata per the DPV role matrix in concepts.md
3. **Publish** — this triggers XSD generation, XML instance generation, and all ancillary outputs
4. Verify the generated XSD validates correctly

**Milestone:** All 10 data models published in SDCStudio. Each has generated XSD, XML placeholder instances, JSON-LD, SHACL, and GQL outputs.

---

## Phase 2: Enforcement — App Generation

**Goal:** Generate the 10 Django apps and assemble the Cordova OS project.

**Who:** SDCStudio App Generator (automated), then Tim for project assembly.

**Narrative beat:** *"The tool wrote 100% of the database integrity code. Zero human errors."*

### Step 2.1: Generate Django Apps

For each published data model, use SDCStudio's App Generator:
1. Select the data model
2. Choose "Generate Django App"
3. SDCStudio produces a complete Django app directory:
   - `models.py` — Django models matching the SDC data model
   - `forms.py` — Validated against XSD schema
   - `views.py` — CRUD views with RDF triple emission on save
   - `admin.py` — Django admin configuration
   - `urls.py` — URL routing
   - `templates/` — Basic HTML templates
   - `rdf_emitter.py` — Writes triples to GraphDB/Fuseki
   - `xsd_schema.py` — Carries the `act` policies

### Step 2.2: Create the Cordova OS Project

Create the Django project shell:

```
cordova/
├── cordova/                      # Project settings
│   ├── settings.py               # All 10 apps in INSTALLED_APPS
│   ├── urls.py                   # Includes all 10 app URL configs
│   └── wsgi.py
├── shell/                        # Hand-written shared UI
│   ├── templates/
│   │   ├── base.html             # Government terminal aesthetic
│   │   ├── role_selector.html    # DPV role picker
│   │   └── dashboard.html        # Cross-domain landing page
│   └── views.py
├── civil_registry/               # Generated
├── vital_statistics/             # Generated
├── healthcare/                   # Generated
├── education/                    # Generated
├── employment/                   # Generated
├── business_registry/            # Generated
├── property_registry/            # Generated
├── tax_revenue/                  # Generated
├── law_enforcement/              # Generated
├── maritime/                     # Generated
└── manage.py
```

The `shell/` app is the **only hand-written code**. It provides:
- Authentication and role selection
- DPV role evaluation middleware (reads `act` policies, filters cell visibility)
- Navigation between the 10 domain apps
- Connection configuration for GraphDB/Fuseki

### Step 2.3: Install and Verify

1. Copy all 10 generated app directories into `cordova/`
2. Add all apps to `INSTALLED_APPS` in settings
3. Run migrations: `python manage.py migrate`
4. Verify: `python manage.py check`
5. Start the dev server and confirm all 10 apps load with empty data

**Milestone:** Cordova OS project runs locally. All 10 domain apps installed, migrated, and serving empty forms. No data yet.

---

## Phase 3: Paint — Synthetic Data, UI, Queries

**Goal:** Populate the demo with realistic data, style the UI, and build the SPARQL queries.

**Who:** Claude (synthetic data generation, UI styling, query writing) + Tim (review and refinement).

**Narrative beat:** *"We built a government-scale OS in a weekend because we didn't have to debate the data model. The AI just read the SDC output and painted the pixels."*

### Step 3.1: Understand the Schema from Placeholder XML

SDCStudio generates `_PLACEHOLDER_` XML instance documents for each published data model. These are structurally complete XML files with placeholder values that conform to the generated XSD.

**The data generation pipeline:**
1. Read each domain's `_PLACEHOLDER_` XML instance
2. Understand the exact field structure, types, constraints, and enumerations
3. Generate synthetic data that conforms precisely to the schema
4. Load via Django management commands or direct database insertion
5. Emit RDF triples to GraphDB/Fuseki

The placeholder XML instances are the contract. Every synthetic record must validate against the XSD. This is how the "Data Physics" guarantee extends to the demo data — even the fake data is structurally governed.

### Step 3.2: Foundation Data

Generate the base population before any domain-specific records:

**Geography** (derived from concepts.md):
- 3 provinces, 9 cities, 9 area codes
- Already defined as code lists in the Cordova bundle

**People** (25,000):
- Cordovan names (Spanish-influenced)
- National IDs in COR-PPCC-NNNNNN format
- Age distribution per concepts.md demographics table
- Addresses distributed across 9 cities
- Family relationships (2-6 member units)
- Phone numbers, email addresses

**Businesses** (~1,500):
- Business names appropriate to Cordova
- Registry numbers (BIZ-NNNNNN)
- Officers linked to people from the population
- Industry distribution across all 11 categories
- Addresses across 9 cities (concentrated in Porto Sereno and Novaciudad)

**Contagion Seed Characters:**
- Carlos Mendoza (COR-AL01-271845) — with full backstory
- Elena Mendoza (COR-CE01-271903) — with employment and property records
- Dr. Isabel Reyes (COR-AL01-195322) — healthcare provider
- Governor Tomás Ávila (COR-CE01-104287) — Auditor role
- Captain Rodrigo Salazar (foreign national)
- Sgt. Maria Santos (CNP-0847)
- Dr. Lucía Ferrer (COR-AL01-188934) — Provincial Health Officer
- Universidad Nacional de Cordova (BIZ-000847) with ~26 faculty and ~312 students
- Pacífico Meridional Shipping S.A. (BIZ-001102)
- *MV Estrella del Sur* (IMO 9847321) with 18 crew

### Step 3.3: Domain Records by Priority

**Priority 1 — Contagion Core:**

| Domain | Record Count | Key Records |
|--------|-------------|-------------|
| Civil Registry | 25,000 | All people + family relationships |
| Maritime | ~2,000 port calls, ~200 vessels | MV Estrella del Sur, PC-2026-0142 |
| Healthcare | ~20,000 patient records | Carlos Mendoza's admission, vitals, labs |

**Priority 2 — Employment & Institutional Links:**

| Domain | Record Count | Key Records |
|--------|-------------|-------------|
| Employment | ~15,000 employment records | Elena at UNC, Carlos at Pacífico Meridional |
| Business Registry | ~1,500 businesses | UNC (BIZ-000847), Pacífico (BIZ-001102) |
| Education | ~4,000 enrollment records | 312 active students at UNC |

**Priority 3 — Governance & Finance:**

| Domain | Record Count | Key Records |
|--------|-------------|-------------|
| Law Enforcement | ~1,500 incidents | IR-2026-AL-00847 (quarantine) |
| Tax & Revenue | ~20,000 filings | Carlos and Elena's tax records |
| Property Registry | ~8,000 properties | Elena's condo at 18 Av. Universidad |
| Vital Statistics | ~30,000 certificates | Birth/death certs for Mendoza family |

### Step 3.4: RDF Triple Loading

After generating records in Django, emit RDF triples to GraphDB/Fuseki:

1. Each domain app's `rdf_emitter.py` converts Django model instances to RDF triples
2. Triples use SDC4 ontology URIs — same predicates across all 10 apps
3. Load into a single named graph per domain (or a shared default graph)
4. Verify with test SPARQL queries

**Estimated triple count:** ~2-3 million triples across all 10 domains for 25,000 people.

### Step 3.5: UI Styling

The generated apps have generic Django templates. Phase 3 styling:

1. **Base template** (`shell/templates/base.html`): Government terminal aesthetic — dark background, monospace headers, amber/green accent colors. Think NORAD meets modern gov.uk.
2. **Role selector**: Clean card-based layout with DPV role descriptions
3. **Domain dashboards**: Each app gets styled list views and detail views
4. **Redaction UI**: Black cells with lock icon, DPV tooltip on hover
5. **Override UI**: Amber glow on overridden cells, override banner with warrant details
6. **Refusal UI**: Visual bounce-back animation, XML tree mesh visualization, red pulse

**Color language** (from director's notes):
- White — Accessible data
- Black — Redacted cells
- Amber — Overridden data (active warrant)
- Red — Refused composition

### Step 3.6: SPARQL Queries

Build the 6 pre-built cross-domain queries from concepts.md, plus the Contagion-specific queries from the-contagion.md:

**Pre-built queries:**
1. Complete Government Profile (Person → all 10 domains)
2. Economic Network Analysis (Business → employees, tax, port, property)
3. Social Services Identification (medical + unemployment + no property)
4. Supply Chain Provenance (vessel → cargo → customs → business → tax)
5. Family Economic Unit (person → family → income, property, tax, education)
6. Institutional Impact (university → graduates → employers → tax)

**Contagion queries:**
7. Contact Tracing (person → family → employment → education → property)
8. Extended Contact Trace (Elena's workplace contacts, Jan 6-15)
9. Geographic Exposure Map (contacts by province/city)

---

## Phase 4: Graphwise Dashboards

**Goal:** Professional graph visualizations and interactive dashboards.

**Who:** Graphwise semantic engineering team + Tim for data/query support.

### The Handoff

Tim provides:
- **The Minting Press:** SDCStudio-generated schema (XSD, SHACL, ontology)
- **The Raw Data:** Cordova dataset in GraphDB (~2-3M triples)
- **The Queries:** 9 pre-built SPARQL queries with expected results
- **The Narrative:** The Contagion scenario script with 7 demo beats

Graphwise provides:
- **The Lens:** Interactive dashboards built on the SDC data
- **Node-link visualizations** for contact tracing and economic networks
- **Choropleth maps** for geographic distribution
- **Timeline views** for the Contagion sequence
- **Role-filtered views** that change based on DPV role selection

### Dashboard Concepts

| Dashboard | Primary Domains | Visualization |
|-----------|----------------|---------------|
| **Citizen 360** | All 10 domains | Node-link graph centered on a person |
| **Economic Atlas** | Business, Employment, Tax, Property | Choropleth map by city/province |
| **Port Operations** | Maritime, Business, Tax | Timeline + Sankey diagram (cargo flow) |
| **Public Health** | Healthcare, Vital Statistics, Civil Registry | Demographic charts + geographic heat map |
| **Justice Overview** | Law Enforcement, Civil Registry | Incident map + disposition breakdown |
| **Contagion Trace** | Maritime, Civil, Employment, Education, Property | Animated contact trace expanding through the graph |

### The Partnership Value

Once the Graphwise engineers see how clean the SDC data is to query (stable schema, consistent predicates, no mapping required), they become internal advocates. The data structure isn't a custom mess they have to reverse-engineer — it's a Reference Model they can rely on.

---

## Phase 5: Deployment

**Goal:** Live demo on GCP accessible for presentations.

### Infrastructure

| Service | Purpose | GCP Resource |
|---------|---------|-------------|
| Cordova OS (Django) | Application server | Cloud Run (2Gi, autoscale 1-5) |
| PostgreSQL | Relational data | Cloud SQL |
| GraphDB | Triple store + SPARQL | Cloud Run or GCE (depends on Graphwise requirements) |
| Graphwise | Dashboards | Per Graphwise deployment model |
| Redis | Cache | Memorystore |

### Deployment Steps

1. Dockerize the Cordova OS project (similar to SDCStudio deployment)
2. Provision Cloud SQL with all 10 app migrations
3. Deploy GraphDB with loaded triples
4. Configure Graphwise connection to GraphDB SPARQL endpoint
5. Deploy Cordova OS to Cloud Run
6. Configure domain/SSL
7. Load synthetic data and verify all Contagion scenario beats

---

## Milestones and Checkpoints

| # | Milestone | Depends On | Verification |
|---|-----------|-----------|-------------|
| M1 | All 10 templates imported into SDCStudio | Bundle imported first | All `@reuse` references resolve |
| M2 | All 10 data models published | M1 | XSD validates, placeholder XML generated |
| M3 | 10 Django apps generated | M2 | Each app directory has models/forms/views/rdf_emitter |
| M4 | Cordova OS project assembled | M3 | `manage.py check` passes, all apps in INSTALLED_APPS |
| M5 | Foundation data loaded | M4 | 25,000 people, 1,500 businesses in database |
| M6 | Contagion seed data loaded | M5 | All named characters and key records present |
| M7 | Priority 1 records loaded | M6 | Civil Registry, Maritime, Healthcare populated |
| M8 | **Contagion scenario runs end-to-end** | M7 | Cross-domain query returns 356 contacts, redaction works, override works, refusal works |
| M9 | All domain records loaded | M8 | ~100,000 records across 10 domains |
| M10 | RDF triples in GraphDB | M9 | All 9 SPARQL queries return expected results |
| M11 | UI styled | M8+ | Color language implemented, DPV tooltips, override/refusal UX |
| M12 | Graphwise dashboards | M10 | 6 dashboards functional with role-filtered views |
| M13 | Deployed to GCP | M11, M12 | Live URL, all 7 demo beats executable |

**Critical path:** M1 → M2 → M3 → M4 → M5 → M6 → M7 → **M8** (Contagion works) → everything else.

M8 is the proof-of-concept gate. If the Contagion scenario runs end-to-end with just 3 domains, the remaining 7 domains and the polish are incremental.

---

## What We Have Now

| Artifact | Status | Location |
|----------|--------|----------|
| Architecture and domain specs | Done | `design/concepts.md` |
| Contagion narrative + demo script | Done | `design/the-contagion.md` |
| Build playbook | Done | `design/build-playbook.md` (this document) |
| Strategic notes | Done | `design/other_thoughts.md` |
| Cordova component bundle | Done | `templates/01-cordova-bundle.md` |
| 10 domain templates | Done | `templates/dm-*.md` |
| Repository documentation | Done | README, LICENSE, CONTRIBUTING, etc. |
| SDCStudio component libraries | Existing | Default (12), NIEM (309), NIH_CDE (221) |

**Next action:** Phase 1, Step 1.1 — Import `01-cordova-bundle.md` into SDCStudio.
