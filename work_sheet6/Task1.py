#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 6, Task 1


def flatten(my_list): #my_list ist Eingabeliste, die Elemente(zb zahlen) und verschachtelte Listen enthält
    result = [] #für entpackte Elemente
    for item in my_list: #gehe durch jedes element in d. eingabeliste zb 1, [2,3],.., item ist platzhalter f. aktuelle Element
        if isinstance(item, list): #prüfe ob aktuelles item eine liste ist, wenn zb [2,3] wird funktion wieder aufgerufen, um weiter zu entpacken, wenn 1 geht code in else block
            result.extend(flatten(item)) #funktion ruft sich selbst auf mit item, um verschacht. liste zu entpack., extend fügt einzelne elemente der entpackten liste zu result hinzu;
            #wenn flatten([2,3]) [2,3]zurückgibt, fügt extend die Zahlen 2 und 3 zu result hinzu
        else: #wenn das element keine liste ist, dann..
            result.append(item) #füge element direkt zur result liste hinzu, wie zb result.append(1) -> result = [1]
    return result

test = [1, [2, 3], [4, [5, 6]]]
print(flatten(test))

test2 = [1, [2, [3, [4, [5, [6]]]]]]
print(flatten(test2))




# def flatten(my_list):
#     result = []
#     stack = list(my_list)  
    
#     while stack:
#         item = stack.pop()  
#         if isinstance(item, list):
#             stack.extend(item[::-1]) 
#         else:
#             result.append(item)
    
#     return result[::-1]  # Ergebnis umdrehen







# flatte2 = lambda l: [item for i in l for item in (flatten(i) if isinstance(i, list) else [i])]

# print(flatte2(test))  