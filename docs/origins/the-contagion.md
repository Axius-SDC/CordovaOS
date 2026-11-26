# The Contagion — Demo Narrative

A step-by-step scenario that forces all ten Cordova domains to interact, proving cross-domain interoperability, schema-enforced privacy, and governed exceptions in a single demo session.

---

## Cast

### Carlos Mendoza
- **National ID:** COR-AL01-271845
- **Age:** 34
- **Occupation:** Merchant marine engineer, crew of *MV Estrella del Sur*
- **Home address:** 42 Calle de las Flores, Porto Sereno, Aldara
- **Family:** Sister Elena Mendoza (Novaciudad). Parents deceased.
- **Role in narrative:** Patient zero. Arrives sick on a cargo vessel.

### Elena Mendoza
- **National ID:** COR-CE01-271903
- **Age:** 31
- **Occupation:** Associate Professor of Marine Biology, Universidad Nacional de Cordova, Campoluz
- **Home address:** 18 Avenida Universidad, Novaciudad, Celara
- **Employer:** Universidad Nacional de Cordova (BIZ-000847)
- **Family:** Brother Carlos Mendoza (Porto Sereno). Parents deceased.
- **Role in narrative:** Contact #1. The link from port to university campus.

### Dr. Isabel Reyes
- **National ID:** COR-AL01-195322
- **Occupation:** Attending physician, Emergency Medicine, Porto Sereno General Hospital
- **Role in narrative:** Creates the medical record. The Healthcare Provider role in the refusal demo.

### Governor Tomás Ávila
- **National ID:** COR-CE01-104287
- **Occupation:** Governor of the Republic of Cordova
- **Role in narrative:** The Auditor role. Runs the cross-domain query. Encounters the redaction.

### Captain Rodrigo Salazar
- **National ID:** (foreign national — no Cordova CID)
- **Nationality:** Panamanian
- **Occupation:** Master of *MV Estrella del Sur*
- **Role in narrative:** Reports crew illness during customs inspection.

### Officer Maria Santos
- **Badge Number:** CNP-0847
- **Rank:** Sergeant, Cordova National Police, Aldara Provincial Command
- **Role in narrative:** Establishes the quarantine perimeter. Creates the incident report.

---

## The Vessel

**MV Estrella del Sur**
- **IMO Number:** 9847321
- **Flag State:** Panama
- **Vessel Type:** General Cargo
- **Gross Tonnage:** 12,400 GT
- **Operator:** Pacífico Meridional Shipping S.A. (BIZ-001102, registered in Cordova)
- **Last port of call:** Cartagena, Colombia
- **Crew complement:** 18

---

## Timeline

All dates in January 2026.

### Day 1 — Wednesday, January 14

**06:00** — *MV Estrella del Sur* enters Cordova territorial waters, inbound from Cartagena. Pilot boat dispatched from Porto Sereno.

**07:30** — Vessel docks at Berth 7, Porto Sereno International Port.

**08:00** — Captain Salazar submits crew manifest and cargo declaration to Port Authority via the Maritime app.

**Records created:**
- Port Call Record (Port Call ID: `PC-2026-0142`)
- Cargo Manifest: 340 TEU containers, mixed general cargo
- Crew List: 18 crew members, including Carlos Mendoza (COR-AL01-271845), role: Engineer

**08:45** — During routine customs walkthrough, Port Health Officer notices Carlos Mendoza is visibly unwell — fever, chills, labored breathing. Captain Salazar confirms Carlos fell ill two days out of Cartagena.

**09:15** — Port Authority flags Carlos for medical screening. Health screening status updated:

```
Crew Member:     Carlos Mendoza
National ID:     COR-AL01-271845
Health Screening: Referred — Symptomatic (fever, respiratory distress)
Screening Date:  2026-01-14
Screening Notes: Onset approx. Jan 12 per master's report.
                 Referred to Porto Sereno General Hospital.
```

**10:30** — Carlos is transported by ambulance to Porto Sereno General Hospital.

---

### Day 1 — The Medical Record

**11:00** — Dr. Isabel Reyes admits Carlos to the Emergency Department.

**Records created in Healthcare app:**

```
Patient Record
  Patient National ID:    COR-AL01-271845
  Primary Care Provider:  Dr. Isabel Reyes

Visit Record
  Visit Date:             2026-01-14
  Provider Name:          Dr. Isabel Reyes
  Facility:               Porto Sereno General Hospital
  Visit Type:             Emergency
  Reason for Visit:       Fever, respiratory distress, 48hr onset
  Diagnosis:              Suspected Novel Respiratory Pathogen (NRP-C)
  Treatment:              Isolation protocol, broad-spectrum antivirals,
                          respiratory support
  Outcome:                Admitted — Isolation Ward

Vital Signs
  Date Recorded:          2026-01-14
  Temperature:            39.8°C
  Heart Rate:             112 bpm
  Blood Pressure:         138/92 mmHg
  Respiratory Rate:       28/min
  Oxygen Saturation:      91%

Lab Results
  Test Name:              NRP-C PCR Panel
  Result Value:           Positive
  Reference Range:        Negative
  Result Status:          Final
  Date Collected:         2026-01-14
```

