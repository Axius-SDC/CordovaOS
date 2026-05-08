---
template_version: "4.0.0"
dataset:
  name: "Governance Access Control Tag Components"
  description: "W3C DPV access control tag components for data classification and consent management. Used in access control models linked via DM.acs."
  creator: "Axius SDC"
  project: "CordovaOS"
enrichment:
  enable_llm: true
---

# Dataset Overview

Components for W3C Data Privacy Vocabulary (DPV) access control tags. After upload, the auto-generated Cluster and DM will be deleted. These components are used in access control models linked via DM.acs (XdLinkType) to enforce data classification and consent requirements at the payload level.

**Standards Alignment**:
- W3C Data Privacy Vocabulary (https://w3c.github.io/dpv/dpv/)

**Access Control Levels**:
- Public: Open data, OGDA compliance
- Internal: Agency-internal only
- Restricted: Need-to-know (CIPSEA, Title 13)
- Confidential: PII, PHI, classified

## Data: Access Control Tag Components

### access_level
**Type**: xdordinal
**Description**: Access level classification tag for the data. Ordered from least to most restrictive. Determines who may access the data and under what conditions.
**Enumeration**:
- 0: PubliclyAvailable: https://w3c.github.io/dpv/dpv/#PubliclyAvailable
- 1: InternalUse: https://w3c.github.io/dpv/dpv/#InternalUse
- 2: RestrictedAccess: https://w3c.github.io/dpv/dpv/#RestrictedAccess
- 3: Confidential: https://w3c.github.io/dpv/dpv/#Confidential

### consent_required
**Type**: xdboolean
**Description**: Whether explicit consent is required before the data can be accessed or processed. Applies to Privacy Act, HIPAA, and other consent-based regulatory frameworks.
**Semantic Links**:
- https://w3c.github.io/dpv/dpv/#ConsentRequired
**Examples**: true, false

### access_justification
**Type**: xdstring
**Description**: Human-readable justification for the access level assignment. Documents why this classification was applied.
**Examples**: HIPAA-protected patient health information, CIPSEA statistical confidentiality pledge, OGDA open-by-default public dataset, Title 26 tax return confidentiality

### access_expiry
**Type**: xdtemporal
**Description**: When the access authorization expires. After this timestamp, access must be re-evaluated. ISO 8601 format.
**Examples**: 2027-01-01T00:00:00Z, 2026-12-31T23:59:59Z
