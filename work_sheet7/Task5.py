#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 7, Task 5

def fibonacci_recursive(n):
    if n <= 0:  # Basisfall: n = 0
        return 0
    elif n == 1:  # Basisfall: n = 1
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)  # Rekursive Berechnung

print(fibonacci_recursive(10)) # 55
