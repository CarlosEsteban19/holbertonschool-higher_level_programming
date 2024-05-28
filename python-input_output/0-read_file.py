#!/usr/bin/python3
"""python input output task 0"""


def read_file(filename=""):
    with open(filename, 'r', encoding="utf-8") as f:
        text = f.read()
        print(text)
        f.close()
