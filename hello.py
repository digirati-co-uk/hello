from app import create_app, DB
from app.models.blob import JsonBlob
app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': DB, 'JsonBlob': JsonBlob}
