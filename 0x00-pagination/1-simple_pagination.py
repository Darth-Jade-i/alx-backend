#!/usr/bin/env python3
"""
This module provides a Server class
to paginate a database of popular baby names.
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index
    for a given pagination request.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index (inclusive)
        and the end index (exclusive) for the given pagination.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a
    database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # Exclude the header row
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of the dataset.

        Args:
            page (int): The page number to retrieve.
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows corresponding
            to the requested page.
        """
        # Verify both arguments
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        # Validate the input parameters
        # assert isinstance(page, int) and page > 0, \
        # """page must be a positive integer"""
        # assert isinstance(page_size, int) and page_size > 0, \
        # """page_size must be a positive integer"""

        # Get the start and end indexes for the requested page
        start_index, end_index = index_range(page, page_size)

        # Retrieve the dataset
        data = self.dataset()

        try:
            # Return the slice of the dataset for the requested page
            if start_index < len(data):
                return data[start_index:end_index]
            else:
                return []
        except IndexError:
            return []
