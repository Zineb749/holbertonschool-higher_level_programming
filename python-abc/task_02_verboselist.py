#!/usr/bin/python3
"""Extending the Python List with Notifications"""
from abc import ABC


class VerboseList(list):
    def append(self, item):
        print("Added [{}] to the list.".format(item))
        super().append(item)

    def extend(self, items):
        print("Extended the list with [{}] items.".format(len(items)))
        super().extend(items)

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=None):
        if index is not None:
            print("Popped [{}] from the list".format(self[index]))
            return super().pop(index)
        else:
            popped_item = super().pop()
            print("Popped [{}] from the list.".format(popped_item))
            return popped_item
