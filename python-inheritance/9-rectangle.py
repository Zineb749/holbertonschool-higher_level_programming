#!/usr/bin/python3
"""basegeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class inherit from basegeometry"""
    def __init__(self, width, height):
        """initialize width and height"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """return rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """return str rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
