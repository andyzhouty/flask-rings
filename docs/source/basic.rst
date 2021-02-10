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

Flask-Rings provides a helper for loading the CSS of Rings.
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

Using custom CDN
----------------

You can configure custom CDN by passing arguments to ``rings.load()``

For example:

.. code:: jinja
    {{ rings.load(css_url="https://raw.sevencdn.com/rice0208/Rings/master/rings.min.css") }}

Using local resources
---------------------

You can set the ``RINGS_SERVE_LOCAL`` to ``True`` to use the resources provided by Flask-Rings.

Note that ``RINGS_SERVE_LOCAL`` defaults to ``True`` if you have the flask debugger on.

Using different versions
------------------------

To use different versions of Rings, you can set the ``RINGS_VERSION`` to the version you want.

Available settings
------------------

This table will contain the available settings for Flask-Rings


+-------------------+-----------+----------------------------+
| Setting Name      | Default   | Description                |
+===================+===========+============================+
| RINGS_SERVE_LOCAL | app.debug | Whether Flask-Rings should |
|                   |           | use the local resource.    |
+-------------------+-----------+----------------------------+
| RINGS_VERSION     | 0.2.0     | Which version Flask-Rings  |
|                   |           | should use.                |
+-------------------+-----------+----------------------------+
