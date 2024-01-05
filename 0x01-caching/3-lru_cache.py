#!/usr/bin/env python3
""" LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache inherits from BaseCaching and
    is a caching system using LRU algorithm
    """

    def __init__(self):
        """ Initialize LRUCache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache using LRU algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Discard the least recently used item (LRU)
                lru_key = self.order.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD: {}".format(lru_key))
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
    lru_cache = LRUCache()

    lru_cache.put("key1", "item1")
    lru_cache.put("key2", "item2")
    lru_cache.put("key3", "item3")
    lru_cache.put("key4", "item4")

    print("Item with key 'key1':", lru_cache.get("key1"))
    print("Item with key 'key5':", lru_cache.get("key5"))

    lru_cache.print_cache()
