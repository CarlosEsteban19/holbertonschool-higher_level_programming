#!/usr/bin/python3
"""
almost empty class BaseGeometry
"""


class BaseGeometry:
    """class definition"""
    def area(self):
        """returns area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        self.name = name
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.value = value


class Rectangle(BaseGeometry):
    """class derived from base geometry"""
    def __init__(self, width, height):

        # deal with width
        super().integer_validator("width", width)
        self.__width = width

        # deal with height
        super().integer_validator("height", height)
        self.__height = height
