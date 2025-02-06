#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """ returns True if objet is instance of a subclass
    of a given class"""
    
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False