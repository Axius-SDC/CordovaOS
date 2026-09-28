# Employment Record 4.4.2

**Model ID**: `dm-v1v3f0pe0y9hhcplq271zh5i`
**Project**: Cordova
**Description**: Track employment relationships between persons and businesses in Cordova.

### Dublin Core Metadata
- **Subject**: Employment Registry
- **Language**: en-US
- **Rights**: CC-BY http://creativecommons.org/licenses/by/3.0/
- **Coverage**: Universal
- **Publisher**: Axius SDC, Inc.

## Package Contents

- `dm-v1v3f0pe0y9hhcplq271zh5i.xsd` -- XML Schema Definition (data model structure)
- `dm-v1v3f0pe0y9hhcplq271zh5i.xml` -- XML instance example with sample data
- `dm-v1v3f0pe0y9hhcplq271zh5i-instance.json` -- JSON instance example (same structure as XML)
- `dm-v1v3f0pe0y9hhcplq271zh5i.jsonld` -- JSON-LD semantic schema description
- `dm-v1v3f0pe0y9hhcplq271zh5i.html` -- Human-readable model documentation
- `dm-v1v3f0pe0y9hhcplq271zh5i_shacl.ttl` -- SHACL shapes for RDF validation
- `dm-v1v3f0pe0y9hhcplq271zh5i.ttl` -- RDF triples extracted from XSD (Turtle format)
- `dm-v1v3f0pe0y9hhcplq271zh5i.rdf` -- RDF triples extracted from XSD (RDF/XML format)
- `dm-v1v3f0pe0y9hhcplq271zh5i.gql` -- GQL CREATE statements for property graph databases
- `SHACL_README.md` -- SHACL usage guide
- `README-AI-PROMPT.md` -- This file

## XML Template Placeholders

The XML instance file (`dm-v1v3f0pe0y9hhcplq271zh5i.xml`) is a **maximal template** containing every
element defined in the schema. Placeholder markers indicate where data should go:

- **`_PH_`** -- Required placeholder. This element MUST be replaced with valid data
  matching the schema constraints.
- **`_OPT_PH_`** -- Optional placeholder. This element CAN be replaced with data,
  or the entire enclosing element can be removed from the instance.
- **Fixed values** (labels, language, encoding) are pre-filled from the schema and
  should be kept as-is.

When using this template with an AI assistant, instruct it to:
1. Replace all `_PH_` markers with appropriate data
2. Replace `_OPT_PH_` markers with data or remove the element
3. Keep all fixed values unchanged

## Component Inventory

