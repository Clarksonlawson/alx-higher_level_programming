#!/usr/bin/python3
"""
Defines a class Square that represents a square.
"""


class Square:
    """
    This class defines a square with a private instance attribute size.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with optional size.

        Parameters:
        - size (int): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Parameters:
        - value (int): The size to set.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
