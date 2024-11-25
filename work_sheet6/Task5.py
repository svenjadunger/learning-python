#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 6, Task 5

def common_divisor(int1, int2, int3):
    # schleife beginnt bei 2 (weil 1 immer ein teiler ist) und schauen alle zahl. von 2 bis zur kleinsten zahl der drei eingaben an
    # wenn eingaben 12,18,24 sind, ist kleinste zahl 12. Schleife prüft zahlen 2,3,...12
    for i in range(2, min(int1, int2, int3) + 1):  # Teste von 2 bis zur kleinsten Zahl.
        #min weil, der ggt von den drei zahlen nie größer als die kleinste der drei zahlen sein kann
        #bedingung prüft, ob i gemeinsamer teiler der drei zahlen ist
        #wenn i die erste z, die zweite z. und die dritte z. teilt, dann ist i gemeinsamer teiler
        if int1 % i == 0 and int2 % i == 0 and int3 % i == 0:
            #sobald gemeinsamer teiler gefunden wird, wird zurückgegeben, f. 12,18,24 erster ggt 2 gefunden u. gegeben
            return i  # Rückgabe, sobald ein gemeinsamer Teiler gefunden wird.
#wenn keine ggt größer als 1 findet, gibt 1 zurück, zb wenn zahlen primzahlen sind und kein ggt auser 1 haben
    return 1  # Wenn kein gemeinsamer Teiler existiert, außer 1.


result = common_divisor(12, 18, 24)
print(result)  # Erwartet: 2

result = common_divisor(7, 11, 13)
print(result)  # Erwartet: 1
