#!/usr/bin/python3
"""opens file and appends"""


def append_write(filename="", text=""):

    """opens file and appends"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
