from conftest import client
import pytest
from sqlalchemy.sql import text

def test_database_connection(client):
    try:
        with client.application.app_context():
            from database import db
            db.session.execute(text('SELECT 1'))
    except Exception as e:
        pytest.fail(f"Could not connect to database: {e}")

def test_get_resource(client):
    response = client.get('/')
    print(response.json)
    assert response.status_code == 200
    assert response.data == b"Hello, World!"

def test_get_nonexistent_resource(client):
    response = client.get('/nonexistent-resource')
    assert response.status_code == 404
    assert response.json == {'error': 'Not Found'}