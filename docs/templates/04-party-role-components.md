---
template_version: "4.0.0"
dataset:
  name: "Governance Party and Role Components"
  description: "Party identity and participation role components. Maps to SDC4 PartyType and ParticipationType structures."
  domain: "Governance"
  creator: "Axius SDC"
  project: "CordovaOS"
enrichment:
  enable_llm: true
---

# Dataset Overview

Components for party identity and participation roles. After upload, the auto-generated Cluster and DM will be deleted. Party identity components (name, identifier, email, organization) will be manually grouped into Party detail Clusters. Function components are used in ParticipationType.

**Standards Alignment**:
- SDC4 PartyType (party-name, party-ref, party-details)
- SDC4 ParticipationType (performer, function, mode)

## Data: Party and Role Components

### Column: party_name
**Type**: xdstring
**Description**: Name of the party (person, organization, or system). Used in PartyType.party-name and in party-details Cluster.
**Constraints**:
  - required: true
**Examples**: Dr. Maria Santos, Porto Sereno General Hospital, Automated Validation System

### Column: party_identifier
**Type**: xdstring
**Description**: Unique identifier for the party. Used for cross-system party resolution.
**Constraints**:
  - required: true
**Examples**: PROV-AGT-001, ORG-PSGH, SYS-VALIDATOR-01

### Column: party_email
**Type**: xdstring
**Description**: Contact email address for the party. Used in party-details Cluster.
**Examples**: m.santos@psgh.gov.cs, admin@portoserenoport.gov.cs

### Column: party_organization
**Type**: xdstring
**Description**: Organization the party belongs to. Used in party-details Cluster.
**Examples**: Porto Sereno General Hospital, Ministry of Health, Port Authority

### Column: function_authorizer
**Type**: xdstring
**Description**: Participation function value for decision authority. Used in ParticipationType.function to indicate the party has authorization power.
**Constraints**:
  - required: true
**Examples**: authorizer

### Column: function_reviewer
**Type**: xdstring
**Description**: Participation function value for review/approval role. Used in ParticipationType.function.
**Constraints**:
  - required: true
**Examples**: reviewer

### Column: function_subject
**Type**: xdstring
**Description**: Participation function value for the person or entity the data is about. Used in ParticipationType.function.
**Constraints**:
  - required: true
**Examples**: subject

### Column: function_provider
**Type**: xdstring
**Description**: Participation function value for data source or originator. Used in ParticipationType.function.
**Constraints**:
  - required: true
**Examples**: provider

### Column: function_processor
**Type**: xdstring
**Description**: Participation function value for automated system acting on data. Used in ParticipationType.function.
**Constraints**:
  - required: true
**Examples**: processor

### Column: participation_mode
**Type**: xdstring
**Description**: How the participation occurred. Used in ParticipationType.mode.
**Examples**: present, remote, telephone, email, automated, delegated
