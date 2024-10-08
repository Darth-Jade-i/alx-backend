#!/usr/bin/python3
""" LFU Caching System """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU Cache system class that
    inherits from `BaseCaching` """

    def __init__(self):
        """ Initialize the `LFUCache` instance """
        # Call the parent class's `init` method
        super().__init__()
        # Dictionary to track usage frequency of each key
        self.usage_frequency = {}
        # List to maintain the order of `LRU` within same frequency
        self.lru_order = []

    def put(self, key, item):
        """
        Assign the `item` value to the dictionary
        `self.cache_data` for the `key` 'key'.
        If the `cache` exceeds its `limit`,
        discard the least frequently used `item`.
        """
        # If `key` or `item` is `None`, do nothing
        if key is None or item is None:
            return

        if key in self.cache_data:
            # If the `key` is already in the `cache`,
            # update the `item` and increase its `frequency`
            self.cache_data[key] = item
            self.usage_frequency[key] += 1
            # Remove and re-append to update `LRU` order
            self.lru_order.remove(key)
            self.lru_order.append(key)
        else:
            # If the `key` is not in the `cache`
            # and the `cache` is `full`
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used `keys`
                min_freq = min(self.usage_frequency.values())
                # This list comprehension creates a list of keys
                # (`lfu_keys`) that have the minimum usage `frequency`
                # in the `self.usage_frequency` dictionary.
                # lfu_keys = [k for k, v in self.usage_frequency
                #             .items() if v == min_freq]
                # Initialize an empty list to store the `LFU` keys
                lfu_keys = []
                # Iterate over each `key-value` pair in the dictionary
                for k, v in self.usage_frequency.items():
                    # Check if the `frequency` of the
                    # current key is equal to `min_freq`
                    if v == min_freq:
                        # If yes, add the key to the `lfu_keys` list
                        lfu_keys.append(k)

                # Find the least recently used among
                # the least frequently used `keys`
                # This generator expression finds the first key in
                # `self.lru_order` that is also present in `lfu_keys`.
                # This key is the least recently used (LRU) key
                # among the least frequently used (LFU) keys.
                # lru_lfu_key = next(k for k in self.
                #                    lru_order if k in lfu_keys)
                # Initialize a variable to store the LRU LFU key
                lru_lfu_key = None
                # Iterate over each key in the LRU order list
                for k in self.lru_order:
                    # Check if the current key is also in the LFU keys list
                    if k in lfu_keys:
                        # If yes, assign this key to lru_lfu_key
                        lru_lfu_key = k
                        # Stop the loop since we've
                        # found the first matching key
                        break

                # Discard the `LRU` `key` among `LFU` `keys`
                del self.cache_data[lru_lfu_key]
                del self.usage_frequency[lru_lfu_key]
                self.lru_order.remove(lru_lfu_key)
                print(f"DISCARD: {lru_lfu_key}")

            # Add the new `key-item` pair to the `cache`
            self.cache_data[key] = item
            self.usage_frequency[key] = 1  # Set `frequency` to 1
            self.lru_order.append(key)  # Add to `LRU` order

    def get(self, key):
        """
        Retrieve the `value` associated
        with the `key` from the `cache`.
        If `key` is `None` or if `key` doesn't
        exist in `self.cache_data`, return `None`.
        """
        # Return `None` if `key` is `None` or doesn't exist
        if key is None or key not in self.cache_data:
            return None

        # Increase the usage frequency and update `LRU` order
        self.usage_frequency[key] += 1
        self.lru_order.remove(key)
        self.lru_order.append(key)

        # Return the `value` associated with the `key`
        return self.cache_data[key]
