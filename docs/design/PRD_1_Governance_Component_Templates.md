# PRD 1: Governance Component Templates

**Date**: May 5, 2026
**Status**: Planning
**Depends on**: Nothing - this is the foundation
**Blocks**: PRD 2 (CordovaOS Model Rebuild)

---

## 1. Objective

Design, build, and validate a set of standards-based, generic governance component templates that can be uploaded to SDCStudio, processed into SDC4 components, published, and reused across any domain. These components become the governance catalog that CordovaOS and all future SDC deployments draw from.

## 2. Design Principles

1. **Generic first.** Every governance component must work across domains. A document approval workflow works the same for a healthcare record, a law enforcement report, or a port manifest. Domain-specific adaptation happens at composition time in PRD 2, not at component design time.

2. **Standards-bound.** Every component binds to a published standard vocabulary:
   - Workflow: W3C SCXML concepts of state and transition
   - Provenance: W3C PROV-O (Entity, Activity, Agent)
   - Retention: W3C DPV (StorageDuration, StorageCondition)
   - Attestation: W3C VC 2.0 (issuer/holder/verifier pattern)
   - Decision tables: OMG DMN (FIRST, UNIQUE, COLLECT hit policies)
   - Activity types: W3C Activity Streams 2.0
   - Access control: W3C DPV vocabulary
   - Party/Role: SDC4 ParticipationType

3. **Minimum knowledge.** Each governance component captures only what distinguishes it from nearby concepts. A workflow state captures the state symbol, ordinal position, and label - not the business logic that uses it.

4. **Publication-ready.** Templates must parse correctly in SDCStudio's AI processing pipeline. This means correct YAML frontmatter, correct cluster/sub-cluster hierarchy, correct column definitions, and correct semantic link format.

5. **Tested end-to-end.** Every component must survive the full pipeline: template -> SDCStudio upload -> AI processing -> human review -> publication -> XSD generation -> XML instance creation -> sdcvalidator pass -> sdcgovernance XACML decision.

## 3. Component Catalog

### 3.1 Workflow State Machines

Each workflow is a ClusterType with sub-clusters defining valid paths. Each sub-cluster contains XdOrdinal components for sequenced states.

| Template | States | Paths | Use Case |
|---|---|---|---|
| **Document Lifecycle** | Draft, Review, Approved, Published, Archived | 1 linear | Standard document progression |
| **Record Intake** | Submitted, Validated, Accepted, Rejected | 2 branching (accept/reject) | Incoming data validation |
| **Incident Response** | Reported, Triaged, Assigned, In Progress, Resolved, Closed | 1 linear with skip rules | Event-driven workflows |
| **Regulatory Filing** | Prepared, Submitted, Under Review, Approved, Returned, Resubmitted | 2 branching (approve/return) with re-entry | Compliance workflows |

**Template format for each workflow:**
- YAML frontmatter with template_version, enrichment settings
- Root ClusterType (the workflow)
- Sub-cluster per valid path
- XdOrdinal per state within each path (ordinal position defines sequence)
- Semantic links to SCXML concepts
- Current-state XdString at DM root level

### 3.2 Provenance Records (W3C PROV-O)

| Template | PROV Type | Components | Use Case |
|---|---|---|---|
| **PROV Entity** | prov:Entity | system-id (XdString), identifier (XdLink), type (XdToken) | What was acted on |
| **PROV Activity** | prov:Activity | timestamp (XdTemporal), activity-type (XdToken from Activity Streams 2.0), description (XdString) | What was done |
| **PROV Agent** | prov:Agent | system-user (Party), agent-type (XdToken), location (Cluster) | Who did it |
| **PROV Bundle** | Complete record | Entity + Activity + Agent composed | Full audit record mapping to SDC4 AuditType |

**Activity types from W3C Activity Streams 2.0:**
Create, Update, Delete, Accept, Reject, Add, Remove, Move, Read, View, Approve

