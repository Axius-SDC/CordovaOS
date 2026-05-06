---
template_version: "4.0.0"
dataset:
  name: "Governance Workflow States"
  description: "Generic workflow state components for CordovaOS governance. XdOrdinal components for four workflow patterns: Document Lifecycle, Record Intake, Incident Response, Regulatory Filing."
  domain: "Governance"
  creator: "Axius SDC"
  project: "CordovaOS"
enrichment:
  enable_llm: true
---

# Dataset Overview

Generic workflow state components using the concepts of state and transition from automata theory, as specified in W3C SCXML. Each component is an XdOrdinal representing a named state with an ordinal position. After upload, the auto-generated Cluster and DM will be deleted. The XdOrdinal components will be manually assembled into workflow ClusterTypes with sub-cluster paths defining valid transitions.

**Standards Alignment**:
- W3C SCXML (state and transition concepts)
- SDC4 XdOrdinal for ordered state sequences

**Workflow Patterns**:
- Document Lifecycle: Draft -> Review -> Approved -> Published -> Archived
- Record Intake: Submitted -> Validated -> Accepted / Rejected
- Incident Response: Reported -> Triaged -> Assigned -> In Progress -> Resolved -> Closed
- Regulatory Filing: Prepared -> Submitted -> Under Review -> Approved / Returned -> Resubmitted

## Data: Workflow State Components

### Column: draft
**Type**: xdordinal
**Description**: Initial state for documents and records before any review. Ordinal position 0 in Document Lifecycle and Record Intake patterns.
**Semantic Links**:
- https://www.w3.org/2011/04/SCXML/state
**Examples**: Draft

### Column: review
**Type**: xdordinal
**Description**: Document is under review by an authorized reviewer. Ordinal position 1 in Document Lifecycle pattern.
**Semantic Links**:
- https://www.w3.org/2011/04/SCXML/state
**Examples**: Review

### Column: approved
**Type**: xdordinal
**Description**: Document or filing has been approved by authorized authority. Ordinal position 2 in Document Lifecycle, position 2 in Regulatory Filing.
**Semantic Links**:
- https://www.w3.org/2011/04/SCXML/state
**Examples**: Approved

### Column: published
**Type**: xdordinal
**Description**: Document has been published and is publicly available. Ordinal position 3 in Document Lifecycle pattern.
**Semantic Links**:
- https://www.w3.org/2011/04/SCXML/state
**Examples**: Published

### Column: archived
**Type**: xdordinal
**Description**: Document has been archived. Terminal state in Document Lifecycle pattern. Ordinal position 4.
**Semantic Links**:
- https://www.w3.org/2011/04/SCXML/state
**Examples**: Archived

### Column: submitted
**Type**: xdordinal
**Description**: Record or filing has been submitted for processing. Ordinal position 0 in Record Intake, position 1 in Regulatory Filing.
**Semantic Links**:
- https://www.w3.org/2011/04/SCXML/state
**Examples**: Submitted

### Column: validated
**Type**: xdordinal
**Description**: Submitted record has passed validation checks. Ordinal position 1 in Record Intake pattern.
**Semantic Links**:
- https://www.w3.org/2011/04/SCXML/state
**Examples**: Validated

### Column: accepted
**Type**: xdordinal
**Description**: Record has been accepted after validation. Ordinal position 2 in Record Intake pattern (accept path).
**Semantic Links**:
- https://www.w3.org/2011/04/SCXML/state
**Examples**: Accepted

### Column: rejected
**Type**: xdordinal
**Description**: Record has been rejected after validation. Ordinal position 2 in Record Intake pattern (reject path).
**Semantic Links**:
- https://www.w3.org/2011/04/SCXML/state
**Examples**: Rejected

### Column: reported
**Type**: xdordinal
**Description**: Incident has been reported. Ordinal position 0 in Incident Response pattern.
**Semantic Links**:
- https://www.w3.org/2011/04/SCXML/state
**Examples**: Reported

### Column: triaged
**Type**: xdordinal
**Description**: Incident has been triaged and categorized. Ordinal position 1 in Incident Response pattern.
**Semantic Links**:
- https://www.w3.org/2011/04/SCXML/state
**Examples**: Triaged

### Column: assigned
**Type**: xdordinal
**Description**: Incident has been assigned to a responsible party. Ordinal position 2 in Incident Response pattern.
**Semantic Links**:
- https://www.w3.org/2011/04/SCXML/state
**Examples**: Assigned

### Column: in_progress
**Type**: xdordinal
**Description**: Incident is actively being worked. Ordinal position 3 in Incident Response pattern.
**Semantic Links**:
- https://www.w3.org/2011/04/SCXML/state
**Examples**: In Progress

### Column: resolved
**Type**: xdordinal
**Description**: Incident has been resolved. Ordinal position 4 in Incident Response pattern.
**Semantic Links**:
- https://www.w3.org/2011/04/SCXML/state
**Examples**: Resolved

### Column: closed
**Type**: xdordinal
**Description**: Incident has been closed. Terminal state in Incident Response pattern. Ordinal position 5.
**Semantic Links**:
- https://www.w3.org/2011/04/SCXML/state
**Examples**: Closed

### Column: prepared
**Type**: xdordinal
**Description**: Regulatory filing has been prepared but not yet submitted. Ordinal position 0 in Regulatory Filing pattern.
**Semantic Links**:
- https://www.w3.org/2011/04/SCXML/state
**Examples**: Prepared

### Column: under_review
**Type**: xdordinal
**Description**: Regulatory filing is under review by the regulatory body. Ordinal position 2 in Regulatory Filing pattern.
**Semantic Links**:
- https://www.w3.org/2011/04/SCXML/state
**Examples**: Under Review

### Column: returned
**Type**: xdordinal
**Description**: Regulatory filing has been returned for correction. Ordinal position 3 in Regulatory Filing pattern (return path).
**Semantic Links**:
- https://www.w3.org/2011/04/SCXML/state
**Examples**: Returned

### Column: resubmitted
**Type**: xdordinal
**Description**: Regulatory filing has been corrected and resubmitted. Ordinal position 4 in Regulatory Filing pattern (re-entry to Under Review).
**Semantic Links**:
- https://www.w3.org/2011/04/SCXML/state
**Examples**: Resubmitted
