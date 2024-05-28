#!/usr/bin/python3
"""python I/O task 2"""


def append_write(filename="", text=""):
    """appends string at end of file, returns number of characters added"""
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
        f.close()
        return len(text)
