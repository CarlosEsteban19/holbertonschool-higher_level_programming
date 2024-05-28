#!/usr/bin/python3
"""python I/O task 4"""
import json


def from_json_string(my_str):
    """returns object (Python data structure) represented by JSON string"""
    return json.loads(my_str)
