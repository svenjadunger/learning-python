#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 7, Task 5

# 1.Recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))


# 2. Iteration
def fibonacci_2(n):
    seq = [0, 1]
    for i in range(n):
        seq.append(seq[-1] + seq[-2])
    return seq[-2]


print(fibonacci_2(5))
