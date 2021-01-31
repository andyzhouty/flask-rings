from flask import current_app


class TestRings(object):
    def test_extension_init(self, client, rings):
        assert "rings" in current_app.extensions

        current_app.extensions = None
        app = current_app._get_current_object()
        rings.init_app(app)
        assert "rings" in current_app.extensions

        delattr(current_app._get_current_object(), "extensions")
        rings.init_app(app)
        assert "rings" in current_app.extensions

    def test_load_css(self, client, rings):
        val = rings.load()
        assert "rings.min.css" in val
