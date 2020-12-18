import sys
sys.path.append(".")

import pytest

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.app_context():
        client = app.test_client()
        yield client


def test_get_home(client):
    resp = client.get(
            '/',
    )
    assert resp.status_code == 200

