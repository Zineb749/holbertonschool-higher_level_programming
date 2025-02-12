#!/usr/bin/python3
"""saves object to json file"""
import json


def save_to_json_file(my_obj, filename):
    """saves object to json file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
