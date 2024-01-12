#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    """Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle instance with specified width, height, x, y, and optional id."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        self.validate_positive_integer("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        self.validate_positive_integer("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x."""
        self.validate_non_negative_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y."""
        self.validate_non_negative_integer("y", value)
        self.__y = value

    def validate_positive_integer(self, attr_name, value):
        """Validate that the attribute is a positive integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attr_name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(attr_name))

    def validate_non_negative_integer(self, attr_name, value):
        """Validate that the attribute is a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attr_name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(attr_name))

    def area(self):
        """Return the area value of the Rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle instance with the character '#' taking into account x and y."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return a string representation of the Rectangle instance."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute in the order: id, width, height, x, y."""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
            elif kwargs:
                for key, value in kwargs.items():
                    setattr(self, key, value)
    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

