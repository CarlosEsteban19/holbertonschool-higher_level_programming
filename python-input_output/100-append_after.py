#!/usr/bin/python3
"""python I/O advanced task 100"""


def append_after(filename="", search_string="", new_string=""):
    """inserts line of text to file, after each line containing specific str"""
    with open(filename, 'r', encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, 'w', encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
