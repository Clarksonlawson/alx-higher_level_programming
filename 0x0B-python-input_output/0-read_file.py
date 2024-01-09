#!/usr/bin/python3
"""
Module: 0-read_file
--------------------

This module provides a function for reading and printing the contents of a text file.

"""

def read_file(filename=""):
    """
    Reads a text file and prints its contents to stdout.

    :param filename: The name of the text file to read.
    :type filename: str

    Usage:
    ------
    read_file("my_file.txt")

    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
