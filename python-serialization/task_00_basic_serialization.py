#!/usr/bin/python3
"""python serialization task 0"""
import json


def serialize_and_save_to_file(data, filename):
    """serialize and save to file"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """load and deserialize"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
