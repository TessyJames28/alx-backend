#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple, List
import csv
import math
index_range = __import__('0-simple_helper_function').index_range


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters
    """

    s_index = (page - 1) * page_size
    e_index = s_index + page_size

    return s_index, e_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return page list based on index range"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        paginate = index_range(page, page_size)
        dataset = self.dataset()
        if (page_size * page) >= len(dataset):
            return []
        return dataset[paginate[0]: paginate[1]]
