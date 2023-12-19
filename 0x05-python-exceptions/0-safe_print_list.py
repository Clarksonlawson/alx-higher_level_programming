def safe_print_list(my_list=[], x=0):
    """
    Print x elements of a list.

    Args:
        my_list (list): The input list.
        x (int): The number of elements to print.

    Returns:
        int: The real number of elements printed.
    """
    printed_elements = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            printed_elements += 1
    except IndexError:
        pass
    finally:
        print()
    
    return printed_elements
