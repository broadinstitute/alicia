import logging
from kv_store import KVStore


class Alicia:
    def __init__(self):
        pass

    @classmethod
    def add_pair(cls, user_id, key_value_pairs, namespace="default"):
        kv_store = KVStore(namespace, user_id)
        data = Alicia.key_value_pairs_to_dict(key_value_pairs)
        kv_store.write(data)

    @classmethod
    def key_value_pairs_to_dict(cls, key_value_pairs):
        new_dict = {}
        for kv_pair in key_value_pairs:
            new_dict[kv_pair.key] = kv_pair.value
        return new_dict
