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
        if value is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
