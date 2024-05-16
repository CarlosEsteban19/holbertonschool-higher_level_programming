#!/usr/bin/python3
"""empty class"""


class Square:
    """empty class"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area of square"""
        return self.__size ** 2

    @property
    def size(self):
        """get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints square"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="" if j + 1 < self.__size else "\n")
