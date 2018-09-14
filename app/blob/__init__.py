from flask import Blueprint

bp = Blueprint('blob', __name__)

from app.blob import routes
