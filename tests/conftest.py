import pytest
from flask import Flask
from app import DB, create_app
from config import TestConfig


@pytest.fixture(name="app")
def application() -> Flask:
    """
    Flask application fixture
    :return: flask application fixture
    """
    app = create_app(TestConfig)
    with app.app_context():
        DB.drop_all()
        DB.create_all()
        yield app