### 3.3 Attestation Models (W3C VC 2.0 Pattern)

| Template | Components | Use Case |
|---|---|---|
| **Standard Attestation** | committer (Party), reason (XdString), proof (XdFile), pending (XdBoolean), committed-timestamp (XdTemporal) | General authority assertion |
| **Delegated Attestation** | Above + delegated-by (Party), delegation-scope (XdString) | Authority delegated from another party |

### 3.4 Party/Role Components

| Template | Function | Use Case |
|---|---|---|
| **Authorizer** | Party with function "authorizer" | Decision authority |
| **Reviewer** | Party with function "reviewer" | Review/approval step |
| **Subject** | Party with function "subject" | Person/entity the data is about |
| **Provider** | Party with function "provider" | Data source/originator |
| **Processor** | Party with function "processor" | Automated system acting on data |

Each Party has a details Cluster (name, identifier, contact) and optional external references (XdLink).

### 3.5 Decision Tables (OMG DMN)

| Template | Hit Policy | Conditions | Outcomes | Use Case |
|---|---|---|---|---|
| **Access Control** | FIRST | risk_score, role, data_classification | PERMIT, DENY | Role + risk-based access |
| **Retention Policy** | FIRST | data_age, sensitivity, legal_hold | retain, archive, purge | Data lifecycle management |
| **Escalation** | FIRST | severity, response_time, jurisdiction | escalate, handle, defer | Incident prioritization |
| **Workflow Guard** | UNIQUE | current_state, actor_role, attestation_status | allow_transition, block | State transition authorization |

### 3.6 Retention Policies (W3C DPV)

| Template | Level | Behavior | Use Case |
|---|---|---|---|
| **Most Recent + Hash** | Minimal retention | Keep latest provenance record, SHA-256 hash of previous | Performance-sensitive, low-regulation |
| **Last N Records** | Moderate retention | Keep N most recent provenance records (configurable N) | Operational audit trail |
| **Full Chain** | Maximum retention | Keep entire provenance history, no pruning | Legal hold, regulatory compliance |

### 3.7 Access Control Tags (W3C DPV)

| Template | Tag | Use Case |
|---|---|---|
| **Public** | dpv:PubliclyAvailable | Open data, OGDA compliance |
| **Internal** | dpv:InternalUse | Agency-internal only |
| **Restricted** | dpv:RestrictedAccess | Need-to-know, CIPSEA, Title 13 |
| **Confidential** | dpv:Confidential | PII, PHI, classified |
| **Consent Required** | dpv:ConsentRequired | Privacy Act, HIPAA |

## 4. Template Design and Construction Strategy

### The Constraint

SDCStudio is designed to build complete data models. When it processes a markdown template, it creates a data Cluster containing all the components and a DM wrapping it. We don't want full models - we want individual components in the catalog that can be composed into any domain model later.

### The Approach

1. **One markdown template per governance dimension** - pack ALL components for that dimension into a single flat Cluster. SDCStudio creates them all in one upload.
2. **SDCStudio AI processes the template** - generates typed SDC4 components from the column definitions.
3. **HITL review** - verify every component (types, constraints, labels, vocabulary bindings). The AI is probabilistic - expect corrections.
4. **Delete the auto-generated Cluster and DM** via Django admin - we only wanted the leaf components.
5. **Manually create proper Clusters** for components that need structural grouping (workflow sub-clusters with paths, validation-details, etc.).
6. **Publish bottom-up** - leaf components first, then Clusters, following the 5-level publication order.

This is a hack - using SDCStudio as a component factory rather than a model builder. Since the Django admin allows deletion of unpublished Clusters/DMs before publication, it works cleanly.

### Template Design Location

All templates designed in:
`/home/twcook/GitHub/CordovaOS/docs/design/templates/`

