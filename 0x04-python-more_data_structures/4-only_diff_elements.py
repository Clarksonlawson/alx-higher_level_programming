#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.

    :param set_1: The first set.
    :param set_2: The second set.
    :return: A set containing elements present in only one of set_1 and set_2.
    """
    return set_1.symmetric_difference(set_2)
