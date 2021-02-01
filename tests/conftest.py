import pytest
from flask import Flask
from flask_rings import Rings


@pytest.fixture(autouse=True)
def app():
    app = Flask(__name__)
    app.testing = True
    app.secret_key = "top secret for testing"

    yield app


@pytest.fixture
def rings(app):
    yield Rings(app)


@pytest.fixture
def client(app):
    context = app.test_request_context()
    context.push()

    with app.test_client() as client:
        yield client

    context.pop()
