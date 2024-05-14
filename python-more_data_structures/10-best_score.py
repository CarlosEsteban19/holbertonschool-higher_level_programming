#!/usr/bin/python3
def best_score(a_dictionary):
    high = []
    num = 0
    if not a_dictionary:
        return None
    for x, y in a_dictionary.items():
        if y > num:
            num = y
            high = x
    return high
