# SDC Data Physics

The foundational philosophy of the Semantic Data Charter.

---

## Preamble: Where the Complexity Lives

SDC does not eliminate complexity. Complex information systems are complex — that reality doesn't change because you adopt a new reference model. What SDC does is **redefine where the complexity lives.**

In traditional enterprise architecture, the complexity is buried in **opaque integration code**: middleware, ETL pipelines, API adapters, message buses, data mapping layers, transformation scripts. This code is written by developers, maintained by developers, and understood only by developers. When it breaks, developers debug it. When requirements change, developers rewrite it. The domain experts who understand the data and the analysts who need to query it are locked out of the system that connects their work.

SDC moves the complexity into two transparent places:

1. **Domain expert definitions.** The people who understand the data — clinicians, registrars, port authorities, tax officials — define the shape and meaning of their data using SDCStudio (or other SDC-compliant tools). They declare the types, constraints, enumerations, access policies, and semantic annotations. This is where the modeling complexity lives. It is visible, auditable, and governed by the people who know the domain.

2. **Query complexity.** The information analysts who need to ask cross-domain questions write SPARQL queries (or XQuery/XPath against XML databases) that traverse the graph. The queries can be sophisticated — multi-hop traversals across ten domains, role-filtered views, temporal bridging across schema versions. This is where the analytical complexity lives. It is visible, testable, and owned by the people who understand the questions.

**What disappears** is the integration layer in between. No middleware translating Civil Registry records into Healthcare records. No ETL pipeline mapping Maritime crew lists to Employment records. No API adapter converting Tax Authority formats to Port Authority formats. The integration is structural — guaranteed by the Reference Model at compile time — so the code that used to bridge these systems simply doesn't need to exist.

The tradeoff is honest: SDC increases the rigor required to define data models (Phase 1) and increases the sophistication required to query across them (Phase 3). But both of these are managed by the right people — domain experts and information analysts — instead of being buried in a codebase that neither group can read.

### The Charter as Constitution

A Semantic Data Charter is, in the most literal sense, a **constitution for data**.

The data model definitions are **laws**: published, versioned, immutable once ratified. They declare the structural rules (types, constraints) and the governance rules (access policies, legal bases) under which data operates. New requirements don't amend existing laws — they mint new ones, just as constitutional amendments extend rather than rewrite the original document.

The Reference Model is the **constitutional framework**: the meta-rules that all laws must conform to. SDC4 defines the type system, the Cluster hierarchy, the `act` governance model, and the RDF emission patterns. Every data model "law" must be valid under this framework, just as every statute must be valid under the constitution.

And like a constitution, the Charter is **readable by non-lawyers**. A domain expert can look at an SDC data model and understand what it says — because the model *is* the domain language, expressed in a structured form. The complexity is in the definitions and the queries, not in hidden plumbing between them.

---

## The Problem: Semantic Coupling

Traditional data modeling is "brittle" because it conflates the **Concept** (The Thing) with the **Label** (The Word).

* **Example:** An XSD defines `<CustomerType>`.
* **The Failure:** When the business redefines "Customer" to "Client" (or changes the scope of what a customer is), the schema must be updated. This breaks backwards compatibility, invalidates historical data, and requires expensive ETL to migrate old records to the new definition.

Every enterprise data architect has lived this nightmare. The label changes, so the schema changes, so the database changes, so the application changes, so the integration changes. A one-word business decision cascades into months of engineering work — and the historical data either gets migrated (expensive, lossy) or abandoned (wasteful, risky).

The root cause is that the schema used the **word** as the identifier. When the word changes, everything downstream breaks.

---

## The SDC Solution: Concept Unique Identifiers (CUIDs)

SDC anchors data not to words, but to **CUIDs (Concept Unique Identifiers)**.

### What Is a CUID?

A CUID is a collision-resistant unique identifier minted once per component definition. It is the component's **permanent address in the semantic space** — bound to a specific structural and semantic definition, independent of the application that uses it, independent of the database that stores it.

