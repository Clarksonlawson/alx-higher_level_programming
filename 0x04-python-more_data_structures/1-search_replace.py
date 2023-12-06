#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list.

    :param my_list: The initial list.
    :param search: The element to replace in the list.
    :param replace: The new element.
    :return: A new list with all occurrences of 'search' replaced by 'replace'.
    """
    return [replace if num == search else num for num in my_list]
