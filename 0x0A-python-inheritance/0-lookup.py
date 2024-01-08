#!/usr/bin/python3
"""
Module for lookup function.
"""

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
    - obj: The object for which attributes and methods are to be retrieved.

    Returns:
    - A list object containing the names of attributes and methods.

    Example:
    >>> lookup(5)
    ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', ... ]

    >>> lookup("hello")
    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', ... ]

    >>> class ExampleClass:
    ...     def example_method(self):
    ...         pass
    ...
    >>> obj = ExampleClass()
    >>> lookup(obj)
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', ... 'example_method']
    """
    return dir(obj)
