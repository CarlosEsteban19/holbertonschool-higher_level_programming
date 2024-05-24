#!/usr/bin/python3
"""comenytario"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Shapde class"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle class"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """return area"""
        return pi * (self.radius ** 2)

    def perimeter(self):
        """return perimeter"""
        if self.radius <= 0:
            return 0
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle class"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """return area"""
        return self.width * self.height

    def perimeter(self):
        """returns perimeter"""
        return (self.width + self.height) * 2


def shape_info(shape):
    """calls and prints area and perimeter of arg"""
    area = shape.area()
    perimeter = shape.perimeter()

    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
