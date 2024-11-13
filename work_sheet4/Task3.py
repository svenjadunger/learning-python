#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 4, Task 3


# Die Listen
N = ['NP', 'Det', 'N'] # Non-Terminals
T = ['the', 'cat'] # Terminals
print("-Checking Grammar Rules-")
print("Non-Terminals (N):", N)
print("Terminals (T):", T)
print("\nPlease enter a rule like 'N -> cat' or 'NP -> the N':")
# Eingabe der Regel von benutzer
rule = input() # z.B. "N -> cat"
# Initialisiere correct_rule als False, weil muss erst bewiesen werden ob es richtig ist
correct_rule = False
# Prüfe ob genau ein -> vorkommt, denn es muss genau EIN Pfeil sein
if rule.count('->') == 1:
    #Teile die Regel in linke und rechte Seite (zb N->cat wird zu left side N and right side cat)
    left_side, right_side = rule.split('->')
    # Entferne Leerzeichen am Anfang und Ende " N " wird zu "N", rechts und links Leerzeichen entfernen
    left_side = left_side.strip()
    right_side = right_side.strip()
    # Teile die rechte Seite in Symbole bei leerzeichen zb "the N" wird zu "the","N"
    right_symbols = right_side.split()
    print(right_symbols) # test geklappt, wird zu ['the', 'N']
    # Hauptprüfung
    # Prüfe ob linke Seite genau ein Symbol aus N ist
    if left_side in N:# NP? DET? N?
        # Wenn rechte Seite ein Symbol hat : muss in T sein
        if len(right_symbols) == 1: # muss genau ein Symbol links sein:
            if right_symbols[0] in T: #nur N darf zu Terminal werden
                correct_rule = True
        # Wenn rechte Seite zwei Symbole hat : erstes in T, zweites in N
        elif len(right_symbols) == 2: # muss genau zwei Symbole rechts sein
            if right_symbols[0] in T and right_symbols[1] in N: #nur NP darf zu "the N" werden
                correct_rule = True

print("Result:")
if correct_rule:
    print("The rule is valid.")
else:
    print("The rule is not valid.")