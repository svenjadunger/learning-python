#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 8, Task 2



def letter_frequency(text):
    """
    Calculate the frequency of each letter in the given text.

    Removes spaces and punctuation before processing. The function is
    case-insensitive, treating uppercase and lowercase letters as the same.

    Args:
        text (str): The input string to analyze.

    Returns:
        dict: A dictionary where keys are letters and values are their
        respective frequencies.
    """
    # Entferne Leerzeichen und Satzzeichen aus d. Text
    cleaned_text = ''.join(char.lower() for char in text if char.isalpha())

    # create empty dictory for buchstabenhäufigkeit
    frequency = {}

    # Zähle die Buchstaben in cleaded text
    for char in cleaned_text:
        if char in frequency:
            frequency[char] += 1 #wenn buchst. bereits im dict. ist, wird zähler um 1 erhöht
        else:
            frequency[char] = 1 #andernfalls wird buchst. m. zähler v. 1 hinzugef.
    return frequency


result = letter_frequency("Hello, World!")
print(result)  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}