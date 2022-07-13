#!/usr/bin/python3
''' LRU Caching module.
'''

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    ''' LRU caching algorithm.
    '''

    def __init__(self):
        ''' Initializes the class instance. '''
        super().__init__()
        self.keys = []

    def put(self, key, item):
        ''' Add an item to a dictionary '''
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        ''' Returns a dictionary item with the given key'''
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            return self.cache_data[key]
        return None
