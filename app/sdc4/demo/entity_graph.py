"""
The entity graph behind a query result: records as nodes, shared identifiers as edges.

Nothing here is stored in the triple store. A record in GraphDB is a hub of
field reifiers, and no triple links one record to another. What links them is
a value two records share in an identifier component, and that is exactly the
claim CordovaOS makes: the join is the component, not a mapping table. So this
module asks the store, for the records a query returned, which identifier
values two or more of them share, and draws each shared value as its own node
with an edge to every record that carries it, labelled by the component it sits
in. The join is on screen as a thing, not implied by a line.

Rules that hold here, from docs/design/README.md:
- every node resolves to a validated instance, addressed by the console;
- every edge is derived from a real shared value, named on the edge;
- nothing is invented to make the picture fuller.
"""
from __future__ import annotations

import re
from typing import Any, Dict, Iterable, List, Optional
from urllib.parse import quote

from django.conf import settings

SDC4 = 'https://semanticdatacharter.com/ns/sdc4/'

#: Variables in a saved query that carry a record IRI rather than a cell.
RECORD_VAR = re.compile(r'inst(_\d+)?')

#: Identifier components whose equal values mean "the same thing", by key.
#: Values are component ct_ids (the mc- part). Two records join when they hold
#: the same value in components of the same key. The person key is one reused
#: component; the business key is three components carrying the same registry
#: number under different labels, which is the reuse the models did not make.
JOIN_KEYS: Dict[str, Dict[str, str]] = {
    'person': {
        'nj7s1gk45tfgyooxpz0qaha3': 'National ID (CID)',
    },
    'business': {
        'ule5u2z3rjpa9pooaifwj1n3': 'organization_identifier',
        'l8f0m7op4xhrxqy1jrnvbuly': 'Business Registry Number',
        'hcfz6urx5c2ayvt8npjl0t4l': 'Source Record ID',
    },
    'place': {
        'l338k7nlvnq2am0owa19yxfc': 'Address (Line 1)',
        'atdtdfzruh7tya0iv5cz365l': 'City',
    },
}

#: Party references (a record's provider party) carry the registry number of a
#: business as a URN. Stripping the prefix makes it joinable to the business key.
PARTY_REF_PREFIX = 'urn:cordova:brn:'

#: Which components name a record on screen, per data model. First present wins,
#: several are joined with a space (given name + surname).
TITLE_LABELS: Dict[str, List[List[str]]] = {
    'uika42uwtj3ijdbegzw2kcwq': [['Given Name (Person)', 'Surname (Person)'], ['National ID (CID)']],
    'ulzd6pe8072mwkqf7i313bov': [['Person Full Name'], ['Certificate Number']],
    'ftluo2nybgxmn7mawttoos20': [['Medical Record Number'], ['National ID (CID)']],
    'upq7w1bqbix5v5ss0mu3kq5n': [['Student ID'], ['National ID (CID)']],
    'pm5cks82lnrvyna1xbwpfxic': [['Job Title', 'Department'], ['Job Title']],
    'vaw4g2kusit5z0kox5mog54g': [['Filing ID']],
    'x250838l7oi6l3yavg9twc1i': [['organization_name'], ['organization_identifier']],
    'x44vt69qqri2bl7vwxb8ck7n': [['Parcel Number'], ['Address (Line 1)']],
    'md2451x882z5j89g66zb50rw': [['Vessel Name', 'Port Call ID'], ['Vessel Name']],
    'yh0opq0bnu6y9y56oukg92uf': [['Incident Report Number']],
}

MAX_RECORDS = 150

PREFIXES = """PREFIX sdc4: <https://semanticdatacharter.com/ns/sdc4/>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dc:   <http://purl.org/dc/elements/1.1/>
"""


def _values(var: str, iris: Iterable[str]) -> str:
    return f'VALUES ?{var} {{ ' + ' '.join(f'<{i}>' for i in iris) + ' }'


def _mc_values(var: str, ct_ids: Iterable[str]) -> str:
    return f'VALUES ?{var} {{ ' + ' '.join(f'sdc4:mc-{c}' for c in ct_ids) + ' }'


def _local(iri: str) -> str:
    return iri.rsplit('/', 1)[-1]


def console_url(dm_ct_id: str, instance_id: str) -> str:
    return f'/console/instance/{dm_ct_id}/{instance_id}/'


def workbench_url(iri: str) -> str:
    base = getattr(settings, 'GRAPHDB_WORKBENCH_URL', 'http://localhost:17200').rstrip('/')
    return f'{base}/graphs-visualizations?uri={quote(iri, safe="")}'


def record_iris_from_bindings(variables: List[str], bindings: List[dict]) -> List[str]:
    """Distinct record IRIs in result order, from every record-carrying variable."""
    seen: Dict[str, None] = {}
    record_vars = [v for v in variables if RECORD_VAR.fullmatch(v)]
    for b in bindings:
        for v in record_vars:
            cell = b.get(v)
            if cell and cell.get('type') == 'uri':
                seen.setdefault(cell['value'], None)
    return list(seen)


def _rows(result: Optional[dict]) -> List[dict]:
    if not result:
        return []
    return [{k: v.get('value', '') for k, v in b.items()} for b in result.get('results', {}).get('bindings', [])]


