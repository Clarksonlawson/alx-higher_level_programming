#!/usr/bin/python3
"""
Module for Square class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a Square, inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
        - size: Size of the square.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the Square.
        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
