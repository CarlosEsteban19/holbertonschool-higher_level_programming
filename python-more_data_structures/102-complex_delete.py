#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    newdic = {}
    for x, y in a_dictionary.items():
        if y != value:
            newdic[x] = y
    return newdic
