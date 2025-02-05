#!/usr/bin/python3
"""Improve Geometry"""


class BaseGeometry:
    """basegeometry class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate that the value is a positive int"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
