#!/usr/bin/python3
"""
Defines the MagicClass class that replicates a given Python bytecode.
"""
import math


class MagicClass:
    """
    Represents the MagicClass class.
    """

    def __init__(self, radius=0):
        """
        Initializes a new MagicClass instance.

        Parameters:
        - radius (int or float): The radius of the MagicClass instance (default is 0).
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """Calculates and returns the area of the MagicClass instance."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates and returns the circumference of the MagicClass instance."""
        return 2 * math.pi * self.__radius
