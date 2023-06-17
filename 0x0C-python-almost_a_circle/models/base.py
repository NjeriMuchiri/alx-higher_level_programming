#!/usr/bin/python3
"""This is the base class of all other classes"""


class Base:
    """Representation of the base class
    Attributes:
        __nb_objects (int): The number of instantiated bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base

        Args:
            id (int): The attribute of the new BAse
    """
        if id is not None:
            self.id = id
        else:
           Base.__nb_objects += 1
           self.id = Base.__nb_objects