| Label | Type | CT ID | Constraints |
|-------|------|-------|-------------|
| **Employment Governed Record** | Cluster | `iduhbx4r8bqw6n327tjivuxq` | 1 components; 4 sub-cluster(s) |
|   Digital Signature Proof | XdFile | `gug5dhtqfv7exbgmm2raxpkq` | -- |
|   **Audit Event** | Cluster | `t2tvd3wylxrstdeu5aw6gkw1` | 13 components |
|     Audit Agent Reference | XdString | `dkc2ccj5te35z9gd4bu1blcq` | maxLen=2000; pattern=`\S+` |
|     Audit Entity Reference | XdString | `gcjyjrnp0wsfoelcp4m05c67` | maxLen=2000; pattern=`\S+` |
|     Audit Event Identifier | XdString | `fjhgr5fyqxt2crmg2cb5c513` | maxLen=255 |
|     Data Subject Reference | XdString | `sndpbhm3xbd6qtbyxmvh3i0e` | maxLen=2000; pattern=`\S+` |
|     On Behalf Of Reference | XdString | `nf1air1zbj8v9w66jozdxmyl` | maxLen=2000; pattern=`\S+` |
|     System Identifier | XdString | `h3kdbvdtyalpvik97saaf0an` | maxLen=255 |
|     System Location Name | XdString | `ujir739mf1g8ajeczs9nzh9m` | maxLen=255 |
|     Audit Event Action | XdToken | `ce1c8sydkov8bkv4dgdmwe5x` | 5 enum(s) |
|     Audit Event Outcome | XdToken | `rpz1czz06jhpahmfz30rblvp` | 4 enum(s) |
|     Confidentiality | XdToken | `vbctgmdcwps5b3r3l6sboa6y` | 6 enum(s) |
|     Provenance Agent Type | XdToken | `jujsdur1igws8orw6tvvlqco` | 13 enum(s) |
|     Purpose of Use | XdToken | `d1evlz8yvdlwt6ia9fjq4pgj` | 11 enum(s) |
|     Audit Recorded At | XdTemporal | `uwiosm2q9ym3ewr4de910s70` | -- |
|   **Employment Record** | Cluster | `rlat8z49fywab5du4maxu4qb` | 4 components; 2 sub-cluster(s) |
|     Business Registry Number | XdString | `l8f0m7op4xhrxqy1jrnvbuly` | exactLen=10; pattern=`BIZ-[0-9]{6}` |
|     National ID (CID) | XdString | `nj7s1gk45tfgyooxpz0qaha3` | exactLen=16; pattern=`COR-(AL|BR|CE)0[1-3]-[0-9]{6}` |
|     City | XdToken | `atdtdfzruh7tya0iv5cz365l` | 9 enum(s) |
|     Province | XdToken | `kv5qqs3o4jwcwz9javgw1pzh` | 3 enum(s) |
|     **Compensation** | Cluster | `i8cqh4dpndwl5l0zz65a7raw` | 2 components |
|       Pay Frequency | XdToken | `ub0fwihnwu5x1pdv68pjwbeu` | 3 enum(s) |
|       Salary Amount | XdQuantity | `aw74ticc3fnjkz4vk4b03jr6` | min=0.00000; units=Cordova Córdoba (COR) |
|     **Employment Association** | Cluster | `bqp3evewda43y5vpp63doh6h` | 17 components; 1 sub-cluster(s) |
|       Employee Full Time Indicator | XdBoolean | `m9j6mlcgmbmijzdnbvup1ipc` | -- |
|       Employee Pay Hourly Indicator | XdBoolean | `sorxqbcl704sxkzfooytxf3b` | -- |
|       Employee Supervisor Indicator | XdBoolean | `gco9v72etkdffpi0mgnm17kp` | -- |
|       Employee Contact Information Reference | XdString | `urzessbeem2kj4z3ld0x6jb1` | maxLen=2000; pattern=`\S+` |
|       Employee Identification | XdString | `wos7ancvqpdggx6xdtnsjdtu` | maxLen=64 |
|       Employee Occupation | XdString | `ns8dekdo3100r8zgj3r5773s` | maxLen=4000 |
|       Employee Rank | XdString | `exwd705vvkcsavizr7yw73r3` | maxLen=4000 |
|       Employee Reference | XdString | `gnv4qotitjshdtauz4osyqp2` | maxLen=2000; pattern=`\S+` |
|       Employee Shift | XdString | `sqet5e8oriiu8t33x9ayau0q` | maxLen=4000 |
|       Employee Supervisor Reference | XdString | `inh39quee7dorifcfdk4jzlj` | maxLen=2000; pattern=`\S+` |
|       Employer Reference | XdString | `mwgznh9pfu2pbmkfszawmshs` | maxLen=2000; pattern=`\S+` |
|       Employment Location Reference | XdString | `w6o1hh3qtc5kldmmhwey90k8` | maxLen=2000; pattern=`\S+` |
|       Employment Status | XdString | `p40w5sobi97p62lxufv11et7` | maxLen=255 |
|       Employee Hours Daily Quantity | XdQuantity | `g75mrb5jkxkch3bwbhp29ooz` | units=Time Units |
|       Employee Hours Weekly Quantity | XdQuantity | `h8gfo9ef1dqo3quzrqhrb550` | units=Time Units |
|       Employment Pay Rate Amount | XdQuantity | `rwr7jf4764u5n0m336juazg6` | units=Currency |
|       Employment Length Duration | XdTemporal | `pahkyfowm2ey1opnqpfue3nn` | -- |
|       **Employment Position** | Cluster | `ul9z1upfg5gwdildfw3zjfrq` | 10 components |
|         Employment Position Essential Indicator | XdBoolean | `nd1wbb7wol3hisrqbb4qmpx0` | -- |
|         Employment Position Temporary Indicator | XdBoolean | `r5draolqjc1faebb1b2muf1q` | -- |
|         Employment Position Department Name | XdString | `guq9lttvawsetx2hq59htcrq` | maxLen=255 |
|         Employment Position Duty | XdString | `joguuevnkhxphbzg6ex5q6ek` | maxLen=4000 |
|         Employment Position Identification | XdString | `movuf8z9eesyiloglnottkj9` | maxLen=64 |
|         Employment Position Location Reference | XdString | `j9vyb9u2lpnk1pwm2v6w9mvf` | maxLen=2000; pattern=`\S+` |
|         Employment Position Name | XdString | `ewpg4vc080p0wkl864sjug1l` | maxLen=255 |
|         Employment Position Required Education | XdString | `ife3z8wi5zsgy9y6n9p164ey` | maxLen=4000 |
|         Employment Position Required Job Skill | XdString | `egi28a30eh1mkd1beytxukel` | maxLen=4000 |
|         Employment Position Basis Code | XdToken | `h0h1m3tdz405xz6zjaplat2x` | 3 enum(s) |
|   **PROV Activity** | Cluster | `vmikfu0irht9fmq7q02t3oqs` | 15 components |
|     Activity Description | XdString | `hhusuzzig19rs46ngz23k5g7` | maxLen=4000 |
|     Activity Identifier | XdString | `wr06h54xqqw2q9id8i9673jy` | maxLen=255 |
|     Activity Label | XdString | `r6hkunjm2q0hlxiknlc9ljix` | maxLen=255 |
|     Activity Location | XdString | `uzai5uey5p1fnn9ezj9u6vor` | maxLen=255 |
|     Activity Type | XdString | `jjzmhdxvbt97pq81iwqubtxk` | maxLen=255 |
|     Error Message | XdString | `xlgjqdpwdbn2re3mdh5yy2rk` | maxLen=4000 |
|     Had Plan Reference | XdString | `vhezo2cckpe92x4c3j2memeh` | maxLen=2000; pattern=`\S+` |
|     Used Entity Reference | XdString | `t0whhrqtnb54te4mk48i1ooj` | maxLen=2000; pattern=`\S+` |
|     Was Associated With Reference | XdString | `r48alj7hc3797qfjnf2uj71n` | maxLen=2000; pattern=`\S+` |
|     Was Ended By Reference | XdString | `ueb5g1ojzlwwt0mnds5zb6wl` | maxLen=2000; pattern=`\S+` |
|     Was Informed By Reference | XdString | `qh84jdzp1kxt85aq4ilo0svk` | maxLen=2000; pattern=`\S+` |
|     Was Started By Reference | XdString | `ginfqbk7q59ld2r4us8sjnv1` | maxLen=2000; pattern=`\S+` |
|     Activity Status | XdToken | `wl6j4ekcmu4hvt2m12zw4zp8` | 6 enum(s) |
|     Ended At | XdTemporal | `a5scyosu6j84vz350mqyrzl2` | -- |
|     Started At | XdTemporal | `sa4nl1kbpdr842fkucvfjkpq` | -- |
|   **PROV Agent** | Cluster | `c179ilk2ns15cd5rzzdfd6f6` | 9 components |
|     Acted On Behalf Of Reference | XdString | `og08xf6bu928uuz6t3y0e23f` | maxLen=2000; pattern=`\S+` |
|     Agent Description | XdString | `gb78cmuyo72hqs5apymdki7l` | maxLen=4000 |
|     Agent Email | XdString | `qb90a0sp9vvb6c5cbcf236ys` | maxLen=255 |
|     Agent Identifier | XdString | `w2ruemcfy35rw60jl1t9dew2` | maxLen=255 |
|     Agent Name | XdString | `xxe21o9ojzmy9wxxky1tnmog` | maxLen=255 |
|     Agent Organization Name | XdString | `eftvwi5byq6cdtd931qyxzw0` | maxLen=255 |
|     Software Name | XdString | `aa663ivutjf2fs4757t0bbzy` | maxLen=255 |
|     Software Version | XdString | `x0lebwtobgaelj5pev3258sd` | maxLen=60 |
|     PROV Agent Type | XdToken | `i16vqj89it3db7d3c5qjko9p` | 3 enum(s) |

