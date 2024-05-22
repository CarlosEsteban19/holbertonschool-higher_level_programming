#!/usr/bin/python3
"""
almost empty class BaseGeometry
"""


BaseGeomerty = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeomerty):
    """class derived from base geometry"""
    def __init__(self, width, height):

        # deal with width
        super().integer_validator("width", width)
        self.__width = width

        # deal with height
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """return area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
