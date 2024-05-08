#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        strcopy = str[:n] + str[n + 1:]
    else:
        strcopy = str
    return strcopy
