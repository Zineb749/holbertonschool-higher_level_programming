#!/usr/bin/python3
"""0. Basic Serialization"""
import pickle


def serialize_and_save_to_file(data, filename):
    """function that serialize and save data"""
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


def load_and_deserialize(filename):
    """function that load and deserialize data"""
    with open(filename, 'rb') as f:
        return pickle.load(f)
