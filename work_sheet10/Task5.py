#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 10, Task 5

import re

def validate_password(password):
    """
    Validates a password based on the following rules:
    - Min 10 characters
    - Contains at least one number
    - No whitespace
   - Contains *,!,?,- OR longer than 15 chars
    - Starts with letter
    - No repeated sequence of 3+ chars
    """
    #1.prüfung: 
    # ^[a-zA-Z]: Muss mit Buchstabe beginnen
    # .{9,}: Gefolgt von mindestens 9 weiteren Zeichen (= mind. 10 insgesamt)
    # $: Ende des Strings
    if not re.match(r'^[a-zA-Z].{9,}$', password):
        return False

    # 2. prüfung:
    # \d: Prüft ob mindestens eine Zahl vorhanden
    # \s: Prüft ob Whitespace vorhanden (nicht erlaubt)
    if not re.search(r'\d', password) or re.search(r'\s', password):
        return False

    # 3. prüfung
    # len(password) > 15: Prüft ob länger als 15 Zeichen
    # [*\-!?]: Prüft ob eines der Sonderzeichen vorhanden
    # - muss escaped werden mit \
    if not (len(password) > 15 or re.search(r'[*\-!?]', password)):
        return False

    # 4. prüfung
    # len(password)-5: muss n. bis zum Ende gehen, da wir mindestens 3 Zeichen suchen, i geht von 0 bis 4
    for i in range(len(password)-5):
        #range(3, len(password)-i): Länge der zu prüfenden Sequenz
        #Startet bei 3 (kürzeste Sequenz, die zu suchen
        # bei i= 0 : j geht von 3 bis 10, prüft sequenzen der länge 3,4,5
        for j in range(3, len(password)-i):
            # bei i=0: j= 3 'tes, j=4 'test', j=5 testt'
            sequence = password[i:i+j]
            # prüft ob sequenz mind. 3 zeichen lang ist
            # password.count(sequence): Zählt wie oft die Sequenz vorkommt
            # bei testtest123: findet test zweimal -> ungültig
            if len(sequence) >= 3 and password.count(sequence) > 1:
                return False

    return True

# Tests
def test_validate_password():
    # Valid passwords
    assert validate_password("Secure123!pass") == True  # Has special char
    assert validate_password("SuperLongPassword123") == True  # Longer than 15

    # Invalid passwords
    assert validate_password("short1") == False  # Too short
    assert validate_password("NoNumbers!") == False  # No numbers
    assert validate_password("123secure!") == False  # Doesn't start with letter
    assert validate_password("Secure secure123!") == False  # Has whitespace
    assert validate_password("SecureSecure123!") == False  # Has repeated sequence

    print("All tests passed!")

test_validate_password()