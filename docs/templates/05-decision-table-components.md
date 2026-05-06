---
template_version: "4.0.0"
dataset:
  name: "Governance Decision Table Components"
  description: "OMG DMN decision table condition and outcome components for access control, retention, escalation, and workflow guard rules."
  domain: "Governance"
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

### Column: risk_score
**Type**: xdcount
**Description**: Numeric risk assessment score. Used as a condition input in access control decision tables. Range 0-10.
**Constraints**:
  - min_value: 0
  - max_value: 10
**Examples**: 0, 3, 5, 8, 10

### Column: data_classification
**Type**: xdstring
**Description**: Data classification level. Used as a condition input in access control and retention decision tables.
**Examples**: Public, Internal, Restricted, Confidential

### Column: actor_role
**Type**: xdstring
**Description**: Role of the actor requesting the action. Used as a condition input in access control and workflow guard decision tables.
**Examples**: authorizer, reviewer, subject, provider, processor, admin, auditor

### Column: severity_level
**Type**: xdordinal
**Description**: Incident severity level. Used as a condition input in escalation decision tables. Ordinal 1-5.
**Examples**: 1, 2, 3, 4, 5

### Column: response_time_hours
**Type**: xdcount
**Description**: Hours elapsed since incident was reported. Used as a condition input in escalation decision tables.
**Constraints**:
  - min_value: 0
**Examples**: 0, 1, 4, 8, 24, 72

### Column: jurisdiction
**Type**: xdstring
**Description**: Geographic or legal jurisdiction. Used as a condition input in escalation and access control decision tables.
**Examples**: Federal, State, Local, International, Porto Sereno, EU, US

### Column: data_age_days
**Type**: xdcount
**Description**: Age of data in days since creation. Used as a condition input in retention policy decision tables.
**Constraints**:
  - min_value: 0
**Examples**: 0, 30, 90, 365, 730, 2555

### Column: sensitivity_level
**Type**: xdstring
**Description**: Data sensitivity classification. Used as a condition input in retention policy decision tables.
**Examples**: Low, Medium, High, Critical

### Column: legal_hold_active
**Type**: xdboolean
**Description**: Whether a legal hold is currently active on the data. Used as a condition input in retention policy decision tables.
**Examples**: true, false

### Column: decision_outcome
**Type**: xdstring
**Description**: The decision result from a DMN evaluation. OASIS XACML-aligned values for governance decisions, plus domain-specific outcomes for retention and escalation.
**Semantic Links**:
- https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html
**Examples**: PERMIT, DENY, escalate, handle, defer, retain, archive, purge, allow_transition, block

### Column: attestation_status
**Type**: xdstring
**Description**: Current status of attestation. Used as a condition input in workflow guard decision tables.
**Examples**: pending, complete, expired, delegated
