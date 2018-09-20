from flask import Blueprint, jsonify

BP = Blueprint('ping', __name__)


@BP.route('/')
def index():
    return "pong"


@BP.route('/status')
def status():
    status_update = {
        "status": "GOOD",
        "message": "Everything is working normally"
    }
    return jsonify(status_update)
