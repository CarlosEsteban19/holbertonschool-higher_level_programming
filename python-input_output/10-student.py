#!/usr/bin/python3
"""python I/O task 9"""


class Student:
    """class that defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if not isinstance(attrs, list):
            return self.__dict__
        if all(isinstance(item, str) for item in attrs):
            thedict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    thedict[key] = value
            return thedict
