#!/usr/bin/python3
"""
Module for is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class;
    otherwise False.

    Args:
    - obj: The object to check.
    - a_class: The class to check against.

    Returns:
    - True if the object is an instance of, or if the object is an instance
      of a class that inherited from, the specified class; otherwise False.

    Example:
    >>> is_kind_of_class(1, int)
    True

    >>> is_kind_of_class(1, float)
    False

    >>> is_kind_of_class(1, object)
    True
    """
    return isinstance(obj, a_class)
