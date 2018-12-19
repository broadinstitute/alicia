from google.cloud import firestore
import google


class KVStore:
    def __init__(self, namespace, id):
        db = firestore.Client()
        self.doc_ref = db.collection(namespace).document(id)

    def overwrite(self, data):
        """Overwrites the document with the provided data"""
        self.doc_ref.set(data)

    def update(self, data):
        """Update the fields provided in data without overwriting the entire document"""
        self.doc_ref.update(data)

    def read(self):
        try:
            return self.doc_ref.get()
        except google.cloud.exceptions.NotFound:
            print(u'No such document!')

