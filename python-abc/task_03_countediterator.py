#!/usr/bin/python3
"""CountedIterator - Keeping Track of Iteration"""
from abc import ABC, abstractmethod


class CountedIterator:
    def __init__(self, iterable):
        self._iterator = iter(iterable)
        self._counter = 0

    def get_count(self):
        return self._counter

    def __next__(self):
        try:
            item = next(self._iterator)
            self._counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        return self
