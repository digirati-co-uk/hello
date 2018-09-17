from app.models.blob import JsonBlob
from app import db
from sqlalchemy.orm.exc import NoResultFound


def test_add_get_blob(app):
    """
    test adding and retrieving a blob
    """

    test_payloads = (
        "payload 1",
        "payload 2",
        "payload 3"
    )

    for payload in test_payloads:
        blob = JsonBlob.add(payload)
        assert str(blob) == f"<JsonBlob {blob.blob_id}>"
