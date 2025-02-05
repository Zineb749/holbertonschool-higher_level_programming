#!/usr/bin/python3
class MyList(list):
    """A class that inherits from list and prints a sorted version of itself."""
    def print_sorted(self):
        print(sorted(self))

