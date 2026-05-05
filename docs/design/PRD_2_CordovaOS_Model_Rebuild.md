# PRD 2: CordovaOS Model Rebuild with Governance

**Date**: May 5, 2026
**Status**: Planning
**Depends on**: PRD 1 (Governance Component Templates)
**Blocks**: PRD 3 (Demo and Visualization)

---

## 1. Objective

Rebuild all 10 CordovaOS government domains using the governance components published in PRD 1. Each domain gets workflow, provenance, attestation, party/role, decision tables, and retention policies. Generate new data instances with governance content populated. Validate end-to-end with sdcvalidator and sdcgovernance.

End result: 10 domains, 100K+ records, fully governed, with XACML decisions and tamper-evident receipts at every governance decision point. Zero ETL. Zero platform dependency. Apache 2.0.

## 2. Design Principles

1. **Compose, don't duplicate.** Governance components from PRD 1 are reused across domains via the SDCStudio component catalog. Domain-specific governance is achieved by composing generic components with domain-specific data, not by creating new governance components per domain.

2. **Domain experts choose the workflow.** Each domain gets the workflow pattern that matches its operational reality. Healthcare uses Record Intake (with validation gate). Law enforcement uses Incident Response. Property uses Document Lifecycle. The generic patterns from PRD 1 are selected, not imposed.

3. **Realistic data.** Governance content in generated instances must be realistic - actual workflow states, actual provenance records with timestamps, actual attestation by named parties. Test data that says "test" in every field proves nothing.

4. **Cross-domain queries must work.** The 10 domains share the same reference model, the same governance component types, and the same provenance vocabulary. A single SPARQL query must be able to trace a person's interactions across Healthcare, Education, Employment, and Tax domains - the CordovaOS contagion trace scenario.

## 3. Domain-Governance Matrix

| # | Domain | Workflow Pattern | Attestation Focus | Decision Table | Retention | Access Control |
|---|---|---|---|---|---|---|
| 1 | Healthcare | Record Intake | Clinical authority (HIPAA) | PHI access control | Full chain (legal) | Confidential + Consent |
| 2 | Education | Document Lifecycle | FERPA attestation | Student record access | Last N records | Restricted |
| 3 | Law Enforcement | Incident Response | Officer attestation, chain of custody | Escalation + access | Full chain (legal) | Restricted |
| 4 | Tax & Revenue | Regulatory Filing | Title 26 authority | Confidentiality enforcement | Full chain (legal) | Confidential |
| 5 | Civil Registry | Document Lifecycle | Identity verification | Public/private access | Most recent + hash | Public + Restricted |
| 6 | Employment | Record Intake | Employer attestation | Cross-agency sharing | Last N records | Internal |
| 7 | Business Registry | Document Lifecycle | Registration authority | Public disclosure | Most recent + hash | Public |
| 8 | Property Registry | Document Lifecycle | Legal transfer attestation | Ownership verification | Full chain (legal) | Public + Restricted |
| 9 | Vital Statistics | Record Intake | Statistical authority (CIPSEA) | Use restriction enforcement | Full chain (regulatory) | Restricted |
| 10 | Maritime Authority | Regulatory Filing | Port authority attestation | Cross-jurisdiction access | Last N records | Internal + Restricted |

## 4. Implementation per Domain

For each of the 10 domains:

### Step 1: Model Design
- Review existing CordovaOS data model in SDCStudio
- Identify which governance components from PRD 1 catalog to compose in
- Select workflow pattern, attestation type, decision table, retention policy, access control tags
- Document the domain-specific governance design

### Step 2: Model Extension (Manual in SDCStudio)
- Open existing CordovaOS model in SDCStudio
- Add governance components from the PRD 1 catalog:
  - Attach the appropriate workflow ClusterType (manually built in PRD 1 with sub-cluster paths) to DM.workflow slot
  - Attach AuditType components to DM.Audit[] slot
  - Attach AttestationType to DM.attestation slot
  - Attach ParticipationType components to DM.Participation[] slot
  - Attach access control XdLink to DM.acs slot
  - Set DM.current-state to an appropriate workflow position
- All structural composition is manual - SDCStudio's md2pd parser does not support nested cluster construction from templates

### Step 3: Publication
- Review all newly added governance components (HITL)
- Publish using bottom-up order (governance components may already be published from PRD 1 catalog - verify)
- Generate new XSD schema with governance slots populated
- Verify the domain data + governance compose correctly in the DM root

### Step 4: Instance Generation
- Generate XML instances for the domain
- Populate governance content:
  - Set current-state to a meaningful workflow position (not just "draft" for everything)
  - Create provenance records with realistic Entity/Activity/Agent data
  - Set attestation status (some pending, some complete)
  - Populate participation records with domain-appropriate parties
