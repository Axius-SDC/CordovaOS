"""
Demo views for C-Suite presentation.

Read-only presentation layer over existing CordovaOS data and GraphDB.
"""
import hashlib
import json
import time
import logging

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from sdc4_shared.utils.dm_registry import get_dm_registry
from sdc4_shared.utils.graphdb_client import GraphDBClient

from .narrative import BEATS
from .sparql_loader import load_query, load_all_queries, QUERY_CATALOG, SPARQL_DIR

logger = logging.getLogger(__name__)


def dashboard(request):
    """Domain cards with instance counts and GraphDB stats."""
    registry = get_dm_registry()

    # Build domain card data
    domains = []
    total_instances = 0
    for dm_ct_id, model_class in sorted(registry.items(), key=lambda x: getattr(x[1], 'DM_LABEL', '')):
        count = model_class.objects.count()
        total_instances += count
        domains.append({
            'label': getattr(model_class, 'DM_LABEL', model_class.__name__),
            'app_label': model_class._meta.app_label,
            'count': count,
        })

    # GraphDB health and triple count (cached for 1 hour)
    client = GraphDBClient()
    graphdb_healthy = client.health_check()
    triple_count = cache.get('dashboard_triple_count', 0)
    if triple_count == 0 and graphdb_healthy:
        result = client.query_sparql('SELECT (COUNT(*) AS ?cnt) WHERE { ?s ?p ?o }')
        if result and 'results' in result:
            bindings = result['results'].get('bindings', [])
            if bindings:
                triple_count = int(bindings[0]['cnt']['value'])
                cache.set('dashboard_triple_count', triple_count, 30)

    context = {
        'domains': domains,
        'total_instances': total_instances,
        'triple_count': triple_count,
        'graphdb_healthy': graphdb_healthy,
        'query_count': len(QUERY_CATALOG),
    }
    return render(request, 'demo/dashboard.html', context)


def narrative(request):
    """7-beat Contagion walkthrough."""
    return render(request, 'demo/narrative.html', {'beats': BEATS})


def explorer(request):
    """SPARQL query editor with pre-loaded queries."""
    queries = load_all_queries()
    # Serialize for JS consumption via json_script
    queries_json = {str(k): v['sparql'] for k, v in queries.items()}
    context = {
        'queries': queries,
        'queries_json': queries_json,
    }
    return render(request, 'demo/explorer.html', context)


@require_POST
def run_query(request):
    """HTMX endpoint: execute a SPARQL query and return results partial."""
    query_number = request.POST.get('query_number')
    raw_sparql = request.POST.get('sparql', '').strip()
    source = request.POST.get('source', 'explorer')

    # Determine SPARQL text
    if query_number:
        sparql = load_query(int(query_number))
        if not sparql:
            entry = QUERY_CATALOG.get(int(query_number))
            if entry:
                expected = SPARQL_DIR / entry['file']
                detail = f'File: {expected} (dir exists: {SPARQL_DIR.exists()}, file exists: {expected.exists()})'
            else:
                detail = f'No catalog entry for query {query_number}'
            logger.error('SPARQL load failed: %s', detail)
            return HttpResponse(
                f'<div class="alert alert-danger">Query file not found. {detail}</div>'
            )
    elif raw_sparql:
        sparql = raw_sparql
    else:
        return HttpResponse(
            '<div class="alert alert-warning">No query provided.</div>'
        )

    # Check cache first
    cache_key = f"sparql:{hashlib.sha256(sparql.encode()).hexdigest()[:16]}"
    cached = cache.get(cache_key)

    if cached:
        variables = cached['variables']
        rows = cached['rows']
        context = {
            'variables': variables,
            'rows': rows,
            'row_count': len(rows),
            'elapsed': '0.000',
        }
    else:
        # Execute against GraphDB
        client = GraphDBClient()
        start = time.monotonic()
        result = client.query_sparql(sparql)
        elapsed = time.monotonic() - start

        if result is None:
            return HttpResponse(
                '<div class="alert alert-danger">'
                'Query execution failed. Check GraphDB connection and query syntax.'
                '</div>'
            )

        # Parse SPARQL JSON results
        variables = result.get('head', {}).get('vars', [])
        bindings = result.get('results', {}).get('bindings', [])
        rows = []
        for binding in bindings:
            row = [binding.get(v, {}).get('value', '') for v in variables]
            rows.append(row)

        # Cache the parsed result
        cache.set(cache_key, {'variables': variables, 'rows': rows})

        context = {
            'variables': variables,
            'rows': rows,
            'row_count': len(rows),
            'elapsed': f'{elapsed:.3f}',
        }

    template = 'demo/_beat_results.html' if source == 'narrative' else 'demo/_query_results.html'
    return render(request, template, context)
