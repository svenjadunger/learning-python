#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 6, Task 2


def is_prime(number):

    if number <= 1: return False

    for num in range(2, int(number ** 0.5) + 1):
        if number % num == 0:
            return False
    return True


user_number = int(input("Enter a number: "))
print(f"Is the number {user_number} prime? {is_prime(user_number)}")