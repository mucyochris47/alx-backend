#!/usr/bin/env python3
"""
    Create a class LIFOCache that inherits
    from BaseCaching and is a caching system:
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """a lif0 caching class"""
    def __init__(self):
        """the initialization method"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ put an item in cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.order.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
            Must return the value in self.cache_data
            linked to key.
            If key is None or if the key doesn’t exist
            in self.cache_data, return None.
        """
        if key is None:
            return None

        if key not in self.cache_data:
            return None

        return self.cache_data.get(key)
