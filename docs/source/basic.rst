Basic Usage
===========

Installation
------------

You can only install flask-rings by using git:

.. code:: bash

    $ pip install git+https://github.com/ringsings/flask-rings.git

or PYPI

.. code:: bash

    $ pip install flask-rings

Initialization
--------------

.. code:: python

    from flask_rings import Rings
    from flask import Flask

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
-----------------

Flask-Rings a helper for loading the CSS of Rings.
Call it in your base template, for example:

.. code-block:: jinja

    <head>
        ...
        {{ rings.load() }}
    </head>