def build(record_iris: List[str], client) -> Dict[str, Any]:
    """
    Nodes and edges for these records, or an empty graph with a reason.

    Never raises: a triple store that is down leaves the table standing and the
    graph saying why it is empty.
    """
    iris = list(record_iris)
    truncated = len(iris) > MAX_RECORDS
    iris = iris[:MAX_RECORDS]
    if not iris:
        return {'nodes': [], 'edges': [], 'legend': [], 'truncated': False, 'reason': 'This query returns no records to draw.'}

    try:
        node_rows = _rows(client.query_sparql(PREFIXES + f"""
SELECT ?inst ?dm ?status ?title WHERE {{
  {_values('inst', iris)}
  ?inst a ?dm . FILTER(STRSTARTS(STR(?dm), "{SDC4}dm-"))
  OPTIONAL {{ ?inst sdc4:validationStatus ?status }}
  OPTIONAL {{ ?dm dc:title ?title FILTER(CONTAINS(?title, " ")) }}
}}"""))
        wanted = sorted({lbl for groups in TITLE_LABELS.values() for g in groups for lbl in g})
        title_rows = _rows(client.query_sparql(PREFIXES + f"""
SELECT ?inst ?label ?v WHERE {{
  {_values('inst', iris)}
  VALUES ?label {{ {' '.join(chr(34) + w + chr(34) for w in wanted)} }}
  ?r sdc4:inInstance ?inst ; rdfs:label ?label ; rdf:reifies <<?mc ?vp ?v>> .
}}"""))
        all_mcs = [ct for comps in JOIN_KEYS.values() for ct in comps]
        value_rows = _rows(client.query_sparql(PREFIXES + f"""
SELECT ?a ?la ?mc ?v WHERE {{
  {_values('a', iris)}
  {_mc_values('mc', all_mcs)}
  ?ra sdc4:inInstance ?a ; rdfs:label ?la ; rdf:reifies <<?mc ?vp ?v>> .
}}"""))
        party_rows = _rows(client.query_sparql(PREFIXES + f"""
SELECT ?a ?name ?rel ?id WHERE {{
  {_values('a', iris)}
  ?p sdc4:inInstance ?a ; sdc4:partyRef ?ref ; sdc4:partyName ?name ; sdc4:partyRelation ?rel .
  FILTER(STRSTARTS(STR(?ref), "{PARTY_REF_PREFIX}"))
  BIND(REPLACE(STR(?ref), "^{PARTY_REF_PREFIX}", "") AS ?id)
}}"""))
    except Exception:
        return {'nodes': [], 'edges': [], 'legend': [], 'truncated': truncated,
                'reason': 'The triple store did not answer, so there is nothing to draw. The table above stands on its own.'}

    titles: Dict[str, Dict[str, str]] = {}
    for r in title_rows:
        titles.setdefault(r['inst'], {})[r['label']] = r['v']

    nodes: Dict[str, dict] = {}
    for r in node_rows:
        iri = r['inst']
        if iri in nodes:
            continue
        dm_ct = _local(r['dm']).replace('dm-', '', 1)
        have = titles.get(iri, {})
        title = ''
        for group in TITLE_LABELS.get(dm_ct, []):
            parts = [have[l] for l in group if have.get(l)]
            if parts:
                title = ' '.join(parts)
                break
        instance_id = _local(iri)
        nodes[iri] = {
            'id': iri, 'type': 'record', 'iri': iri, 'instance_id': instance_id, 'dm_ct_id': dm_ct,
            'domain': r.get('title') or dm_ct, 'status': r.get('status') or 'unknown',
            'title': title or instance_id,
            'console_url': console_url(dm_ct, instance_id), 'workbench_url': workbench_url(iri),
        }
    for iri in iris:  # records the store did not describe still get a node, so the count is honest
        if iri not in nodes:
            nodes[iri] = {'id': iri, 'type': 'record', 'iri': iri, 'instance_id': _local(iri), 'dm_ct_id': '',
                          'domain': 'unknown', 'status': 'unknown', 'title': _local(iri), 'console_url': '',
                          'workbench_url': workbench_url(iri)}

    def key_of(ct_id: str) -> str:
        for key, comps in JOIN_KEYS.items():
            if ct_id in comps:
                return key
        return 'value'

    # One identifier node per (kind, value); an edge from every record that carries it.
    # A value only one record carries is not a join and is not drawn.
    holders: Dict[str, Dict[str, Any]] = {}
    for r in value_rows:
        if r['a'] not in nodes:
            continue
        kind = key_of(_local(r['mc']).replace('mc-', '', 1))
        vid = f"id:{kind}:{r['v']}"
        h = holders.setdefault(vid, {'kind': kind, 'value': r['v'], 'edges': {}, 'components': set()})
        h['edges'][r['a']] = r['la']
        h['components'].add(r['la'])
    for r in party_rows:
        if r['a'] not in nodes:
            continue
        vid = f"id:business:{r['id']}"
        h = holders.setdefault(vid, {'kind': 'business', 'value': r['id'], 'edges': {}, 'components': set()})
        via = f"party reference ({r['rel']}: {r['name']})"
        h['edges'][r['a']] = via
        h['components'].add(via)
        h['name'] = r['name']

    edges: List[dict] = []
    for vid, h in holders.items():
        if len(h['edges']) < 2:
            continue
        nodes[vid] = {'id': vid, 'type': 'identifier', 'kind': h['kind'], 'title': h['value'],
                      'name': h.get('name', ''), 'components': sorted(h['components']),
                      'degree': len(h['edges'])}
        for rec, via in h['edges'].items():
            edges.append({'id': f"{rec}|{vid}", 'source': rec, 'target': vid, 'label': via, 'kind': h['kind']})

    legend = sorted({n['domain'] for n in nodes.values() if n['type'] == 'record'})
    return {'nodes': list(nodes.values()), 'edges': edges, 'legend': legend, 'truncated': truncated, 'reason': ''}
