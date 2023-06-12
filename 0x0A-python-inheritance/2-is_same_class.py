#!/usr/bin/python3
"""Function that checks the class type"""


def is_same_class(obj, a_class):
    """ This function that returns True/False if obj is a type of a_class

    Args:
        obj(any): object to check
        a_class: type of the class

    Returns:
        True if type of obj is a_class
        False, otherwise
    """
    if type(obj) == a_class:
        return True
    return False
