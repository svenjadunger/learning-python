#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 9, Task 1

def mad_libs(word1, word2, word3):
    """
    Fills a Mad Libs style text with given words.

    Args:
        word1 (str): A noun.
        word2 (str): A verb in past tense.
        word3 (str): An adjective.

    Returns:
        str: The completed text.
    """
    text = f" I saw an {word1} that {word2} very {word3}."
    return text

# Example usage
result = mad_libs("bear", "smiled", "gracefully")
print(result)
