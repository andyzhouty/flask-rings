"""
    flask_rings
    ~~~~~~~~~~~~~~
    :copyright: (c) 2021 by Andy Zhou.
    :license: LGPL-3.0, see LICENSE for more details.
"""
from flask import Flask, Markup


class Rings(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        if not hasattr(app, "extensions") or app.extensions is None:
            app.extensions = {}
        app.extensions["rings"] = self
        app.jinja_env.globals["rings"] = self

        app.config.setdefault("RINGS_SERVE_LOCAL", app.debug)

    @staticmethod
    def load(css_url=None):
        """Load static files for rings"""
        if css_url is None:
            css_url = "https://cdn.jsdelivr.net/gh/ringsings/rings/rings.min.css"
        return Markup(
            """
            <link rel="stylesheet" href="{}">
        """.format(
                css_url
            )
        )
