#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 4, Task 3

# Die Listen
N = ['NP', 'Det', 'N']     # Non-Terminals 
T = ['the', 'cat']         # Terminals 


print("-Prüfung von Grammatikregeln-")
print("Nicht-Terminale (N):", N)
print("Terminale (T):", T)
print("\nBitte geben Sie eine Regel ein, wie z.B. 'N --> cat'):")


# Eingabe der Regelc
rule = input()             # z.B. "N --> cat"

# Initialisiere correct_rule als False
correct_rule = False

#  Prüfe ob genau ein --> vorkommt
if rule.count('-->') == 1:
   #Teile die Regel in linke und rechte Seite (zb N-->cat wird zu left N right cat)
   left_side, right_side = rule.split('-->')
   
   #  Entferne Leerzeichen am Anfang und Ende " N " wird zu "N"
   left_side = left_side.strip()
   right_side = right_side.strip()
   
   #  Teile die rechte Seite in Symbole bei leerzeichen zb "the N" wird zu "the","N"
   right_symbols = right_side.split()
   
   # Hauptprüfung
   # Prüfe ob linke Seite genau ein Symbol aus N ist
   if left_side in N: #NP? DET? N?
       # Wenn rechte Seite ein Symbol hat : muss in T sein
       if len(right_symbols) == 1:
           if right_symbols[0] in T: #isz dieses symbol in the,cat? (T)
               correct_rule = True
       # Wenn rechte Seite zwei Symbole hat : erstes in T, zweites in N
       elif len(right_symbols) == 2:
           if right_symbols[0] in T and right_symbols[1] in N:
               correct_rule = True

print("Ergebnis:")
if correct_rule:
    print("Die Regel ist gültig.")
else:
    print("Die Regel ist nicht gültig.")