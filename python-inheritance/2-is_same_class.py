#!/usr/bin/python3
"""
function that returns True if object is exactly
an instance of the specified class; otherwise False.
"""


def is_same_class(obj, a_class):
    """class comparison function"""
    if type(obj) is a_class:
        return True
    else:
        return False
