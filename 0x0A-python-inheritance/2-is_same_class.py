#!/usr/bin/python3
def is_same_class(obj, a_class):
    """ This function that returns True/False if obj is a type of a_class

    Args:
        obj: object
        a_class: type of the class

    Returns:
        True if type of obj is a_class
        False, otherwise
    """
    return type(obj) is a_class
