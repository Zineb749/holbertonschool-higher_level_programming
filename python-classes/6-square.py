#!/usr/bin/python3
"""Defines a Square class with private size and position attributes."""


class Square:
    """Represents a square with size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square instance with a validated size and position.

        Args:
            size (int): The size of the square's side.
            position (tuple): The position (x, y) for printing.

        Raises:
            TypeError: If size is not an integer or position is not a tuple of two positive integers.
            ValueError: If size is negative.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to update and validate the size.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method to retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to update and validate the position.

        Raises:
            TypeError: If value is not a tuple of two non-negative integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square using '#' with the specified position.

        - If size == 0, prints an empty line.
        - Uses spaces to adjust the horizontal position.
        - Does not fill lines with spaces when position[1] > 0.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
