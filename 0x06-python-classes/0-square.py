#!/usr/bin/python3
"""
Defines a Square class with a size attribute.
"""


class Square:
    """
    Represents a square.

    Attributes:
    - size (int): The size of the square.
    """
    def __init__(self, size=0):
        """Initializes a new instance of the Square class."""
        self.__size = size
