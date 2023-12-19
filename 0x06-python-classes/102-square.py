#!/usr/bin/python3
"""
Defines a Square class that represents a square.
"""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Parameters:
        - size (int or float): The size of the square (default is 0).
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
        - value (int or float): The size to set.

        Raises:
        - TypeError: If size is not a number.
        - ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparison."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparison."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparison."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparison."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparison."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparison."""
        return self.area() >= other.area()


if __name__ == "__main__":
    # Example usage
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
