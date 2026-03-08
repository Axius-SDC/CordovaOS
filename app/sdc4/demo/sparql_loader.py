"""
Load SPARQL .rq files from the /sparql/ directory.
"""
from pathlib import Path
from django.conf import settings

# Docker mount at /sparql (see docker-compose.yml), fallback to host path
_docker_path = Path('/sparql')
_host_path = settings.BASE_DIR.parent.parent / 'sparql'
SPARQL_DIR = _docker_path if _docker_path.exists() else _host_path

QUERY_CATALOG = {
    1: {
        'file': '01_complete_government_profile.rq',
        'title': 'Complete Government Profile',
        'description': 'All government touchpoints for a single person across all 10 domains.',
        'domains': ['All 10 domains'],
    },
    2: {
        'file': '02_economic_network_analysis.rq',
        'title': 'Economic Network Analysis',
        'description': 'Trace the economic network around a business: employees, tax filings, port shipments.',
        'domains': ['Employment', 'Business', 'Tax', 'Maritime', 'Property'],
    },
    3: {
        'file': '03_social_services_identification.rq',
        'title': 'Social Services Identification',
        'description': 'Find people with healthcare records in a specific city, cross-referencing Civil Registry.',
        'domains': ['Healthcare', 'Civil Registry', 'Employment', 'Property'],
    },
    4: {
        'file': '04_supply_chain_provenance.rq',
        'title': 'Supply Chain Provenance',
        'description': 'Trace cargo from vessel arrival through business operator to business registry.',
        'domains': ['Maritime', 'Business', 'Tax'],
    },
    5: {
        'file': '05_family_economic_unit.rq',
        'title': 'Family Economic Unit',
        'description': 'All records for a person across domains that carry the National ID component.',
        'domains': ['Civil Registry', 'Employment', 'Property', 'Tax', 'Education'],
    },
    6: {
        'file': '06_institutional_impact.rq',
        'title': 'Institutional Impact',
        'description': 'University alumni economic footprint via Business Registry and Education records.',
        'domains': ['Education', 'Employment', 'Business', 'Tax'],
    },
    7: {
        'file': '07_contagion_contact_tracing.rq',
        'title': 'Contagion Contact Tracing',
        'description': '4-tier exposure network starting from patient zero through maritime, civil, and education domains.',
        'domains': ['Healthcare', 'Maritime', 'Law Enforcement', 'Education'],
    },
}


def load_query(num):
    """Read a single .rq file and return its text."""
    entry = QUERY_CATALOG.get(num)
    if not entry:
        return None
    path = SPARQL_DIR / entry['file']
    if not path.exists():
        return None
    return path.read_text()


def load_all_queries():
    """Return all queries with metadata and SPARQL text."""
    result = {}
    for num, meta in QUERY_CATALOG.items():
        sparql = load_query(num)
        result[num] = {**meta, 'sparql': sparql or ''}
    return result
