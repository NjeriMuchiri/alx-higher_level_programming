#!/usr/bin/python3
"""Function that defines an inherited list class MyList """

class MyList(list):
    """It implements sorted printing for the built-in list class"""

    def print_sorted(self):
        """Print a list in sorted ascending order"""
        print(sorted(self))
