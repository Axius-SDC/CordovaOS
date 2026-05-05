# CordovaOS Governance Rebuild - Planning Document

**Date**: May 5, 2026
**Status**: Planning
**Goal**: Rebuild CordovaOS with full governance components to demonstrate the complete SDC capability stack

---

## Objective

Rebuild CordovaOS's 10 government domains with standards-based governance components that exercise every governance dimension SDC supports. The result is a production-quality demo showing:

- 10 domains, 100K+ records, 0 lines of ETL code
- Every record governed with workflow, provenance, attestation, party/role
- sdcvalidator structural validation (pass/fail)
- sdcgovernance advisory (XACML PERMIT/DENY with hash-chained receipts)
- Context graphs generated automatically (RDF, OWL, SHACL, JSON-LD)
- No platform dependency. Apache 2.0.

## Design Principle

Governance components are **generic and standards-based first, domain-applied second**. A workflow state machine for document approval works the same whether the document is a healthcare record, a law enforcement report, or a port manifest. The components are designed once, published to the catalog, and composed into domain-specific models.

## Phase 1: Generic Governance Components (via ProvGov templates)

### 1.1 Workflow State Machines
Design reusable workflow patterns applicable across government domains:

- **Document Lifecycle**: Draft -> Review -> Approved -> Published -> Archived
- **Record Intake**: Submitted -> Validated -> Accepted / Rejected
- **Incident Response**: Reported -> Triaged -> Assigned -> Resolved -> Closed
- **Regulatory Filing**: Prepared -> Submitted -> Under Review -> Approved / Returned

Each workflow uses XdOrdinal components in ClusterType sub-cluster paths, borrowing the concepts of state and transition from automata theory as specified in W3C SCXML. **Note**: The XdOrdinal leaf components are created via md2pd templates (flat), but the ClusterType structure with sub-cluster paths must be manually constructed in SDCStudio. The md2pd parser does not support nested cluster creation.

### 1.2 Provenance Records
Standard W3C PROV-O patterns:

- **Entity** (system-id): what was acted on
- **Activity** (timestamp, type): what was done (W3C Activity Streams 2.0 types)
- **Agent** (system-user): who did it (Party component)

With DPV retention policies: most recent + hash, last N records, full chain.

### 1.3 Attestation Models
W3C VC 2.0 pattern:

- **Committer** (Party): who has authority to attest
- **Reason** (XdString): basis for attestation
- **Proof** (XdFile): cryptographic or documentary evidence
- **Pending** (XdBoolean): whether attestation is still awaited

### 1.4 Party/Role Components
Standard participation patterns:

- **Government Official** (role: authorizer, reviewer, approver)
- **Citizen** (role: subject, applicant, reporter)
- **System** (role: automated processor, validator)
- **External Partner** (role: data provider, consuming agency)

### 1.5 Decision Tables
OMG DMN patterns:

- **Access Control**: risk score + role + data classification -> PERMIT/DENY
- **Retention Policy**: data age + sensitivity + legal hold -> retain/archive/purge
- **Escalation**: severity + response time + jurisdiction -> escalate/handle/defer

### 1.6 Retention Policies
W3C DPV:

- **Most Recent + Hash**: keep latest version, hash of previous for integrity
- **Last N Records**: keep N most recent provenance records
- **Full Chain**: keep entire provenance history (regulatory/legal hold)

## Phase 2: Upload and Publish Through SDCStudio

For each of the 8 governance dimension templates (see PRD 1):

1. Upload flat markdown template to SDCStudio (one per dimension, all components in a single Cluster)
2. SDCStudio AI processes the template - creates flat leaf components
3. HITL review of every generated component (types, constraints, labels, vocabulary bindings)
4. Edit as needed
5. Delete the auto-generated flat Cluster and DM via Django admin
6. Manually construct all structural Clusters in SDCStudio:
   - Workflow ClusterTypes with sub-cluster paths and XdOrdinal sequences
   - Party detail Clusters
   - Validation-details Clusters
7. Publish using the bottom-up publication order (leaf components first, then Clusters)
8. Verify all components are in the catalog and reusable

**Key constraint**: The md2pd parser produces flat clusters only. ALL structural nesting is manual construction in SDCStudio.

## Phase 3: Rebuild CordovaOS Domain Models

Apply generic governance components to all 10 CordovaOS domains:

| Domain | Primary Workflow | Key Governance |
|---|---|---|
| Healthcare | Patient Record Lifecycle | HIPAA attestation, PHI access control |
| Education | Student Record Lifecycle | FERPA attestation, de-identification |
| Law Enforcement | Incident Response | Chain of custody provenance, officer attestation |
| Tax & Revenue | Filing Lifecycle | Title 26 confidentiality, audit trail |
| Civil Registry | Document Lifecycle | Identity verification attestation |
| Employment | Record Intake | Cross-agency sharing governance |
| Business Registry | Registration Lifecycle | Public/private access control |
| Property Registry | Transfer Lifecycle | Legal attestation, provenance chain |
| Vital Statistics | Record Lifecycle | Privacy Act, statistical use restrictions |
| Maritime Authority | Manifest Lifecycle | Cross-jurisdiction interoperability |

Each domain model composes:
- Domain-specific data components (existing CordovaOS models)
- Generic workflow (from Phase 1)
- Generic provenance (from Phase 1)
- Domain-specific attestation (adapted from generic pattern)
- Domain-specific decision tables (adapted from generic pattern)
- Retention policy (from Phase 1)

## Phase 4: Generate Data with Governance

Create XML instances for each domain that include:
- Domain data (existing CordovaOS records)
- Populated workflow state (current-state set to a meaningful position)
- Provenance records (Entity/Activity/Agent for the creation event)
- Attestation (committer assigned, pending or complete)
- Party/role participation records

## Phase 5: Validate End-to-End

For each domain:
1. **sdcvalidator**: structural validation against generated XSD. Pass/fail.
2. **sdcgovernance**: governance advisory
   - Workflow: evaluate a state transition (PERMIT/DENY)
   - Attestation: verify authority (PERMIT/DENY)
   - Decision table: evaluate access control rule (PERMIT/DENY)
   - Provenance: verify PROV-O record completeness
3. Every decision produces a hash-chained receipt
4. Verify receipt chain integrity across multiple decisions

## Phase 6: Demo and Documentation

Produce:
- Demo script walking through one domain end-to-end
- Context graph visualization (one SPARQL query crossing 3+ domains)
- Receipt chain visualization (hash chain across 10+ decisions)
- Slide deck (NotebookLM can generate from the documentation)
- Blog post: "10 Domains, 100K Records, Full Governance, Zero ETL"

## Dependencies

- SDCStudio must parse ProvGov templates correctly (test first)
- sdcgovernance 4.0.0 is on PyPI (done)
- sdcvalidator must validate governance-bearing XSD schemas (test)
- CordovaOS data models exist in SDCStudio (Tim confirmed they're still there)

## Timeline

TBD - scope after the current content and launch priorities settle.

---

*Internal planning document. This is Phase 8 of the sdcgovernance PRD.*
