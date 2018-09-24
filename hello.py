from app import create_app, DB
from app.models.blob import JsonBlob
application = create_app()


@application.shell_context_processor
def make_shell_context():
    return {'db': DB, 'JsonBlob': JsonBlob}
