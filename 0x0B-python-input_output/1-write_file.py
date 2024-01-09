#!/usr/bin/python3
"""
Module: 1-write_file
---------------------

This module provides a function for writing a string to a text file and
returns the number of characters written.

"""

def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.

    :param filename: The name of the text file.
    :type filename: str
    :param text: The string to be written to the file.
    :type text: str
    :return: The number of characters written.
    :rtype: int

    Usage:
    ------
    num_chars = write_file("my_file.txt", "Hello, World!")
    print(num_chars)

    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_chars = file.write(text)
    return num_chars
