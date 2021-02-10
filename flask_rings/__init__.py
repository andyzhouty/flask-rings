"""
    flask_rings
    ~~~~~~~~~~~~~~
    :copyright: (c) 2021 by Andy Zhou.
    :license: LGPL-3.0, see LICENSE for more details.
"""
from flask import Flask, Markup, Blueprint, current_app
from flask.helpers import url_for
from wtforms import HiddenField


def is_hidden_field_filter(field):
    return isinstance(field, HiddenField)


class Rings(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        if not hasattr(app, "extensions") or app.extensions is None:
            app.extensions = {}
        app.extensions["rings"] = self
        app.jinja_env.globals["rings"] = self
        app.jinja_env.globals["rings_is_hidden_field"] = is_hidden_field_filter

        app.config.setdefault("RINGS_SERVE_LOCAL", app.debug)
        app.config.setdefault("RINGS_VERSION", "0.2.0")

        # register blueprint for flask-rings.
        blueprint = Blueprint(
            "rings",
            __name__,
            template_folder="templates",
            static_folder="static",
            static_url_path="/rings" + app.static_url_path,
        )
        app.register_blueprint(blueprint)

    @staticmethod
    def load(css_url=None):
        """Load static files for rings"""
        print(current_app.config["RINGS_SERVE_LOCAL"])
        if css_url is None:
            css_url = (
                "https://cdn.jsdelivr.net/gh/rice0208/Rings@{}/rings.min.css".format(
                    current_app.config["RINGS_VERSION"]
                )
            )
        if current_app.config["RINGS_SERVE_LOCAL"]:
            css_url = url_for("rings.static", filename="css/rings.min.css")

        return Markup(
            """
            <link rel="stylesheet" href="{}">
        """.format(
                css_url
            )
        )
