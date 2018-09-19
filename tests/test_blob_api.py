import json


def test_add_retrieve(app):
    """
    Test adding a blob
    :param app: Flask applicaiton
    """
    data = {
        'payload': 'test payload'
    }
    client = app.test_client()

    post_response = client.post('/blob/blobs', data=json.dumps(data), content_type='application/json')
    assert post_response.status_code == 201
    blob_id = json.loads(post_response.data.decode()).get('blob_id')

    get_response = client.get(f'/blob/blobs/{blob_id}')
    assert get_response.status_code == 200
    response_payload = json.loads(get_response.data.decode()).get('payload')
    assert response_payload == data['payload']


def test_get_all(app):
    """
    Test getting multiple blobs
    :param app: Flask applicaiton
    """

    data = [
        {
            'payload': 'test payload'
        },
        {
            'payload': 'second payload'
        },
        {
            'payload': 'third payload'
        }
    ]
    client = app.test_client()

    for blob in data:
        post_response = client.post('/blob/blobs', data=json.dumps(blob), content_type='application/json')
        assert post_response.status_code == 201
        blob_id = json.loads(post_response.data.decode()).get('blob_id')
        blob['blob_id'] = blob_id

    get_response = client.get(f'/blob/blobs')
    assert get_response.status_code == 200
    response_data = json.loads(get_response.data.decode())
    assert(response_data == data)


def test_missing_payload(app):
    """
    Test adding a blob without a payload
    :param app: Flask applicaiton
    """
    data = {
        # empty!
    }
    client = app.test_client()

    post_response = client.post('/blob/blobs', data=json.dumps(data), content_type='application/json')
    assert post_response.status_code == 400


def test_delete(app):
    """
    Test deleting a blob 
    :param app: Flask applicaiton
    """
    data = {
        'payload': 'test payload'
    }
    client = app.test_client()

    post_response = client.post('/blob/blobs', data=json.dumps(data), content_type='application/json')
    assert post_response.status_code == 201
    blob_id = json.loads(post_response.data.decode()).get('blob_id')

    get_response = client.get(f'/blob/blobs/{blob_id}')
    assert get_response.status_code == 200
    response_payload = json.loads(get_response.data.decode()).get('payload')
    assert response_payload == data['payload']

    delete_rsponse = client.delete(f'/blob/blobs/{blob_id}')
    assert delete_rsponse.status_code == 204

    reget_response = client.get(f'/blob/blobs/{blob_id}')
    assert reget_response.status_code == 404