**Every cell in this record carries `Restricted:PatientCare` access policy.**

Dr. Reyes contacts the Provincial Health Authority, Aldara. A novel respiratory pathogen from a crew member arriving from South America — this requires immediate public health response.

---

### Day 1 — The Quarantine

**14:00** — Dr. Lucía Ferrer, Provincial Health Officer for Aldara, issues a quarantine order for the Porto Sereno port district.

**15:00** — Sergeant Maria Santos, Cordova National Police, establishes a quarantine monitoring zone.

**Records created in Law Enforcement app:**

```
Incident Report
  Incident Report Number:  IR-2026-AL-00847
  Incident Category:       Public Health Emergency
  Incident Date:           2026-01-14
  Incident Location:       Porto Sereno International Port,
                           Berths 1-12 and adjacent warehouses
  Incident City:           Porto Sereno
  Incident Province:       Aldara
  Incident Summary:        Quarantine zone established per Provincial
                           Health Authority order. Crew member of
                           MV Estrella del Sur admitted to PSGH with
                           suspected novel respiratory pathogen.
                           All 17 remaining crew confined to vessel.
                           Port district access restricted.
  Incident Status:         Open

Quarantine Enforcement
  Quarantine Zone:         Porto Sereno Port District, Berths 1-12,
                           Warehouse Row A-D, Port Admin Building
  Quarantine Start Date:   2026-01-14
  Quarantine End Date:     (null — still active)
  Issuing Authority:       Provincial Health Authority, Aldara
  Compliance Status:       Compliant
```

**16:00** — Port Authority suspends all vessel movements. Two other vessels at berth (fishing trawler *Cordova Star*, container ship *Pacific Horizon*) are ordered to remain docked.

**18:00** — Local news reports: "Porto Sereno port closed due to health emergency. Details not yet available."

---

### Day 2 — Thursday, January 15

**08:00** — Governor Tomás Ávila is briefed by the Minister of Health. Situation summary:

- One crew member hospitalized in isolation
- Port quarantined, 3 vessels and approximately 60 crew members confined
- Diagnosis exists but the Governor does not have medical clearance to see it
- The crew member is a Cordovan national with family contacts on the island

The Governor needs to know: **Who has this person been in contact with since arriving? Where did he go? Who else might be exposed?**

The Governor's staff opens the Cordova OS dashboard and selects the **Auditor** role.

---

## Act II — The Cross-Domain Query

### Scene 1: The Auditor's View

The Governor's analyst logs into Cordova OS as **Auditor** and navigates to the Citizen 360 dashboard. They search for Carlos Mendoza by national ID: `COR-AL01-271845`.

**What the Auditor sees across all ten domains:**

| Domain | Visible Content | Redacted |
|--------|----------------|----------|
| **Civil Registry** | Name, National ID, DOB, address, family: Elena Mendoza (COR-CE01-271903, sister, Novaciudad) | — |
| **Maritime** | Crew member on MV Estrella del Sur, arrived Jan 14, role: Engineer, Port Call PC-2026-0142 | — |
| **Healthcare** | Record exists. Created 2026-01-14 by Dr. Isabel Reyes at Porto Sereno General Hospital. | **Diagnosis: REDACTED** — Purpose Mismatch |
| **Employment** | Employed by Pacífico Meridional Shipping S.A. (BIZ-001102), role: Marine Engineer, since 2019 | — |
| **Law Enforcement** | IR-2026-AL-00847: Quarantine zone established, reference to this individual | — |
| **Tax & Revenue** | Tax filings exist for 2024, 2025. Status: Paid in Full | Amounts redacted |
| **Property Registry** | One property: 42 Calle de las Flores, Porto Sereno. Sole owner. | Assessed value redacted |
| **Business Registry** | Named as crew of vessel operated by BIZ-001102 | — |
| **Education** | No records | — |
| **Vital Statistics** | Birth certificate exists. Parents: deceased (death certificates on file). | — |

The Auditor can see the **shape** of Carlos's life across every domain — but not the medical diagnosis and not the financial details. The governance layer is working.

### Scene 2: The Contact Tracing Query

The analyst runs the cross-domain contact tracing query. This is a single SPARQL query that traverses the graph:

