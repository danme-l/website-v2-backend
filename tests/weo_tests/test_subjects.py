import json
from conftest import client

def test_get_subjects(client):
    response = client.get('/weo/subjects')
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    assert isinstance(data, list)
    assert len(data) > 0

def test_subjects_contents(client):
    response = client.get('/weo/subjects')
    data = json.loads(response.get_data(as_text=True))
    for entry in data:
        assert isinstance(entry, dict)
        assert 'descriptor' in entry
        assert 'notes' in entry
        assert 'scale' in entry
        assert 'subject_id' in entry
        assert 'units' in entry
        assert set(entry.keys()) == {'descriptor', 'notes', 'scale','subject_id', 'units'}