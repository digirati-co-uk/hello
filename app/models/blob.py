from uuid import uuid4
from app.database import DB


class JsonBlob(DB.Model):

    blob_id = DB.Column(DB.CHAR(36), primary_key=True)
    payload = DB.Column(DB.Text())

    def __repr__(self) -> str:
        return "<JsonBlob {blob_id}>".format(blob_id=self.blob_id)

    @staticmethod
    def add(payload):

        blob = JsonBlob(blob_id=str(uuid4()), payload=payload)
        DB.session.add(blob)
        DB.session.commit()
        return blob

    def to_dict(self):
        data = {
            'blob_id': self.blob_id,
            'payload': self.payload,
        }
        return data
