from google.appengine.ext import ndb


class AliciaEntity(ndb.Expando):
    pass


class KVStore:
    def __init__(self, namespace, user_id):
        self.storage_key = ndb.Key(AliciaEntity, user_id, namespace=namespace)
        self.entity = AliciaEntity(key=self.storage_key)

    def write(self, data):
        for key, value in data.iteritems():
            setattr(self.entity, key, value)
        self.entity.put()

    def read(self):
        return self.entity.get()

    def query_by_key(self, key):
        return self.entity.query(self.entity.key == key)

