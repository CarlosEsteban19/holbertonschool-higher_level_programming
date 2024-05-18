#!/usr/bin/python3
"""Square class"""


class Square:
    """define a square"""
    def __init__(self, size=0):
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

    def __lt__(self, other):
        """handle less than <"""
        return self.area() < other.area()

    def __le__(self, other):
        """handle less than or equal <="""
        return self.area() <= other.area()

    def __eq__(self, other):
        """handle is equal =="""
        return self.area() == other.area()

    def __ne__(self, other):
        """handle not equal !="""
        return self.area() != other.area()

    def __gt__(self, other):
        """handle greater than >"""
        return self.area() > other.area()

    def __ge__(self, other):
        """hanlde greater than or equal >="""
        return self.area() >= other.area()
