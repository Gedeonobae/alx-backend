#!/usr/bin/env python3
"""
Implements caching
"""

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """implements the LIFO caching algorithm"""
    def __init__(self):
        super().__init__()
        self.last_key = ""

    def put(self, key, item):
        """ Adds an item to the dictinary"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.last_key))
                self.cache_data.pop(self.last_key)
            self.last_key = key

    def get(self, key):
        """accesses a dictinary item using a key and
           returns it if it exists
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