```
templates/
  01-workflow-components.md       # All workflow state XdOrdinals for all 4 patterns
  02-provenance-components.md     # All PROV-O components (entity, activity, agent fields)
  03-attestation-components.md    # All attestation fields
  04-party-role-components.md     # All party/role function definitions
  05-decision-table-components.md # All decision table condition/outcome fields
  06-retention-components.md      # All retention policy fields
  07-validation-details.md        # Entity state hash components (XdFileType)
  08-access-control-tags.md       # DPV access control tag components
```

### Template Contents

Each template is a single markdown file with YAML frontmatter and one root Cluster containing all components for that dimension. After SDCStudio upload and component review, the auto-generated Cluster and DM are deleted; only the leaf components remain in the catalog.

#### 01-workflow-components.md

One Cluster containing all XdOrdinal state components across all 4 workflow patterns. Each XdOrdinal gets a unique label and ordinal position.

| Component Label | Type | Ordinal | Workflow Pattern | Semantic Link |
|---|---|---|---|---|
| Draft | XdOrdinal | 0 | Document Lifecycle, Record Intake | SCXML state concept |
| Review | XdOrdinal | 1 | Document Lifecycle | SCXML state concept |
| Approved | XdOrdinal | 2 | Document Lifecycle, Regulatory Filing | SCXML state concept |
| Published | XdOrdinal | 3 | Document Lifecycle | SCXML state concept |
| Archived | XdOrdinal | 4 | Document Lifecycle | SCXML state concept |
| Submitted | XdOrdinal | 0 | Record Intake, Regulatory Filing | SCXML state concept |
| Validated | XdOrdinal | 1 | Record Intake | SCXML state concept |
| Accepted | XdOrdinal | 2 | Record Intake | SCXML state concept |
| Rejected | XdOrdinal | 2 | Record Intake (branch) | SCXML state concept |
| Reported | XdOrdinal | 0 | Incident Response | SCXML state concept |
| Triaged | XdOrdinal | 1 | Incident Response | SCXML state concept |
| Assigned | XdOrdinal | 2 | Incident Response | SCXML state concept |
| In Progress | XdOrdinal | 3 | Incident Response | SCXML state concept |
| Resolved | XdOrdinal | 4 | Incident Response | SCXML state concept |
| Closed | XdOrdinal | 5 | Incident Response | SCXML state concept |
| Prepared | XdOrdinal | 0 | Regulatory Filing | SCXML state concept |
| Under Review | XdOrdinal | 1 | Regulatory Filing | SCXML state concept |
| Returned | XdOrdinal | 2 | Regulatory Filing (branch) | SCXML state concept |
| Resubmitted | XdOrdinal | 3 | Regulatory Filing (re-entry) | SCXML state concept |

**Post-upload manual work**: Delete auto-generated Cluster/DM. Manually create 4 workflow ClusterTypes with sub-clusters defining valid paths. Assign XdOrdinal components to the correct paths.

**Note**: Some states are shared across patterns (Draft, Approved, Submitted). These reuse the same CUID2 - component reuse in action. Others are unique to a specific pattern (Triaged, Prepared).

#### 02-provenance-components.md

One Cluster containing all PROV-O related fields:

| Component Label | Type | Semantic Link | Purpose |
|---|---|---|---|
| System Identifier | XdString | prov:Entity | Which system handled the data |
| Activity Timestamp Start | XdTemporal | prov:startedAtTime | When the activity began |
| Activity Timestamp End | XdTemporal | prov:endedAtTime | When the activity completed |
| Activity Type | XdString | W3C Activity Streams 2.0 | What kind of activity (Create, Update, Approve, etc.) |
| Activity Description | XdString | rdfs:comment | Human-readable activity description |
| System Location Name | XdString | prov:atLocation | Where the system is located |
| System Location Identifier | XdString | - | System location code/ID |

**Post-upload manual work**: Delete Cluster/DM. These components are used within AuditType structure. Party components for system-user come from template 04.

#### 03-attestation-components.md

One Cluster containing attestation fields:

