#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache inherits from BaseCaching and
    is a caching system using MRU algorithm
    """

    def __init__(self):
        """ Initialize MRUCache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache using MRU algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Discard the most recently used item (MRU)
                mru_key = self.order.pop()
                del self.cache_data[mru_key]
                print("DISCARD: {}".format(mru_key))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item from the cache by key and update access order
        """
        if key is not None:
            if key in self.cache_data:
                # Update access order
                self.order.remove(key)
                self.order.append(key)
                return self.cache_data[key]
        return None


if __name__ == "__main__":
    mru_cache = MRUCache()

    mru_cache.put("key1", "item1")
    mru_cache.put("key2", "item2")
    mru_cache.put("key3", "item3")
    mru_cache.put("key4", "item4")

    print("Item with key 'key1':", mru_cache.get("key1"))
    print("Item with key 'key5':", mru_cache.get("key5"))

    mru_cache.print_cache()
