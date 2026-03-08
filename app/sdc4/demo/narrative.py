"""
7-beat narrative content for "The Contagion" crisis walkthrough.
"""

BEATS = [
    {
        'number': 1,
        'title': 'Patient Zero Identified',
        'query_number': 1,
        'icon': 'bi-person-exclamation',
        'color': 'danger',
        'narrative': (
            'Carlos Mendoza (CID COR-AL01-271845) presents at a Porto Sereno clinic '
            'with acute respiratory symptoms. His complete government profile reveals '
            'touchpoints across all 10 domains — employment, education, property, tax, '
            'civil registry, and more. A single query reconstructs his entire civic footprint.'
        ),
        'query_label': 'Pull Government Profile',
    },
    {
        'number': 2,
        'title': 'Economic Network Exposure',
        'query_number': 2,
        'icon': 'bi-building',
        'color': 'warning',
        'narrative': (
            'Carlos works for a business registered as BIZ-001102. Tracing its economic '
            'network reveals employees, tax filings, and port shipments connected to the '
            'same entity. Every person in this network is a potential exposure.'
        ),
        'query_label': 'Map Business Network',
    },
    {
        'number': 3,
        'title': 'Social Services Cross-Reference',
        'query_number': 3,
        'icon': 'bi-hospital',
        'color': 'info',
        'narrative': (
            'Public health officials need to identify everyone in Porto Sereno who has '
            'recent healthcare records. Cross-referencing Civil Registry addresses with '
            'Healthcare facility visits finds people who may have been exposed at the '
            'same clinics Carlos visited.'
        ),
        'query_label': 'Find At-Risk Population',
    },
    {
        'number': 4,
        'title': 'Supply Chain Trace',
        'query_number': 4,
        'icon': 'bi-truck',
        'color': 'primary',
        'narrative': (
            'The MV Estrella del Sur arrived at Porto Sereno days before Carlos\'s '
            'symptoms appeared. Tracing the vessel\'s cargo and operator through the '
            'Business Registry reveals who handled the shipment and whether the '
            'contagion came ashore with the cargo.'
        ),
        'query_label': 'Trace Vessel & Cargo',
    },
    {
        'number': 5,
        'title': 'Family & Household Exposure',
        'query_number': 5,
        'icon': 'bi-people',
        'color': 'success',
        'narrative': (
            'Carlos\'s household must be quarantined. Pulling all records sharing his '
            'National ID across domains shows family members, dependents, and anyone '
            'co-registered at the same address — the immediate exposure ring.'
        ),
        'query_label': 'Map Household Unit',
    },
    {
        'number': 6,
        'title': 'Institutional Impact Assessment',
        'query_number': 6,
        'icon': 'bi-mortarboard',
        'color': 'secondary',
        'narrative': (
            'The university where Carlos studied (BIZ-000847) has thousands of students '
            'and faculty. Pulling Business Registry details and Education records shows '
            'the institutional footprint — anyone connected to the university who may '
            'need testing.'
        ),
        'query_label': 'Assess Institutional Reach',
    },
    {
        'number': 7,
        'title': 'Full Contagion Contact Trace',
        'query_number': 7,
        'icon': 'bi-diagram-3',
        'color': 'danger',
        'narrative': (
            'The complete 4-tier contact trace. Tier 1: Patient Zero\'s healthcare record. '
            'Tier 2: Maritime vessels and crew at Porto Sereno. '
            'Tier 3: Law enforcement quarantine response records. '
            'Tier 4: Education contacts at the affected campus. '
            'One query, four domains, hundreds of contacts — executed in seconds because '
            'SDC4 components share deterministic identifiers across every domain.'
        ),
        'query_label': 'Run Full Contact Trace',
    },
]
