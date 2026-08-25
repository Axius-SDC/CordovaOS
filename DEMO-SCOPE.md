# Demo scope: make the answer show its work

*Scoped 2026-08-25. Target: demo-ready for 2026-09-28, when the Substack piece "When Proof Gets Cheap" publishes and points at it.*

---

## The gap, stated plainly

The README makes the claim that matters: every record is **governance-composed**, carrying its own Provenance and a structural Audit record, bound to the data at the source rather than bolted on afterward.

Then you run `make demo` and you cannot see any of it.

A grep of the demo app finds provenance mentioned twice in `views.py` and once each in two templates. The property that makes CordovaOS unlike anything else in this space is asserted in the README and invisible in the thing people actually run.

**You can already ask a cross-domain question and get an answer. You cannot ask why that answer is admissible.** That is the whole argument, and it is the one thing an adjacent situational-awareness project cannot copy by adding a nicer front end.

**The good news, confirmed by inspection:** the data is already there. The graph carries `prov:Entity`, `prov:Agent`, `prov:Activity`, `prov:startedAtTime`, `prov:endedAtTime`, `prov:atLocation`, plus `sdc4:Audit`, `sdc4:AuditType` and `sdc4:AuditBaseShape`. **Nothing has to be re-modeled or re-generated.** This is a surfacing job.

## The design principle: familiar first, then beyond

Earlier framing here was "a receipt, not a dashboard," and that was wrong for the audience. A C-suite visitor needs a surface they recognize or there is nothing to measure the difference against.

**So it should open looking like a BI tool.** Plain-language questions, a table of results, the shapes anyone has seen. That familiarity is the control condition. The argument is not made by looking austere; it is made by what happens when they click a value and get something no BI tool can give them.

Familiar, then beyond. In that order, deliberately.

---

## Piece 0: the plain-language question deck

**Why first:** it is the entry point, it is cheap, and without it the other pieces have no audience. The explorer today is a developer surface, a `<select>` of `01. Complete Government Profile (Civil-Registry, Healthcare-Record)` over a raw SPARQL editor. A chief executive cannot start there.

**What changes:** the seven canned queries get plain-language front doors, presented as cards, phrased as questions a person would actually ask.

| Ask | Runs |
|---|---|
| "Who was exposed at the ferry terminal, and where do they work?" | 07 contagion contact tracing |
| "Where did this shipment come from, and who handled it?" | 04 supply chain provenance |
| "What does the government know about this resident, across every department?" | 01 complete government profile |
| "Which households would a benefits change actually reach?" | 03 social services identification |
| "If this employer closed, what else moves?" | 02 economic network analysis |
| "Which institutions does this event touch?" | 06 institutional impact |
| "Who is economically dependent on whom in this family?" | 05 family economic unit |

The SPARQL editor stays, demoted behind a "show the query" disclosure. Seeing the SPARQL is itself part of the argument for the technical half of the audience, so it must remain reachable, just not first.

**Files:** `templates/demo/explorer.html`, plus a `question` field added to the catalog in `sparql_loader.py`.

---

## Piece 1: the provenance drawer

**This is the core. Everything else is staging for it.**

Click any value in any result and get its lineage: which institution produced it, which component defined it and at what version, what constraints were in force, when it was true as distinct from when it was recorded, and whether it validated.

### The blocker to fix first

`run_query` currently flattens every binding to a bare string:

```python
row = [binding.get(v, {}).get('value', '') for v in variables]
```

That discards `type` and `datatype`, which means **the URI of the node is thrown away before it reaches the template.** Nothing downstream can ask about a cell because nothing downstream knows what a cell refers to.

Change the row shape to keep it:

```python
row = [{
    'value':    binding.get(v, {}).get('value', ''),
    'type':     binding.get(v, {}).get('type', ''),       # 'uri' | 'literal' | 'bnode'
    'datatype': binding.get(v, {}).get('datatype', ''),
} for v in variables]
```

Cells with `type == 'uri'` become explainable. Everything else renders as it does today. **Note the cache:** `run_query` caches parsed results by SPARQL hash, so the cache entries change shape. Bump the cache key prefix or the first run after deploy will render old-format rows into the new template.

### The new endpoint

