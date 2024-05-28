#!/usr/bin/python3
"""python I/O task 1"""


def write_file(filename="", text=""):
    """writes string to text file, returns number of characters written"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        f.close()
        return len(text)
