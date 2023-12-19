def safe_print_integer(value):
    """
    Print an integer with "{:d}".format().

    Args:
        value: The input value, which can be any type (integer, string, etc.).

    Returns:
        bool: True if value has been correctly printed,
              otherwise, returns False.
    """
    try:
        print("{:d}".format(value))
        print()  # Print a new line after the integer
        return True
    except (ValueError, TypeError):
        return False

