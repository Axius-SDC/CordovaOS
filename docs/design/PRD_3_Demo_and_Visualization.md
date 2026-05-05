# PRD 3: Demo and Visualization

**Date**: May 5, 2026
**Status**: Planning - BLOCKED on GraphDB license research
**Depends on**: PRD 2 (CordovaOS Model Rebuild)

---

## 1. Objective

Deploy the fully governed CordovaOS dataset to Graphwise GraphDB (enterprise edition) and build a visual demo that shows the complete SDC capability stack in action. This demo serves three strategic purposes:

1. **Federal sales**: the artifact for DOE Genesis Mission, NOAA CDO, Jake Pasner, and Dia Adams conversations
2. **Graphwise activation**: teaches the Graphwise team how SDC data works in their platform, triggering them to drive adoption
3. **Practitioner training**: a reference implementation that practitioners can study and replicate

## 2. Open Items (Research Required)

- [ ] Graphwise GraphDB enterprise license: activation process, deployment requirements, feature set
- [ ] GraphDB Workbench visualization capabilities: what's built-in vs. what needs custom development
- [ ] SPARQL federation: can GraphDB federate queries across the 10 CordovaOS domain graphs?
- [ ] GraphDB + sdcgovernance integration: can governance decisions be triggered from within GraphDB, or is it a separate validation step?
- [ ] Hosting: local development machine, Bosgame P3, or cloud instance for demo purposes?

## 3. Demo Scenarios (Draft)

Pending PRD 2 completion and GraphDB research. Initial concepts:

### Demo 1: The Governed Contagion Trace
Walk through the CordovaOS contagion trace with governance visible at every boundary crossing. Visual: graph nodes colored by domain, governance decisions shown as edge annotations (PERMIT/DENY badges), provenance chain visible as a timeline.

### Demo 2: The Governance Audit Dashboard
Query all XACML decisions across 10 domains. Visual: receipt chain timeline, decision distribution (PERMIT/DENY/INDETERMINATE), drill-down to individual decision context.

### Demo 3: The Privacy Boundary
Demonstrate data access control enforcement. Visual: researcher queries for cross-domain data, DENY decisions appear with explanations, the boundary is visible in the graph.

### Demo 4: Context Graph Explorer
Navigate the automatically generated context graph. Visual: RDF/OWL entities, relationships, vocabulary bindings, semantic links - all generated as compiler output from the SDC models. "This is what a context graph looks like when it's not a project."

## 4. Graphwise Engagement Strategy

The demo is designed so that the Graphwise team can:
- See SDC data loaded and queryable in their platform
- Understand the RDF/OWL/SHACL output structure
- Build their own dashboards and visualizations on top
- Identify customer use cases where SDC + GraphDB is the right stack
- Refer their customers to Axius SDC for the modeling and governance layer

The demo meeting with Graphwise should include:
- Tim walking through the CordovaOS governance demo
- Graphwise team exploring the data in their own platform
- Discussion of joint customer scenarios
- Agreement on how practitioners refer clients for GraphDB upgrades (sales@axius-sdc.com flow)

## 5. Deliverables

- [ ] GraphDB instance with all 10 CordovaOS domains loaded
- [ ] At least 4 demo scenarios with scripted walkthroughs
- [ ] Graph visualizations for each scenario (screenshots/screen recordings)
- [ ] Slide deck for external presentations (NotebookLM can generate from documentation)
- [ ] Blog post: "10 Domains, 100K Records, Full Governance, Zero ETL"
- [ ] Video walkthrough (optional, high impact)

## 6. Timeline

TBD - dependent on GraphDB license activation and PRD 2 completion.

---

*This PRD depends on PRD 2 (CordovaOS Model Rebuild). GraphDB license research is the first action item.*
