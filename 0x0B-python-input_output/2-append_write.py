#!/usr/bin/python3
"""
Module: 2-append_write
-----------------------

This module provides a function for appending a string to the end of a text file
and returns the number of characters added.

"""

def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file and returns the number of characters added.

    :param filename: The name of the text file.
    :type filename: str
    :param text: The string to be appended to the file.
    :type text: str
    :return: The number of characters added.
    :rtype: int

    Usage:
    ------
    num_chars_added = append_write("my_file.txt", "Additional text.")
    print(num_chars_added)

    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_chars_added = file.write(text)
    return num_chars_added
