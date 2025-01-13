#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 10, Task 3

import re

def convert_date(date):
    """
    Converts date from yyyy-mm-dd to dd-mm-yyyy format

    Args:
        date (str): Date in format yyyy-mm-dd
    Returns:
        str: Date in format dd-mm-yyyy
    """
    #\d{4} = genau 4 ziffern also jahr
    # \d{2} = genau 2 ziffern (monat und tag)
    # () erstellen gruppen
    # also:  (YYYY)-(MM)-(DD)
    pattern = r'(\d{4})-(\d{2})-(\d{2})'
    # die ersertung : r'\3-\2-\1'
    #erste gruppe jahr, zweite monat, dritte tag
    # re.sub() extrahiert gruppen, erstellt neue reihenfolge
    return re.sub(pattern, r'\3-\2-\1', date)

# Tests
def test_date_conversion():
    # Simple date conversion
    assert convert_date("2023-12-24") == "24-12-2023"
    assert convert_date("2024-01-15") == "15-01-2024"

    print("All tests passed!")

test_date_conversion()