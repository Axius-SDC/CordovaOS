---
template_version: "4.0.0"
dataset:
  name: "Governance Attestation Components"
  description: "W3C VC 2.0 pattern attestation components for authority assertions. Maps to SDC4 AttestationType structure."
  domain: "Governance"
  creator: "Axius SDC"
  project: "CordovaOS"
enrichment:
  enable_llm: true
---

# Dataset Overview

Components for attestation authority assertions following the W3C Verifiable Credentials 2.0 issuer/holder/verifier pattern. After upload, the auto-generated Cluster and DM will be deleted. These leaf components are used within AttestationType structures. The committer (Party) comes from template 04.

**Standards Alignment**:
- W3C Verifiable Credentials Data Model 2.0 (https://www.w3.org/TR/vc-data-model-2.0/)

## Data: Attestation Components

### Column: attestation_reason
**Type**: xdstring
**Description**: Reason or type of attestation. Describes the basis for the authority assertion. Should be coded from a standard vocabulary where possible.
**Constraints**:
  - required: true
**Semantic Links**:
- https://www.w3.org/2018/credentials#credentialSubject
**Examples**: Clinical authority review, HIPAA compliance attestation, Chain of custody verification, FERPA authorization

### Column: attestation_proof
**Type**: xdfile
**Description**: Cryptographic or documentary proof of attestation. GPG signature, digital certificate, or reference to documentary evidence.
**Semantic Links**:
- https://www.w3.org/2018/credentials#proof
**Examples**: GPG signature block, X.509 certificate reference, notarized document scan

### Column: attestation_view
**Type**: xdfile
**Description**: Visual representation of the attested content. Screen capture, PDF rendering, or other visual evidence of what was attested to.
**Examples**: Screenshot of record at time of attestation, PDF of signed form

### Column: delegation_scope
**Type**: xdstring
**Description**: Scope of delegated authority when attestation is performed on behalf of another party. Defines the boundaries of the delegation.
**Examples**: All patient records in Ward 3, Tax filings for fiscal year 2025, Maritime manifests for Port of Porto Sereno

### Column: committed_timestamp
**Type**: xdtemporal
**Description**: Timestamp when the attestation was committed. ISO 8601 format. This is when the authority assertion became active.
**Examples**: 2026-05-05T14:00:00Z, 2026-03-15T09:30:00-04:00
