from flask import current_app
from flask_rings import Rings


def test_extension_init(client):
    assert "rings" in current_app.extensions


def test_load_css(client, rings):
    # test using jsdelivr cdn
    val = rings.load()
    assert "cdn.jsdelivr.net" in val
    current_app.config["RINGS_SERVE_LOCAL"] = True
    # test using local resources
    val = rings.load()
    assert "rings.min.css" in val
    assert "cdn.jsdelivr.net" not in val


def test_rings_in_blueprints(client):
    assert "rings" in current_app.blueprints
