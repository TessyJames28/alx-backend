#!/usr/bin/env python3
"""LIFO caching"""
Base = __import__('base_caching').BaseCaching


class LIFOCache(Base):
    """LIFO Cache implementation"""

    def __init__(self):
        """initialise the init class"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """method that puts the key-value pairs in the FIFO algo"""
        if key is not None and item is not None and key not in self.cache_data:
            if len(self.cache_data) >= Base.MAX_ITEMS:
                last_item = self.stack.pop()
                self.cache_data.pop(last_item)
                print("DISCARD: {}".format(last_item))
        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        """get the values in the FIFO algorithm"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
