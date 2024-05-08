#!/usr/bin/python3
def remove_char_at(str, n):
    strcopy = str[:n] + str[n + 1:]
    return strcopy
