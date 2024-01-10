#!/usr/bin/python3
"""
Module: 8-class_to_json
------------------------

This module provides a function that returns the dictionary description
with a simple data structure (list, dictionary, string, integer, and boolean)
for JSON serialization of an object.

"""

def class_to_json(obj):
    """
    Returns the dictionary description for JSON serialization of an object.

    :param obj: The instance of a Class.
    :type obj: object
    :return: The dictionary representation of the object.
    :rtype: dict

    Usage:
    ------
    my_dict = class_to_json(my_object)
    print(my_dict)

    """
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    return obj.__slots__.copy()
