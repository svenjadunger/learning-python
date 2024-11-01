#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 2, Task 3


fellowship = ['gandalf', 'aragorn', 'frodo', 'sam', 'merry', 'pippin', 'gimli', 'legolas', 'boromir']
hobbits = ['frodo', 'sam', 'pippin', 'merry']

print('saruman' in fellowship)
print(fellowship[0] == 'gandalf')
# print(fellowship[2:7] == hobbits) true set
print('sam' in fellowship and 'sam' in hobbits)
print(fellowship[-3] == 'gimli' or 'gimli' in hobbits) # third hobbit