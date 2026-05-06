---
template_version: "4.0.0"
dataset:
  name: "Governance Provenance Components"
  description: "W3C PROV-O components for provenance tracking. Maps to SDC4 AuditType structure: Entity (system-id), Activity (timestamp, type), Agent (system-user)."
  domain: "Governance"
  creator: "Axius SDC"
  project: "CordovaOS"
enrichment:
  enable_llm: true
---

# Dataset Overview

Components for W3C PROV-O provenance records mapped to SDC4 AuditType. After upload, the auto-generated Cluster and DM will be deleted. These leaf components are used within AuditType structures when building domain data models.

**Standards Alignment**:
- W3C PROV-O (https://www.w3.org/TR/prov-o/)
- W3C PROV-DM (https://www.w3.org/TR/prov-dm/)
- W3C Activity Streams 2.0 (https://www.w3.org/TR/activitystreams-core/)

## Data: Provenance Components

### Column: system_identifier
**Type**: xdstring
**Description**: Identifier of the system that handled the data. Maps to prov:Entity context in the PROV-O export. This is the AuditType.system-id field.
**Constraints**:
  - required: true
**Semantic Links**:
- http://www.w3.org/ns/prov#Entity
**Examples**: healthcare-ehr-prod, law-enforcement-rms, tax-revenue-system

### Column: activity_timestamp_start
**Type**: xdtemporal
**Description**: When the provenance activity began. Maps to prov:startedAtTime. ISO 8601 format.
**Constraints**:
  - required: true
**Semantic Links**:
- http://www.w3.org/ns/prov#startedAtTime
**Examples**: 2026-05-05T08:00:00Z, 2026-01-15T14:30:00-05:00

### Column: activity_timestamp_end
**Type**: xdtemporal
**Description**: When the provenance activity completed. Maps to prov:endedAtTime. ISO 8601 format.
**Semantic Links**:
- http://www.w3.org/ns/prov#endedAtTime
**Examples**: 2026-05-05T08:00:01Z, 2026-01-15T14:30:05-05:00

### Column: activity_type
**Type**: xdstring
**Description**: Type of activity from the W3C Activity Streams 2.0 vocabulary. Describes what was done to the data.
**Constraints**:
  - required: true
**Semantic Links**:
- https://www.w3.org/ns/activitystreams#Activity
**Examples**: Create, Update, Delete, Accept, Reject, Approve, Add, Remove, Read, View

### Column: activity_description
**Type**: xdstring
**Description**: Human-readable description of the provenance activity. What was done and why.
**Examples**: Initial patient record creation, Updated vital signs after examination, Approved for discharge

### Column: system_location_name
**Type**: xdstring
**Description**: Name of the physical or logical location where the system resides. Maps to prov:atLocation.
**Semantic Links**:
- http://www.w3.org/ns/prov#atLocation
**Examples**: Porto Sereno General Hospital, Oak Ridge National Laboratory, Census Bureau HQ

### Column: system_location_identifier
**Type**: xdstring
**Description**: Code or identifier for the system location. Used for cross-system location resolution.
**Examples**: LOC-PSGH-001, ORNL-BLDG-4500, CB-SUITLAND-MD