## Structural Hierarchy

```
DM: Employment Record 4.4.2
  [Cluster] Employment Governed Record
    [XdFile] Digital Signature Proof
    [Cluster] Audit Event
      [XdString] Audit Agent Reference
      [XdString] Audit Entity Reference
      [XdString] Audit Event Identifier
      [XdString] Data Subject Reference
      [XdString] On Behalf Of Reference
      [XdString] System Identifier
      [XdString] System Location Name
      [XdToken] Audit Event Action
      [XdToken] Audit Event Outcome
      [XdToken] Confidentiality
      [XdToken] Provenance Agent Type
      [XdToken] Purpose of Use
      [XdTemporal] Audit Recorded At
    [Cluster] Employment Record
      [XdString] Business Registry Number
      [XdString] National ID (CID)
      [XdToken] City
      [XdToken] Province
      [Cluster] Compensation
        [XdToken] Pay Frequency
        [XdQuantity] Salary Amount
      [Cluster] Employment Association
        [XdBoolean] Employee Full Time Indicator
        [XdBoolean] Employee Pay Hourly Indicator
        [XdBoolean] Employee Supervisor Indicator
        [XdString] Employee Contact Information Reference
        [XdString] Employee Identification
        [XdString] Employee Occupation
        [XdString] Employee Rank
        [XdString] Employee Reference
        [XdString] Employee Shift
        [XdString] Employee Supervisor Reference
        [XdString] Employer Reference
        [XdString] Employment Location Reference
        [XdString] Employment Status
        [XdQuantity] Employee Hours Daily Quantity
        [XdQuantity] Employee Hours Weekly Quantity
        [XdQuantity] Employment Pay Rate Amount
        [XdTemporal] Employment Length Duration
        [Cluster] Employment Position
          [XdBoolean] Employment Position Essential Indicator
          [XdBoolean] Employment Position Temporary Indicator
          [XdString] Employment Position Department Name
          [XdString] Employment Position Duty
          [XdString] Employment Position Identification
          [XdString] Employment Position Location Reference
          [XdString] Employment Position Name
          [XdString] Employment Position Required Education
          [XdString] Employment Position Required Job Skill
          [XdToken] Employment Position Basis Code
    [Cluster] PROV Activity
      [XdString] Activity Description
      [XdString] Activity Identifier
      [XdString] Activity Label
      [XdString] Activity Location
      [XdString] Activity Type
      [XdString] Error Message
      [XdString] Had Plan Reference
      [XdString] Used Entity Reference
      [XdString] Was Associated With Reference
      [XdString] Was Ended By Reference
      [XdString] Was Informed By Reference
      [XdString] Was Started By Reference
      [XdToken] Activity Status
      [XdTemporal] Ended At
      [XdTemporal] Started At
    [Cluster] PROV Agent
      [XdString] Acted On Behalf Of Reference
      [XdString] Agent Description
      [XdString] Agent Email
      [XdString] Agent Identifier
      [XdString] Agent Name
      [XdString] Agent Organization Name
      [XdString] Software Name
      [XdString] Software Version
      [XdToken] PROV Agent Type
```

## Semantic Links

