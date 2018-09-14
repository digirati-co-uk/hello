from app import db


class JsonBlob(db.Model):

    blob_id = db.Column(db.CHAR(36), primary_key=True)
    payload = db.Column(db.Text())

    def __repr__(self) -> str:
        return "<JsonBlob {blob_id}".format(blob_id=self.blob_id)

    def to_dict(self):
        data = {
            'blob_id': self.blob_id,
            'payload': self.payload,
        }
        return data
