# CordovaOS Shell App Design

## Overview

The shell app is the only hand-written code in CordovaOS. It provides:
1. **Guided walkthrough** ("The Contagion") — a 7-beat narrative that teaches SDC4 capabilities
2. **Free exploration** — browse all 10 domain apps and run cross-domain SPARQL queries
3. **Role selector** — DPV role-based access control (8 roles, different data visibility)

Both modes run in the same deployment. The walkthrough is a layer on top of the same data and apps that free exploration uses.

## Architecture

```
app/sdc4/
├── shell/                        # The shell app (hand-written)
│   ├── __init__.py
│   ├── apps.py
│   ├── urls.py
│   ├── views.py
│   ├── templatetags/
│   │   └── shell_tags.py         # Role-based filtering template tags
│   ├── static/shell/
│   │   ├── css/
│   │   │   └── cordova.css       # Government terminal aesthetic
│   │   └── js/
│   │       ├── walkthrough.js    # Contagion walkthrough engine
│   │       └── sparql.js         # SPARQL query runner UI
│   └── templates/shell/
│       ├── base.html             # Master template (replaces per-app bases)
│       ├── home.html             # Landing page with role selector
│       ├── dashboard.html        # Domain grid + quick stats
│       ├── walkthrough.html      # Contagion guided experience
│       ├── sparql.html           # Cross-domain query playground
│       └── partials/
│           ├── _role_selector.html
│           ├── _domain_card.html
│           ├── _query_card.html
│           ├── _beat_panel.html
│           └── _redaction_tooltip.html
├── civil_registry/               # Generated (unchanged)
├── healthcare_record/            # Generated (unchanged)
├── ...                           # 8 more generated apps
└── sdc4/                         # Project settings
    ├── settings.py
    ├── urls.py
    └── views.py                  # Updated: delegates to shell
```

## Pages

### 1. Home / Role Selector (`/`)

Full-screen landing with Cordova branding.

```
┌──────────────────────────────────────────────┐
│  🇨🇷  REPUBLIC OF CORDOVA                    │
│  National Information Systems                │
│                                              │
│  Select your role:                           │
│                                              │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐     │
│  │ Citizen  │ │Healthcare│ │  Law     │     │
│  │          │ │ Provider │ │Enforcmnt│     │
│  └──────────┘ └──────────┘ └──────────┘     │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐     │
│  │   Tax    │ │  Port    │ │  Civil   │     │
│  │Authority │ │Authority │ │Registrar│     │
│  └──────────┘ └──────────┘ └──────────┘     │
│  ┌──────────┐ ┌──────────┐                   │
│  │Employer/ │ │ Auditor  │                   │
│  │   HR     │ │          │                   │
│  └──────────┘ └──────────┘                   │
│                                              │
│  ── or ──                                    │
│                                              │
│  [ Start the Walkthrough ]                   │
│  Experience "The Contagion" scenario         │
│                                              │
│  Porto Sereno • Aldara Province • Cordova    │
└──────────────────────────────────────────────┘
```

The role is stored in the Django session. It persists across page loads until changed.

### 2. Dashboard (`/dashboard/`)

After role selection, shows the domain grid with role-appropriate access indicators.

