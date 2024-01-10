#!/usr/bin/python3
"""
Module: 6-load_from_json_file
-------------------------------

This module provides a function that creates an object from a JSON file.

"""

import json

def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    :param filename: The name of the JSON file.
    :type filename: str
    :return: The Python data structure represented by the JSON file.
    :rtype: object

    Usage:
    ------
    my_object = load_from_json_file("my_file.json")
    print(my_object)

    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
