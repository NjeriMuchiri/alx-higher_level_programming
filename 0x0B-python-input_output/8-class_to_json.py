#!/usr/bin/python3
"""funcftion that converts python class to JSON"""


def class_to_json(obj):
    """Return the dictionary representation of a simple data structure"""
    return obj.__dict__
