class Square:
    """Class that defines a square with size validation, area calculation, and printing."""
    
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

    @property
    def size(self):
        """Getter method to retrieve the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size attribute with validation."""
        self.__size = value
        self.__validate_size()

    def area(self):
        """Public method to calculate and return the square area."""
        return self.__size ** 2

    def my_print(self):
        """Public method to print the square."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
