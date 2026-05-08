---
template_version: "4.0.0"
dataset:
  name: "Governance Party and Role Components"
  description: "Party identity and participation role components. Maps to SDC4 PartyType and ParticipationType structures."
  creator: "Axius SDC"
  project: "CordovaOS"
enrichment:
  enable_llm: true
---

# Dataset Overview

Components for party identity and participation roles. After upload, the auto-generated Cluster and DM will be deleted. Party identity components (name, identifier, email, organization) will be manually grouped into Party detail Clusters. The participation_function component provides role values for ParticipationType.

**Standards Alignment**:
- SDC4 PartyType (party-name, party-ref, party-details)
- SDC4 ParticipationType (performer, function, mode)

## Data: Party and Role Components

### party_name
**Type**: xdstring
**Description**: Name of the party (person, organization, or system). Used in PartyType.party-name and in party-details Cluster.
**Constraints**:
  - required: true
**Examples**: Dr. Maria Santos, Porto Sereno General Hospital, Automated Validation System

### party_identifier
**Type**: xdstring
**Description**: Unique identifier for the party. Used for cross-system party resolution.
**Constraints**:
  - required: true
**Examples**: PROV-AGT-001, ORG-PSGH, SYS-VALIDATOR-01

### party_email
**Type**: xdstring
**Description**: Contact email address for the party. Used in party-details Cluster.
**Examples**: m.santos@psgh.gov.cs, admin@portoserenoport.gov.cs

### party_organization
**Type**: xdstring
**Description**: Organization the party belongs to. Used in party-details Cluster.
**Examples**: Porto Sereno General Hospital, Ministry of Health, Port Authority

### participation_function
**Type**: xdstring
**Description**: Participation function value indicating the party's role in the data interaction. Used in ParticipationType.function.
**Constraints**:
  - required: true
**Enumeration**:
- authorizer: Party with decision authority
- reviewer: Party performing review or approval
- subject: Person or entity the data is about
- provider: Data source or originator
- processor: Automated system acting on data

### participation_mode
**Type**: xdstring
**Description**: How the participation occurred. Used in ParticipationType.mode.
**Enumeration**:
- present: In-person participation
- remote: Remote electronic participation
- telephone: Voice communication
- email: Email communication
- automated: System-initiated without human action
- delegated: Acting on behalf of another party
