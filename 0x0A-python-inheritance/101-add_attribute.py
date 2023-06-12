#!/usr/bin/python3
"""Defines a function that can add any attribute to objects if possible"""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible
    Args:
        obj (any): Object to add an attribute to
        att (str): The name of the attribute to add to object
        value (any): The value of att

    Raises:
        TypeError: if the attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
