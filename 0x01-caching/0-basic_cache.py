#!/usr/bin/env python3
"""Basic Dictionary"""
Base = __import__('base_caching').BaseCaching


class BasicCache(Base):
    """basic dictionary"""

    def put(self, key, item):
        """method that put a new key-value pair to the dictionary"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """method used to get value from the dictionary"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
