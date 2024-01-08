#!/usr/bin/python3
"""
Module for BaseGeometry class.
"""


class BaseGeometry:
    """
    A class representing BaseGeometry with an area() method.
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented".

        Raises:
        - Exception: Always with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
