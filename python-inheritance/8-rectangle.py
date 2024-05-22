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
