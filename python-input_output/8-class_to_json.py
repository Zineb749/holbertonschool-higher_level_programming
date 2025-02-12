#!/usr/bin/pyhton3
"""json serialization"""


def class_to_json(obj):
    """json serialization"""
    return obj.__dict__
