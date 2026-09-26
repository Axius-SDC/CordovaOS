# CordovaOS SPARQL Queries

Seven cross-domain SPARQL queries demonstrating SDC4's deterministic graph traversal.
Queries 1-6 are general-purpose government analytics. Query 7 is the Contagion contact-tracing scenario.

## Prerequisites

- All 10 domain apps loaded with synthetic data
- RDF triples extracted to GraphDB/Fuseki triplestore
- Prefix `sdc4:` = `https://semanticdatacharter.com/ns/sdc4/`

## Query Index

| # | Name | Domains Traversed | Purpose |
|---|------|-------------------|---------|
| 1 | Complete Government Profile | All 10 | All government touchpoints for one person |
| 2 | Economic Network Analysis | Employment, Business, Tax, Maritime, Property | Business ecosystem map |
| 3 | Social Services Identification | Healthcare, Civil Registry, Employment, Property | At-risk population discovery |
| 4 | Supply Chain Provenance | Maritime, Business, Tax | Cargo-to-tax audit trail |
| 5 | Family Economic Unit | Civil Registry, Employment, Property, Tax, Education | Household aggregate view |
| 6 | Institutional Impact | Education, Employment, Business, Tax | University alumni economic footprint |
| 7 | Contagion Contact Tracing | Healthcare, Maritime, Law Enforcement, Education | 4-tier exposure network |

## Cross-Domain Join Mechanism

SDC4 instances join across domains by one mechanism: a **shared component**. The
National ID (`mc-nj7s1gk45tfgyooxpz0qaha3`) is composed by eight of the ten 4.4.0
models and the Business Registry Number (`mc-l8f0m7op4xhrxqy1jrnvbuly`) by four,
each by its identifier slot in the component library. Same component definition,
same value predicates, no mapping table. Every other identifier a query anchors on
(a diagnosis code, a vessel name, an organization name) is likewise the published
component's `mc-` id, read from `app/sdc4/mediafiles/dmlib/dm-<ct_id>.xsd`.