In SDCStudio, CUIDs are generated using the [CUID2 algorithm](https://github.com/paralleldrive/cuid2) — a secure, collision-resistant ID format designed for distributed systems. A typical CUID looks like:

```
clxk8s0oo0001jn08g5r3h7z4
```

This string has no semantic content. It doesn't encode the component's name, type, project, or version. It is a pure coordinate — a point in semantic space.

### The Immutability Rule

**Once a CUID is minted, its definition, constraints, scope, and access policies are frozen forever.**

* The CUID's **structural definition** — its data type, constraints, enumerations, and `act` (access control) policies — is permanent.
* Its **semantic definition** — RDF/XML predicate-object pairs using standardized predicates from OWL, RDFS, SKOS, etc. — is equally frozen.
* If a concept evolves, a **new CUID is minted** with its own definition. Conceptual equivalence between the old and new CUIDs is expressed through semantic annotations, not by reusing the same identifier.
* Each definition can carry as many predicate-object pairs as needed to fully describe its meaning.

A record created in 2024 using `CUID-A` will *always* be valid against the 2024 Data Model. It never "rots." It is a perfect fossil of the reality at the moment of creation.

### The Schema as Coordinate System

The SDC schema is not a dictionary (where words have definitions that can change). It is a **coordinate system** (where points have fixed positions).

| Traditional Schema | SDC Schema |
|-------------------|-----------|
| `<CustomerType>` is the identifier | `clxk8s0oo0001jn08g5r3h7z4` is the identifier |
| Redefining "Customer" as "Client" breaks the schema and requires migration | "Customer" and "Client" are separate CUIDs; shared semantics expressed via RDF/XML predicate-object pairs (OWL, RDFS, SKOS) |
| Historical records must be migrated | Historical records remain valid forever |
| The schema is a living document | The schema is a published, immutable artifact |

---

## Non-Destructive Evolution: The Semantic Ledger

Concepts evolve. Businesses change. Regulations expand. SDC handles this not by updating definitions, but by **minting new ones**. SDC functions as a **Semantic Ledger** — append-only, never overwrite.

### How It Works

**Scenario:** The business concept of "Customer" (`CUID-A`) evolves into a broader concept of "Client" (`CUID-B`).

**The Execution:** We do not patch `CUID-A`. We mint `CUID-B`.

* `CUID-A` ("Customer") — minted 2024, definition frozen, still valid for all 2024 records.
* `CUID-B` ("Client") — minted 2026, broader scope, used for all new records going forward.
* `CUID-A` is marked as **deprecated** — not deleted, not modified, just flagged.

**The Result:**
* **Old Data:** Remains 100% valid against the 2024 Data Model. Zero migration. Zero ETL. The records are perfect fossils.
* **New Data:** Is minted against the 2026 Data Model using `CUID-B`.
* **Both coexist** in the same graph, in the same triple store, queryable together.

### Versioning: The Mechanism

SDCStudio enforces this through a **modified semantic versioning** scheme:

**Format:** `MAJOR.MINOR.PATCH`

* **MAJOR** = SDC Reference Model version (currently **4** for SDC4)
* **MINOR** = Feature releases for the specific artifact
* **PATCH** = Bug fixes and minor updates

Every component minted under SDC4 carries a `4.x.x` version. This version number permanently binds the CUID to the SDC4 Reference Model's structural rules — its type system (XdString, XdBoolean, XdCount, XdQuantity, XdTemporal, etc.), its Cluster hierarchy, its `act` governance model, and its RDF emission patterns.

A `4.x.x` CUID will always be structurally compatible with every other `4.x.x` CUID. This is why the Cordova demo works: ten different domain apps, all `4.x.x`, all structurally interoperable without integration code.

---

## The XSD Is the Source of Truth

Before discussing query interfaces, this must be clear: **the XSD (XML Schema Definition) is the authoritative source of truth for every SDC data model.**

The published XSD contains:

* **Structural constraints** — data types, cardinality, enumerations, min/max values, pattern restrictions
* **RDF/XML semantics** — the semantic annotations are embedded directly in the schema, not layered on top
* **`act` governance policies** — access control tags declaring who can see, use, and compose each cell
* **CUID bindings** — every component's permanent identifier is declared in the schema
* **Reference Model conformance** — the XSD enforces SDC4 type system rules at validation time

An XSD-valid record is, by definition, structurally governed. The schema is both the blueprint and the enforcer. Any record that validates against the XSD is guaranteed to carry correct types, constraints, semantics, and governance — because the XSD *is* all of those things.

### Two Query Interfaces, One Source of Truth

The XSD's structural and semantic content is accessible through two query paths:

| Storage | Query Language | Strength |
|---------|---------------|----------|
| **XML Database** (MarkLogic, BaseX, eXist-db) | XQuery / XPath | Native XSD validation, schema-aware queries, direct access to structural constraints and RDF/XML annotations |
| **RDF Triple Store** (GraphDB, Fuseki) | SPARQL | Graph traversal across domains, federated queries, semantic bridging between CUIDs |

These are not competing approaches. They are **two views of the same truth**:

* **XQuery/XPath** operates on the XML instances and their schemas directly. It can validate, query, and traverse the data with full awareness of the XSD structure. If the data models are stored in an XML database, every structural constraint, every semantic annotation, every `act` policy is queryable via XPath without any transformation.

* **SPARQL** operates on the RDF triples extracted from those same XML instances. It excels at cross-domain graph traversal — the kind of queries the Cordova demo showcases (Maritime → Civil Registry → Employment → Education in one query).

The Cordova demo uses SPARQL and GraphDB because the demo's headline feature is cross-domain graph traversal. But the same evolutionary bridging described below works equally well in an XML database via XQuery — the `sdc:supersedes` relationships can be expressed as XML elements and queried via XPath, with full XSD validation at every step.

---

## Evolutionary Bridging via the Graph

The graph is one interface to the evolutionary relationships between CUIDs. It is particularly convenient for cross-domain queries because SPARQL was designed for exactly this kind of traversal.

### Semantic Bridging

The graph stores the evolutionary relationship between CUIDs:

```turtle
cuid:CUID-B  sdc:supersedes  cuid:CUID-A .
cuid:CUID-A  sdc:status      sdc:Deprecated .
cuid:CUID-B  sdc:status      sdc:Active .
cuid:CUID-A  sdc:mintedDate  "2024-03-15"^^xsd:date .
cuid:CUID-B  sdc:mintedDate  "2026-01-20"^^xsd:date .
```

### Querying Across Time

A SPARQL query can traverse these edges to bridge across evolutionary boundaries:

```sparql
# "Show me all Clients" — including historical records minted as "Customers"
SELECT ?record ?label ?minted_date
WHERE {
  {
    # Current definition
    ?record sdc:definedBy cuid:CUID-B .
    BIND("Client" AS ?label)
  }
  UNION
  {
    # Historical definition (superseded)
    ?record sdc:definedBy cuid:CUID-A .
    cuid:CUID-B sdc:supersedes cuid:CUID-A .
    BIND("Customer (historical)" AS ?label)
  }
  ?record sdc:mintedDate ?minted_date .
}
ORDER BY ?minted_date
```

The query returns both 2024 "Customer" records and 2026 "Client" records — because the graph knows they are semantically related. No migration happened. No ETL ran. The old records were never touched.

The same query is equally possible via XQuery against an XML database — the `sdc:supersedes` relationship is expressed in the XSD, and XPath can follow it. SPARQL is shown here because the Cordova demo uses a triple store, but the underlying principle is storage-agnostic: **the evolutionary metadata is in the schema, not in the query engine.**

---

## Reference Model Evolution: SDC4 to SDC5

The hardest version of the brittleness critique: **What happens when the Reference Model itself changes?**

The answer follows the same pattern, one level up.

### The Scenario

SDC4 has been in use for years. Thousands of CUIDs minted, millions of records created. Now SDC5 is published with an expanded type system, new governance features, and revised ontology URIs.

### The Execution

1. **SDC4 is not patched.** Every `4.x.x` CUID, every SDC4 Data Model, every SDC4-generated app remains frozen and valid. The records are fossils — permanently governed by the SDC4 Reference Model that created them.

2. **SDC5 CUIDs are minted fresh.** New components carry `5.x.x` versions. They conform to SDC5's type system and governance model. They are structurally incompatible with SDC4 components (different major version = different Reference Model).

3. **The graph bridges them.** The triple store holds both SDC4 and SDC5 triples. Semantic bridging edges connect equivalent concepts across Reference Model versions:

```turtle
cuid:SDC5-PersonType  sdc:succeeds  cuid:SDC4-PersonType .
cuid:SDC5-PersonType  sdc:referenceModel  sdc:SDC5 .
cuid:SDC4-PersonType  sdc:referenceModel  sdc:SDC4 .
```

4. **Queries traverse the bridge.** A SPARQL query for "all Person records" can follow the `sdc:succeeds` edge to include both SDC4 and SDC5 records, with the graph providing the structural mapping between the two Reference Model versions.

### Why This Works

The key insight: **the Reference Model version is encoded in every CUID's version number.** A `4.x.x` component will never be confused with a `5.x.x` component. They coexist in the graph as distinct entities with an explicit evolutionary relationship — not as ambiguous versions of "the same thing."

This is fundamentally different from traditional schema migration, where version N+1 replaces version N and the old data must be transformed. In SDC, version N and version N+1 are both permanent residents of the graph. The bridge is metadata, not migration.

---

## Governance Travels with the CUID

A CUID carries not just its structural definition but also its **access policies** — the `act` (access control tag) elements that declare who can see, use, and compose this data.

When `CUID-B` supersedes `CUID-A`, the governance policies may also evolve:

* `CUID-A` ("Customer", 2024): `act` allows `dpv:ServiceProvision`, `dpv:DirectMarketing`
* `CUID-B` ("Client", 2026): `act` allows `dpv:ServiceProvision` only — direct marketing removed per new privacy regulation

**Old records keep old policies.** A 2024 record minted under `CUID-A` retains its 2024 `act` policies. It was governed by the rules that existed when it was created. The data is a fossil — including its governance.

**New records get new policies.** A 2026 record minted under `CUID-B` carries the updated, stricter policies.

This means the graph contains records with *different governance rules for the same conceptual entity*, and both are correct — because each record is governed by the rules that were in force at the time of its creation. The Auditor can see this in the provenance: "This record was minted under CUID-A with 2024 governance. This record was minted under CUID-B with 2026 governance. Both are valid. Neither has been tampered with."

This is the intersection of the CUID immutability argument with the W3C DPV privacy model used in the Cordova demo. The governance doesn't just protect the data — it is part of the data, frozen at the moment of creation, and auditable forever.

---

## The Reusability Consequence

Because CUIDs are immutable and project-independent, they are **infinitely reusable**.

The SDCStudio component library currently contains:

| Project | Components | Purpose |
|---------|-----------|---------|
| Default | 12 | Universal components (address, phone, email) |
| NIEM | 309 | US federal justice, maritime, person components |
| NIH_CDE | 221 | National Institutes of Health Common Data Elements |
| Cordova | 18 | Demo-specific (National ID, provinces, cities) |

When the Cordova demo's Civil Registry template declares `@NIEM:Person Full Name`, it is referencing a CUID that was minted for the NIEM project. That CUID carries its definition, constraints, and type — and those are identical whether the component is used in a US federal justice system, a Cordova civil registry, or a pharmaceutical clinical trial.

**This is the moat.** The SDC4 specification and Reference Model are open source. Anyone can read them. But the library of minted, validated, reusable CUIDs — each with frozen definitions, tested constraints, and proven interoperability — is the accumulated intellectual capital. Every new project that reuses an existing CUID instead of creating a new one strengthens the network effect.

---

## Summary

SDC achieves **Agility without Brittleness** by separating three concerns:

| Concern | Mechanism | Source of Truth | Mutability |
|---------|-----------|----------------|-----------|
| **Structure** | CUID + Reference Model version | XSD | Immutable — frozen at mint time |
| **Semantics** | Evolutionary edges (supersedes, succeeds) | XSD (expressed as RDF/XML annotations) | Evolving — append-only ledger |
| **Governance** | `act` elements with DPV vocabulary | XSD | Immutable per CUID — evolves only through new CUIDs |
| **Query** | SPARQL (triple store) or XQuery/XPath (XML database) | Derived from XSD | Storage-agnostic |

The XSD is the source of truth. The graph (or XML database) is the query interface. The evolutionary metadata lives in the schema — not in any particular storage engine.

We don't ask the data to change. We don't ask the schema to change. We ask the **query layer** to understand the history.

The data is a fossil. The schema is the geological record. The query engine is the paleontologist.
