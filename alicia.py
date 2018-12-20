import logging
# from kv_store import KVStore


class Alicia:
    def __init__(self):
        pass

    def add_pair(self, user_id, key_value_pairs, namespace="default"):
        # kv_store = KVStore(namespace, user_id)
        data = Alicia.key_value_pairs_to_dict(key_value_pairs)
        logging.info("Data is: %s" % data)

    @classmethod
    def key_value_pairs_to_dict(cls, key_value_pairs):
        new_dict = {}
        for kv_pair in key_value_pairs:
            new_dict[kv_pair.key] = kv_pair.value
        return new_dict
