#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer).

    :param my_list: The input list.
    :return: The sum of all unique integers in the list.
    """
    unique_set = set(my_list)
    return sum(unique_set)
