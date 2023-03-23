import json
from conftest import client

def test_get_countries(client):
    response = client.get('/weo/countries')
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    assert isinstance(data, list)
    assert len(data) > 0
    for entry in data:
        assert isinstance(entry, dict)
        assert 'country' in entry
        assert 'country_id' in entry
        assert set(entry.keys()) == {'country', 'country_id'}