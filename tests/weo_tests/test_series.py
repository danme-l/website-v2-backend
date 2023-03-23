import json
from conftest import client

def test_get_series_for_country_and_subject(client):
    response = client.get('/weo/series?countryId=156CAN&subjectId=NGDP_RPCH')
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    print(data[0:5])
    assert isinstance(data, list)
    assert len(data) > 0
    assert data[0]['country_id'] == '156CAN'
    assert data[0]['subject_id'] == 'NGDP_RPCH'

def test_value_is_numeric(client):
    response = client.get('/weo/series?countryId=156CAN&subjectId=NGDP_RPCH')
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    values = [data[x]['value'] for x in range(len(data))]
    assert all(isinstance(v, float) for v in values)