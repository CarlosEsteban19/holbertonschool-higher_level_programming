#!/usr/bin/python3
"""
function that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """class compare function"""
    if isinstance(obj, a_class) and not type(obj) is a_class:
        return True
    return False
