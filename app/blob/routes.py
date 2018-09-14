from flask import jsonify, request, url_for
from uuid import uuid4
from app import db
from app.blob import bp
from app.blob.errors import bad_request
from app.models.blob import JsonBlob


@bp.route('/blobs/<string:blob_id>', methods=['GET'])
def get_blob(blob_id):
    return jsonify(JsonBlob.query.get_or_404(blob_id).to_dict())


@bp.route('/blobs', methods=['GET'])
def get_blobs():

    data = [item.to_dict() for item in JsonBlob.query.all()]
    return jsonify(data)


@bp.route('/blobs/', methods=['POST'])
def create_blob():
    data = request.get_json() or {}
    if 'payload' not in data:
        return bad_request('must include payload field')

    blob = JsonBlob(blob_id=str(uuid4()), payload=data['payload'])
    db.session.add(blob)
    db.session.commit()
    response = jsonify(blob.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('blob.get_blob', blob_id=blob.blob_id)
    return response, 201
