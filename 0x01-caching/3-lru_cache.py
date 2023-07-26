#!/usr/bin/env python3
"""LRU caching"""
Base = __import__('base_caching').BaseCaching


class LRUCache(Base):
    """LRU Cache implementation"""

    def __init__(self):
        """initialise the init class"""
        super().__init__()
        self.accessed_items = []

    def put(self, key, item):
        """method that puts the key-value pairs in the FIFO algo"""
        if key is not None and item is not None:
            if len(self.cache_data) >= Base.MAX_ITEMS and key not in self.cache_data:  # nopep8
                lru_item = self.accessed_items.pop(0)
                self.cache_data.pop(lru_item)
                print("DISCARD: {}".format(lru_item))

        if key in self.cache_data:
            self.accessed_items.remove(key)

        self.cache_data[key] = item
        self.accessed_items.append(key)

    def get(self, key):
        """get the values in the FIFO algorithm"""
        if key is not None and key in self.cache_data:
            self.accessed_items.remove(key)
            self.accessed_items.append(key)
            return self.cache_data[key]
        return None
