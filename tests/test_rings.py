from flask import current_app
from flask_rings import Rings


def test_extension_init(client):
    assert "rings" in current_app.extensions


def test_load_css(client, rings):
    # test using jsdelivr cdn
    val = rings.load()
    assert "https://cdn.jsdelivr.net/gh/rice0208/Rings@0.2.0/rings.min.css" in val
    # test using specific version
    current_app.config["RINGS_VERSION"] = "0.1.5"
    val = rings.load()
    assert "https://cdn.jsdelivr.net/gh/rice0208/Rings@0.1.5/rings.min.css" in val
    # test using local resources
    current_app.config["RINGS_SERVE_LOCAL"] = True
    val = rings.load()
    assert "rings.min.css" in val
    assert "cdn.jsdelivr.net" not in val


def test_rings_in_blueprints(client):
    assert "rings" in current_app.blueprints
