#!/usr/bin/python3
"""
Defines a class Square that represents a square.
"""


class Square:
    """
    This class defines a square with a private instance attribute size.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Parameters:
        - size (int): The size of the square.
        """
        self.__size = size
