#!/usr/bin/env python3
"""
    Create a class MRUCache that inherits from BaseCaching
    and is a caching system:
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """most recent caching algorith"""
    def __init__(self):
        """the initialization overriding the base"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """put kitems in the cache_data"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)

        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = self.order.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
            Must return the value in self.cache_data linked to key.
            If key is None or if the key doesn’t exist in
            self.cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
        return self.cache_data.get(key)
