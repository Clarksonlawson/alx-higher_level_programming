#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.

    :param a_dictionary: The input dictionary.
    :param key: The key (a string) to delete.
    :return: A new dictionary with the key deleted.
    """
    a_dictionary.pop(key, None)
    return a_dictionary
