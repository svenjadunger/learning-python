#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 5, Task 4

n = int(input("Please enter a number of stars (maximum):  ")) #zb 5

# aufsteigend (1,6)
for i in range(1, n + 1): #i=1, ... i=5
    print('*' * i) #'*' * 1 = *,.... '*' * 5 = *****

# absteigend (4, 0, -1) ende bei 1 (1 exklusive, n. gezählt)
for i in range(n - 1, 0, -1): #i=4, i=3,.. i=1
    print('*' * i) # '*' * 4 = ****,..... *
    
    
