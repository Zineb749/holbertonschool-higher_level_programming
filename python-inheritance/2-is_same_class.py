#!/usr/bin/python3
"""exact same object"""


def is_same_class(obj, a_class):
    """function that return True if object is an instance of the class"""
    if type(obj) is a_class:
        return True
    else:
        return False
