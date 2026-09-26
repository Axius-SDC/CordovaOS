"""The schema reader resolves every element id the 4.3.1 generators carry as a literal, from the published schemas by label."""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from schema import Schema  # noqa: E402

DATAGEN = os.path.join(os.path.dirname(__file__), "..")
LITERAL = re.compile(r'^([A-Z_0-9]+)\s*=\s*\(\s*"(ms-[a-z0-9]+)"\s*,\s*"(ms-[a-z0-9]+)"\s*\)', re.M)
CLUSTER = re.compile(r'^([A-Z_0-9]+)\s*=\s*"(ms-[a-z0-9]+)"', re.M)
CT = re.compile(r'^CT_ID\s*=\s*"([a-z0-9]+)"', re.M)


def modules():
    for path in sorted(glob.glob(os.path.join(DATAGEN, "*.py"))):
        src = open(path, encoding="utf-8").read()
        m = CT.search(src)
        if m:
            yield os.path.basename(path), m.group(1), src


def test_every_literal_pair_in_every_generator_is_a_component_and_its_adapter_in_that_schema():
    total = 0
    for name, ct_id, src in modules():
        s = Schema.for_dm(ct_id)
        pairs = {(comp, adapter) for path, comp, adapter in s.paths if adapter}
        clusters = {comp for path, comp, adapter in s.paths if s.base.get(comp) == "ClusterType"}
        for var, comp, adapter in LITERAL.findall(src):
            assert (comp[3:], adapter[3:]) in pairs, (name, var, comp, adapter)
            total += 1
        for var, ms in CLUSTER.findall(src):
            if var.startswith("CL_") or var in ("GOVERNED_RECORD",):
                assert ms[3:] in clusters, (name, var, ms)
                total += 1
    assert total >= 200, total


def test_paths_resolve_by_label_and_ambiguity_is_refused():
    s = Schema.for_dm("ftluo2nybgxmn7mawttoos20")   # Healthcare Record
    assert s.cluster("Patient Record") == "ms-ygtbvvmzcw3ukfsg3axqry97"
    assert s.leaf("Patient Record/National ID (CID)") == ("ms-nj7s1gk45tfgyooxpz0qaha3", "ms-znhjge005ihiusslkmbcc4h4")
    assert s.enums("Visit Record/Outcome")[:2] == ["Treated and Released", "Admitted"]
    assert s.units("Visit Record/Body Temperature") == "Temperature (SI - Metric)"
    v = Schema.for_dm("ulzd6pe8072mwkqf7i313bov")   # Vital Statistics: the CID sits in four sub-records, one adapter per component
    assert v.leaf("National ID (CID)")[0] == "ms-nj7s1gk45tfgyooxpz0qaha3" == v.leaf("Birth Record/National ID (CID)")[0]
    assert len({p for p, comp, adapter in v.paths if comp == "nj7s1gk45tfgyooxpz0qaha3"}) == 4
    try:
        v.leaf("No Such Leaf")
        raise AssertionError("missing path accepted")
    except KeyError as e:
        assert "no element" in str(e)
