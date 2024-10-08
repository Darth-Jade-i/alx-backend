#!/usr/bin/env python3
"""
MRU Caching System Module
"""

# Import the parent class BaseCaching
# from the base_caching module
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache defines a caching system that follows
    the MRU (Most Recently Used) algorithm.
    """

    def __init__(self):
        """
        Initialize the MRUCache instance by calling
        the parent class BaseCaching's initializer.
        """
        # Call the parent class initializer to
        # set up the cache_data dictionary
        super().__init__()

        # Initialize an empty list to keep
        # track of the access order of keys
        self.access_order = []

    def put(self, key, item):
        """
        Add an item in the cache using MRU algorithm.
        If the cache exceeds MAX_ITEMS,
        the most recently used item is discarded.

        Parameters:
        - key: the key under which the item will be stored
        - item: the item to be stored in the cache
        """
        # Check if both key and item are not None
        if key is not None and item is not None:
            # Check if the key already exists in cache_data
            if key in self.cache_data:
                # Remove the key from access_order to update its position
                self.access_order.remove(key)
            # Add the key to the end of the
            # access_order list (most recently used)
            self.access_order.append(key)

            # Assign the item to self.cache_data using the key
            self.cache_data[key] = item

            # Check if the number of items in
            # cache_data exceeds the maximum allowed
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Identify the most recently used key
                # (the last key in access_order)
                mru_key = self.access_order.pop(-2)

                # Remove the most recently used key from the cache_data
                del self.cache_data[mru_key]

                # Print the discarded key to notify which key was removed
                print("DISCARD: {}".format(mru_key))

    def get(self, key):
        """
        Retrieve an item by key from the cache.
        If the key is None or does not exist, return None.

        Parameters:
        - key: the key to look up in the cache

        Returns:
        - The value associated with the key if it exists in the cache
        - None if the key is None or doesn't exist in the cache
        """
        # Check if the key is not None and exists in cache_data
        if key is not None and key in self.cache_data:
            # Remove the key from access_order to update its position
            self.access_order.remove(key)
            # Add the key to the end of the
            # access_order list (most recently used)
            self.access_order.append(key)
            # Return the value associated with the key from self.cache_data
            return self.cache_data.get(key)

        # Return None if key is None or doesn't exist in cache_data
        return None