| Component Label | Type | Semantic Link | Purpose |
|---|---|---|---|
| Attestation Reason | XdString | W3C VC 2.0 | Type/basis of attestation |
| Attestation Proof | XdFile | W3C VC 2.0 | Cryptographic or documentary evidence |
| Attestation View | XdFile | W3C VC 2.0 | Visual representation of attested content |
| Delegation Scope | XdString | - | Scope of delegated authority |
| Committed Timestamp | XdTemporal | - | When attestation was committed |

**Post-upload manual work**: Delete Cluster/DM. These are used within AttestationType. Committer Party comes from template 04.

#### 04-party-role-components.md

One Cluster containing party/role definitions:

| Component Label | Type | Semantic Link | Purpose |
|---|---|---|---|
| Party Name | XdString | - | Name of the party |
| Party Identifier | XdString | - | Unique identifier for the party |
| Party Email | XdString | - | Contact email |
| Party Organization | XdString | - | Organization affiliation |
| Function Authorizer | XdString | - | Role: decision authority |
| Function Reviewer | XdString | - | Role: review/approval |
| Function Subject | XdString | - | Role: person/entity the data is about |
| Function Provider | XdString | - | Role: data source/originator |
| Function Processor | XdString | - | Role: automated system |
| Participation Mode | XdString | - | How participation occurred (present, remote, automated) |

**Post-upload manual work**: Delete Cluster/DM. Manually create Party detail Clusters from identity components (Name, Identifier, Email, Organization). Function components are used in ParticipationType.

#### 05-decision-table-components.md

One Cluster containing decision table condition and outcome fields:

| Component Label | Type | Semantic Link | Purpose |
|---|---|---|---|
| Risk Score | XdCount | - | Numeric risk assessment (0-10) |
| Data Classification | XdString | - | Public/Internal/Restricted/Confidential |
| Actor Role | XdString | - | Role of the actor requesting action |
| Severity Level | XdOrdinal | - | Incident severity (1-5) |
| Response Time Hours | XdCount | - | Hours since incident reported |
| Jurisdiction | XdString | - | Geographic/legal jurisdiction |
| Data Age Days | XdCount | - | Age of data in days |
| Sensitivity Level | XdString | - | Data sensitivity classification |
| Legal Hold Active | XdBoolean | - | Whether legal hold applies |
| Decision Outcome | XdString | OMG DMN | PERMIT/DENY/escalate/retain/archive/purge |
| Attestation Status | XdString | - | pending/complete |

**Post-upload manual work**: Delete Cluster/DM. These components are used as inputs and outputs in DMN decision table definitions.

#### 06-retention-components.md

One Cluster containing retention policy fields:

| Component Label | Type | Semantic Link | Purpose |
|---|---|---|---|
| Retention Level | XdString | W3C DPV StorageDuration | most_recent/last_n/full_chain |
| Retention Count N | XdCount | - | Number of records to retain (for last_n) |
| Retention Hash | XdString | - | Hash of pruned records (for most_recent) |
| Retention Justification | XdString | - | Why this retention level was chosen |
| Storage Condition | XdString | W3C DPV StorageCondition | Conditions governing storage |

**Post-upload manual work**: Delete Cluster/DM. These components are used in DPV retention policy models linked via DM.acs.

#### 07-validation-details.md

One Cluster containing entity state hash components:

| Component Label | Type | Semantic Link | Purpose |
|---|---|---|---|
| Entity State Before Hash Function | XdString | sdc4:hash-function | Algorithm identifier ("SHA-256") |
| Entity State Before Hash Result | XdFile | sdc4:hash-result | Computed hash of entity state before activity |
| Entity State After Hash Function | XdString | sdc4:hash-function | Algorithm identifier ("SHA-256") |
| Entity State After Hash Result | XdFile | sdc4:hash-result | Computed hash of entity state after activity |

