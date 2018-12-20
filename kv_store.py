from google.appengine.ext import ndb


class KVEntity(ndb.Expando):
    pass


class KVStore:
    def __init__(self, namespace, user_id):
        self.storage_key = ndb.Key(KVEntity, user_id, namespace=namespace)
        self.entity = KVEntity(key=self.storage_key)

    def write(self, data):
        self.entity.data = data
        self.entity.put()

    def read(self):
        return self.entity.get()

