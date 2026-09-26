"""The schema reader resolves component and adapter ids by label path from the published 4.4.0 models."""
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from schema import DMLIB, Schema  # noqa: E402


def _by_title(prefix):
    for name in sorted(os.listdir(DMLIB)):
        m = re.match(r"dm-([a-z0-9]{24})\.xsd$", name)
        if m:
            s = Schema.for_dm(m.group(1))
            if s.label.get(s.dm, "").startswith(prefix):
                return s
    raise AssertionError(prefix)


def test_paths_resolve_by_label_and_ambiguity_is_refused():
    s = _by_title("Healthcare Record")
    assert s.cluster("Patient Record").startswith("ms-")
    comp, adapter = s.leaf("Patient Record/National ID (CID)")
    assert comp == "ms-nj7s1gk45tfgyooxpz0qaha3" and adapter.startswith("ms-")   # the kept Cordova CID, its adapter minted per model
    assert s.enums("Encounter/Encounter Status")[:2] == ["planned", "arrived"]
    assert s.units("Vital Signs Panel/Body Temperature") == "Temperature (SI - Metric)"
    assert s.temporal_kinds("Condition/Onset Date") == ["xdtemporal-datetime"]
    assert len(s.states()) >= 3, s.states()   # the bound ProvGov workflow
    assert s.leaf("Code Display Text") == s.leaf("Allergen (SNOMED CT)/Code Display Text")   # one component, one adapter, every Coded Value cluster
    b = _by_title("Law Enforcement Record")
    try:
        b.leaf("Disposition Date")   # Cordova's charge disposition date and NIEM's j:Disposition date share the label
        raise AssertionError("ambiguity accepted")
    except KeyError as e:
        assert "ambiguous" in str(e)
    try:
        s.leaf("No Such Leaf")
        raise AssertionError("missing path accepted")
    except KeyError as e:
        assert "no element" in str(e)


def test_a_component_keeps_one_adapter_across_the_sub_records_that_compose_it():
    v = _by_title("Vital Statistics Record")
    hits = {(comp, adapter) for p, comp, adapter in v.paths if comp == "nj7s1gk45tfgyooxpz0qaha3"}
    assert len(hits) == 1 and len([p for p, comp, a in v.paths if comp == "nj7s1gk45tfgyooxpz0qaha3"]) == 4
    assert v.leaf("Birth Record/National ID (CID)") == v.leaf("Death Record/National ID (CID)")


def test_every_model_has_a_governed_record_and_a_bound_workflow():
    for name in sorted(os.listdir(DMLIB)):
        m = re.match(r"dm-([a-z0-9]{24})\.xsd$", name)
        if not m:
            continue
        s = Schema.for_dm(m.group(1))
        assert s.label[s.dm].endswith("4.4.0"), s.label[s.dm]
        assert s.states(), s.label[s.dm]
        data = [p for p, comp, a in s.paths if len(p) == 1 and s.base.get(comp) == "ClusterType"]
        assert data and data[0][0].endswith("Governed Record"), (s.label[s.dm], data)
        assert s.required(data[0][0])
