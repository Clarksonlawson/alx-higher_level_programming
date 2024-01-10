#!/usr/bin/python3
"""
Module: 100-append_after
------------------------

This module defines a function append_after(filename, search_string, new_string)
that inserts a line of text to a file after each line containing a specific string.

"""

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing a specific string.

    :param filename: Name of the file.
    :type filename: str
    :param search_string: The string to search for.
    :type search_string: str
    :param new_string: The string to insert after lines containing the search string.
    :type new_string: str

    Usage:
    ------
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")

    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
