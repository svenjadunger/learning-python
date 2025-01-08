def map_languages(dict1, dict2):
    """
    Maps words from language1 to language3 using two intermediate dictionaries.

    The function takes two dictionaries:
    - `dict1` maps words from language1 to language2.
    - `dict2` maps words from language2 to language3.

    It computes and returns a new dictionary that maps words from language1 to language3.
    Only words present in both dictionaries are included in the resulting mapping.

    Args:
        dict1 (dict): A dictionary mapping words from language1 to language2.
        dict2 (dict): A dictionary mapping words from language2 to language3.

    Returns:
        dict: A dictionary mapping words from language1 to language3.

    """
    #dic wird erstellt
    result = {}
    #durchöäuft dict1 wobei, key1 wort in sprache1(zb red ist)
    #value1 wort in sprache2 zb rot
    for key1, value1 in dict1.items():  # Returns all key-value pairs, for example: [(‘red’, ‘rot’), (‘green’, ‘grün’)].
        #prüft ob sprache2 wort in dict2 existiert
        if value1 in dict2:
            #bei übereinstimmung schlüssel= sprache1-wort, wert:sprache3-wort
            result[key1] = dict2[value1]
    return result
    # in one line: return {key: dict2[value] for key, value in dict1.items() if value in dict2}

dict1 = {'red': 'rot', 'green': 'grün'}
dict2 = {'rot': 'красный', 'gelb': 'sarı', 'blau': 'mavi'}
result = map_languages(dict1, dict2)
print(result)  # {'red': 'красный'}
