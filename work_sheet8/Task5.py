#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 8, Task 5

#ein leeres dic. wird als standardw. verw., um berechn. fibonac-werte zu speichern: memo={}
#d. schlüssel ist num, d. zugehör. wert is ergebn. der fibonac-berechn.
def fibonacci(num, memo={}):
    """accepts an integer as an
    argument and calculates the value of the sequence at that position"""
    if num in memo:  # Prüfen, ob wert bereits in dict. gespeich. ist
        return memo[num] #falls ja, gesp. wert sofort zurückgeb.
    if num == 0:  # die Fibonaccizahl an position(0) = 0 ist 0
        return 0
    if num == 1:  #d. fibonacci-zahl an pos(1) = 1 ist 1
        return 1
    #wenn wert no. n. berechn. wurde, wird fib.zahl rekursiv berechn. u. in memo gespeichert:
    memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo)
    return memo[num]

print(fibonacci(10))  #55
print(fibonacci(20))  #6765
print(fibonacci(40))  #102334155

