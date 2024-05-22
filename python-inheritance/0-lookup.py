#!/usr/bin/python3
"""function that returns list of attributes and methods of an object"""


def lookup(obj):
    """look up function"""

    list = dir(obj)
    return list
