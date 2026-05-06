---
template_version: "4.0.0"
dataset:
  name: "Governance Retention Policy Components"
  description: "W3C DPV retention policy components for provenance record lifecycle management. Three levels: most recent + hash, last N records, full chain."
  domain: "Governance"
  creator: "Axius SDC"
  project: "CordovaOS"
enrichment:
  enable_llm: true
---

# Dataset Overview

Components for W3C Data Privacy Vocabulary (DPV) retention policies. After upload, the auto-generated Cluster and DM will be deleted. These components are used in retention policy models linked via DM.acs (XdLinkType).

**Standards Alignment**:
- W3C Data Privacy Vocabulary (https://w3c.github.io/dpv/dpv/)
- W3C DPV StorageDuration
- W3C DPV StorageCondition

**Retention Levels**:
- Most Recent + Hash: keep latest record, SHA-256 hash of previous (performance-sensitive)
- Last N Records: keep N most recent provenance records (operational audit)
- Full Chain: keep entire provenance history (legal hold, regulatory compliance)

## Data: Retention Policy Components

### Column: retention_level
**Type**: xdstring
**Description**: The retention policy level. Determines how many provenance records are preserved.
**Constraints**:
  - required: true
**Semantic Links**:
- https://w3c.github.io/dpv/dpv/#StorageDuration
**Examples**: most_recent, last_n, full_chain

### Column: retention_count_n
**Type**: xdcount
**Description**: Number of provenance records to retain when using the last_n retention level. Only applicable when retention_level is last_n.
**Constraints**:
  - min_value: 1
**Examples**: 5, 10, 25, 100

### Column: retention_hash
**Type**: xdstring
**Description**: SHA-256 hash of pruned provenance records. Used with most_recent retention level to maintain integrity verification of the pruned history.
**Examples**: a3f5b2c1d4e6f7890123456789abcdef0123456789abcdef0123456789abcdef

### Column: retention_justification
**Type**: xdstring
**Description**: Human-readable justification for the chosen retention level. Documents why this retention policy was selected for this data.
**Examples**: HIPAA requires full chain for patient records, Operational audit trail for internal systems, Performance optimization for high-volume transaction logs

### Column: storage_condition
**Type**: xdstring
**Description**: Conditions governing storage of the provenance records. Aligned with W3C DPV StorageCondition vocabulary.
**Semantic Links**:
- https://w3c.github.io/dpv/dpv/#StorageCondition
**Examples**: encrypted_at_rest, access_controlled, legal_hold, regulatory_compliance, standard