```sparql
# Contact Trace: Starting from a person, find all potential contacts
# through family, employment, education, and maritime connections

PREFIX sdc: <https://semanticdatacharter.org/ont/sdc4/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dpv: <https://w3id.org/dpv#>

SELECT ?contact_name ?contact_id ?relationship ?domain ?location ?connection_path
WHERE {
  # Start: Carlos Mendoza
  ?person sdc:nationalID "COR-AL01-271845" .

  {
    # Path 1: Family relationships (Civil Registry)
    ?person sdc:hasRelationship ?rel .
    ?rel sdc:relatedPerson ?contact .
    ?contact sdc:fullName ?contact_name .
    ?contact sdc:nationalID ?contact_id .
    ?rel sdc:relationshipType ?relationship .
    BIND("Civil Registry" AS ?domain)
    BIND("Direct family" AS ?connection_path)

    # Follow the contact to their employment
    OPTIONAL {
      ?employment sdc:employeeID ?contact_id .
      ?employment sdc:employerName ?employer .
      ?employment sdc:workCity ?location .
    }
  }
  UNION
  {
    # Path 2: Vessel crew (Maritime)
    ?crew_entry sdc:crewMemberID "COR-AL01-271845" .
    ?crew_entry sdc:partOfPortCall ?port_call .
    ?other_crew sdc:partOfPortCall ?port_call .
    ?other_crew sdc:crewMemberName ?contact_name .
    ?other_crew sdc:crewMemberID ?contact_id .
    FILTER(?other_crew != ?crew_entry)
    BIND("Sibling crew" AS ?relationship)
    BIND("Maritime" AS ?domain)
    BIND("Same vessel" AS ?connection_path)
  }
  UNION
  {
    # Path 3: Family → Employment → Co-workers
    ?person sdc:hasRelationship ?rel .
    ?rel sdc:relatedPerson ?family_member .
    ?family_member sdc:nationalID ?family_id .
    ?employment sdc:employeeID ?family_id .
    ?employment sdc:employerBRN ?employer_brn .
    ?coworker_emp sdc:employerBRN ?employer_brn .
    ?coworker_emp sdc:employeeID ?contact_id .
    FILTER(?contact_id != ?family_id)
    ?contact sdc:nationalID ?contact_id .
    ?contact sdc:fullName ?contact_name .
    BIND("Family member's coworker" AS ?relationship)
    BIND("Employment" AS ?domain)
    BIND("Family → Employer → Coworker" AS ?connection_path)
  }
  UNION
  {
    # Path 4: Family → Employment → Institution → Students/Staff
    ?person sdc:hasRelationship ?rel .
    ?rel sdc:relatedPerson ?family_member .
    ?family_member sdc:nationalID ?family_id .
    ?employment sdc:employeeID ?family_id .
    ?employment sdc:employerName ?institution .
    ?enrollment sdc:institutionName ?institution .
    ?enrollment sdc:studentID ?contact_id .
    ?contact sdc:nationalID ?contact_id .
    ?contact sdc:fullName ?contact_name .
    BIND("Institutional contact" AS ?relationship)
    BIND("Education" AS ?domain)
    BIND("Family → Employer → Institution → Student" AS ?connection_path)
  }
}
ORDER BY ?connection_path ?contact_name
```

### Director's Note: "Minting vs. Mining"

When the query executes, show a progress bar labeled **"Retrieval Pipeline."** Make it go **instantly** to 100%.

*Voiceover:* "In a standard RAG system, this query would take 30 seconds of probabilistic reasoning to guess these links. Because we 'Minted' the links at the source — Civil Registry to Employment to Education — the retrieval is deterministic. We aren't guessing the path; we are just reading it."

This is the GraphRAG contrast point. Traditional RAG mines unstructured text for relationships. SDC mints the relationships at data creation time. The graph doesn't infer that Carlos has a sister named Elena — it *knows*, because the Civil Registry cell declared it.

### Scene 3: The Query Results

The query returns results in tiers:

**Tier 1 — Direct family contacts:**

| Contact | ID | Relationship | Location |
|---------|----|-------------|----------|
| Elena Mendoza | COR-CE01-271903 | Sister | Novaciudad |

**Tier 2 — Vessel crew (17 contacts):**

| Contact | ID | Relationship | Location |
|---------|----|-------------|----------|
| Rodrigo Salazar | (foreign) | Sibling crew | MV Estrella del Sur, Berth 7 |
| ... (16 more crew) | ... | Sibling crew | MV Estrella del Sur, Berth 7 |

*Note: All crew are confined to vessel under quarantine order IR-2026-AL-00847.*

**Tier 3 — Family member's workplace contacts:**

