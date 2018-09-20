from flask import Blueprint, jsonify, request, url_for
from app.database import DB
from app.blob.errors import bad_request
from app.models.blob import JsonBlob

BP = Blueprint('blob', __name__)


@BP.route('/blobs/<string:blob_id>', methods=['GET'])
def get_blob(blob_id):
    return jsonify(JsonBlob.query.get_or_404(blob_id).to_dict())


@BP.route('/blobs', methods=['GET'])
def get_blobs():

    data = [item.to_dict() for item in JsonBlob.query.all()]
    return jsonify(data)


@BP.route('/blobs', methods=['POST'])
def create_blob():
    data = request.get_json() or {}
    if 'payload' not in data:
        return bad_request('must include payload field')

    blob = JsonBlob.add(data['payload'])
    response = jsonify(blob.to_dict())
    response.headers['Location'] = url_for('blob.get_blob', blob_id=blob.blob_id)
    return response, 201


@BP.route('/blobs/<string:blob_id>', methods=['DELETE'])
def delete_blob(blob_id):
    blob = JsonBlob.query.get_or_404(blob_id)
    DB.session.delete(blob)
    DB.session.commit()
    return '', 204
