#!/usr/bin/env python3
"""
FIFO caching
"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """implements the FIFO caching algorithm"""
    def __init__(self):
        super().__init__()
        self._keys = []

    def put(self, key, item):
        """Adds an item to the dictionary"""
        if key and item:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
                if key not in self.cache_data.keys():
                    print("DISCARD: {}".format(self._keys[0]))
                    self.cache_data.pop(self._keys[0])
                    self._keys.pop(0)
            self.cache_data[key] = item
            if key not in self._keys:
                self._keys.append(key)

    def get(self, key):
        """accesses a dictinary item using a key and
           returns it if it exists
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