| Contact | ID | Relationship | Domain Path | Location |
|---------|----|----|-------------|----------|
| Elena Mendoza | COR-CE01-271903 | Employee | Family → Employer | Universidad Nacional de Cordova, Campoluz |
| Dr. Ramón Gutiérrez | COR-BR01-334201 | Coworker | Family → Employer → Coworker | Universidad Nacional de Cordova, Campoluz |
| Prof. Ana Lucero | COR-BR01-298744 | Coworker | Family → Employer → Coworker | Universidad Nacional de Cordova, Campoluz |
| ... (24 more faculty/staff) | ... | Coworker | Family → Employer → Coworker | Universidad Nacional de Cordova, Campoluz |

**Tier 4 — Institutional contacts (students at Elena's institution):**

| Contact | ID | Relationship | Domain Path | Location |
|---------|----|----|-------------|----------|
| (312 active students) | ... | Institutional contact | Family → Employer → Institution → Student | Universidad Nacional de Cordova, Campoluz |

**Total contacts identified: 356**
- 1 direct family member
- 17 vessel crew (quarantined)
- 26 workplace coworkers of family member
- 312 students at family member's institution

**Query traversal path:**

```
Maritime (crew manifest)
    → Civil Registry (Carlos → family → Elena)
        → Employment (Elena → Universidad Nacional de Cordova)
            → Employment (all employees at same institution)
            → Education (all students at same institution)
```

**Four domains. One query. Zero integration code.**

### Scene 4: The Redacted Cell

In the query results, one field stands out:

```
┌─────────────────────────────────────────────────────────┐
│ Healthcare Record for COR-AL01-271845                   │
│                                                         │
│ Facility:     Porto Sereno General Hospital              │
│ Provider:     Dr. Isabel Reyes                          │
│ Admitted:     2026-01-14                                │
│ Diagnosis:    ██████████████████████████████             │
│                                                         │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ ⓘ  Access Denied                                    │ │
│ │                                                     │ │
│ │  Your Role:    dpv:Authority (Auditor)              │ │
│ │  Data Purpose: dpv:ProvideHealthcare                │ │
│ │  Required:     dpv:HealthcareOrganisation           │ │
│ │  Reason:       Purpose Mismatch                     │ │
│ │                (dpv:GovernmentalOversight            │ │
│ │                 ≠ dpv:ProvideHealthcare)             │ │
│ │                                                     │ │
│ │  To access: Request Governed Override               │ │
│ └─────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

### Director's Note: Color Language

Establish a consistent color vocabulary throughout the demo:

- **White** — Normal, accessible data
- **Black / dark gray** — Redacted cells (data exists but content hidden)
- **Amber / glowing gold** — Overridden data (visible under a specific, expiring legal warrant)
- **Red pulse** — Refused composition (schema rejection in progress)

The redacted diagnosis cell should be visibly **black** — not blank, not missing. The audience needs to see that the cell *exists* and has *weight*. A blank space suggests missing data. A black cell with a lock icon says: "The data is here. You don't have clearance."

The DPV tooltip appears on hover — the audience sees *why* in standardized W3C vocabulary, not a cryptic permission code.

The Governor sees that Carlos is hospitalized. Sees when. Sees by whom. Sees where. But not **why**. The data itself is enforcing the boundary — not application code, not a permissions table in a database, not an API gateway. The Cell's `act` element carries the policy, and the policy says: only `dpv:HealthcareOrganisation` can read clinical content.

**This is the "Ah-Ha" moment.**

The Governor has enough information to act — he knows the contact network, the geographic exposure zones (Porto Sereno port district, Universidad Nacional de Cordova campus in Campoluz), and the quarantine status. He does not need the diagnosis to coordinate the public safety response. The governance layer gave him exactly what he needs and nothing more.

---

## Act III — The Governed Override

### Scene 5: The Emergency

**Day 3 — Friday, January 16, 09:00**

The situation escalates. Two more crew members on *MV Estrella del Sur* develop symptoms. Dr. Reyes reports to the Provincial Health Authority that this is not a routine infection — the pathogen has characteristics suggesting high transmissibility.

Governor Ávila convenes an emergency cabinet meeting. The Minister of Health recommends expanding contact tracing to include all persons who were physically present at the Porto Sereno port terminal on January 14 between 06:00 and 16:00. To properly assess the public health risk, the Minister argues that the Governor's crisis team needs to know the specific pathogen.

The Governor authorizes a Governed Override.

### Scene 6: The Override Process

In the Cordova OS dashboard (Auditor role), the analyst clicks "Request Governed Override" on the redacted healthcare cell.

**The system creates an ExceptionalValue object:**

```
Exception:Override Cell
  Override ID:           OVR-2026-00003
  Requesting User:       Governor's Office Crisis Team
  Requesting Role:       dpv:Authority (Auditor)
  Target Cell:           Healthcare/Visit/Diagnosis for COR-AL01-271845
  Target Cell Purpose:   dpv:ProvideHealthcare
  Justification Purpose: dpv:VitalInterest (Public Health Emergency)
  Legal Basis:           dpv:LegitimateInterest, dpv:VitalInterest
  Authorization:         Governor Tomás Ávila (COR-CE01-104287)
  Timestamp:             2026-01-16T09:47:23-04:00
  Status:                PENDING APPROVAL
```

**This override request is itself a governed Cell in the graph.** It has provenance. It has attestation. It is queryable. It is auditable. It does not exist in a log file or an email thread — it is a first-class semantic data object.

The override requires approval from a role with `dpv:HealthcareOrganisation` authority. Dr. Reyes (or the Provincial Health Officer) must approve the release.

### Scene 7: Approval and Disclosure

Dr. Lucía Ferrer, Provincial Health Officer for Aldara, approves the override:

```
Exception:Override Cell (Updated)
  Override ID:           OVR-2026-00003
  Status:                APPROVED
  Approved By:           Dr. Lucía Ferrer (COR-AL01-188934)
  Approver Role:         dpv:HealthcareOrganisation (Provincial Health Officer)
  Approval Timestamp:    2026-01-16T10:12:08-04:00
  Scope:                 Diagnosis and lab results ONLY.
                         Full clinical notes remain restricted.
  Expiration:            2026-02-16T10:12:08-04:00 (30 days)
```

### Director's Note: The Amber Glow

When the override is approved, don't just unlock the cell. **Change the color of the data.**

The diagnosis cell transitions from **black** (redacted) to **glowing amber**. This visualizes that the data is "hot" — it is visible *only* because of a specific, expiring legal warrant (`OVR-2026-00003`). The amber color tells the audience instantly: this is not normal access. This is an exception, and the system knows it.

The Auditor's view now shows:

```
┌─────────────────────────────────────────────────────────┐
│ Healthcare Record for COR-AL01-271845          [AMBER]  │
│                                                         │
│ Facility:     Porto Sereno General Hospital              │
│ Provider:     Dr. Isabel Reyes                          │
│ Admitted:     2026-01-14                                │
│ Diagnosis:    Suspected Novel Respiratory Pathogen       │
│               (NRP-C) — PCR Confirmed Positive          │
│                                                         │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ ⚠  Governed Override Active                         │ │
│ │                                                     │ │
│ │  Override:   OVR-2026-00003                         │ │
│ │  Authorized: Governor Tomás Ávila                   │ │
│ │  Approved:   Dr. Lucía Ferrer (Prov. Health)        │ │
│ │  Basis:      dpv:VitalInterest                      │ │
│ │  Expires:    2026-02-16                             │ │
│ │  Scope:      Diagnosis + lab results only           │ │
│ └─────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────┘
```

The diagnosis is now visible — but **only because a governed, auditable, time-limited exception was created**. When the override expires, the cell returns from amber back to black. The entire chain — who asked, who approved, why, when, under what legal basis — is permanently recorded in the graph.

---

## Act IV — The Refusal

### Scene 8: The Wrong Composition

The demo switches perspective. Now we show what happens when someone tries to misuse the data.

**Setup:** A public health communications officer (working under the Healthcare Provider role) is drafting a public advisory about the port health emergency. They want to include specific patient data to make the advisory more compelling.

The officer opens the Healthcare app and attempts to export Carlos Mendoza's diagnosis cell into a document context tagged with purpose `dpv:PublicRelations`.

### Scene 9: The Schema Rejects It

The system does not show a permission dialog. There is no "Access Denied" popup.

### Director's Note: The Visual Bounce-Back

This moment must look fundamentally different from a standard "403 Forbidden" error.

- **Standard App:** Pop-up says "Access Denied." User shrugs.
- **SDC Demo:** The composition operation **physically bounces back**. If the UI uses drag-and-drop, the cell snaps back to its source. If it uses a form action, the submit visually recoils.
- **Side Panel Animation:** Trigger a split-view showing the two schema trees (Source Cell vs. Target Context) attempting to mesh. The connection point **glows red** — the `act` policies are incompatible and the trees cannot bind.
- **Real-Time Minting:** Show the `ExceptionalValue` cell being created in the graph in real-time. The audience watches a new node appear in the Graphwise visualization — the *failure itself* is now data.
- *The line:* "We didn't just block it. We recorded the attempt."

The **schema validation itself fails**:

```
═══════════════════════════════════════════════════════════
  SCHEMA VALIDATION FAILURE
═══════════════════════════════════════════════════════════

  Composition rejected at schema level.

  Source Cell:
    Type:     sdc:XdStringType (Diagnosis)
    act:      dpv:ProvideHealthcare
    Policy:   Restricted:PatientCare

  Target Context:
    Purpose:  dpv:PublicRelations
    Context:  Public Health Advisory Document

  Validation Result:
    FAIL — Purpose binding violation

    The source cell declares Restricted:PatientCare policy.
    This policy permits composition only with contexts whose
    purpose is within the dpv:ProvideHealthcare hierarchy.

    dpv:PublicRelations is NOT within dpv:ProvideHealthcare.

    The cell cannot bind to this context.

  ─────────────────────────────────────────────────────────

  ExceptionalValue Created:
    EV ID:        EV-2026-00847
    EV Type:      sdc:PurposeMismatch
    Source Cell:  Healthcare/Visit/Diagnosis/COR-AL01-271845
    Target:       Public Advisory Draft #PA-2026-003
    Timestamp:    2026-01-16T14:22:31-04:00
    Actor:        Communications Officer (dpv:HealthcareOrganisation)

  This failure is a governed, auditable Cell in the graph.
  It is visible to the Auditor role.

═══════════════════════════════════════════════════════════
```

**This is the Refusal Moment.**

The data didn't wait for an application to protect it. The data *carried its own constraints* and *refused to bind* with an incompatible context. The failure isn't an error — it's a **governed event**. It produced an ExceptionalValue Cell that:

1. Records exactly what was attempted
2. Records who attempted it
3. Records when
4. Records why it failed (specific DPV purpose mismatch)
5. Is itself a first-class object in the graph
6. Is visible to the Auditor role

**This is Data Physics.** The constraints are intrinsic to the data. They don't depend on application code, network configuration, or access control lists. They travel with the Cell.

---

## Act V — The Expanding Crisis

### Scene 10: The Network Grows

**Day 4 — Saturday, January 17**

Contact tracing reveals that Carlos Mendoza visited his sister Elena in Novaciudad on a previous shore leave (December 28, 2025 — two weeks before the current port call). This information comes from the Maritime domain: the previous port call record for *MV Estrella del Sur* shows Carlos disembarked for a 3-day shore leave.

**The contact network now expands:**

Elena was potentially exposed on December 28. She returned to work at Universidad Nacional de Cordova on January 6 after the holiday break. If she was infected, every person she contacted between January 6 and January 15 is a potential secondary contact.

The analyst runs a refined query:

```sparql
# Extended contact trace: Elena Mendoza's contacts from Jan 6-15

SELECT ?contact_name ?contact_id ?contact_type ?institution ?dates
WHERE {
  # Elena's employment record
  ?employment sdc:employeeID "COR-CE01-271903" .
  ?employment sdc:employerBRN ?employer_brn .
  ?employment sdc:employerName ?institution .

  {
    # Coworkers at same institution
    ?coworker_emp sdc:employerBRN ?employer_brn .
    ?coworker_emp sdc:employeeID ?contact_id .
    FILTER(?contact_id != "COR-CE01-271903")
    ?contact sdc:nationalID ?contact_id .
    ?contact sdc:fullName ?contact_name .
    BIND("Faculty/Staff" AS ?contact_type)
    BIND("Jan 6-15 (work days)" AS ?dates)
  }
  UNION
  {
    # Students enrolled at same institution, active status
    ?enrollment sdc:institutionName ?institution .
    ?enrollment sdc:enrollmentStatus "Active" .
    ?enrollment sdc:studentNationalID ?contact_id .
    ?contact sdc:nationalID ?contact_id .
    ?contact sdc:fullName ?contact_name .
    BIND("Student" AS ?contact_type)
    BIND("Jan 6-15 (semester)" AS ?dates)
  }
}
ORDER BY ?contact_type ?contact_name
```

**Results:**

| Category | Count | Location |
|----------|-------|----------|
| Faculty and staff | 26 | Universidad Nacional de Cordova, Campoluz |
| Active students | 312 | Universidad Nacional de Cordova, Campoluz |
| **Total secondary contacts** | **338** | Campoluz, Brevina |

### Scene 11: Cross-Province Response

The crisis now spans two provinces:

- **Aldara** (Porto Sereno): Port quarantine, vessel crew confined, Carlos hospitalized
- **Brevina** (Campoluz): University campus potentially exposed through Elena

Governor Ávila's graph query shows the geographic spread:

```
Porto Sereno (Aldara)          Novaciudad (Celara)          Campoluz (Brevina)
       │                              │                            │
  MV Estrella del Sur            Elena's home              Universidad Nacional
  18 crew (quarantined)          (Dec 28 visit)            26 staff + 312 students
       │                              │                            │
  Carlos Mendoza ──── sister ──── Elena Mendoza ──── employed ─────┘
  (hospitalized)                  (contact #1)
```

The Auditor can see this entire network in a single Graphwise visualization — nodes for people, edges for relationships, colored by domain source (blue for Civil Registry, green for Maritime, orange for Employment, purple for Education). The healthcare node exists but its content is redacted — a dark node with a lock icon.

### Scene 12: The Property Connection

A secondary query reveals additional exposure vectors through the Property Registry:

Elena Mendoza owns a condominium at 18 Avenida Universidad, Novaciudad. The Property Registry shows this is a 24-unit building. Through Civil Registry address matching, 19 other Cordovan residents share the same building address.

```
Property Registry → Address → Civil Registry (residents at same address)
```

**19 additional contacts identified** — Elena's neighbors in Novaciudad who may have shared common areas (lobby, elevator, parking) during the potential exposure window.

**Running total: 375 contacts across 3 provinces, identified through 6 domain apps in 3 queries.**

---

## Act VI — The Audit Trail

### Scene 13: What the Auditor Sees

At the end of the demo, switch fully to the Auditor role and show the governance trail.

The Auditor's dashboard shows every governed event that occurred during the crisis:

```
Governance Events — Contagion Response
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2026-01-14 08:00  Port Call PC-2026-0142 created
                  Attested by: Port Authority Officer
                  Domain: Maritime

2026-01-14 09:15  Health Screening Referral created
                  Attested by: Port Health Officer
                  Domain: Maritime

2026-01-14 11:00  Patient Record created
                  Attested by: Dr. Isabel Reyes
                  Domain: Healthcare
                  Policy: Restricted:PatientCare
                  [Content: REDACTED]

2026-01-14 15:00  Incident Report IR-2026-AL-00847 created
                  Attested by: Sgt. Maria Santos, CNP
                  Domain: Law Enforcement
                  Quarantine Zone: Porto Sereno Port District

2026-01-15 10:30  Cross-domain query executed
                  Actor: Governor's Office (Auditor role)
                  Domains traversed: Maritime, Civil Registry,
                  Employment, Education
                  Contacts identified: 356
                  Redacted cells encountered: 1 (Healthcare/Diagnosis)

2026-01-16 09:47  Governed Override requested
                  OVR-2026-00003
                  Requestor: Governor Tomás Ávila
                  Target: Healthcare/Diagnosis for COR-AL01-271845
                  Basis: dpv:VitalInterest

2026-01-16 10:12  Governed Override approved
                  OVR-2026-00003
                  Approver: Dr. Lucía Ferrer (Prov. Health)
                  Scope: Diagnosis + lab results only
                  Expires: 2026-02-16

2026-01-16 14:22  Schema composition REJECTED
                  EV-2026-00847
                  Actor: Communications Officer
                  Attempted: Diagnosis → Public Advisory
                  Reason: Purpose Mismatch
                  (dpv:ProvideHealthcare ≠ dpv:PublicRelations)
```

Every event is a Cell. Every Cell has provenance. The Auditor sees the **governance** without seeing the **data**. The system is transparent about *how* it was used without exposing *what* was private.

---

## Act VII — The Architecture Flex

### Scene 14: Drop to Terminal

The final beat. After the emotional arc of the crisis, the override, and the refusal — drop the curtain and show the machinery.

### Director's Note: Show the Code, Not a Slide

Switch from the Cordova OS dashboard to a terminal window. Show the Django project file structure:

```
$ tree cordova/ -L 1

cordova/
├── cordova/                 # Project settings, URLs
├── shell/                   # Shared UI (hand-written)
├── civil_registry/          # Generated by SDCStudio
├── vital_statistics/        # Generated by SDCStudio
├── healthcare/              # Generated by SDCStudio
├── education/               # Generated by SDCStudio
├── employment/              # Generated by SDCStudio
├── business_registry/       # Generated by SDCStudio
├── property_registry/       # Generated by SDCStudio
├── tax_revenue/             # Generated by SDCStudio
├── law_enforcement/         # Generated by SDCStudio
├── maritime/                # Generated by SDCStudio
└── manage.py
```

Then show one generated app's internals:

```
$ tree cordova/maritime/ -L 1

maritime/
├── models.py               # Generated from SDC data model
├── forms.py                # Generated — validated against XSD
├── views.py                # Generated — RDF triples emitted on save
├── urls.py                 # Generated
├── templates/              # Generated
├── rdf_emitter.py          # Generated — writes triples to GraphDB
└── xsd_schema.py           # Generated — carries the act policies
```

*The line:* **"Ten different domains. Zero integration code. The SDC Compiler wrote the interoperability so we didn't have to."**

Pause. Let it land. The audience just watched a cross-domain crisis response that traversed six government systems in a single query — and now they're looking at ten folders, each generated by the same compiler from the same Reference Model.

The natural question from the audience: "How did you integrate ten systems?"

The answer: "We didn't. The Reference Model compiled interoperability in."

---

## Demo Script Summary

For a live presentation, the Contagion scenario runs in seven beats:

| Beat | Duration | What You Show | Presentation Notes | What the Audience Learns |
|------|----------|--------------|--------------------|-----------------------|
| **1. Arrival** | 2 min | Port call record, crew manifest, health screening referral in Maritime app | Standard data entry. Establish normalcy. | Data entry in a generated app. RDF triples emitted on save. |
| **2. Cross-Domain Query** | 3 min | Single SPARQL query traverses 4 domains, returns 356 contacts | Progress bar goes instantly to 100%. *"We minted the links, we're just reading them."* | Minting vs. Mining. Deterministic graph retrieval, not probabilistic RAG. |
| **3. The Redaction** | 2 min | Healthcare diagnosis is a **black cell** with lock icon. DPV tooltip on hover. | Color language: white = accessible, black = redacted. The cell has *weight* — it's not blank. | Schema-enforced privacy. Access control in the data, not the app. |
| **4. The Override** | 3 min | Governor requests override. PHO approves. Cell transitions from **black to amber**. | Amber = "hot" data, visible only under expiring legal warrant. | Governed exceptions are first-class objects. Safety means auditable flexibility, not rigidity. |
| **5. The Refusal** | 2 min | Composition **bounces back**. Side panel shows XML trees failing to mesh (**red** at connection point). ExceptionalValue minted in real-time. | *"We didn't just block it. We recorded the attempt."* | Data Physics. The data enforces its own constraints. The failure is data. |
| **6. The Audit** | 2 min | Auditor view shows complete governance trail. Every event is a Cell. | Review color language: white, black, amber, red — all visible in the audit trail. | Transparency without exposure. Governance is observable and queryable. |
| **7. The Flex** | 1 min | Drop to terminal. Show `cordova/` directory: 10 generated app folders + 1 shell. | *"Ten domains. Zero integration code. The SDC Compiler wrote the interoperability."* | The compiler is the integration. No glue code. |

**Total: ~15 minutes for the core narrative.**

---

## Key Messages Reinforced

Each beat maps to a proof point from the architecture document:

| Beat | Proof Point |
|------|------------|
| Arrival | #8 — The Compiler Is the Integration |
| Cross-Domain Query | #4 — Graph-Native Queries, #6 — Zero Integration Code |
| The Redaction | #2 — Schema-Enforced Privacy, #7 — Role-Based Visibility from the Data |
| The Override | #3 — Governed Exceptions |
| The Refusal | #2 — Schema-Enforced Privacy (the "Data Physics" moment) |
| The Audit | #5 — Provenance Everywhere, #1 — Same Person, Ten Systems |
| The Flex | #6 — Zero Integration Code, #8 — The Compiler Is the Integration |

---

## Data Requirements

To run the Contagion scenario, the following synthetic data must be seeded:

### Mandatory Records

1. **Civil Registry:** Carlos Mendoza, Elena Mendoza, Dr. Isabel Reyes, Governor Ávila, Sgt. Santos, Dr. Ferrer, Captain Salazar (foreign — limited record), plus ~350 university contacts
2. **Maritime:** *MV Estrella del Sur* vessel record, Port Call PC-2026-0142, cargo manifest, crew list of 18, previous port call (Dec 2025 shore leave)
3. **Healthcare:** Carlos's patient record, visit record, vitals, lab results — all with `Restricted:PatientCare` policy
4. **Employment:** Elena at Universidad Nacional de Cordova, Carlos at Pacífico Meridional Shipping, ~26 university faculty/staff
5. **Education:** ~312 active students enrolled at Universidad Nacional de Cordova
6. **Law Enforcement:** Incident report IR-2026-AL-00847, quarantine enforcement sub-cluster
7. **Business Registry:** Universidad Nacional de Cordova (BIZ-000847), Pacífico Meridional Shipping S.A. (BIZ-001102)
8. **Property Registry:** Elena's condominium at 18 Avenida Universidad with ~19 other residents
9. **Tax & Revenue:** At minimum, Carlos and Elena's tax records (for redaction demo)
10. **Vital Statistics:** Carlos and Elena's birth certificates, parents' death certificates

### Background Population

The Contagion scenario records exist within the broader synthetic dataset of 25,000 people, 1,500 businesses, and 8,000 properties. The named characters are seeded specifically; the contact network (university staff, students, building residents) is drawn from the general population.