```
┌──────────────────────────────────────────────┐
│ CORDOVA OS  [Role: Tax Authority ▼]  [Walkthrough] [SPARQL] │
├──────────────────────────────────────────────┤
│                                              │
│  Domain Applications                         │
│                                              │
│  ┌─────────────┐ ┌─────────────┐ ┌────────────┐
│  │Civil Registry│ │Vital Stats  │ │ Healthcare │
│  │ Identity    │ │  ██████████ │ │ ██████████ │
│  │ 25,000 recs │ │  No Access  │ │  No Access │
│  │ [Open]      │ │             │ │            │
│  └─────────────┘ └─────────────┘ └────────────┘
│  ┌─────────────┐ ┌─────────────┐ ┌────────────┐
│  │ Education   │ │ Employment  │ │ Business   │
│  │  ██████████ │ │ Income Only │ │ Full Access│
│  │  No Access  │ │ 18,000 recs │ │ 1,500 recs │
│  │             │ │ [Open]      │ │ [Open]     │
│  └─────────────┘ └─────────────┘ └────────────┘
│  ┌─────────────┐ ┌─────────────┐ ┌────────────┐
│  │  Property   │ │Tax & Revenue│ │Law Enforce │
│  │ Full Access │ │ Full Access │ │ ██████████ │
│  │ 8,000 recs  │ │ 30,000 recs │ │  No Access │
│  │ [Open]      │ │ [Open]      │ │            │
│  └─────────────┘ └─────────────┘ └────────────┘
│  ┌─────────────┐                               │
│  │  Maritime   │                               │
│  │ Port Fees   │                               │
│  │ 2,000 recs  │                               │
│  │ [Open]      │                               │
│  └─────────────┘                               │
│                                              │
│  Cross-Domain Queries ──────────────────     │
│  [Government Profile] [Economic Network]     │
│  [Social Services]    [Supply Chain]         │
│  [Family Unit]        [Institutional Impact] │
│  [🔴 Contagion Trace]                        │
└──────────────────────────────────────────────┘
```

Cards for inaccessible domains show a DPV-vocabulary explanation on hover:
```
Access Denied
  Your Role: dpv:GovernmentalOrganisation (Tax Authority)
  Data Purpose: dpv:ProvideHealthcare
  Reason: Purpose Mismatch
```

### 3. Walkthrough (`/walkthrough/`)

The Contagion scenario as a guided, multi-beat experience. Each beat is a self-contained panel that demonstrates an SDC4 capability.

**Beat structure** — each beat has:
- **Title** and **timestamp** (Jan 14-17, 2026 timeline)
- **Narrative text** explaining what's happening in the story
- **Live data** pulled from the actual database/triplestore
- **Proof point** — what SDC4 capability this demonstrates
- **Action buttons** — "Run this query" / "Switch role" / "Try the override"
- **Next beat** navigation

**The 7 Beats:**

| Beat | Title | Color | SDC4 Proof Point |
|------|-------|-------|-----------------|
| 1 | Arrival | White | Cross-domain identity (same Person cell, 10 systems) |
| 2 | The Query | White | Graph-native queries (4-domain SPARQL in one traversal) |
| 3 | Redaction | Black | Schema-enforced privacy (medical data redacted by DPV role) |
| 4 | Override | Amber | Governed exceptions (override creates auditable ExceptionalValue) |
| 5 | Refusal | Red | Schema-level composition refusal (not app-level "permission denied") |
| 6 | The Audit | White | Provenance everywhere (who saw what, when, under what authority) |
| 7 | Architecture Flex | White | Zero integration code (compiler output, not glue code) |

**Beat 1 — Arrival:**
- Show the Maritime Port Call record for MV Estrella del Sur
- Show Carlos Mendoza's crew record linked to his Civil Registry identity
- "Notice: the same National ID appears in Maritime AND Civil Registry with zero mapping code"

**Beat 2 — The Query:**
- Run the Contagion Contact Tracing SPARQL query live
- Show the 4-tier traversal: Carlos → family (Elena) → coworkers → students
- Visualize the 356 contacts on a simple graph/list
- "This query traverses 4 domain apps in a single SPARQL request"

**Beat 3 — Redaction:**
- Switch role to Auditor
- Show Carlos's Government Profile — all domains visible, but Healthcare shows "REDACTED"
- Show the DPV tooltip: "Purpose Mismatch: dpv:ProvideHealthcare ≠ dpv:Authority"
- "The medical diagnosis travels with the data. The graph doesn't change — the view does."

**Beat 4 — Override:**
- Governor invokes Governed Override to see the diagnosis
- Show the ExceptionalValue Cell being created (auditable, timestamped, justified)
- The override expires (amber = temporary warrant)
- "Even the exception is a governed object. Nothing escapes the physics."

**Beat 5 — Refusal:**
- Switch to Healthcare Provider role
- Attempt to compose Carlos's medical record into a public marketing report
- Show the XSD Schema Validation Failure (not a UI error)
- Show the ExceptionalValue:Refusal Cell created
- "The data itself refused. Not application code — the schema."

