import falcon
from tests import client

def test_status(client):
    response = 'Everything is fine!'
    result = client.simulate_get('/v1/status')

    assert result.json['response'] == response and result.status_code == 200