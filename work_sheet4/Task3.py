#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 4, Task 3


N = ['NP', 'Det', 'N']
T = ['the', 'cat']

print("-Checking Grammar Rules-")
print("Non-Terminals (N):", N)
print("Terminals (T):", T)
print("\nPlease enter a rule like 'N -> cat' or 'NP -> the N':")

rule = input()
correct_rule = False

if rule.count('->') == 1:
    string_value_left, string_value_right = rule.split('->')
    
    string_value_left = string_value_left.strip()
    string_value_left_list = string_value_left.split()
    
    if len(string_value_left_list) == 1:
        right_side = string_value_right.strip()
        right_symbols = right_side.split()
        
        if string_value_left_list[0] in N:
            if len(right_symbols) == 1:
                if right_symbols[0] in T:
                    correct_rule = True
            elif len(right_symbols) == 2:
                if right_symbols[0] in T and right_symbols[1] in N:
                    correct_rule = True

print("Result:")
if correct_rule:
    print("The rule is valid.")
else:
    print("The rule is not valid.")