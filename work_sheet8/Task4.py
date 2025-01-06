#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 8, Task 4

def string_to_dict(input_string):
    """
        Convert a string into a dictionary where each character is assigned an index.

        Args:
            input_string (str): The string to transform.

        Returns:
            dict: A dictionary mapping indices (int) to characters (str) from the input string.

    """

    return {index: char for index, char in enumerate(input_string)}
#die funkt. enumerate() fügt jedem element des strings input_string autom. index hinzu
#zb "abc" → (0, 'a'), (1, 'b'), (2, 'c')

#{index:char for index, char in enumerate(input_string)} erstellt dic. aus index-zeichen-paaren

result = string_to_dict("abc")
print(result)  #{0: 'a', 1: 'b', 2: 'c'}