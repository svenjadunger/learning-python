#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 6, Task 2


def is_prime(number):
    if number <= 1:
        return False  # zahlen kleiner oder gleich 1(zb -5,0,1) keine primzahlen
    if number <= 3:
        return True  # 2 und 3 sind die einzigen kleinen primzahlen, hier wäre Zahl 2 oder 3=true
    if number % 2 == 0 or number % 3 == 0:
        return False  # ist zahl gerade?(außer 2), danach ist die durch 3 teilbar?(außer 3);  4,6,8 -> false


# für alle übrigen Zahlen Check...
#starten bei 5 , weil wir 2 und 3 schon geprüft haben
    # primzahlen-theorie, Primzahlen > 3 haben die Form 6k±1 die n. durch 2 oder 3 teilbar sind
    i = 5
    while i * i <= number: #schleife läuft nur, solange quadr. von i kleiner oder gleich der zahl nr ist
        # Wir prüfen nur bis zur Wurzel der Zahl
        # Beispiel für 25: 
        # i=5: 5*5=25 ≤ 25 (ja, prüfen)
        # i=11: 11*11=121 > 25 (nein, fertig)
        if number % i == 0 or number % (i + 2) == 0: #prüft ob number durch i oder i+2 teilbar ist, wenn teilbar dann false
            return False
        # Prüft zwei Zahlen auf einmal:
        # i und (i+2)
        # Bei i=5 prüfen wir also 5 und 7
        # Bei i=11 prüfen wir 11 und 13
        # usw.
        i += 6 #nach jedem durchlauf wird i um 6 erhöht
        # Der Trick: Wir springen in 6er-Schritten!
        # Von 5 zu 11 zu 17 zu 23...
        # Warum? Weil mögliche Primzahlen oft in der Form 6k±1 kommen

    return True
print(is_prime(7))    # True, weil 7 nur durch 1 und sich selbst teilbar
print(is_prime(12))   # False, weil 12 durch 2,3,4,6 teilbar
print(is_prime(2))    # True, weil 2 die kleinste Primzahl ist
print(is_prime(1))    # False, weil 1 per Definition keine Primzahl ist