**Beat 6 — The Audit:**
- Show the Auditor's view of all governance events
- Override event, refusal event, all access timestamps
- "Every action is a first-class object in the graph"

**Beat 7 — Architecture Flex:**
- Side-by-side: traditional integration (10 APIs, middleware, ETL) vs SDC4 (compiler output)
- Count the lines of glue code: zero
- Show the generated app structure
- "The Reference Model is the integration layer. SDCStudio compiled it in."

### 4. SPARQL Playground (`/sparql/`)

Interactive query runner with the 7 pre-built queries plus a free-form editor.

```
┌──────────────────────────────────────────────┐
│ SPARQL Query Playground     [Role: Auditor ▼]│
├──────────────────────────────────────────────┤
│                                              │
│  Pre-built Queries:                          │
│  [Government Profile] [Economic Network]     │
│  [Social Services]    [Supply Chain]         │
│  [Family Unit]        [Institutional Impact] │
│  [🔴 Contagion Trace]                        │
│                                              │
│  ┌────────────────────────────────────────┐  │
│  │ # Query 1: Complete Government Profile │  │
│  │ PREFIX sdc4: <https://...>             │  │
│  │ SELECT ?domain ?component ?value       │  │
│  │ WHERE {                                │  │
│  │   ...                                  │  │
│  │ }                                      │  │
│  │                                        │  │
│  │ Parameters:                            │  │
│  │ National ID: [COR-AL01-271845    ]     │  │
│  │                                        │  │
│  │ [ Run Query ]                          │  │
│  └────────────────────────────────────────┘  │
│                                              │
│  Results:                                    │
│  ┌────────────────────────────────────────┐  │
│  │ Domain          │ Component    │ Value │  │
│  │─────────────────┼──────────────┼───────│  │
│  │ Civil Registry  │ Given Name   │Carlos │  │
│  │ Civil Registry  │ Surname      │Mendoza│  │
│  │ Healthcare      │ REDACTED     │ ███   │  │
│  │ Maritime        │ Vessel Name  │MV Est │  │
│  │ ...             │              │       │  │
│  └────────────────────────────────────────┘  │
│                                              │
│  [Download CSV] [Download JSON]              │
└──────────────────────────────────────────────┘
```

The SPARQL playground sends queries to GraphDB's REST API (`/repositories/sdc4_rdf`) via a Django view that proxies the request (adding role-based graph filtering).

## Visual Design

### Color Palette — Government Terminal Aesthetic

Not a flashy SPA. Intentionally austere — this is a government system, not a consumer app.

```css
--cordova-navy:     #1a2744;   /* navbar, headers */
--cordova-slate:    #2d3748;   /* sidebar, secondary */
--cordova-gold:     #d4a843;   /* accents, Cordova seal */
--cordova-white:    #f7fafc;   /* backgrounds */
--cordova-red:      #c53030;   /* redacted / refused */
--cordova-amber:    #d69e2e;   /* override / warning */
--cordova-green:    #38a169;   /* accessible / granted */
--cordova-black:    #1a202c;   /* redacted blocks */
```

### Layout

- **Top navbar**: Fixed, dark navy. "REPUBLIC OF CORDOVA" left, role selector + nav right.
- **No sidebar** — domain access is from the dashboard cards.
- **Content area**: White/light, clean typography, generous spacing.
- **Bootstrap 5** — same framework as the generated apps for consistency.
- **No CDN dependencies for production** — bundle Bootstrap locally for sovereign deployment.

## Technical Implementation

### Session-Based Role

```python
# shell/middleware.py
class RoleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.cordova_role = request.session.get('cordova_role', None)
        return self.get_response(request)
```

### Role-Based Domain Access

