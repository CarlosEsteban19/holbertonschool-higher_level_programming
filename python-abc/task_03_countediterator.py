#!/usr/bin/python3
"""comentario"""


class CountedIterator(iter):
    """Class derived from iter"""
    def __init__(self, data):
        self.data = data
        self.counter = 0

    def get_count(self):
        """returns count"""
        return self.counter

    def __next__(self):
        """override __next__"""
        try:
            item = next(self.data)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
