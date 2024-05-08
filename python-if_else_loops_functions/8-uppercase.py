#!/usr/bin/python3
def uppercase(str):
    for letra in str:
        if 'a' <= letra <= 'z':
            LETRA = chr(ord(letra) - 32)
        else:
            LETRA = letra
        print(LETRA, end="")
    print()
