#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 5, Task 4

n = int(input("Please enter a number of stars (maximum):  "))

for i in range(1, n + 1):
    print('*' * i)
for i in range(n - 1, 0, -1):
    print('*' * i)
    
    
