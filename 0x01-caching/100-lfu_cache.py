#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache inherits from BaseCaching and
    is a caching system using LFU algorithm
    """

    def __init__(self):
        """ Initialize LFUCache
        """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """ Add an item to the cache using LFU algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Find the least frequency used item(s)
                min_frequency = min(self.frequency.values())
                items_to_discard = [k for k, v in self.frequency
                                    .items() if v == min_frequency]

                if len(items_to_discard) > 1:
                    # If more than 1 item to discard, use LRU
                    # algorithm to discard the least recently used
                    lru_key = min(self.frequency, key=lambda
                                  k: self.frequency[k])
                    items_to_discard.remove(lru_key)
                else:
                    lru_key = items_to_discard[0]

                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                print("DISCARD: {}".format(lru_key))

            self.cache_data[key] = item
            self.frequency[key] = 1

    def get(self, key):
        """ Get an item from the cache by key and update frequency
        """
        if key is not None:
            if key in self.cache_data:
                # Update frequency
                self.frequency[key] += 1
                return self.cache_data[key]
        return None


if __name__ == "__main__":
    lfu_cache = LFUCache()

    lfu_cache.put("key1", "item1")
    lfu_cache.put("key2", "item2")
    lfu_cache.put("key3", "item3")
    lfu_cache.put("key4", "item4")

    print("Item with key 'key1':", lfu_cache.get("key1"))
    print("Item with key 'key5':", lfu_cache.get("key5"))

    lfu_cache.print_cache()
