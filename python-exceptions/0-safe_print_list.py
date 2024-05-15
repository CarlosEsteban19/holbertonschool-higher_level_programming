#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="" if i + 1 < x else "\n")
    except IndexError:
        print()
        return i
    return i + 1
