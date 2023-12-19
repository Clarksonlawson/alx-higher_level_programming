class Square:
    """Class that defines a square with size, position validation, area calculation, and printing."""
    
    def __init__(self, size=0, position=(0, 0)):
        """Initialization method with optional size, position, and validation."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method to retrieve the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method to retrieve the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the position attribute with validation."""
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(x, int) for x in value) or any(x < 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public method to calculate and return the square area."""
        return self.__size ** 2

    def my_print(self):
        """Public method to print the square with position."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
