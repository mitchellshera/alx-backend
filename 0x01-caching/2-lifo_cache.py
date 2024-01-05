#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache inherits from BaseCaching and
    is a caching system using LIFO algorithm
    """

    def __init__(self):
        """ Initialize LIFOCache
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache using LIFO algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Discard the last item put in cache (LIFO)
                discarded_key = list(self.cache_data.keys())[-1]
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache by key
        """
        if key is not None:
            return self.cache_data.get(key)


if __name__ == "__main__":
    lifo_cache = LIFOCache()

    lifo_cache.put("key1", "item1")
    lifo_cache.put("key2", "item2")
    lifo_cache.put("key3", "item3")
    lifo_cache.put("key4", "item4")

    print("Item with key 'key1':", lifo_cache.get("key1"))
    print("Item with key 'key5':", lifo_cache.get("key5"))

    lifo_cache.print_cache()
