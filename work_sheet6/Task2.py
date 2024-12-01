#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 6, Task 2


def is_prime(number):

    value_prime = True

    if number > 1:

        for num in range(2, int(number ** 0.5) + 1):
            if number % num == 0:
                value_prime = False
    else:
        value_prime = False

    return value_prime

user_number = int(input("Enter a number: "))
print(f"Is the number {user_number} prime? {is_prime(user_number)}")