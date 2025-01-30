#!/usr/bin/python3

"""Represents a square with a private size attribute."""


class Square:

    """Represents a square with a private size attribute."""

    def __init__(self, size):

        """Initializes a Square instance with a private size attribute.

Args:
size: The size of the square (no type or value verification)."""
        self.__size = size
