import pytest
from flask import Flask
from app import db, create_app
from config import TestConfig
import json


@pytest.fixture(name="app")
def application() -> Flask:
    """
    Flask application fixture
    :return: flask application fixture
    """
    app = create_app(TestConfig)
    with app.app_context():
        db.drop_all()
        db.create_all()
        yield app


def test_add_retrieve(app):
    """
    Test adding a blob
    :param app: Flask applicaiton
    """
    data = {
        'payload': 'test payload'
    }
    client = app.test_client()

    post_response = client.post('/blob/blobs/', data=json.dumps(data), content_type='application/json')
    assert post_response.status_code == 201

