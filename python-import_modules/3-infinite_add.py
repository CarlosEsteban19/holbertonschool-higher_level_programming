#!/usr/bin/python3
from sys import argv
from add_0 import add
if __name__ == "__main__":
    if len(argv) == 1:
        print("0")
    else:
        for i in range(1, len(argv)):
            result = add(int(argv[i]), int(argv[i + 1]))
        print(result)
