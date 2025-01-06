


def lists_to_dict(keys, values):
    """
    Converts two lists into a dictionary, where the first list contains the keys and the second list contains the values.

    Parameters:
    keys (list): List of keys.
    values (list): List of values.

    Returns:
    dict: Dictionary created from the two lists.
    """
    if len(keys) != len(values):
        raise ValueError("Lists must have the same length.")
    else:
        dictionary = {}
        for i in range(len(keys)):
            dictionary[keys[i]] = values[i]

        return dictionary
        # alternative ohne for: return dict(zip(keys, values))


keys = ['a', 'b', 'c']
values = [1, 2, 3]
result = lists_to_dict(keys, values)
print(result)  # Result: {'a': 1, 'b': 2, 'c': 3}
