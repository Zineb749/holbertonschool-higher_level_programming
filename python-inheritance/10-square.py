#!/usr/bin/python3
"""rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class inherit from rectangle"""
    def __init__(self, size):
        """initialise size"""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """return square area"""
        return self.__size * self.__size
