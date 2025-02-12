#!/usr/bin/python3
"""creates an object from json file"""
import json


def load_from_json_file(filename):
    """creates an object from a json file"""

    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data 