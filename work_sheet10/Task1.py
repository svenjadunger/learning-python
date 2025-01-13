#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 10, Task 1

import re

def validate_email(email):
    """
    Checks if an email address is valid.
    Minimal requirements: 
    - One @ symbol
    - Text before and after @
    - A dot after @ with text after it
    
    Args:
        email (str): The email address to validate
        
    Returns:
        bool: True if valid, False if invalid
    """
    
    #.+ = ein oder mehr beliebige zeichen
    #@ symbol
    #\. = ist ein echter punkt (der backslash escaped den punkt)
    pattern = r'.+@.+\..+'
    
    #re.match() sucht nach dem pattern am anfang des strings
    #bool() macht daraus true oder false
    return bool(re.match(pattern, email))

# Tests with different email addresses
def test_validate_email():
    # Test valid emails
    assert validate_email("test@example.com") == True
    assert validate_email("a@b.c") == True
    
    # Test invalid emails
    assert validate_email("test@") == False
    assert validate_email("@domain.com") == False
    assert validate_email("testdomain.com") == False
    
    print("All tests passed!")

test_validate_email()