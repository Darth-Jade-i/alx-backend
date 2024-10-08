#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        # Initialize dataset and indexed dataset as None
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        # Load and cache the dataset from the CSV file if not already done
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # Exclude the header from the dataset
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        # Create an indexed version of the dataset if not already done
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get the pagination index, handling cases
        where rows have been deleted.

        Args:
            index (int): The start index for the page.
                        Defaults to None.
            page_size (int): The size of the page to return.
                            Defaults to 10.

        Returns:
            Dict: A dictionary containing the current index,
            next index, page size, and the data for the page.
        """
        # assert index is not None
        if index is None:
            index = 0
        # validate the index
        assert isinstance(index, int)
        # Ensure the index is within the valid range
        assert 0 <= index < len(self.indexed_dataset()), \
            """Index out of range"""
        # validate the page_size
        assert isinstance(page_size, int) and page_size > 0

        # Retrieve the indexed dataset
        indexed_data = self.indexed_dataset()
        data = []
        current_index = index

        # Gather the dataset for the current page
        # while skipping deleted entries
        while len(data) < page_size and current_index < len(indexed_data):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        # Determine the next index, considering the end of the dataset
        if current_index < len(indexed_data):
            next_index = current_index
        else:
            next_index = None

        # Return the pagination details as a dictionary
        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
