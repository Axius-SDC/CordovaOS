---
template_version: "4.0.0"
dataset:
  name: "Governance Validation Details Components"
  description: "Entity state hash components using the SDC4 RM XdFileType pattern (hash-function + hash-result) for tamper-evident provenance chains."
  domain: "Governance"
  creator: "Axius SDC"
  project: "CordovaOS"
enrichment:
  enable_llm: true
---

# Dataset Overview

Components for entity state hashes that create tamper-evident provenance chains. Uses the SDC4 RM XdFileType hash pattern (hash-function + hash-result). After upload, the auto-generated Cluster and DM will be deleted. These components will be manually assembled into a validation-details Cluster with entity-state-before and entity-state-after sub-groupings within the data Cluster.

**Standards Alignment**:
- SDC4 RM XdFileType (hash-function, hash-result elements)

**SDC5 Note**: An issue has been filed on the sdc5-planning branch to add a validation slot directly to AuditType, eliminating the need to place these components in the data Cluster.

## Data: Validation Details Components

### Column: entity_state_before_hash_function
**Type**: xdstring
**Description**: Hash algorithm identifier for the entity state before the activity. Always SHA-256 for sdcgovernance.
**Constraints**:
  - required: true
**Semantic Links**:
- https://semanticdatacharter.com/ns/sdc4/hash-function
**Examples**: SHA-256

### Column: entity_state_before_hash_result
**Type**: xdfile
**Description**: Computed SHA-256 hash of the entity state before the activity. Used to verify the entity was not tampered with between recorded activities.
**Constraints**:
  - required: true
**Semantic Links**:
- https://semanticdatacharter.com/ns/sdc4/hash-result
**Examples**: a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2

### Column: entity_state_after_hash_function
**Type**: xdstring
**Description**: Hash algorithm identifier for the entity state after the activity. Always SHA-256 for sdcgovernance.
**Constraints**:
  - required: true
**Semantic Links**:
- https://semanticdatacharter.com/ns/sdc4/hash-function
**Examples**: SHA-256

### Column: entity_state_after_hash_result
**Type**: xdfile
**Description**: Computed SHA-256 hash of the entity state after the activity. The next activity's entity_state_before_hash_result must match this value for the chain to be valid.
**Constraints**:
  - required: true
**Semantic Links**:
- https://semanticdatacharter.com/ns/sdc4/hash-result
**Examples**: f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3b2a1f6e5
