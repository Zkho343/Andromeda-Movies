import pytest
from flask import session


def test_register(client):
    response_code = client.get('/auth/register').status_code
    assert response_code == 200


def test_logout(client, auth):
    auth.login()
    with client:
        auth.logout()
        assert 'user_id' not in session


def test_login_required_to_comment(client):
    response = client.post('/review')
    assert response.headers['Location'] == 'http://localhost/auth/login'


def test_review(client, auth):
    auth.login()


def test_remove(client, auth):
    auth.login()
