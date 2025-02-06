#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """ returns True if object is an istance of the classs or 
    class that inherited from"""
    return (isinstance(obj, a_class))