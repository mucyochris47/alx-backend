#!/usr/bin/env python3
"""
    class LRUCache that inherits from BaseCaching
    and is a caching system:
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """the least recently used caching"""
    def __init__(self):
        """ the initialization overiding base"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """put an item in lru cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
            Must return the value in self.cache_data linked to key.
            If key is None or if the key doesn’t exist in
            self.cache_data, return None.
        """
        if key not in self.cache_data:
            return None
        if key in self.order:
            self.order.remove(key)
            self.order.append(key)
        return self.cache_data.get(key)
