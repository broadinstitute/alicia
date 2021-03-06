import logging
from kv_store import KVStore, AliciaEntity


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

    @classmethod
    def get_all_pairs(cls, user_id, namespace="default"):
        kv_store = KVStore(namespace, user_id)
        kv_store_attrs = kv_store.read()
        if not kv_store_attrs:
            return {}
        else:
            pairs = kv_store_attrs.__dict__.get('_values')
            return {k: getattr(kv_store_attrs, k) for k in pairs.keys()}

    @classmethod
    def get_single_pair(cls, all_pairs, key):
        return all_pairs.get(key)

    @classmethod
    def delete_key(cls, user_id, key, namespace="default"):
        kv_store = KVStore(namespace, user_id)
        kv_store.delete_key(key)

    @classmethod
    def get_all_items(cls, namespace="default"):
        pass

