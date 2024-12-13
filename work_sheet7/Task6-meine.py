#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 7, Task 6

def list_depth(lst):
    if not isinstance(lst, list): #ist lst eine liste?
        return 0 #falls n. zb zahl, string: tiefe=0
    if not lst: #prüft ob liste leer ist
        return 1 #leere liste hat tiefe 1
        
    max_depth = 0 #speichert die größte gefundene tiefe
    for item in lst: #f. jedes element
        depth = list_depth(item) #ruft sich selbst auf um dessen tiefe zu finden
        max_depth = max(max_depth, depth) #speichert die größere zahl: aktuelle max_depth od. neue depth
    
    return 1 + max_depth #return max. Untertiefe +1

# Test
test = [
[1, [2, [3, 4], 5]],  # Tiefe 3
[1, 2, 3],            # Tiefe 1
[]                    # Tiefe 1
]

for t in test:
    print(f"Input: {t}")
    print(f"Tiefe: {list_depth(t)}\n")