**Post-upload manual work**: Delete Cluster/DM. Manually create validation-details Cluster with entity-state-before and entity-state-after sub-groupings using the XdFileType hash pattern.

#### 08-access-control-tags.md

One Cluster containing DPV access control tag components:

| Component Label | Type | Semantic Link | Purpose |
|---|---|---|---|
| Access Level Public | XdString | dpv:PubliclyAvailable | Open data, OGDA compliance |
| Access Level Internal | XdString | dpv:InternalUse | Agency-internal only |
| Access Level Restricted | XdString | dpv:RestrictedAccess | Need-to-know, CIPSEA, Title 13 |
| Access Level Confidential | XdString | dpv:Confidential | PII, PHI, classified |
| Consent Required | XdBoolean | dpv:ConsentRequired | Privacy Act, HIPAA consent gate |
| Access Justification | XdString | - | Reason for access level assignment |
| Access Expiry | XdTemporal | - | When access authorization expires |

**Post-upload manual work**: Delete Cluster/DM. These components are used in access control models linked via DM.acs (XdLinkType).

## 5. Validation Pipeline

For each of the 8 templates:

### Step 1: Template Review (HITL)
- Verify YAML frontmatter is correct
- Verify all columns have correct Type, Semantic Link, and Constraints
- Verify component labels are clear and unambiguous

### Step 2: SDCStudio Upload
- Upload template to SDCStudio
- Observe AI processing pipeline (2 stages)
- Document any processing errors or unexpected interpretations

### Step 3: Component Review (HITL - Critical)
- Review every generated component
- Check data types, constraints, labels, vocabulary bindings
- The AI is probabilistic - expect corrections needed
- Start with leaf elements (Units, Strings, Booleans) and work up

### Step 4: Delete Auto-Generated Cluster and DM
- Via Django admin, delete the auto-generated Cluster and DM
- Verify only the leaf components remain in the catalog
- Do NOT publish the auto-generated Cluster or DM

### Step 5: Manual Cluster Construction (HITL)
- Create proper ClusterTypes for components that need structural grouping:
  - 4 workflow ClusterTypes with sub-clusters defining valid paths
  - Party detail Clusters
  - Validation-details Cluster with entity-state-before/after sub-groupings
- Assign components to the correct Clusters

### Step 6: Publication
- Follow the 5-level bottom-up publication order
- Verify SDCStudio blocks publication if dependencies aren't met
- Leaf components first, then Clusters

### Step 7: Verification
- Verify all published components appear in the SDCStudio catalog
- Verify components are reusable (can be added to a new model)
- Spot-check vocabulary bindings on published components

## 6. Success Criteria

1. All templates in Section 3 are designed, uploaded, and published without errors
2. XSD schemas generated from published models contain all governance slots
3. XML instances with governance content pass sdcvalidator
4. sdcgovernance returns correct XACML decisions on governance content
5. Receipt chain is valid across multiple decisions
6. All components are in the SDCStudio catalog and reusable for PRD 2

## 7. Risks

| Risk | Mitigation |
|---|---|
| SDCStudio AI misinterprets governance template structure | HITL review at Step 3. Budget time for corrections. |
| Workflow ClusterType with sub-clusters doesn't parse correctly | Test with simplest workflow (2-state linear) first before complex branching |
| Governance slots not populated in generated XSD | Verify DM root structure matches RM_Reference.md slot definitions |
| sdcgovernance expects different XML structure than SDCStudio generates | Compare generated XML against sdcgovernance test fixtures for format compatibility |

## 8. Timeline

Estimated 5-7 working days with significant HITL time:
- Day 1-2: Design all templates
- Day 3-4: Upload, process, review, edit, publish (iterative)
- Day 5-6: XSD generation, instance creation, validation testing
- Day 7: Debug, fix, re-validate

---

*This PRD feeds directly into PRD 2 (CordovaOS Model Rebuild). All components published here become the governance catalog for the 10 CordovaOS domains.*