| Component | Predicate | Object URI |
|-----------|-----------|------------|
| Employment Governed Record | `dcterms:publisher` | `https://axius-sdc.com` |
| Employment Governed Record | `dcterms:source` | `https://github.com/Axius-SDC/CordovaOS` |
| Employment Governed Record | `dcterms:identifier` | `https://axius-sdc.com/library/cordova/employment-governed-record` |
| Employment Governed Record | `skos:exactMatch` | `http://www.w3.org/ns/prov#Entity` |
| Employment Governed Record | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-yh04hv0wanvyer6p7pjx49fx` |
| Digital Signature Proof | `rdfs:isDefinedBy` | `https://www.w3.org/TR/vc-data-model/#credentials` |
| Digital Signature Proof | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q210824` |
| Digital Signature Proof | `skos:broadMatch` | `http://www.w3.org/ns/prov#Entity` |
| Audit Event | `dcterms:publisher` | `https://axius-sdc.com` |
| Audit Event | `dcterms:source` | `http://hl7.org/fhir/R4/` |
| Audit Event | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/audit-event` |
| Audit Event | `skos:exactMatch` | `http://hl7.org/fhir/StructureDefinition/AuditEvent` |
| Audit Agent Reference | `dcterms:publisher` | `https://axius-sdc.com` |
| Audit Agent Reference | `dcterms:source` | `http://hl7.org/fhir/R4/` |
| Audit Agent Reference | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/audit-agent-reference` |
| Audit Agent Reference | `skos:exactMatch` | `http://hl7.org/fhir/R4/auditevent-definitions.html#AuditEvent.agent.who` |
| Audit Agent Reference | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-bads7w1q6wmhn18u6dxwt28t` |
| Audit Entity Reference | `dcterms:publisher` | `https://axius-sdc.com` |
| Audit Entity Reference | `dcterms:source` | `http://hl7.org/fhir/R4/` |
| Audit Entity Reference | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/audit-entity-reference` |
| Audit Entity Reference | `skos:exactMatch` | `http://hl7.org/fhir/R4/auditevent-definitions.html#AuditEvent.entity.what` |
| Audit Entity Reference | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-sjp1x177mlpq3howdltptm3c` |
| Audit Event Identifier | `dcterms:publisher` | `https://axius-sdc.com` |
| Audit Event Identifier | `dcterms:source` | `http://hl7.org/fhir/R4/` |
| Audit Event Identifier | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/audit-event-identifier` |
| Audit Event Identifier | `skos:exactMatch` | `http://purl.org/dc/terms/identifier` |
| Data Subject Reference | `dcterms:publisher` | `https://axius-sdc.com` |
| Data Subject Reference | `dcterms:source` | `http://hl7.org/fhir/R4/` |
| Data Subject Reference | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/data-subject-reference` |
| Data Subject Reference | `skos:exactMatch` | `http://hl7.org/fhir/R4/auditevent-definitions.html#AuditEvent.patient` |
| Data Subject Reference | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-x2rc9cg84d2famryqzdic0as` |
| On Behalf Of Reference | `dcterms:publisher` | `https://axius-sdc.com` |
| On Behalf Of Reference | `dcterms:source` | `http://hl7.org/fhir/R4/` |
| On Behalf Of Reference | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/on-behalf-of-reference` |
| On Behalf Of Reference | `skos:exactMatch` | `http://hl7.org/fhir/R4/provenance-definitions.html#Provenance.agent.onBehalfOf` |
| On Behalf Of Reference | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-j9gvyx6u9pb7v1dd0m6joxd6` |
| System Identifier | `dcterms:publisher` | `https://axius-sdc.com` |
| System Identifier | `dcterms:source` | `http://hl7.org/fhir/R4/` |
| System Identifier | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/system-identifier` |
| System Identifier | `skos:exactMatch` | `http://hl7.org/fhir/R4/auditevent-definitions.html#AuditEvent.source.observer` |
| System Identifier | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-des67jo3ki9w0zgaz2i2t2cq` |
| System Location Name | `dcterms:publisher` | `https://axius-sdc.com` |
| System Location Name | `dcterms:source` | `http://hl7.org/fhir/R4/` |
| System Location Name | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/system-location-name` |
| System Location Name | `skos:exactMatch` | `http://hl7.org/fhir/R4/auditevent-definitions.html#AuditEvent.agent.location` |
| System Location Name | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-l6fwy1a2l5i43t308pknygp7` |
| Audit Event Action | `dcterms:publisher` | `https://axius-sdc.com` |
| Audit Event Action | `dcterms:source` | `http://hl7.org/fhir/R4/` |
| Audit Event Action | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/audit-event-action` |
| Audit Event Action | `skos:exactMatch` | `http://hl7.org/fhir/audit-event-action` |
| Audit Event Action | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-o8lawuczf9vry55e98cjg12r` |
| Audit Event Outcome | `dcterms:publisher` | `https://axius-sdc.com` |
| Audit Event Outcome | `dcterms:source` | `http://hl7.org/fhir/R4/` |
| Audit Event Outcome | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/audit-event-outcome` |
| Audit Event Outcome | `skos:exactMatch` | `http://hl7.org/fhir/audit-event-outcome` |
| Audit Event Outcome | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-lgmleqp52a6kl268drrtfjk5` |
| Confidentiality | `dcterms:publisher` | `https://axius-sdc.com` |
| Confidentiality | `dcterms:source` | `http://terminology.hl7.org/` |
| Confidentiality | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/confidentiality` |
| Confidentiality | `skos:exactMatch` | `http://terminology.hl7.org/CodeSystem/v3-Confidentiality` |
| Confidentiality | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-hp8q52t8tgmis92c4ljrfy7e` |
| Provenance Agent Type | `dcterms:publisher` | `https://axius-sdc.com` |
| Provenance Agent Type | `dcterms:source` | `http://hl7.org/fhir/R4/` |
| Provenance Agent Type | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/provenance-agent-type` |
| Provenance Agent Type | `skos:exactMatch` | `http://terminology.hl7.org/CodeSystem/provenance-participant-type` |
| Provenance Agent Type | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-syt8l7pmb64eym2chcn43ai7` |
| Purpose of Use | `dcterms:publisher` | `https://axius-sdc.com` |
| Purpose of Use | `dcterms:source` | `http://terminology.hl7.org/` |
| Purpose of Use | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/purpose-of-use` |
| Purpose of Use | `skos:exactMatch` | `http://terminology.hl7.org/CodeSystem/v3-ActReason` |
| Purpose of Use | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-y87ikto4p56zlkx4o2d63ain` |
| Audit Recorded At | `dcterms:publisher` | `https://axius-sdc.com` |
| Audit Recorded At | `dcterms:source` | `http://hl7.org/fhir/R4/` |
| Audit Recorded At | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/audit-recorded-at` |
| Audit Recorded At | `skos:exactMatch` | `http://hl7.org/fhir/R4/auditevent-definitions.html#AuditEvent.recorded` |
| Employment Record | `dcterms:publisher` | `https://axius-sdc.com` |
| Employment Record | `dcterms:source` | `https://github.com/Axius-SDC/CordovaOS` |
| Employment Record | `dcterms:identifier` | `https://axius-sdc.com/library/cordova/employment-record` |
| Employment Record | `skos:exactMatch` | `https://schema.org/EmployeeRole` |
| Employment Record | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-bn5gaw6rtyjb3vr8vi27bvyk` |
| Business Registry Number | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q12047291` |
| Business Registry Number | `rdfs:isDefinedBy` | `http://schema.org/identifier` |
| Business Registry Number | `skos:broadMatch` | `https://schema.org/identifier` |
| National ID (CID) | `rdfs:isDefinedBy` | `http://schema.org/identifier` |
| National ID (CID) | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q1140371` |
| National ID (CID) | `skos:broadMatch` | `https://schema.org/identifier` |
| City | `rdfs:isDefinedBy` | `http://schema.org/City` |
| City | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| City | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Province | `rdfs:isDefinedBy` | `http://schema.org/AdministrativeArea` |
| Province | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Province | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Province | `rdfs:isDefinedBy` | `https://schema.org/State` |
| Compensation | `dcterms:publisher` | `https://axius-sdc.com` |
| Compensation | `dcterms:source` | `https://github.com/Axius-SDC/CordovaOS` |
| Compensation | `dcterms:identifier` | `https://axius-sdc.com/library/cordova/compensation` |
| Compensation | `skos:closeMatch` | `https://schema.org/ItemList` |
| Compensation | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-vzabxfc733qk7lo1knaggxfs` |
| Pay Frequency | `rdfs:isDefinedBy` | `http://release.niem.gov/niem/niem-core/6.0/niem-core.owl#PayPeriodFrequencyCode` |
| Pay Frequency | `skos:exactMatch` | `https://schema.org/DefinedTermSet` |
| Pay Frequency | `rdf:type` | `http://www.w3.org/2004/02/skos/core#ConceptScheme` |
| Salary Amount | `rdfs:isDefinedBy` | `https://schema.org/MonetaryAmount` |
| Salary Amount | `skos:broadMatch` | `http://qudt.org/vocab/quantitykind/Currency` |
| Salary Amount | `rdfs:isDefinedBy` | `https://www.wikidata.org/wiki/Q178848` |
| Employment Association | `dcterms:publisher` | `https://axius-sdc.com` |
| Employment Association | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employment-association` |
| Employment Association | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employment Association | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmploymentAssociationType` |
| Employment Association | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-umsm60kz9jn1196s80jmy1n0` |
| Employee Full Time Indicator | `dcterms:publisher` | `https://axius-sdc.com` |
| Employee Full Time Indicator | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employee-full-time-indicator` |
| Employee Full Time Indicator | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employee Full Time Indicator | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmployeeFullTimeIndicator` |
| Employee Pay Hourly Indicator | `dcterms:publisher` | `https://axius-sdc.com` |
| Employee Pay Hourly Indicator | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employee-pay-hourly-indicator` |
| Employee Pay Hourly Indicator | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employee Pay Hourly Indicator | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmployeePayHourlyIndicator` |
| Employee Supervisor Indicator | `dcterms:publisher` | `https://axius-sdc.com` |
| Employee Supervisor Indicator | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employee-supervisor-indicator` |
| Employee Supervisor Indicator | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employee Supervisor Indicator | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmployeeSupervisorIndicator` |
| Employee Contact Information Reference | `dcterms:publisher` | `https://axius-sdc.com` |
| Employee Contact Information Reference | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employee-contact-information-reference` |
| Employee Contact Information Reference | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employee Contact Information Reference | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmployeeContactInformation` |
| Employee Identification | `dcterms:publisher` | `https://axius-sdc.com` |
| Employee Identification | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employee-identification` |
| Employee Identification | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employee Identification | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmployeeIdentification` |
| Employee Occupation | `dcterms:publisher` | `https://axius-sdc.com` |
| Employee Occupation | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employee-occupation` |
| Employee Occupation | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employee Occupation | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmployeeOccupationText` |
| Employee Rank | `dcterms:publisher` | `https://axius-sdc.com` |
| Employee Rank | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employee-rank` |
| Employee Rank | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employee Rank | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmployeeRankText` |
| Employee Reference | `dcterms:publisher` | `https://axius-sdc.com` |
| Employee Reference | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employee-reference` |
| Employee Reference | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employee Reference | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/Employee` |
| Employee Shift | `dcterms:publisher` | `https://axius-sdc.com` |
| Employee Shift | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employee-shift` |
| Employee Shift | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employee Shift | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmployeeShiftText` |
| Employee Supervisor Reference | `dcterms:publisher` | `https://axius-sdc.com` |
| Employee Supervisor Reference | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employee-supervisor-reference` |
| Employee Supervisor Reference | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employee Supervisor Reference | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmployeeSupervisor` |
| Employer Reference | `dcterms:publisher` | `https://axius-sdc.com` |
| Employer Reference | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employer-reference` |
| Employer Reference | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employer Reference | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/Employer` |
| Employment Location Reference | `dcterms:publisher` | `https://axius-sdc.com` |
| Employment Location Reference | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employment-location-reference` |
| Employment Location Reference | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employment Location Reference | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmploymentLocation` |
| Employment Status | `dcterms:publisher` | `https://axius-sdc.com` |
| Employment Status | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employment-status` |
| Employment Status | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employment Status | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmploymentStatus` |
| Employee Hours Daily Quantity | `dcterms:publisher` | `https://axius-sdc.com` |
| Employee Hours Daily Quantity | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employee-hours-daily-quantity` |
| Employee Hours Daily Quantity | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employee Hours Daily Quantity | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmployeeHoursDailyQuantity` |
| Employee Hours Daily Quantity | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-l3atyf51amrlzxnz81jhor8c` |
| Employee Hours Weekly Quantity | `dcterms:publisher` | `https://axius-sdc.com` |
| Employee Hours Weekly Quantity | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employee-hours-weekly-quantity` |
| Employee Hours Weekly Quantity | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employee Hours Weekly Quantity | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmployeeHoursWeeklyQuantity` |
| Employee Hours Weekly Quantity | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-xc1d8d22kesm73rqo9l8disu` |
| Employment Pay Rate Amount | `dcterms:publisher` | `https://axius-sdc.com` |
| Employment Pay Rate Amount | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employment-pay-rate-amount` |
| Employment Pay Rate Amount | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employment Pay Rate Amount | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmploymentPayRateAmount` |
| Employment Length Duration | `dcterms:publisher` | `https://axius-sdc.com` |
| Employment Length Duration | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employment-length-duration` |
| Employment Length Duration | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employment Length Duration | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmploymentLengthDuration` |
| Employment Position | `dcterms:publisher` | `https://axius-sdc.com` |
| Employment Position | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employment-position` |
| Employment Position | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employment Position | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmploymentPositionType` |
| Employment Position Essential Indicator | `dcterms:publisher` | `https://axius-sdc.com` |
| Employment Position Essential Indicator | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employment-position-essential-indicator` |
| Employment Position Essential Indicator | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employment Position Essential Indicator | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmploymentPositionEssentialIndicator` |
| Employment Position Temporary Indicator | `dcterms:publisher` | `https://axius-sdc.com` |
| Employment Position Temporary Indicator | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employment-position-temporary-indicator` |
| Employment Position Temporary Indicator | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employment Position Temporary Indicator | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmploymentPositionTemporaryIndicator` |
| Employment Position Department Name | `dcterms:publisher` | `https://axius-sdc.com` |
| Employment Position Department Name | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employment-position-department-name` |
| Employment Position Department Name | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employment Position Department Name | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmploymentPositionDepartmentName` |
| Employment Position Duty | `dcterms:publisher` | `https://axius-sdc.com` |
| Employment Position Duty | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employment-position-duty` |
| Employment Position Duty | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employment Position Duty | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmploymentPositionDutyText` |
| Employment Position Identification | `dcterms:publisher` | `https://axius-sdc.com` |
| Employment Position Identification | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employment-position-identification` |
| Employment Position Identification | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employment Position Identification | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmploymentPositionIdentification` |
| Employment Position Location Reference | `dcterms:publisher` | `https://axius-sdc.com` |
| Employment Position Location Reference | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employment-position-location-reference` |
| Employment Position Location Reference | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employment Position Location Reference | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmploymentPositionLocation` |
| Employment Position Name | `dcterms:publisher` | `https://axius-sdc.com` |
| Employment Position Name | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employment-position-name` |
| Employment Position Name | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employment Position Name | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmploymentPositionName` |
| Employment Position Required Education | `dcterms:publisher` | `https://axius-sdc.com` |
| Employment Position Required Education | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employment-position-required-education` |
| Employment Position Required Education | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employment Position Required Education | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmploymentPositionRequiredEducationText` |
| Employment Position Required Job Skill | `dcterms:publisher` | `https://axius-sdc.com` |
| Employment Position Required Job Skill | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employment-position-required-job-skill` |
| Employment Position Required Job Skill | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employment Position Required Job Skill | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmploymentPositionRequiredJobSkillText` |
| Employment Position Basis Code | `dcterms:publisher` | `https://axius-sdc.com` |
| Employment Position Basis Code | `dcterms:identifier` | `https://axius-sdc.com/library/niem/employment-position-basis-code` |
| Employment Position Basis Code | `dcterms:source` | `https://docs.oasis-open.org/niemopen/niem-model/v6.0/ps02/xsd/niem-core.xsd` |
| Employment Position Basis Code | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmploymentPositionBasisCode` |
| Employment Position Basis Code | `skos:exactMatch` | `https://docs.oasis-open.org/niemopen/ns/model/niem-core/6.0/EmploymentPositionBasisCodeSimpleType` |
| PROV Activity | `dcterms:publisher` | `https://axius-sdc.com` |
| PROV Activity | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/prov-activity` |
| PROV Activity | `skos:exactMatch` | `http://www.w3.org/ns/prov#Activity` |
| PROV Activity | `dcterms:source` | `https://www.w3.org/TR/prov-o/` |
| Activity Description | `dcterms:publisher` | `https://axius-sdc.com` |
| Activity Description | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/activity-description` |
| Activity Description | `skos:exactMatch` | `http://purl.org/dc/terms/description` |
| Activity Description | `dcterms:source` | `https://www.w3.org/TR/prov-o/` |
| Activity Description | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-m9xg6e182m1oq77ssrf9iujv` |
| Activity Identifier | `dcterms:publisher` | `https://axius-sdc.com` |
| Activity Identifier | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/activity-identifier` |
| Activity Identifier | `skos:exactMatch` | `http://purl.org/dc/terms/identifier` |
| Activity Identifier | `dcterms:source` | `https://www.w3.org/TR/prov-o/` |
| Activity Identifier | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-fpnn1dew0kcevc8ptohndc5t` |
| Activity Label | `dcterms:publisher` | `https://axius-sdc.com` |
| Activity Label | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/activity-label` |
| Activity Label | `skos:exactMatch` | `http://www.w3.org/2000/01/rdf-schema#label` |
| Activity Label | `dcterms:source` | `https://www.w3.org/TR/prov-o/` |
| Activity Label | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-n4kaez29vbknku2jy8n56gfm` |
| Activity Location | `dcterms:publisher` | `https://axius-sdc.com` |
| Activity Location | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/activity-location` |
| Activity Location | `skos:exactMatch` | `http://www.w3.org/ns/prov#atLocation` |
| Activity Location | `dcterms:source` | `https://www.w3.org/TR/prov-o/` |
| Activity Location | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-ciuklf1kl8bphpudye4i47am` |
| Activity Type | `dcterms:publisher` | `https://axius-sdc.com` |
| Activity Type | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/activity-type` |
| Activity Type | `skos:exactMatch` | `http://www.w3.org/ns/prov#type` |
| Activity Type | `dcterms:source` | `https://www.w3.org/TR/prov-o/` |
| Activity Type | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-ceusvbe55b266gcdzf5qnurc` |
| Error Message | `dcterms:publisher` | `https://axius-sdc.com` |
| Error Message | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/error-message` |
| Error Message | `dcterms:source` | `https://schema.org/` |
| Error Message | `skos:exactMatch` | `https://schema.org/error` |
| Error Message | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-eakhqr9l9nbblppgxc5fq25n` |
| Had Plan Reference | `dcterms:publisher` | `https://axius-sdc.com` |
| Had Plan Reference | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/had-plan-reference` |
| Had Plan Reference | `skos:exactMatch` | `http://www.w3.org/ns/prov#hadPlan` |
| Had Plan Reference | `dcterms:source` | `https://www.w3.org/TR/prov-o/` |
| Had Plan Reference | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-xvdfh1nzfar33yxmgl3jgvqo` |
| Used Entity Reference | `dcterms:publisher` | `https://axius-sdc.com` |
| Used Entity Reference | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/used-entity-reference` |
| Used Entity Reference | `skos:exactMatch` | `http://www.w3.org/ns/prov#used` |
| Used Entity Reference | `dcterms:source` | `https://www.w3.org/TR/prov-o/` |
| Used Entity Reference | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-ixv0fa8xlde52mdeymr4zaka` |
| Was Associated With Reference | `dcterms:publisher` | `https://axius-sdc.com` |
| Was Associated With Reference | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/was-associated-with-reference` |
| Was Associated With Reference | `skos:exactMatch` | `http://www.w3.org/ns/prov#wasAssociatedWith` |
| Was Associated With Reference | `dcterms:source` | `https://www.w3.org/TR/prov-o/` |
| Was Associated With Reference | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-gs0e1hp2rpjl6qfg9v8d047f` |
| Was Ended By Reference | `dcterms:publisher` | `https://axius-sdc.com` |
| Was Ended By Reference | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/was-ended-by-reference` |
| Was Ended By Reference | `skos:exactMatch` | `http://www.w3.org/ns/prov#wasEndedBy` |
| Was Ended By Reference | `dcterms:source` | `https://www.w3.org/TR/prov-o/` |
| Was Ended By Reference | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-jr1e3n5kg31nqz1ynh28kitp` |
| Was Informed By Reference | `dcterms:publisher` | `https://axius-sdc.com` |
| Was Informed By Reference | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/was-informed-by-reference` |
| Was Informed By Reference | `skos:exactMatch` | `http://www.w3.org/ns/prov#wasInformedBy` |
| Was Informed By Reference | `dcterms:source` | `https://www.w3.org/TR/prov-o/` |
| Was Informed By Reference | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-rz60y6aujd274j4i7jpyxvpr` |
| Was Started By Reference | `dcterms:publisher` | `https://axius-sdc.com` |
| Was Started By Reference | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/was-started-by-reference` |
| Was Started By Reference | `skos:exactMatch` | `http://www.w3.org/ns/prov#wasStartedBy` |
| Was Started By Reference | `dcterms:source` | `https://www.w3.org/TR/prov-o/` |
| Was Started By Reference | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-kmodjk1e5xu9z94zgiaxx1hu` |
| Activity Status | `dcterms:publisher` | `https://axius-sdc.com` |
| Activity Status | `dcterms:source` | `https://w3id.org/dpv` |
| Activity Status | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/activity-status` |
| Activity Status | `skos:closeMatch` | `https://w3id.org/dpv#ActivityStatus` |
| Activity Status | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-yehcpzf43j0b5zp9ck59t9eg` |
| Ended At | `dcterms:publisher` | `https://axius-sdc.com` |
| Ended At | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/ended-at-time` |
| Ended At | `skos:exactMatch` | `http://www.w3.org/ns/prov#endedAtTime` |
| Ended At | `dcterms:source` | `https://www.w3.org/TR/prov-o/` |
| Started At | `dcterms:publisher` | `https://axius-sdc.com` |
| Started At | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/started-at-time` |
| Started At | `skos:exactMatch` | `http://www.w3.org/ns/prov#startedAtTime` |
| Started At | `dcterms:source` | `https://www.w3.org/TR/prov-o/` |
| PROV Agent | `dcterms:publisher` | `https://axius-sdc.com` |
| PROV Agent | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/prov-agent` |
| PROV Agent | `skos:exactMatch` | `http://www.w3.org/ns/prov#Agent` |
| PROV Agent | `dcterms:source` | `https://www.w3.org/TR/prov-o/` |
| Acted On Behalf Of Reference | `dcterms:publisher` | `https://axius-sdc.com` |
| Acted On Behalf Of Reference | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/acted-on-behalf-of-reference` |
| Acted On Behalf Of Reference | `skos:exactMatch` | `http://www.w3.org/ns/prov#actedOnBehalfOf` |
| Acted On Behalf Of Reference | `dcterms:source` | `https://www.w3.org/TR/prov-o/` |
| Acted On Behalf Of Reference | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-dce4w62jxjngjnmc5y26fq66` |
| Agent Description | `dcterms:publisher` | `https://axius-sdc.com` |
| Agent Description | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/agent-description` |
| Agent Description | `skos:exactMatch` | `http://purl.org/dc/terms/description` |
| Agent Description | `dcterms:source` | `https://www.w3.org/TR/prov-o/` |
| Agent Description | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-w79xppnskig5vq31er8gh7nk` |
| Agent Email | `dcterms:publisher` | `https://axius-sdc.com` |
| Agent Email | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/agent-email` |
| Agent Email | `skos:exactMatch` | `http://xmlns.com/foaf/0.1/mbox` |
| Agent Email | `dcterms:source` | `https://www.w3.org/TR/prov-o/` |
| Agent Email | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-yp6pm5xyovxhkjimrrb8h9xy` |
| Agent Identifier | `dcterms:publisher` | `https://axius-sdc.com` |
| Agent Identifier | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/agent-identifier` |
| Agent Identifier | `skos:exactMatch` | `http://purl.org/dc/terms/identifier` |
| Agent Identifier | `dcterms:source` | `https://www.w3.org/TR/prov-o/` |
| Agent Identifier | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-hhfnj5hd1yzt252jfq5pdjj1` |
| Agent Name | `dcterms:publisher` | `https://axius-sdc.com` |
| Agent Name | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/agent-name` |
| Agent Name | `skos:exactMatch` | `http://xmlns.com/foaf/0.1/name` |
| Agent Name | `dcterms:source` | `https://www.w3.org/TR/prov-o/` |
| Agent Name | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-yya0pdgjd2w0wlz5r3h516om` |
| Agent Organization Name | `dcterms:publisher` | `https://axius-sdc.com` |
| Agent Organization Name | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/agent-organization-name` |
| Agent Organization Name | `dcterms:source` | `https://schema.org/` |
| Agent Organization Name | `skos:exactMatch` | `https://schema.org/legalName` |
| Agent Organization Name | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-ifw5zfe4oiijbxjn1ylc2wm3` |
| Software Name | `dcterms:publisher` | `https://axius-sdc.com` |
| Software Name | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/software-name` |
| Software Name | `dcterms:source` | `https://schema.org/` |
| Software Name | `skos:exactMatch` | `https://schema.org/SoftwareApplication` |
| Software Name | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-rsjfjz8m5z7a58h5793duqbs` |
| Software Version | `dcterms:publisher` | `https://axius-sdc.com` |
| Software Version | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/software-version` |
| Software Version | `dcterms:source` | `https://schema.org/` |
| Software Version | `skos:exactMatch` | `https://schema.org/softwareVersion` |
| Software Version | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-tep9wanrrtqfw0k76huv6tvd` |
| PROV Agent Type | `dcterms:publisher` | `https://axius-sdc.com` |
| PROV Agent Type | `dcterms:identifier` | `https://axius-sdc.com/library/provgov/prov-agent-type` |
| PROV Agent Type | `skos:exactMatch` | `http://www.w3.org/ns/prov#Agent` |
| PROV Agent Type | `dcterms:source` | `https://www.w3.org/TR/prov-o/` |
| PROV Agent Type | `prov:wasRevisionOf` | `https://semanticdatacharter.com/ns/sdc4/mc-nesxtz8c5o665swc9lhvqkjj` |

