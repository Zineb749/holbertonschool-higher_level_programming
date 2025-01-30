#!/usr/bin/python3
"""Defines a Square class with a private size attribute and validation."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """Initializes a Square instance with a validated size.

        Args:
            size (int): The size of the square's side (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to update the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
