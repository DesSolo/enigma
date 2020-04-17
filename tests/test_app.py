import pytest
import requests
import config

address = 'http://127.0.0.1:8000'


@pytest.fixture()
def client():
    return requests.Session()


@pytest.mark.parametrize(
    'uri, status_code',
    [
        ('/', 200),
        ('/' * 20, 404),
        ('/NotRegistered', 404),
    ]
)
def test_pages(client, uri, status_code):
    response = client.get(address + uri)
    assert response.status_code == status_code


@pytest.fixture()
def response_message(client):
    message = 'test_message'
    data = {
        'msg': message,
        'due': 1
    }
    response = client.post(address + '/', data=data)
    return response


def test_add_message(response_message):
    assert response_message.status_code == 200


def test_response_not_empty(response_message):
    assert response_message.text != ''


def test_valid_config(response_message):
    response_body = response_message.text
    assert config.PROTOCOL in response_body
    assert len(response_body.split('/')[-1]) == config.TOKEN_BYTES * 2


def test_get_message(client, response_message):
    response = client.get(response_message.text)
    assert response.status_code == 200
    assert 'test_message' in response.text


@pytest.mark.parametrize(
    'user_agent',
    config.DENY_USER_AGENTS
)
def test_user_agents(client, user_agent, response_message):
    headers = {'User-Agent': user_agent}
    response_index = client.get(address + '/', headers=headers)
    assert response_index.status_code == 200
    response_secret = client.get(response_message.text, headers=headers)
    assert response_secret.status_code == 403


def test_expire_message(client, response_message):
    response_fits_time = client.get(response_message.text)
    assert response_fits_time.status_code == 200
    response_second = client.get(response_message.text)
    assert response_second.status_code == 404


@pytest.mark.parametrize(
    'msg, due, status_code',
    [
        ('test', -10, 405),
        ('test', 0, 405),
        ('test', 5, 405),
        ('', 1, 405),
    ] + [('test', i, 200) for i in config.DAYS_RANGE]
)
def test_post_params(client, msg, due, status_code):
    data = {
        'msg': msg,
        'due': due
    }
    response = client.post(address + '/', data=data)
    assert response.status_code == status_code