## Using This Model with AI Assistants

### Quick Start Prompt

Copy and customize this prompt for your AI assistant:

```
I have an SDC4-compliant data model called "Employment Record 4.4.2" and need help
creating a data entry application.

**Attached Files:**
- XML Schema (dm-v1v3f0pe0y9hhcplq271zh5i.xsd)
- Example instance (dm-v1v3f0pe0y9hhcplq271zh5i.xml)
- HTML documentation (dm-v1v3f0pe0y9hhcplq271zh5i.html)

**What I Need:**
I need a [specify framework: Python Reflex / React / Django / etc.] application that:

1. **Data Import**: Import data from CSV files
2. **Data Storage**: Store in [SQLite / PostgreSQL / MySQL / etc.] database
3. **Data Entry**: Forms for creating/editing records with validation
4. **Data Browser**: View, filter, and search records
5. **Export**: Export data back to CSV or XML

**Database Design:**
Each SDC4 Cluster in the schema should map to a database table with
appropriate relationships.

**My Specific Requirements:**
[Add your specific needs here]

Please analyze the schema and propose an application architecture.
```

### Example Use Cases

**Python Reflex Data Entry App:**
```
Create a Python Reflex application for data entry based on the
"Employment Record 4.4.2" SDC4 schema (dm-v1v3f0pe0y9hhcplq271zh5i.xsd).
Include CSV import, SQLite storage, forms with validation, and a data browser.
Use the sdcvalidator library for full SDC4 XML validation.
```

