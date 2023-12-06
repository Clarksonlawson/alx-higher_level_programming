#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns the key with the biggest integer value.

    :param a_dictionary: The input dictionary.
    :return: The key with the biggest integer value, or None if no score is found.
    """
    if a_dictionary:
        best_key = max(a_dictionary, key=lambda k: a_dictionary[k])
        return best_key
    else:
        return None
