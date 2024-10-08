#!/usr/bin/env python3
"""
This module implements a FIFO caching
system that inherits from BaseCaching.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache is a caching system that inherits from BaseCaching.
    This cache operates on a First In, First Out (FIFO) basis.
    """

    def __init__(self):
        """
        Initialize the class instance and call the parent class initializer.
        """
        # Call the initializer of the parent class
        # to set up the cache_data dictionary
        super().__init__()
        # Initialize a list to keep track of
        # the order of insertion (FIFO order)
        self.order = []

    def put(self, key, item):
        """
        Adds an item to the cache, following the FIFO algorithm.

        Args:
            key (str): The key under which the item should be stored.
            item (any): The item to be stored in the cache.

        Returns:
            None
        """
        # Check if both key and item are not None
        if key is not None and item is not None:
            # If the key already exists in the cache,
            # remove it from the order list
            if key in self.cache_data:
                self.order.remove(key)
            # Add the key to the order list
            # (it will be the most recent one)
            self.order.append(key)
            # Store the item in the cache dictionary with the provided key
            self.cache_data[key] = item

            # Check if the number of items in the cache exceeds the max limit
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Identify the first item (FIFO) to be discarded
                discarded_key = self.order.pop(0)
                # Remove the discarded item from the cache
                del self.cache_data[discarded_key]
                # Print the key of the discarded item
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        Retrieves an item from the cache by key.

        Args:
            key (str): The key corresponding to the item to retrieve.

        Returns:
            any: The item if found, otherwise None.
        """
        # Check if the key is not None and exists in the cache
        if key is not None:
            # Return the item associated with the key,
            # or None if key doesn't exist
            return self.cache_data.get(key)
        return None
