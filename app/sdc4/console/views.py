"""
Executive console views.

A read-only presentation layer beside /demo/. The demo is the engineer's view;
this is the view for the person who signs. Its one rule is that every figure on
screen resolves to a validated instance, so the console never renders anything it
cannot open.
"""
import logging

from django.http import Http404, HttpResponse
from django.shortcuts import render

from .instances import field_rows, get_instance, instance_header

logger = logging.getLogger(__name__)

PANES = ('graph', 'document', 'table')


def _load(ct_id, instance_id):
    model, obj = get_instance(ct_id, instance_id)
    if model is None:
        raise Http404(f'No data model registered for CT_ID {ct_id}')
    if obj is None:
        raise Http404(f'No instance {instance_id} in {model.DM_LABEL}')
    return model, obj


def _pane_context(model, obj, pane):
    """Build only the projection being asked for."""
    if pane == 'document':
        # The authoritative format, rendered verbatim. Nothing is reformatted:
        # what the reader sees is the bytes that were validated.
        return {'xml_content': obj.xml_content}
    if pane == 'table':
        return {'rows': field_rows(obj)}
    # graph
    return {
        'graph_uri': obj.fuseki_graph_uri,
        'rdf_sync_status': obj.rdf_sync_status,
    }


def instance(request, ct_id, instance_id):
    """One record, shown three ways."""
    model, obj = _load(ct_id, instance_id)
    pane = request.GET.get('pane', 'document')
    if pane not in PANES:
        pane = 'document'

    context = {
        'h': instance_header(model, obj),
        'pane': pane,
        'panes': PANES,
    }
    context.update(_pane_context(model, obj, pane))
    return render(request, 'console/instance.html', context)


def pane(request, ct_id, instance_id, pane):
    """HTMX endpoint: swap one projection without reloading the record."""
    if pane not in PANES:
        return HttpResponse('<p class="hint">Unknown projection.</p>', status=400)
    model, obj = _load(ct_id, instance_id)
    context = _pane_context(model, obj, pane)
    context['h'] = instance_header(model, obj)
    return render(request, f'console/_pane_{pane}.html', context)
