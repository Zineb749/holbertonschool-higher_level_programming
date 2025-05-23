#!/usr/bin/python3
"""Defines a Square class with a private size attribute and validation."""


class Square:

    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """Initializes a Square instance.

        Args:
            size (int): The size of the square's side (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size

    def area(self):

        """Calculates and returns the area of the square."""

        return self.__size * self.__size
