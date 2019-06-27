from falcon import testing
import pytest
from app.main import app

@pytest.fixture()
def client():
    # Assume the hypothetical `myapp` package has a function called
    # `create()` to initialize and return a `falcon.API` instance.
    return testing.TestClient(app)

def test_status(client):
    response = 'Everything is fine!'

    result = client.simulate_get('/v1/status')
    assert result.json['response'] == response
