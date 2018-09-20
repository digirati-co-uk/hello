import json


def test_ping_pong(app):
    """
    Test ping pong
    :param app: Flask applicaiton
    """
    client = app.test_client()

    get_response = client.get(f'/ping/')
    assert get_response.status_code == 200
    assert get_response.data.decode() == "pong"


def test_ping_status(app):
    """
    Test ping status
    :param app: Flask applicaiton
    """
    client = app.test_client()

    get_response = client.get(f'/ping/status')
    assert get_response.status_code == 200
    response_data = json.loads(get_response.data.decode())
    assert response_data.get('status') == "GOOD"
