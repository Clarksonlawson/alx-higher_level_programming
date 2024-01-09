#!/usr/bin/python3
"""
Module: 5-save_to_json_file
-----------------------------

This module provides a function that writes an object to a text file,
using a JSON representation.

"""

import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.

    :param my_obj: The object to be written to the file.
    :type my_obj: object
    :param filename: The name of the text file.
    :type filename: str

    Usage:
    ------
    save_to_json_file(my_list, "my_list.json")

    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