**React/Next.js Web App:**
```
Build a React/Next.js application with a REST API backend for the
"Employment Record 4.4.2" schema (dm-v1v3f0pe0y9hhcplq271zh5i.xsd).
Frontend: data entry forms and browser using the schema structure.
Backend: Node.js/Express with PostgreSQL for storage.
```

**Django Admin Interface:**
```
Generate Django models from the "Employment Record 4.4.2" SDC4 schema (dm-v1v3f0pe0y9hhcplq271zh5i.xsd)
with a custom admin interface.
Each cluster should be a Django model with appropriate field types.
Include CSV import/export via Django admin actions.
```

**REST API Only:**
```
Create a FastAPI REST API for the "Employment Record 4.4.2" data model (dm-v1v3f0pe0y9hhcplq271zh5i.xsd).
Endpoints for CRUD operations on each cluster.
Include XML validation using sdcvalidator.
Return both JSON and XML responses.
```

## SDC4 Validation (Optional but Recommended)

For full SDC4 compliance with XML validation, use the `sdcvalidator` Python library.

### Installation

```bash
pip install sdcvalidator
```

### Basic Usage

```python
from sdcvalidator import SDC4Validator

# Initialize validator with your SDC4 data model schema
validator = SDC4Validator('dm-v1v3f0pe0y9hhcplq271zh5i.xsd')

# Validate and get a detailed report
report = validator.validate_and_report('data.xml')

if report['valid']:
    print('Valid SDC4 XML instance')
else:
    print('Validation errors:')
    for error in report['errors']:
        print(f"  - {error['xpath']}: {error['reason']}")
```

