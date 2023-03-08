import pytest
from app import create_app
from database import db

@pytest.fixture
def app():
    app = create_app()
    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.session.remove()

@pytest.fixture
def client(app):
    return app.test_client()