```python
# shell/access.py
ROLE_ACCESS = {
    'citizen': {
        'civil_registry': 'full',
        'vital_statistics': 'full',
        'healthcare_record': 'full',
        'education_record': 'full',
        'employment_record': 'full',
        'business_registry': 'full',
        'property_registry': 'full',
        'tax_revenue': 'full',
        'law_enforcement': 'full',
        'maritime': 'full',
    },
    'healthcare': {
        'civil_registry': 'limited',
        'vital_statistics': 'full',
        'healthcare_record': 'full',
    },
    'law_enforcement': {
        'civil_registry': 'identity',
        'law_enforcement': 'full',
        'maritime': 'crew',
    },
    'tax_authority': {
        'civil_registry': 'identity',
        'employment_record': 'income',
        'business_registry': 'full',
        'property_registry': 'full',
        'tax_revenue': 'full',
        'maritime': 'port_fees',
    },
    'port_authority': {
        'civil_registry': 'crew_id',
        'business_registry': 'shipping',
        'maritime': 'full',
        'tax_revenue': 'port_fees',
    },
    'civil_registrar': {
        'civil_registry': 'full',
        'vital_statistics': 'full',
    },
    'employer_hr': {
        'civil_registry': 'verify',
        'education_record': 'verify',
        'employment_record': 'own_staff',
        'business_registry': 'own',
    },
    'auditor': {
        # All domains, provenance only
        'civil_registry': 'provenance',
        'vital_statistics': 'provenance',
        'healthcare_record': 'provenance',
        'education_record': 'provenance',
        'employment_record': 'provenance',
        'business_registry': 'provenance',
        'property_registry': 'provenance',
        'tax_revenue': 'provenance',
        'law_enforcement': 'provenance',
        'maritime': 'provenance',
    },
}
```

### SPARQL Proxy View

```python
# shell/views.py
import requests
from django.http import JsonResponse

def sparql_query(request):
    """Proxy SPARQL queries to GraphDB with role-based filtering."""
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=405)

    query = request.POST.get('query', '')
    role = request.session.get('cordova_role', 'citizen')

    # Send to GraphDB
    response = requests.post(
        f"{settings.GRAPHDB_URL}/repositories/{settings.GRAPHDB_REPOSITORY}",
        data={'query': query},
        headers={'Accept': 'application/sparql-results+json'},
    )

    return JsonResponse(response.json())
```

### Walkthrough Engine

The walkthrough is a single-page experience with JavaScript-driven beat navigation. Each beat loads its content from a Django view that returns HTML partials.

```javascript
// shell/static/shell/js/walkthrough.js
const beats = [
    { id: 1, title: 'Arrival', endpoint: '/walkthrough/beat/1/' },
    { id: 2, title: 'The Query', endpoint: '/walkthrough/beat/2/' },
    { id: 3, title: 'Redaction', endpoint: '/walkthrough/beat/3/' },
    { id: 4, title: 'Override', endpoint: '/walkthrough/beat/4/' },
    { id: 5, title: 'Refusal', endpoint: '/walkthrough/beat/5/' },
    { id: 6, title: 'The Audit', endpoint: '/walkthrough/beat/6/' },
    { id: 7, title: 'Architecture Flex', endpoint: '/walkthrough/beat/7/' },
];
```

### URL Structure

```python
# shell/urls.py
urlpatterns = [
    path('', views.home, name='home'),
    path('set-role/', views.set_role, name='set-role'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('walkthrough/', views.walkthrough, name='walkthrough'),
    path('walkthrough/beat/<int:beat>/', views.walkthrough_beat, name='walkthrough-beat'),
    path('sparql/', views.sparql_page, name='sparql'),
    path('sparql/run/', views.sparql_query, name='sparql-run'),
]
```

## Build Sequence

1. Create `shell` Django app with base template and role middleware
2. Build home page with role selector
3. Build dashboard with domain cards and access indicators
4. Build SPARQL playground (query editor + results table)
5. Build walkthrough engine (beat navigation + partial loading)
6. Write beat content templates (7 beats)
7. Style with government terminal aesthetic
8. Replace CDN links with locally bundled Bootstrap

## What the Shell Does NOT Do

- Does not modify any generated app code
- Does not implement the DPV `act` evaluation engine (that comes with the generated apps)
- Does not manage data — synthetic data is loaded via management commands
- Does not implement authentication — this is a demo, all roles are session-based selection
