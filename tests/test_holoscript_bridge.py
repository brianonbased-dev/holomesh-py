"""Tests for the HoloScript bridge receipt."""

import json
from pathlib import Path

from holomesh.client import (
    HOLOSCRIPT_BRIDGE_SOURCE,
    HOLOSCRIPT_HOLOKEY_ID_MARKER,
    HoloMesh,
)


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_holoscript_bridge_receipt_maps_auth_to_holokey_without_secret_values():
    """A fake API key may affect presence booleans, never receipt content."""
    secret_api_key = "test-secret-api-key"
    mesh = HoloMesh(
        "test-agent",
        api_key=secret_api_key,
        wallet_address="0x1111111111111111111111111111111111111111",
    )

    receipt = mesh.holoscript_bridge_receipt()
    serialized = json.dumps(receipt, sort_keys=True)

    assert receipt["schema"] == "holoscript.mesh-python-bridge-receipt.v1"
    assert receipt["holokey"]["marker"] == HOLOSCRIPT_HOLOKEY_ID_MARKER
    assert receipt["holokey"]["api_key_present"] is True
    assert receipt["holokey"]["wallet_address_present"] is True
    assert receipt["holokey"]["secret_material_included"] is False
    assert receipt["triad"]["proof"] == "secret-free receipt plus pytest replay"
    assert receipt["native_holoscript"]["source"] == HOLOSCRIPT_BRIDGE_SOURCE
    assert secret_api_key not in serialized


def test_native_holoscript_bridge_contract_exists_and_names_receipt_method():
    """The Python bridge receipt must stay tied to a native .holo contract."""
    bridge_source = REPO_ROOT / HOLOSCRIPT_BRIDGE_SOURCE
    source_text = bridge_source.read_text(encoding="utf-8")

    assert bridge_source.is_file()
    assert "HOLOSCRIPT_HOLOKEY_ID" in source_text
    assert "triad" in source_text
    assert "holoscript_bridge_receipt" in source_text
