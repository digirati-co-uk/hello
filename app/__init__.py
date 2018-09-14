from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)

    from app.ping import bp as ping_bp
    app.register_blueprint(ping_bp, url_prefix="/ping")
    from app.blob import bp as blob_bp
    app.register_blueprint(blob_bp, url_prefix="/blob")

    return app
