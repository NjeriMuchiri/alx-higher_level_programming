#!/usr/bin/python3
"""Function that defines if the obj is an instamce of"""


def is_kind_of_class(obj, a_class):
    """This function checks if the obj is an instance of
    or if the object is an instance of a class that
    inherited from the specfied class

    Args:
        obj: Object itself
        a_class: the class

    Return:
        True: if the obj is an instance of
        Otherwise False
    """

    if isinstance(obj, a_class):
        return True
    return False