`explain_value(request)`, an HTMX GET taking a node URI, running a provenance query against GraphDB, returning a partial.

New file `sparql/provenance_for_node.rq`, parameterized on the node, retrieving:

- `prov:wasGeneratedBy` activity, with `startedAtTime` / `endedAtTime` / `atLocation`
- `prov:wasAttributedTo` agent, resolved to the institution
- the `sdc4:Audit` record bound to the instance
- the component the instance conforms to, and its version
- valid-time against record-time
- validation verdict, and signature if present

### What the drawer shows

Two registers, stacked. Plain language on top, the underlying triples underneath a disclosure. The C-suite reader reads the top. The architect they bring to the second meeting reads the bottom, and that the bottom exists is what makes the top believable.

**Files:** `views.py` (new view + row shape + cache key), `urls.py`, `templates/demo/_query_results.html` (cell markup, `hx-get` on URI cells), new `templates/demo/_provenance_drawer.html`, new `sparql/provenance_for_node.rq`.

---

## Piece 2: the auditor's question

A single staged view that reproduces Part Three of the story rather than leaving the visitor to discover it.

> An auditor asks about a record from four years ago. Under what specification was it released, and against which version of the rules?

The answer arrives with its meaning attached. Not a report generated afterward by a system asserting what it believes. The record itself, unchanged since the day it was written.

**Use query 04, supply chain provenance.** It is the one of the seven that is already about a thing's history, which is what an audit is. Contagion is the better *story* and stays where it is; audit is the better *proof* and gets its own room.

The view is narrow on purpose: one question, one answer, every value in it explainable via Piece 1. It should be reachable in one click from the dashboard, because it is the thing we most want a check-signer to see.

**Files:** `views.py`, `urls.py`, new `templates/demo/auditor.html`, dashboard link.

---

## Piece 3: boundary marking on the contagion trace

The trace already crosses four institutional boundaries. Today the crossing is invisible, which means the claim is being made in prose and not shown.

Mark each crossing in the narrative beats and show that the meaning survived it: same component, same constraints, different institution, no mapping step in between.

**The one unknown to resolve first:** how a value's originating institution is determined at query time. If each domain loads into its own named graph, this is nearly free, `GRAPH ?g` in the provenance query and a lookup. If institution is instead carried on the instance or inferred from the component namespace, it is a slightly different query and no harder. **Verify this in week one**, because Piece 1 needs the same answer and both pieces stall without it.

**Files:** `narrative.py`, `templates/demo/narrative.html`, `templates/demo/_beat_results.html`.

---

## What this demonstrates that a BI tool cannot

Worth stating explicitly, because it is the sentence the whole demo exists to earn:

1. **Click any value and get its lineage** — because provenance is bound to the instance, not reconstructed from a pipeline log that may or may not still exist.
2. **The same question returns the same answer with the same verdict, every time** — deterministically validated rather than probabilistically assembled.
3. **The answer crosses institutional boundaries with its meaning intact**, and can show you exactly where it crossed.

A BI tool can do none of these, and adding a prettier front end to a pile of feeds does not get you closer to any of them.

---

## Sequencing

| Order | Work | Why here |
|---|---|---|
| 1 | Resolve the institution-attribution question | Pieces 1 and 3 both depend on it. Cheapest thing that can invalidate the plan. |
| 2 | Piece 1, row shape + `explain_value` + drawer | The core. Everything else stages it. |
| 3 | Piece 0, question deck | Cheap, and makes Piece 1 reachable by the intended audience. |
| 4 | Piece 2, auditor's question | Uses Piece 1; adds no new machinery. |
| 5 | Piece 3, boundary marking | Highest polish, lowest risk, first thing to cut if September tightens. |

**If the month compresses, ship 1 and 0 and stop.** A familiar surface where every value explains itself is the entire argument. Two and three are amplification.

## Risks

**The drawer becomes a debug view.** Failure mode is dumping triples at a chief executive. The plain-language layer is not decoration; it is the deliverable, and the triples sit underneath it.

**Load time.** `make demo-full` already takes hours. Every explain click is another GraphDB round trip. Cache aggressively per node, and test the drawer against the small dataset before anyone tries it on the full one.

**Scope drift into a product.** This is a demonstrator. If it acquires a roadmap it has become the application company we said we would not be.
