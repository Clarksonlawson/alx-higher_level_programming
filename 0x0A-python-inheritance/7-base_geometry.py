#!/usr/bin/python3
"""
Module for BaseGeometry class.
"""


class BaseGeometry:
    """
    A class representing BaseGeometry with area() and integer_validator() methods.
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented".

        Raises:
        - Exception: Always with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the given value.

        Args:
        - name: A string representing the name of the value.
        - value: The value to be validated.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less or equal to 0.

        Example:
        >>> bg = BaseGeometry()
        >>> bg.integer_validator("my_int", 12)
        >>> bg.integer_validator("width", 89)
        >>> bg.integer_validator("name", "John")
        Traceback (most recent call last):
        ...
        TypeError: name must be an integer
        >>> bg.integer_validator("age", 0)
        Traceback (most recent call last):
        ...
        ValueError: age must be greater than 0
        >>> bg.integer_validator("distance", -4)
        Traceback (most recent call last):
        ...
        ValueError: distance must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
