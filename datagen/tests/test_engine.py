"""The template engine: every 4.4.0 model fills from label paths and validates under its own XSD 1.1 schema."""
import os
import re
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from engine import EV, Quantity, Template  # noqa: E402
from schema import DMLIB, Schema  # noqa: E402

MODELS = {}   # every published model the app carries, by title
for _name in sorted(os.listdir(DMLIB)):
    _m = re.match(r"dm-([a-z0-9]{24})\.xsd$", _name)
    if _m:
        _s = Schema.for_dm(_m.group(1))
        MODELS[_s.label.get(_s.dm, _m.group(1))] = {"ct_id": _m.group(1)}
HEALTHCARE = next(v["ct_id"] for k, v in MODELS.items() if k.startswith("Healthcare"))
VITAL = next(v["ct_id"] for k, v in MODELS.items() if k.startswith("Vital"))


def _schema(ct_id):
    from sdcvalidator import build_xsd11_schema
    return build_xsd11_schema(os.path.join(DMLIB, f"dm-{ct_id}.xsd"),
                              uri_mapper={"https://semanticdatacharter.com/ns/sdc4/sdc4.xsd": os.path.abspath(os.path.join(DMLIB, "sdc4.xsd"))}, validation="lax")


def test_the_template_is_completed_from_the_schema_where_the_scaffold_wrote_a_shared_leaf_once():
    # SDCStudio issue #705: the scaffold writes a component composed in several clusters under the first one only
    t = Template.for_dm(VITAL)
    assert len({id(e) for e in t.paths["National ID (CID)"]}) == 4   # the four sub-records (the schema declares it once, the scaffold wrote it once)
    for sub in ("Birth Record", "Death Record", "Marriage Record", "Divorce Record"):
        assert f"{sub}/National ID (CID)" in t.paths
    h = Template.for_dm(HEALTHCARE)
    assert "Diagnosis (ICD-10-CM)/Code Display Text" in h.paths and "Allergen (SNOMED CT)/Code Display Text" in h.paths


def test_a_temporal_shape_the_model_does_not_allow_is_refused():
    t = Template.for_dm(HEALTHCARE)
    with pytest.raises(AssertionError, match="allows"):
        t.instance({"Condition/Onset Date": "2025-03-12"}, instance_id="i-x", current_state=t.schema.states()[0])


def test_a_state_outside_the_bound_workflow_is_refused():
    t = Template.for_dm(HEALTHCARE)
    with pytest.raises(AssertionError, match="current-state"):
        t.instance({"Patient Record/National ID (CID)": "COR-AL01-000001"}, instance_id="i-x", current_state="Documented")


