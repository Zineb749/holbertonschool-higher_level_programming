#!/usr/bin/python3
"""Student class definition"""


class Student:
    """Student class with first_name, last_name, and age attributes."""

    def __init__(self, first_name, last_name, age):
        """Initialize the attributes of the student object."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of a Student instance."""
    def to_json(self, attrs=None):
        """Return a dictionary representation of a Student instance."""
        if attrs is None:
            return self.__dict__
        else:

            return {key: value for key, value in
                    self.__dict__.items() if key in attrs}
