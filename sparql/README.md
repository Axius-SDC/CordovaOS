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
| 7 | Contagion Contact Tracing | Maritime, Civil Registry, Employment, Education | 4-tier exposure network (356 contacts) |

## Cross-Domain Join Mechanism

SDC4 instances join across domains via two mechanisms:

1. **Shared component ct_id** -- National ID (`mc-nj7s1gk45tfgyooxpz0qaha3`) and Business Registry Number (`mc-l8f0m7op4xhrxqy1jrnvbuly`) are reused by ct_id across domain schemas. Same component definition, same value predicates.

2. **Party identity** -- `sdc4:party-id` on subject/provider parties carries CID (persons) or BRN (businesses), enabling cross-domain identity resolution without probabilistic matching.
