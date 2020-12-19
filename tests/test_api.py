import sys
sys.path.append(".")

import pytest

from api.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.app_context():
        client = app.test_client()
        yield client


def test_home(client):
    resp = client.get('/',)
    assert resp.status_code == 200


def test_short_url(client):
    resp = client.put('/short_url?url=https://teaches.cc/',)
    assert resp.status_code == 405
    resp = client.get('/short_url?url=123',)
    assert resp.status_code == 400
    resp = client.get('/short_url?url=https://teaches.cc/',)
    assert resp.status_code == 200
    data = resp.data
    url = eval(data.decode('utf8'))['short_url']
    resp = client.get(url, )
    assert resp.status_code == 302
    resp = client.get('/short_url?url=https://teaches.cc/',)
    assert resp.data == data