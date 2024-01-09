#!/usr/bin/python3
"""
Module: 4-from_json_string
---------------------------

This module provides a function that returns an object (Python data structure)
represented by a JSON string.

"""

import json

def from_json_string(my_str):
    """
    Returns an object represented by a JSON string.

    :param my_str: The JSON string to be converted to an object.
    :type my_str: str
    :return: The Python data structure represented by the JSON string.
    :rtype: object

    Usage:
    ------
    my_object = from_json_string(json_string)
    print(my_object)

    """
    return json.loads(my_str)