- Target: minimum 10,000 records per domain (100K+ total across all 10)

### Step 5: Validation
- sdcvalidator: structural validation of every instance against its XSD. Must all pass.
- sdcgovernance: governance validation
  - Test one valid workflow transition per domain (expect PERMIT)
  - Test one invalid workflow transition per domain (expect DENY)
  - Test attestation verification per domain
  - Test decision table evaluation per domain
  - Verify receipt chain integrity

### Step 6: Context Graph Generation
- Generate RDF/Turtle output for each domain
- Load into graph store (Fuseki for development, GraphDB for PRD 3 demo)
- Verify cross-domain SPARQL queries work:
  - The contagion trace: Patient Zero -> Healthcare -> Employment -> Household -> Schools
  - The provenance trace: follow the audit chain across domain boundaries
  - The governance trace: show XACML decisions across all 10 domains

## 5. Cross-Domain Validation Scenarios

These scenarios prove the architecture works at scale:

### Scenario 1: The Contagion Trace (existing CordovaOS demo)
- Patient Zero presents at Porto Sereno clinic (Healthcare)
- Trace crosses Civil Registry, Employment, Education, Maritime Authority
- NEW: every boundary crossing now has provenance records and governance decisions
- The SPARQL query returns the trace AND the governance chain

### Scenario 2: The Governance Audit
- A regulator asks: "Show me every PERMIT and DENY decision across all domains for the last 30 days"
- Query the receipt chain across all 10 domains
- Return: decision, timestamp, instance_id, rule applied, hash chain integrity

### Scenario 3: The Privacy Boundary
- A researcher requests access to Healthcare + Vital Statistics data
- Healthcare access control: Confidential + Consent Required -> DENY (no consent on file)
- Vital Statistics access control: Restricted (CIPSEA) -> DENY (not an authorized statistical agency)
- Both DENYs produce receipts explaining why

### Scenario 4: The Workflow Violation
- An agent attempts to move a Law Enforcement incident from "Reported" directly to "Resolved" (skipping Triaged and Assigned)
- sdcgovernance returns DENY with valid alternatives: "From Reported, valid transitions are: Triaged"
- Receipt chain records the attempted violation

### Scenario 5: The Attestation Gap
- A Property Registry transfer is attempted with attestation status "pending"
- sdcgovernance evaluates: attestation required for this transition, committer not yet assigned
- Returns INDETERMINATE with explanation
- Receipt records the gap

## 6. Data Generation Strategy

CordovaOS already has data generation scripts. For the governance rebuild:

- Existing domain data (names, dates, identifiers) stays the same
- Governance content is added as a layer on top:
  - Workflow states distributed realistically (not all "draft" - some in review, some approved, some archived)
  - Provenance records with varied activity types (Create, Update, Approve, Reject)
  - Attestation with a mix of pending and complete
  - Party/role assignments that match the domain (doctors in Healthcare, officers in Law Enforcement)
- Each instance gets a unique provenance chain start (the creation event)

## 7. Success Criteria

1. All 10 domains have governance components composed from the PRD 1 catalog
2. All 10 domains generate valid XSD schemas with governance slots populated
3. 100K+ XML instances across 10 domains pass sdcvalidator
4. sdcgovernance returns correct XACML decisions for all 5 cross-domain scenarios
5. Receipt chains are valid and verifiable across domain boundaries
6. Cross-domain SPARQL queries return correct results including governance data
7. The contagion trace scenario works with governance provenance visible

## 8. Risks

| Risk | Mitigation |
|---|---|
| Existing CordovaOS models in SDCStudio may have drifted or been modified | Verify current state before starting. Tim confirmed they still exist. |
| 100K instances with governance content is a large generation task | Script the governance content generation. Provenance and workflow states can be templated. |
| Cross-domain SPARQL queries may perform poorly at 100K records in Fuseki | Fuseki is for development. GraphDB (PRD 3) is for the demo. Optimize queries before scaling. |
| Governance components from PRD 1 may need revision after domain composition reveals issues | Budget time for iteration between PRD 1 and PRD 2. The pipeline is iterative, not waterfall. |

## 9. Timeline

Estimated 7-10 working days (after PRD 1 is complete):
- Day 1-2: Review existing CordovaOS models, design domain-governance mappings
- Day 3-5: Model extension, publication, XSD generation (2 domains/day)
- Day 6-7: Instance generation with governance content (scripted)
- Day 8-9: Validation (sdcvalidator + sdcgovernance across all domains)
- Day 10: Cross-domain scenarios, SPARQL queries, debug

---

*This PRD depends on PRD 1 (Governance Component Templates) and feeds into PRD 3 (Demo and Visualization).*
