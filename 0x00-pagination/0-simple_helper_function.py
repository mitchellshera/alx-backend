#!/usr/bin/env python3
'''module for simple helper'''


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of start and end indexes for a given page and page size.

    Parameters:
      - page (int): Page number (1-indexed).
      - page_size (int): Number of items per page.

    Returns:
      - tuple: A tuple containing start and end indexes.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
