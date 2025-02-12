#!/usr/bin/python3
"""Saves an object to a JSON file and loads an object from a JSON file."""
import json


def save_to_json_file(my_obj,):
    """Saves an object to a JSON file."""
    with open('add_item.json', 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """Creates an object from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data
