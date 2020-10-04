import flask
import pytest

from flask.testing import FlaskClient

from app.flask import create_app


@pytest.fixture
def app() -> flask.Flask:
    app = create_app()

    with app.app_context():
        yield app


@pytest.fixture
def client(app) -> FlaskClient:
    with app.test_client() as client:
        yield client


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