### ExceptionalValue Recovery

When validation errors occur, sdcvalidator can quarantine invalid data
with ISO 21090 ExceptionalValue elements:

```python
validator = SDC4Validator('dm-v1v3f0pe0y9hhcplq271zh5i.xsd')
recovered_tree = validator.validate_with_recovery('data.xml')
validator.save_recovered_xml('recovered_data.xml', 'data.xml')
```

**Note**: XML validation is completely optional. You can build applications
using only JSON, implement custom validation, or add sdcvalidator later.

## GQL Graph Database Usage

The `dm-v1v3f0pe0y9hhcplq271zh5i.gql` file contains GQL CREATE statements for property
graph databases (e.g., Neo4j, Amazon Neptune, TigerGraph).

### Loading into Neo4j

```cypher
// Load the GQL file content
// Copy the CREATE statements from dm-v1v3f0pe0y9hhcplq271zh5i.gql into the Neo4j browser
```

### Example Queries

```cypher
// Find all components in this data model
MATCH (n:ModelComponent) RETURN n.label, n.sdcType

// Show the structural hierarchy
MATCH (dm:DataModel)-[:HAS_ROOT_CLUSTER]->(c:Cluster)-[:CONTAINS_COMPONENT]->(comp)
RETURN dm.label, c.label, comp.label, comp.sdcType

// Find components with specific constraints
MATCH (n:ModelComponent) WHERE n.minLength IS NOT NULL
RETURN n.label, n.minLength, n.maxLength
```

