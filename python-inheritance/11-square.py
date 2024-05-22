#!/usr/bin/python3
"""
almost empty class BaseGeometry
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class derived from Rectangle"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area of square"""
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__width, self.__height)
