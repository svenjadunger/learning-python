#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 6, Task 2

# Primzahl = Zahl, die durch 1 und sich selbst teilbar ist; 2,3,5,7,11,13,17,19,....

def is_prime(number):
    if number <= 1: #zb 1
        return False  
    if number <= 3: #zb 2
        return True  # 2 und 3 sind die einzigen kleinen primzahlen
    if number % 2 == 0 or number % 3 == 0:
        return False  #zb 12


    # primzahlen-theorie, Primzahlen > 3 haben die Form 6k±1 die n. durch 2 oder 3 teilbar sind, prüfen nur bis zur wurzel d.zahl
    i = 5
    while i * i <= number: 
        if number % i == 0 or number % (i + 2) == 0:
            return False
        # Bei i=5 prüfen wir also 5 und 7
        i += 6 #nach jedem durchlauf wird i um 6 erhöht (6er-schritte, von 5 zu 11)
        # Warum? Weil mögliche Primzahlen oft in der Form 6k±1 kommen

    return True #zb 7
print(is_prime(7))    # True
print(is_prime(12))   # False
print(is_prime(2))    # True
print(is_prime(1))    # False

