from flask import Flask
from flask_migrate import Migrate
from config import Config
from app.database import DB

MIGRATE = Migrate()


def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)
    DB.init_app(app)
    MIGRATE.init_app(app, DB)

    from app.ping.routes import BP as PING_BP
    app.register_blueprint(PING_BP, url_prefix="/ping")
    from app.blob.routes import BP as BLOB_BP
    app.register_blueprint(BLOB_BP, url_prefix="/blob")

    return app