def _every_leaf(t: Template):
    """A value for every leaf the schema declares, of the shape the schema asks for; one Exceptional Value on the first quantity."""
    s = t.schema
    vals, ev_path = {}, None
    for p, comp, adapter in s.paths:
        base, path = s.base.get(comp, ""), "/".join(p)
        if base == "ClusterType" or not adapter or path not in t.paths:
            continue
        body = s.types[comp]
        if base == "XdTokenType":
            vals[path] = s.enums(path)[0]
        elif base == "XdStringType":
            m = re.search(r'name="xdstring-value"[^>]*>(.*?)</xsd:element>', body, re.S)
            pat = re.search(r'<xsd:pattern value="([^"]*)"', m.group(1)) if m else None
            vals[path] = {r"\S+": "urn:cordova:x:1", r"COR-(AL|BR|CE)0[1-3]-[0-9]{6}": "COR-AL01-000001", r"BIZ-[0-9]{6}": "BIZ-000001",
                          r"(AL|BR|CE)-0[1-3]-[0-9]{6}": "AL-01-000001", r".+@.+\..+": "a@b.co", r"\+?\d[\d\s\-\(\)]{6,18}": "+99-100-555-0000",
                          r"[0-9]{5,5}": "00001", r"[0-9]{6,18}": "123456", r"[A-Z0-9]{6,6}": "UN1234", r"[A-Z0-9]{3,3}": "COR", r"[A-Z]{2,2}": "CO",
                          r"[0-9]{1,8}": "1234", r"[0-9]{1,3}": "12", r"[A-TV-Z][0-9][0-9AB](\.[0-9A-TV-Z]{1,4})?": "J11.1"}.get(pat.group(1).replace("&quot;", '"') if pat else None, "text")
        elif base == "XdTemporalType":
            vals[path] = {"xdtemporal-datetime": "2025-03-12T09:00:00", "xdtemporal-date": "2025-03-12", "xdtemporal-year": "2025", "xdtemporal-year-month": "2025-03",
                          "xdtemporal-duration": "P3D", "xdtemporal-time": "09:00:00"}[s.temporal_kinds(path)[0]]
        elif base in ("XdQuantityType", "XdCountType", "XdFloatType", "XdDoubleType"):
            if ev_path is None:
                vals[path], ev_path = EV("ASKU"), path
            else:
                vals[path] = Quantity("12" if base == "XdCountType" else "12.5", "unit")
        elif base == "XdBooleanType":
            vals[path] = True
        elif base == "XdFileType":
            vals[path] = b"signature bytes" if "Signature" in path else "https://cordova.example/file.png"
        elif base == "XdOrdinalType":
            vals[path] = (1, "one")
        elif base == "XdLinkType":
            vals[path] = ""
    if ev_path is None:   # a model without a quantity states its absence on a text value instead
        ev_path = next(p for p, v in vals.items() if v == "text")
        vals[ev_path] = EV("ASKU")
    return vals, ev_path


@pytest.mark.parametrize("title", sorted(MODELS))
def test_every_model_fills_every_leaf_and_validates_except_the_one_stated_absence(title):
    ct = MODELS[title]["ct_id"]
    t = Template.for_dm(ct)
    vals, ev_path = _every_leaf(t)
    assert len(vals) > 40, title
    xml = t.instance(vals, instance_id="i-test000000000000000001", current_state=t.schema.states()[0],
                     subject=("Subject", "Name"), provider=("Provider", "Cordova"),
                     audit={"system_id": "urn:cordova:system:x", "user": "Cordova System"}, attestation={"reason": "Test", "committer": "Registrar", "pending": False})
    assert "_PH_" not in xml
    errors = [str(e) for e in _schema(ct).iter_errors(xml)]
    assert len(errors) == 1, (title, errors[:3])   # exactly the Exceptional Value in place of a required value: invalid on purpose
    assert "-value" in errors[0], errors[0]
    assert "<ev-name>Asked but Unknown</ev-name>" in xml
    # without the absence, valid
    vals[ev_path] = Quantity("1", "unit") if t.schema.base_of(ev_path) in ("XdQuantityType", "XdCountType", "XdFloatType", "XdDoubleType") else "text"
    xml = t.instance(vals, instance_id="i-test000000000000000002", current_state=t.schema.states()[0], subject=("Subject", "Name"), provider=("Provider", "Cordova"),
                     audit={"system_id": "urn:cordova:system:x", "user": "Cordova System"}, attestation={"reason": "Test", "committer": "Registrar", "pending": False})
    assert not list(_schema(ct).iter_errors(xml)), title


def test_omitted_optional_members_are_dropped_and_the_instance_stays_valid():
    t = Template.for_dm(HEALTHCARE)
    xml = t.instance({"Patient Record/National ID (CID)": "COR-AL01-271845", "Vital Signs Panel/Body Temperature": Quantity("37.2", "Cel")},
                     instance_id="i-test000000000000000003", current_state=t.schema.states()[0], subject=("Patient", "Carlos Mendoza"), provider=("Hospital", "Porto Sereno General"),
                     audit={"system_id": "urn:cordova:system:healthcare", "user": "Cordova Healthcare System"}, attestation={"reason": "Recorded", "committer": "Registrar", "pending": False})
    assert "Allergy Intolerance" not in xml and "Vital Signs Panel" in xml
    assert not list(_schema(HEALTHCARE).iter_errors(xml))
