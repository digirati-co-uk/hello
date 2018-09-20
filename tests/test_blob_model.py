import pytest
from app.models.blob import JsonBlob


@pytest.mark.usefixtures('app')
def test_add_get_blob():
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
