#!/usr/bin/python3
"""Insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a text after each line containing a given file string
    Args:
        filename: the name of the file
        search_string: string to search for within the file
        new_string: string to insert
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
