#!/usr/bin/env python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache by key
        """
        if key is not None:
            return self.cache_data.get(key)


if __name__ == "__main__":
    basic_cache = BasicCache()

    basic_cache.put("key1", "item1")
    basic_cache.put("key2", "item2")
    basic_cache.put("key3", "item3")

    print("Item with key 'key1':", basic_cache.get("key1"))
    print("Item with key 'key4':", basic_cache.get("key4"))

    basic_cache.print_cache()
