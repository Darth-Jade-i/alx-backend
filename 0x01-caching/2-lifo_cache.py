#!/usr/bin/env python3
"""LIFO Caching System Module"""

# Import the parent class BaseCaching from base_caching module
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache defines a caching system that follows
    the LIFO (Last In, First Out) algorithm.
    """

    def __init__(self):
        """
        Initialize the LIFOCache instance by calling
        the parent class BaseCaching's initializer.
        """
        # Call the parent class initializer to set up the cache_data dictionary
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache using LIFO algorithm.
        If the cache exceeds MAX_ITEMS, the last item added
        is discarded.

        Parameters:
        - key: the key under which the item will be stored
        - item: the item to be stored in the cache
        """
        # Check if key and item are not None
        if key is not None and item is not None:
            # Add the item to the cache_data dictionary
            # Assign the item to self.cache_data using the key
            self.cache_data[key] = item

            # Check if the number of items in cache_data size
            # exceeds the MAX_ITEMS limit, maximum allowed
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Get the last key added to the cache before the current one
                last_key = list(self.cache_data.keys())[-2]

                # Discard the last key
                # Remove the last key from the cache
                # to follow LIFO discipline/principle
                del self.cache_data[last_key]

                # Print the discarded key to notify which key was removed
                print("DISCARD: {}".format(last_key))

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
        # Return the value associated with the key or None if key is not found
        return self.cache_data.get(key) if key is not None else None
