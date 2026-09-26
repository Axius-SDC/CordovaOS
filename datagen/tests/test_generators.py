"""The whole demo dataset generates, and every record validates against its model's XSD 1.1 schema."""
import glob
import os
import re
import subprocess
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from schema import DMLIB  # noqa: E402

DATAGEN = os.path.join(os.path.dirname(__file__), "..")


@pytest.fixture(scope="module")
def dataset(tmp_path_factory):
    out = tmp_path_factory.mktemp("import_data")
    env = dict(os.environ, CORDOVA_DEMO_SCALE="1", CORDOVA_IMPORT_DIR=str(out))
    run = subprocess.run([sys.executable, "generate_all.py"], cwd=DATAGEN, env=env, capture_output=True, text=True, timeout=600)
    assert run.returncode == 0, run.stderr[-2000:]
    return out, run.stdout


def test_the_demo_dataset_is_the_documented_size(dataset):
    out, stdout = dataset
    counts = {d: len(glob.glob(os.path.join(out, d, "*.xml"))) for d in sorted(os.listdir(out))}
    assert len(counts) == 10, counts
    assert sum(counts.values()) == 1460, counts
    assert "TOTAL" in stdout


def test_every_record_validates_and_only_the_stated_absences_are_invalid(dataset):
    from sdcvalidator import build_xsd11_schema
    out, _ = dataset
    schemas = {}
    invalid, with_ev, unexpected = 0, 0, []
    for path in sorted(glob.glob(os.path.join(out, "*", "*.xml"))):
        xml = open(path, encoding="utf-8").read()
        ct = re.search(r"dm-([a-z0-9]{24})", xml[:2000]).group(1)
        if ct not in schemas:
            schemas[ct] = build_xsd11_schema(os.path.join(DMLIB, f"dm-{ct}.xsd"), validation="lax",
                                             uri_mapper={"https://semanticdatacharter.com/ns/sdc4/sdc4.xsd": os.path.abspath(os.path.join(DMLIB, "sdc4.xsd"))})
        errors = list(schemas[ct].iter_errors(xml))
        has_ev = "<ev-name>" in xml
        with_ev += has_ev
        invalid += bool(errors)
        if errors and not (has_ev and len(errors) == 1):
            unexpected.append((os.path.basename(path), str(errors[0])[:200]))
    assert not unexpected, unexpected[:5]
    assert invalid == with_ev == 7, (invalid, with_ev)


def test_the_dataset_is_the_same_on_every_run(dataset, tmp_path):
    """Seeded generators: the same records, values and relationships every time; only timestamps and identifiers move."""
    out, _ = dataset
    again = tmp_path / "again"
    env = dict(os.environ, CORDOVA_DEMO_SCALE="1", CORDOVA_IMPORT_DIR=str(again))
    subprocess.run([sys.executable, "generate_all.py"], cwd=DATAGEN, env=env, capture_output=True, text=True, timeout=600, check=True)
    strip = re.compile(r"<(creation_timestamp|instance_id)>[^<]*</\1>")
    def corpus(root):
        return sorted(strip.sub("", open(p, encoding="utf-8").read()) for p in glob.glob(os.path.join(root, "*", "*.xml")))
    assert corpus(out) == corpus(again)
