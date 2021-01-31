import pytest
from flask import Flask
from flask_rings import Rings


@pytest.fixture(autouse=True)
def app():
    app = Flask(__name__)
    app.testing = True
    # Ignore warnings from flask_sqlalchemy
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = "top secret for testing"

    yield app


@pytest.fixture(autouse=True)
def rings(app):
    yield Rings(app)


@pytest.fixture
def client(app):
    context = app.test_request_context()
    context.push()

    with app.test_client() as client:
        yield client

    context.pop()
