import json
from werkzeug.wrappers import response
from urlshort.app import create_app


def test_shorten(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'URL Shortener' in response.data


def test_redirect_to_url(client):
    response = client.get('/aBc')
    assert response.status_code == 404


def test_get_your_url(client):
    response = client.get('/your-url')
    assert response.status_code == 302
    assert b'You should be redirected automatically to target URL' in response.data


def test_api(client):
    response = client.get('/api')
    assert response.status_code == 200
    assert b'[]\n' in response.data


def test_healthz(client):
    response = client.get('/_status/healthz')
    assert response.status_code == 200
    assert b'{"status":"OK"}\n' == response.data
