"""
One cross-domain question, answered from the triple store.

National ID (CID) is one published component. Eight of the ten 4.4.0 models
compose it (civil registry, vital statistics, healthcare, education,
employment, tax, property, law enforcement), and because they compose the same
component rather than eight local conventions, the join needs no mapping table
and no integration project. That is the whole argument, and it is measurable
rather than asserted. The same holds for the Business Registry Number, which
the business registry, employment, tax and maritime models share.

Every query names the component it reads: a triple term with the component
unbound (rdf:reifies <<?mc ?p ?v>>) makes the store scan every reifier, and a
label alone does not bind it. The reifier's own IRI carries the component as
well (.../dm/v_<component ct_id>_<instance id>).
"""
import time
from typing import Any, Dict, List

from sdc4_shared.utils.graphdb_client import GraphDBClient

PREFIXES = """PREFIX sdc4: <https://semanticdatacharter.com/ns/sdc4/>
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
"""

# Every record the state holds for a person, grouped by the person.
BREADTH = PREFIXES + """
SELECT ?cid (COUNT(DISTINCT ?dm) AS ?domains) (COUNT(DISTINCT ?i) AS ?records)
WHERE {
  GRAPH ?g {
    ?f rdfs:label "National ID (CID)" ;
       sdc4:inInstance  ?i ;
       sdc4:inDataModel ?dm ;
       rdf:reifies <<sdc4:mc-nj7s1gk45tfgyooxpz0qaha3 ?vp ?cid>> .
  }
}
GROUP BY ?cid
ORDER BY DESC(?domains) DESC(?records)
LIMIT %d
"""

# How many people are known to one domain, two, three, four.
SPREAD = PREFIXES + """
SELECT ?domains (COUNT(*) AS ?people) WHERE {
  { SELECT ?cid (COUNT(DISTINCT ?dm) AS ?domains) WHERE {
      GRAPH ?g {
        ?f rdfs:label "National ID (CID)" ;
           sdc4:inInstance ?i ; sdc4:inDataModel ?dm ;
           rdf:reifies <<sdc4:mc-nj7s1gk45tfgyooxpz0qaha3 ?vp ?cid>> .
      }
    } GROUP BY ?cid }
} GROUP BY ?domains ORDER BY ?domains
"""

TOTALS = PREFIXES + """
SELECT (COUNT(DISTINCT ?cid) AS ?people) (COUNT(DISTINCT ?i) AS ?records)
       (COUNT(DISTINCT ?dm) AS ?domains)
WHERE {
  GRAPH ?g {
    ?f rdfs:label "National ID (CID)" ;
       sdc4:inInstance ?i ; sdc4:inDataModel ?dm ;
       rdf:reifies <<sdc4:mc-nj7s1gk45tfgyooxpz0qaha3 ?vp ?cid>> .
  }
}
"""

# One record per person, so a row can open in the explorer.
SAMPLES = PREFIXES + """
SELECT ?cid ?dm (SAMPLE(?i) AS ?inst) WHERE {
  GRAPH ?g {
    ?f rdfs:label "National ID (CID)" ;
       sdc4:inInstance ?i ; sdc4:inDataModel ?dm ;
       rdf:reifies <<sdc4:mc-nj7s1gk45tfgyooxpz0qaha3 ?vp ?cid>> .
    FILTER(?cid IN (%s))
  }
} GROUP BY ?cid ?dm
"""


