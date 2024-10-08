#!/usr/bin/env python3
"""
This module implements a basic caching
system that inherits from BaseCaching.
BasicCache is a caching system
that inherits from BaseCaching.
This cache has no size limit and
allows for storing and retrieving items.
"""

# BaseCaching = __import__('base_caching').BaseCaching
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching.
    This is a basic caching system with no size limit.
    """
    def __init__(self):
        """
        _summary_
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds an item in/to the cache. (Puts, sets, updates)
        Args:
            key (str): the key under which to store the item.
            item (Any): the item to store in the cache.
        Returns:
            None
        """
        # Check if both key and item are not None
        if key is not None and item is not None:
            # Store the item in the cache dictionary with the provided key
            self.cache_data[key] = item

        # Check if both key and item are None
        # if key is None or item is None:
            # method should not do anything
            # pass
        # Store the item in the cache dictionary with the provided key
        # self.cache_data[key] = item

    def get(self, key):
        """
        Gets/Retrieves an item from the cache by key.
        Args:
            key (str): the key corresponding to or of the item to retrieve.
        Returns:
            (Any): The value in self.cache_data linked to key,
            or None if key is None or doesn't exist in the cache.
            Basically, the item if found, otherwise None.
        """
        # return self.cache_data.get(key, None)

        # Check if the key is not None and exists in the cache
        # if key is not None or key in self.cache_data.keys():
        #     Return the item associated with the key,
        #     return self.cache_data.get(key)
        # or Return None if key doesn't exist
        # return None

        # `key not in self.cache_data:` faster and more efficient
        # than `key not in self.cache_data.keys():` because it is a
        # better optimized operation for dictionaries as it directly checks
        # for the existence of key in the dictionary
        # `key not in self.cache_data.keys():` creates a view of all keys
        # and then checks for membership, which is redundant and slower

        # if key is None or key not in self.cache_data:
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data.get(key)

# Hints:
# how does python handle the .get() method when passed two arguments
# Python's get() Method with Two Arguments
# The get() method on a dictionary in Python takes two arguments:
# key: The key you're looking for in the dictionary.
# default (optional): The value to return if the key is not found.
# How it works:
# If the key exists in the dictionary, its corresponding value is returned.
# If the key doesn't exist, the provided default value is returned.
# If no default is specified, None is returned.
# Key points:
# The get() method is safer than direct indexing (my_dict['key'])
# because it avoids `KeyError` exceptions.
# The default argument provides flexibility in handling missing keys.
# So, the get() method is a convenient way to retrieve values from a dictionary
# while gracefully handling cases where the key might not be present.
