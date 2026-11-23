import pathlib
import pytest
import yaml
from app import summarize

CASES = yaml.safe_load((pathlib.Path(__file__).parent.parent / "attacks.yaml").read_text())


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_attack_is_resisted(case):
    output = summarize(case["document"])
    for bad in case["forbidden"]:
        assert bad.lower() not in output.lower(), f"Injection succeeded: {bad!r} in output"
