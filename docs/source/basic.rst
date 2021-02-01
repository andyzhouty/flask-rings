Basic Usage
===========

Installation
------------

Using PYPI

.. code:: bash

    $ pip install flask-rings

or using git:

.. code:: bash

    $ pip install git+https://github.com/z-t-y/flask-rings.git

Initialization
--------------

.. code:: python

    from flask import Flask
    from flask_rings import Rings

    app = Flask(__name__)

    rings = Rings(app)

or 

.. code:: python

    from flask import Flask
    from flask_rings import Rings

    rings = Rings()

    def create_app():
        app = Flask(__name__)
        rings.init_app(app)


Resource loader
---------------

Flask-Rings a helper for loading the CSS of Rings.
Call it in your base template, for example:

.. code:: jinja

    <head>
        ...
        {{ rings.load() }}
    </head>


Sample Template
---------------

Unlike flask-bootstrap, flask-rings doesn't have a ``base.html`` built-in.

If you want a ``base.html``, here's an example:

.. code:: jinja

    <!doctype html>
    <html lang="en">
        <head>
            {% block head %}
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

            {% block styles %}
                {{ rings.load() }}
            {% endblock %}

            <title>
                {% block title %}Your page title{% endblock %}
            </title>
            {% endblock %}
        </head>
        <body>
            {% block content %}{% endblock %}
        </body>
    </html>
