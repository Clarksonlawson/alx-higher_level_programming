#!/usr/bin/python3
"""
Module: 3-to_json_string
-------------------------

This module provides a function that returns the JSON representation of an object (string).

"""

import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object.

    :param my_obj: The object to be converted to JSON.
    :return: The JSON representation of the object.
    :rtype: str

    Usage:
    ------
    json_string = to_json_string(my_list)
    print(json_string)

    """
    return json.dumps(my_obj)