## Tips for Working with AI Assistants

### 1. Start with Architecture Discussion

Before asking for code, ask the AI to:
- Analyze the schema structure
- Identify complex relationships
- Recommend database design
- Suggest appropriate frameworks

### 2. Iterate in Phases

- **Phase 1**: Basic data models and storage
- **Phase 2**: Data entry forms
- **Phase 3**: Data browser and search
- **Phase 4**: CSV import/export
- **Phase 5**: Advanced features (auth, reporting, etc.)

### 3. Leverage the Documentation

The `dm-v1v3f0pe0y9hhcplq271zh5i.html` file contains human-readable descriptions,
constraint definitions, business rules, and semantic links.
Share this with the AI for better understanding.

### 4. Database Schema Mapping

**Option 1: Normalized Tables (Traditional)**
```
Cluster -> Database Table
Sub-Cluster -> Separate Table with Foreign Key
Component -> Table Column
```

**Option 2: JSON Embedding (Simpler)**
```
Main Cluster -> Table
Sub-Clusters -> JSON Column
Components -> Mixed (simple types as columns, complex as JSON)
```

Ask your AI assistant which approach fits your use case.

## Additional Resources

**SDC4 Specification:**
- [Semantic Data Charter](https://semanticdatacharter.org)

**sdcvalidator Documentation:**
- [PyPI Package](https://pypi.org/project/sdcvalidator/)

**Framework Documentation:**
- [Python Reflex](https://reflex.dev)
- [Django](https://www.djangoproject.com)
- [React](https://react.dev)
- [FastAPI](https://fastapi.tiangolo.com)

---

**Generated by SDCStudio** -- Your SDC4-compliant data modeling platform
