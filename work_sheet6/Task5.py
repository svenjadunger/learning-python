#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 6, Task 5


def common_divisor(int1, int2, int3):
    for i in range(2, min(int1, int2, int3) + 1): 
        if int1 % i == 0 and int2 % i == 0 and int3 % i == 0:
            return i  
    return 1  


result = common_divisor(12, 18, 24)
print(result)  # 2

result = common_divisor(7, 11, 13)
print(result)  # 1

result = common_divisor(12, 3, 9)
print(result) 