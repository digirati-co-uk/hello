from app.ping import bp
from flask import jsonify


@bp.route('/')
def index():
    return "pong"


@bp.route('/status')
def status():
    status_update = {
        "status": "GOOD",
        "message": "Everything is working normally"
    }
    return jsonify(status_update)
