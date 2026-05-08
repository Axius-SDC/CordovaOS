---
template_version: "4.0.0"
dataset:
  name: "Governance Workflow States"
  description: "Generic workflow state components for CordovaOS governance. Four XdOrdinal components, one per workflow pattern: Document Lifecycle, Record Intake, Incident Response, Regulatory Filing."
  creator: "Axius SDC"
  project: "CordovaOS"
enrichment:
  enable_llm: true
---

# Dataset Overview

Generic workflow state components using the concepts of state and transition from automata theory, as specified in W3C SCXML. Each component is a single XdOrdinal whose enumeration defines the ordered states for one workflow pattern. After upload, the auto-generated Cluster and DM will be deleted. The four XdOrdinal components will be manually assembled into workflow ClusterTypes with sub-cluster paths defining valid transitions.

**Standards Alignment**:
- W3C SCXML (state and transition concepts)
- SDC4 XdOrdinal for ordered state sequences

**Workflow Patterns**:
- Document Lifecycle: Draft -> Review -> Approved -> Published -> Archived
- Record Intake: Submitted -> Validated -> Accepted / Rejected
- Incident Response: Reported -> Triaged -> Assigned -> In Progress -> Resolved -> Closed
- Regulatory Filing: Prepared -> Submitted -> Under Review -> Approved / Returned -> Resubmitted

## Data: Workflow State Components

### document_lifecycle_state
**Type**: xdordinal
**Description**: Ordered states for the document lifecycle workflow pattern. Tracks a document from initial draft through review, approval, publication, and archival.
**Enumeration**:
- 0: Draft: https://www.w3.org/2011/04/SCXML/state
- 1: Review: https://www.w3.org/2011/04/SCXML/state
- 2: Approved: https://www.w3.org/2011/04/SCXML/state
- 3: Published: https://www.w3.org/2011/04/SCXML/state
- 4: Archived: https://www.w3.org/2011/04/SCXML/state

### record_intake_state
**Type**: xdordinal
**Description**: Ordered states for the record intake workflow pattern. Tracks a submitted record through validation to acceptance or rejection.
**Enumeration**:
- 0: Submitted: https://www.w3.org/2011/04/SCXML/state
- 1: Validated: https://www.w3.org/2011/04/SCXML/state
- 2: Accepted: https://www.w3.org/2011/04/SCXML/state
- 3: Rejected: https://www.w3.org/2011/04/SCXML/state

### incident_response_state
**Type**: xdordinal
**Description**: Ordered states for the incident response workflow pattern. Tracks an incident from initial report through triage, assignment, active work, resolution, and closure.
**Enumeration**:
- 0: Reported: https://www.w3.org/2011/04/SCXML/state
- 1: Triaged: https://www.w3.org/2011/04/SCXML/state
- 2: Assigned: https://www.w3.org/2011/04/SCXML/state
- 3: In Progress: https://www.w3.org/2011/04/SCXML/state
- 4: Resolved: https://www.w3.org/2011/04/SCXML/state
- 5: Closed: https://www.w3.org/2011/04/SCXML/state

### regulatory_filing_state
**Type**: xdordinal
**Description**: Ordered states for the regulatory filing workflow pattern. Tracks a filing from preparation through submission, review, and potential return/resubmission cycle.
**Enumeration**:
- 0: Prepared: https://www.w3.org/2011/04/SCXML/state
- 1: Submitted: https://www.w3.org/2011/04/SCXML/state
- 2: Under Review: https://www.w3.org/2011/04/SCXML/state
- 3: Approved: https://www.w3.org/2011/04/SCXML/state
- 4: Returned: https://www.w3.org/2011/04/SCXML/state
- 5: Resubmitted: https://www.w3.org/2011/04/SCXML/state
