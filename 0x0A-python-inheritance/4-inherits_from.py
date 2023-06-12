#!usr/bin/python3
"""Function that checks whether inheritance is directly or indirectly"""


def inherits_from(obj, a_class):
    """Defines if the obj is an instance of a class that
    inherited directly or indirectly from specified class

    Args:
        obj: object itself
        a_class: the class

    Return:
        True: if obj is an instance of a class
        otherwise - False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
