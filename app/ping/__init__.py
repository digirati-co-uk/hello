from flask import Blueprint

bp = Blueprint('ping', __name__)

from app.ping import routes
