#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 5, Task 5


number = input('Enter a number: ')

if number.isdecimal():
    decimal_number = int(number)
    # print(bin(decimal_number))
    # print(f'{decimal_number:b}')
    binary_digits = []
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_digits.append(str(remainder))
        decimal_number //= 2
    binary_digits.reverse()
    binary_result = ''.join(binary_digits)
    print(binary_result)
    # print(*binary_digits, sep="")
else:
    print('Invalid Input!')

    
    
    
    
    
    
    
    
    
    
    
    
    