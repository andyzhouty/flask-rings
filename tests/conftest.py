import pytest
from flask import Flask
from flask_rings import Rings
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(1, 20)])
    password = PasswordField("Password", validators=[DataRequired(), Length(8, 150)])
    remember = BooleanField("Remember me")
    submit = SubmitField()


@pytest.fixture
def hello_form():
    return HelloForm


@pytest.fixture(autouse=True)
def app():
    app = Flask(__name__)
    app.testing = True
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
