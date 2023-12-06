def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.

    :param a_dictionary: The input dictionary.
    :param key: The key (a string) to replace or add.
    :param value: The value of any type to associate with the key.
    """
    a_dictionary[key] = value
    return a_dictionary
