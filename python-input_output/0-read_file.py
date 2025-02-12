#!/usr/bin/python3
"""Reads and prints the content of a UTF-8 text file."""


def read_file(filename=""):
    """Prints the content of the given file."""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
