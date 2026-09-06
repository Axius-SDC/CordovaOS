"""
One cross-domain question, answered from the triple store.

The question the mockup asked, which businesses employ exposed people and what
trade is at risk, is not answerable from this dataset: employment records carry
the employer as free text rather than as a business identifier, so the chain
breaks between Employment and Business Registry. Rather than stage it, this asks
the question the data does support, which happens to be the better one anyway.

National ID (CID) is one published component. Four domains use it, and because
they use the same component rather than four local conventions, the join needs
no mapping table and no integration project. That is the whole argument, and it
is measurable rather than asserted.
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
       rdf:reifies <<?mc ?vp ?cid>> .
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
           rdf:reifies <<?mc ?vp ?cid>> .
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
       rdf:reifies <<?mc ?vp ?cid>> .
  }
}
"""

# One record per person, so a row can open in the explorer.
SAMPLES = PREFIXES + """
SELECT ?cid ?dm (SAMPLE(?i) AS ?inst) WHERE {
  GRAPH ?g {
    ?f rdfs:label "National ID (CID)" ;
       sdc4:inInstance ?i ; sdc4:inDataModel ?dm ;
       rdf:reifies <<?mc ?vp ?cid>> .
    FILTER(?cid IN (%s))
  }
} GROUP BY ?cid ?dm
"""


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
