#!/usr/bin/python3
def roman_to_int(roman_string):
    clave = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev = 0
    for char in reversed(roman_string):
        if char in clave:
            value = clave[char]
            if value < prev:
                total -= value
            else:
                total += value
            prev = value
    return total
