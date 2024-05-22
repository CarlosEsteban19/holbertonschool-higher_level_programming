#!/usr/bin/python3
"""class that inherits from list"""


class MyList(list):
    """class derived from list"""

    def print_sorted(self):
        """prints the list in ascending sorted order"""
        print(sorted(self))
