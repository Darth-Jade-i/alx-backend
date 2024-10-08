#!/usr/bin/env python3
"""
This module provides a Server class
to paginate a database of popular baby names
and a method for hypermedia pagination.
"""

import csv
import math
from typing import List, Tuple, Dict, Any


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

        # Return the slice of the dataset for the requested page
        if start_index < len(data):
            return data[start_index:end_index]
        else:
            return []

    def get_hyper(self, page: int = 1,
                  page_size: int = 10) -> Dict[str, Any]:
        """
        Get a page of the dataset with hypermedia metadata.

        Args:
            page (int): The page number to retrieve.
            page_size (int): The number of items per page.

        Returns:
            Dict[str, Any]: A dictionary containing
            the page data and hypermedia metadata.
        """
        # Get the page data using the existing get_page method
        data = self.get_page(page, page_size)

        # Calculate the total number of pages
        total_pages = math.ceil(len(self.dataset()) / page_size)

        # Determine the next and previous page numbers
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # Create the hypermedia metadata dictionary
        hypermedia = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }

        return hypermedia
