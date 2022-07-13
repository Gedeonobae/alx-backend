#!/usr/bin/python3
''' MRU Caching
'''

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    ''' Implements the MRU caching algorithm '''
    def __init__(self):
        ''' Initializes the class instance. '''
        super().__init__()
        self.keys = []

    def put(self, key, item):
        ''' Adds an item to the dictionary'''
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(-2)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        ''' Return item stored by the key else returns None.'''
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            return self.cache_data[key]
        return None
