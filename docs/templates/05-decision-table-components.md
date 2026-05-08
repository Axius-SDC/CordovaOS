---
template_version: "4.0.0"
dataset:
  name: "Governance Decision Table Components"
  description: "OMG DMN decision table condition and outcome components for access control, retention, escalation, and workflow guard rules."
  creator: "Axius SDC"
  project: "CordovaOS"
enrichment:
  enable_llm: true
---

# Dataset Overview

Components for OMG DMN decision table conditions and outcomes. After upload, the auto-generated Cluster and DM will be deleted. These leaf components are used as inputs and outputs in DMN decision table definitions with FIRST, UNIQUE, or COLLECT hit policies.

**Standards Alignment**:
- OMG Decision Model and Notation (DMN)

**Decision Table Patterns**:
- Access Control: risk_score + role + classification -> PERMIT/DENY
- Retention Policy: data_age + sensitivity + legal_hold -> retain/archive/purge
- Escalation: severity + response_time + jurisdiction -> escalate/handle/defer
- Workflow Guard: current_state + actor_role + attestation_status -> allow/block

## Data: Decision Table Components

### risk_score
**Type**: xdcount
**Description**: Numeric risk assessment score. Used as a condition input in access control decision tables. Range 0-10.
**Constraints**:
  - range: [0, 10]
**Examples**: 0, 3, 5, 8, 10

### data_classification
**Type**: xdordinal
**Description**: Data classification level. Used as a condition input in access control and retention decision tables. Ordered from least to most restrictive.
**Enumeration**:
- 0: Public: https://w3c.github.io/dpv/dpv/#PubliclyAvailable
- 1: Internal: https://w3c.github.io/dpv/dpv/#InternalUse
- 2: Restricted: https://w3c.github.io/dpv/dpv/#RestrictedAccess
- 3: Confidential: https://w3c.github.io/dpv/dpv/#Confidential

### actor_role
**Type**: xdstring
**Description**: Role of the actor requesting the action. Used as a condition input in access control and workflow guard decision tables.
**Enumeration**:
- authorizer: Decision authority role
- reviewer: Review and approval role
- subject: Person or entity the data is about
- provider: Data source or originator
- processor: Automated system acting on data
- admin: System administrator
- auditor: Audit and compliance role

### severity_level
**Type**: xdordinal
**Description**: Incident severity level. Used as a condition input in escalation decision tables.
**Enumeration**:
- 1: Informational: Low-impact event requiring no immediate action
- 2: Low: Minor issue with limited operational impact
- 3: Medium: Moderate issue requiring timely response
- 4: High: Significant issue requiring urgent response
- 5: Critical: Severe issue requiring immediate escalation

### response_time_hours
**Type**: xdcount
**Description**: Hours elapsed since incident was reported. Used as a condition input in escalation decision tables.
**Constraints**:
  - range: [0, null]
**Examples**: 0, 1, 4, 8, 24, 72

### jurisdiction
**Type**: xdstring
**Description**: Geographic or legal jurisdiction. Used as a condition input in escalation and access control decision tables.
**Examples**: Federal, State, Local, International, Porto Sereno, EU, US

### data_age_days
**Type**: xdcount
**Description**: Age of data in days since creation. Used as a condition input in retention policy decision tables.
**Constraints**:
  - range: [0, null]
**Examples**: 0, 30, 90, 365, 730, 2555

### sensitivity_level
**Type**: xdordinal
**Description**: Data sensitivity classification. Used as a condition input in retention policy decision tables. Ordered from least to most sensitive.
**Enumeration**:
- 0: Low: Minimal sensitivity, standard handling
- 1: Medium: Moderate sensitivity, controlled access
- 2: High: High sensitivity, restricted access required
- 3: Critical: Maximum sensitivity, strict access controls

### legal_hold_active
**Type**: xdboolean
**Description**: Whether a legal hold is currently active on the data. Used as a condition input in retention policy decision tables.
**Examples**: true, false

### decision_outcome
**Type**: xdstring
**Description**: The decision result from a DMN evaluation. OASIS XACML-aligned values for governance decisions, plus domain-specific outcomes for retention and escalation.
**Semantic Links**:
- https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html
**Enumeration**:
- PERMIT: https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html
- DENY: https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html
- escalate: Domain-specific escalation outcome
- handle: Domain-specific handle-in-place outcome
- defer: Domain-specific deferred action outcome
- retain: Retention policy keep outcome
- archive: Retention policy archive outcome
- purge: Retention policy purge outcome
- allow_transition: Workflow guard permit transition
- block: Workflow guard block transition

### attestation_status
**Type**: xdstring
**Description**: Current status of attestation. Used as a condition input in workflow guard decision tables.
**Enumeration**:
- pending: Attestation not yet completed
- complete: Attestation successfully completed
- expired: Attestation has expired and must be renewed
- delegated: Attestation performed by delegated authority
