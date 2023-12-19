class Square:
    """Class that defines a square with size validation and area calculation."""
    
    def __init__(self, size=0):
        """Initialization method with optional size and validation."""
        self.__size = size
        self.__validate_size()

    def __validate_size(self):
        """Private method to validate the size attribute."""
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Public method to calculate and return the square area."""
        return self.__size ** 2
