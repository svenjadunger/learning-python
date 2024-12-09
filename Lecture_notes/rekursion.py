"""

Rekursion oder rekursive Funktionen sind Funktionen, die so definiert sind, dass sie sich selbst aufrufen. Die Funktion ruft sich also selbst auf, die sich dann wieder selbst aufruft, die sich wiederum selbst aufruft, die sich wiederum selbst aufruft ... Wenn das wie eine unendliche Geschichte klingt, dann ist es das irgendwie auch ..



Im Allgemeinen möchten Sie bei jedem rekursiven Schritt zuerst prüfen, ob der Basisfall erreicht wurde, bevor Sie „die nächste Rekursionsschicht betreten“ (sonst rekursieren Sie unendlich). Daher wird eine rekursive Funktion normalerweise mit einer Bedingungsklausel definiert, in der die erste Bedingung, die Sie prüfen, der Basisfall ist, der die Funktion selbst nicht aufruft.



def recursive_func(PARAMS):
    if BASE_CASE_CONDITION:
        return BASE_CASE_OUTPUT
    else:
        recursive_func(DIFFERENT_PARAM)
        

Jeder Aufruf der Funktion selbst (recursive_func) verwendet einen anderen Parameter und bringt uns dem Basisfall näher.

Warum Rekursion verwenden? Rekursive Funktionen können nützlich sein, wenn Sie ein größeres Problem in kleinere und leichter zu lösende Versionen aufteilen und diese iterativ lösen können. 


fibonacci numbers:
a sequence where the next value equals the sum of its 2 previous values:
0 1 1 2 3 5 8 13 21...


def Fibonaxxi(idx)
    if idx <= 1:
        return idx
    else:
        return Fibonacci(idx-1)+Fibonacci(idx-2)
        
print(fribonacci(0)) -> 0              3 -> 2


A rekursive algortithm
factorial:

5! = 5* 4 * 3 * 2 * 1
= 5 * 4!

4! = 4 * 3 * 2 * 1

= 4 * 3!


Base cases:
0! = 1
1! = 1


function getFacotiral(n)
    if n < 2, return 1
    else return n* getFactorial(n-1)



def get.rekursive_factioral(n):
    if n <0:
        return -1
    elif n < 2:
        return 1
    else:
        return n* get_rekursive-facotieal(n-1)
        
print(get_rekursive:factorial(6))



Randbemerkung: Sehr oft wird bei der Erklärung von Rekursion die Fibonacci-Zahlenfolge als Beispiel verwendet. Zufälligerweise beschäftigt sich eine der Übungen in Ihren Aufgaben auch mit der Fibonacci-Folge, sodass Sie die Lösung hier wahrscheinlich ganz einfach „kostenlos“ im Internet finden. Das ist in Ordnung, bitte nehmen Sie sich einfach einen Moment Zeit, um sicherzustellen, dass Sie die Lösung wirklich verstehen.




sum(4) -> (1+2+3+4) -> 10



def sum(n)
    if n== 0:
        return 0
    else:
        return n + sum(n-1)
        
































"""