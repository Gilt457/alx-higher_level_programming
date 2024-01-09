#!/usr/bin/python3
"""Module that defines a Student class"""


class Student:
    """A class that represents a student."""

    def __init__(self, first_name, last_name, age):
        """Creates a new Student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student.
        If attrs is a list of strings, only includes those attributes
        in the list
        """
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return vars(self)

    def reload_from_json(self, json):
        """Updates all attributes of the Student
        """
        for k, v in json.items():
            setattr(self, k, v)