# Which businesses employ people exposed in the contagion city, and what the state holds on
# those businesses. Exposure: a healthcare encounter at a Porto Sereno facility. The chain is
# three components: the CID joins the patient to their employment record, the Business Registry
# Number joins the employment record to the registered business and to its tax filings.
HC = 'dcsd8bxr8a6lzcptwwyms44t'
EMP = 'v1v3f0pe0y9hhcplq271zh5i'
BUS = 'nb7gtyimcusmritzx0o0x40o'
TAX = 'apc16uwrj02wgitw7ji1utng'
TRADE = PREFIXES + """
SELECT ?brn ?org (COUNT(DISTINCT ?cid) AS ?exposed) (COUNT(DISTINCT ?tax) AS ?filings) (SAMPLE(?biz) AS ?inst)
WHERE {
  GRAPH ?g1 {
    ?h rdfs:label "National ID (CID)" ; sdc4:inInstance ?hc ; sdc4:inDataModel sdc4:dm-%(hc)s ;
       rdf:reifies <<sdc4:mc-nj7s1gk45tfgyooxpz0qaha3 ?p1 ?cid>> .
    ?f rdfs:label "Managing Organization Reference" ; sdc4:inInstance ?hc ; rdf:reifies <<sdc4:mc-k1ahxtkgbqehv11vx9aw2fzz ?p2 ?fac>> .
    FILTER(CONTAINS(STR(?fac), "porto-sereno"))
  }
  GRAPH ?g2 {
    ?e rdfs:label "National ID (CID)" ; sdc4:inInstance ?emp ; sdc4:inDataModel sdc4:dm-%(emp)s ;
       rdf:reifies <<sdc4:mc-nj7s1gk45tfgyooxpz0qaha3 ?p3 ?cid>> .
    ?b rdfs:label "Business Registry Number" ; sdc4:inInstance ?emp ; rdf:reifies <<sdc4:mc-l8f0m7op4xhrxqy1jrnvbuly ?p4 ?brn>> .
  }
  GRAPH ?g3 {
    ?o rdfs:label "Business Registry Number" ; sdc4:inInstance ?biz ; sdc4:inDataModel sdc4:dm-%(bus)s ;
       rdf:reifies <<sdc4:mc-l8f0m7op4xhrxqy1jrnvbuly ?p5 ?brn>> .
    ?n rdfs:label "Organization Name" ; sdc4:inInstance ?biz ; rdf:reifies <<sdc4:mc-xcn8r67fg7soty17homzok44 ?p6 ?org>> .
  }
  OPTIONAL {
    GRAPH ?g4 {
      ?t rdfs:label "Business Registry Number" ; sdc4:inInstance ?tax ; sdc4:inDataModel sdc4:dm-%(tax)s ;
         rdf:reifies <<sdc4:mc-l8f0m7op4xhrxqy1jrnvbuly ?p7 ?brn>> .
    }
  }
}
GROUP BY ?brn ?org
ORDER BY DESC(?exposed) ?org
LIMIT %(limit)d
""" % {'hc': HC, 'emp': EMP, 'bus': BUS, 'tax': TAX, 'limit': 12}


def trade_at_risk() -> dict:
    """Which businesses employ exposed people, and what the state already holds on them."""
    client = GraphDBClient()
    started = time.monotonic()
    try:
        rows = _rows(client, TRADE)
    except Exception:
        return {'unavailable': 'The triple store did not answer.'}
    elapsed = time.monotonic() - started
    out = []
    for r in rows:
        inst = _v(r, 'inst')
        out.append({
            'brn': _v(r, 'brn'), 'org': _v(r, 'org'),
            'exposed': int(_v(r, 'exposed', '0')), 'filings': int(_v(r, 'filings', '0')),
            'open': {'ct_id': BUS, 'instance_id': inst.rsplit('/', 1)[-1]} if inst else None,
        })
    return {'rows': out, 'businesses': len(out), 'exposed': sum(r['exposed'] for r in out),
            'filings': sum(r['filings'] for r in out), 'elapsed': f'{elapsed:.2f}', 'query': TRADE}


def _rows(client, query):
    result = client.query_sparql(query)
    return (result or {}).get('results', {}).get('bindings', [])


def _v(binding, key, default=''):
    return binding.get(key, {}).get('value', default)


def coverage(limit: int = 12) -> Dict[str, Any]:
    """Answer the question, or explain plainly why it cannot be answered."""
    client = GraphDBClient()
    started = time.monotonic()
    try:
        totals = _rows(client, TOTALS)
        breadth = _rows(client, BREADTH % limit)
        spread = _rows(client, SPREAD)
    except Exception:
        return {'unavailable': 'The triple store did not answer.'}
    if not totals or not breadth:
        return {'unavailable': 'No records carrying a National ID were found.'}

    cids = [_v(b, 'cid') for b in breadth]
    literals = ', '.join('"%s"' % c.replace('"', '') for c in cids)
    samples = _rows(client, SAMPLES % literals) if literals else []
    elapsed = time.monotonic() - started

    # First record found for each person, used only to open the explorer.
    first: Dict[str, Dict[str, str]] = {}
    for s in samples:
        cid = _v(s, 'cid')
        if cid not in first:
            first[cid] = {
                'ct_id': _v(s, 'dm').rsplit('/', 1)[-1].replace('dm-', ''),
                'instance_id': _v(s, 'inst').rsplit('/', 1)[-1],
            }

    people: List[Dict[str, Any]] = []
    for b in breadth:
        cid = _v(b, 'cid')
        people.append({
            'cid': cid,
            'domains': int(_v(b, 'domains', '0')),
            'records': int(_v(b, 'records', '0')),
            'open': first.get(cid),
        })

    t = totals[0]
    return {
        'people': int(_v(t, 'people', '0')),
        'records': int(_v(t, 'records', '0')),
        'domains': int(_v(t, 'domains', '0')),
        'spread': [
            {'domains': int(_v(s, 'domains', '0')), 'people': int(_v(s, 'people', '0'))}
            for s in spread
        ],
        'rows': people,
        'elapsed': f'{elapsed:.2f}',
        'query': BREADTH % limit,
    }
