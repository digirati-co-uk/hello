from app import db
from uuid import uuid4


class JsonBlob(db.Model):

    blob_id = db.Column(db.CHAR(36), primary_key=True)
    payload = db.Column(db.Text())

    def __repr__(self) -> str:
        return "<JsonBlob {blob_id}>".format(blob_id=self.blob_id)

    @staticmethod
    def add(payload):

        blob = JsonBlob(blob_id=str(uuid4()), payload=payload)
        db.session.add(blob)
        db.session.commit()
        return blob

    def to_dict(self):
        data = {
            'blob_id': self.blob_id,
            'payload': self.payload,
        }
        return data
