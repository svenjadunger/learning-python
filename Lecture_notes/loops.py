# """
# while
# „Tu etwas, bis eine bestimmte Bedingung erfüllt ist“, am besten durch eine sogenannte „while-Schleife“ ausdrücken, die die folgende grundlegende Syntax hat:

# while [BEDINGUNG, die eine Variable verwendet]:
# # tue dies, solange die Bedingung erfüllt ist
# # aktualisiere die Bedingungsvariable, sodass die Bedingung irgendwann nicht mehr erfüllt ist und die Schleife endet


# Das zweite Szenario, d. h. „Tu etwas mit jedem Element in einer Sammlung von Elementen“, lässt sich am besten durch eine sogenannte „for-Schleife“ mit der folgenden Syntax ausdrücken:


# for num in [1,2,3,4,5]:
# # drucke die Zahl aus, die die Schleifenvariable „num“ in der aktuellen Iteration annimmt
# print(num)


# for [LOOP_VARIABLE] in [ITERABLE OBJECT]:
# # tue dies


# print("meow")
# print("meow")
# print("meow")

# i = 3
# while i != 0:
#     print("meow") -> endless loop
    
#     i = i - 1 // asking question again again aber changing value immer 1 weniger bis es irgendwann 0 erreicht
    

# i = 0
# while i < 3: up to but not through 3
#     print("meow")
#     i = i + 1 normalerw. zählt man von 0 aus -----> i += 1 ++ gibts ned in python
    

# for i in [0,1,2]:
#     print("meow") -> meow meow meow  -> nicht gut
    
    
# for _ in range(3):
#     print("meow") -> 3 values  _ heißt ja its a variable but its not necessary to name
    
    
# print("meow" * 3) meowmeowmeow


# print("meow\n" * 3, end="") jezt gibts am ende kein leerzeichen mehr
    


# while: infinitve loop the answer is always true, wenn wir nbr haben ausbrechen aus loop
# while True:
#     n = int(input("whats n?"))
#     if n > 0:
#         break
        
# for _ in range(n):
#     print("meow")

# // wenn wir 10 eingeben kommt 10x meow


# funktionen::
# def main():
#     meow(3)
    
    
# def meow(n):
#     for _ in range(n):
#         print("meow")
        
# main() meow meow meow




# def main():
#     number = get_number()
#     meow(number)
    
    
# def get_number():
#     while True:
#         n = int(input("Whats n?"))
#         if n > 0:
#             break
#         return n
    
    
# def meow(n):
#     for _ in range(n):
#         print("meow")
        


# LIST

# students = ["Hermione", "Harry", "Ron"]

# for student in students:
#     print(student)
    

# for i in range(len(students)):
#     print(studetns[i])   //hermione harry ron
    

# for i in range(len(students)):
#     print(i + 1, studetns[i])  1 hermione, 2 harry, 3 ron




# for _ in range(3):
#     print("#")

# def main()
#     print_column(3)
    
# def print_column(height):
#     print('#\n * height, end="")
        
# main()





# def main():
#     print_row(4)
    
# def print_row(width):
#     print("?" * width)  /????
    
    
# main()






# def main()
#     print_square(3)
    
    
    
# def print_square(size):

# #for each row in square
#     for i in range(size):
    
#     #for each brick in row
#         for j in range(size):
        
#         #print brick
#             print('#', end="")
#         print()
        
#       /  ###
#         ###
#         ###


# main()








# def print_square(size)

#     for i in range(size):
#         print('#' * size)

# main()



# VIDEO 2





# nums = [1,2,3,4,5]

# for num in nums:
#     if num == 3:
#      print('found!')
#      break
#     print(num) // 1,2,3,4,5
    


# nums = [1,2,3,4,5]

# for num in nums:
#     if num == 3:
#      print('found!')
#      break
#   print (num) // 1,2 found!
    


# for num in nums:
#     if num == 3:
#      print('found!')
#      continue
#   print (num) // 1,2 found! 4,5
  
  
# nums = [1,2,3,4,5]

# for num in nums:
#     for letter in 'abc':
#         print(num,letter) / 1a, 1b, 1c, 2a, 2b, 2c


# WHILE LOOP


# for i in range(10):
#     print(i) 0,1,2,...9
    
# for i in range(1,11):
#     print(i) 1,2,...10
    
    
    
# x = 0

# while loop geht fürimmer bis die condition false ist

# while x < 10:
#     print(x)
#     x += 1    0,1,2,....9
    
    
    
# while x < 10:
#     if x ==5:
#         break
#     print(x)
#     x += 1    0,1,..4
    
    
# x = 0
# while True:
#     if x ==5:
#         break
#     print(x)
#     x += 1    0,1,..4
    
    
# RANGE
# # "Mach das 3 mal"
# for i in range(3):
#     print("Hallo!")

# # Gibt aus:
# # Hallo!
# # Hallo!
# # Hallo!

# Also kurz gesagt: range() ist einfach ein Werkzeug, das dir eine Reihe von Zahlen gibt, die du zum Zählen oder Wiederholen von Aktionen nutzen kannst.


# NEUES VIDEO

# for loops: execute a block of code a FIXED number of times- you can iterate over a range, string, sequence,etc

# von 1-10 (10 nicht inklusiv deswehen 11)
# for x in range(1,11):
#     print(x)
    
    
# reversed:

# for x in reversed(range(1,11)):
#     print(X) 10,9,...1 happy new year

# print(happy new year)





# for x in reversed(range(1,11,2)):
#     print(X)  .... 5,7,9



# credit.card = "1234-3134-13244"

# for x in credit.card:
#     print(x)



# for x in range(1,21):
#     if x == 13:
#         continue
#     else:
#         print(x) // haben 13 ausgelassen





# for x in range(1,21):
#     if x == 13:
#         break
#     else:
#         print(x) // 1-12
        
        




# Aufgaben: 
# Task 1: For-Loops (10 P)
# Using for-loops, write a program that outputs all even numbers between 0
# and 10, including 0.

# hier ist eine for loop die eine zahlenreihe nimmt(oder ausgibt) bis 11, range heißt eig hier range(0,11) d.h. 0 ist included bis 10, 11 ist nicht included
# wenn i modulo 2 also wenn die zahlen durch 2 geteilt werden muss der rest 0 ergeben. das geht also nur bei 0,2,4,...








# Task 2: Writing a Split Function (20 P)
# By now, everyone has probably used the .split() function at least once.
# Your task is to write a script with similar functionality. To do this, a string
# and a character should be input by the user using two input() statements.
# Then, the string should be split at all occurrences of the character, and the
# resulting parts should be stored in a list. This list should then be displayed
# on the screen.
# Note: The .split() method must not be used for this task.

# string = input("Gib den String ein: ")
# separator = input("Gib das Trennzeichen ein: ")
# result = [] #leere liste
# current_part = "" #leerer string, hier buchstaben sammeln, bis trennzeichen kommt
# for char in string: #geht durch jeden einzelnen buchstaben in 'Hallo,Welt', char ist 'H', dann 'a',...
# if char == separator: #frage: ist das das Trennzeichen? zb ein Komma
# result.append(current_part) #wenn ja bei Komma, nimm alles was in currentpart ist und tue es in result
# current_part = "" #mach current part wieder leer für nächsten teil
# else:
# current_part += char #wenn nein füge buchstaben zu currentpart hinzu
# result.append(current_part)
# print(result)

# es gibt eine variable mit string und eine benutzereingabe, bei der man einen string eingeben muss, das gleiche für den seperator, man soll ein trennzeichen eingeben. zb Hi,Bye

# ich erstelle eine leere liste result = [] und einen current_part = also einen leren string "" hier kommen dann die buchstaben zum sammeln rein bis das trennzeichen kommt

# die schleife geht durch jeden einzelnen buchstaben in string zb H, dann I
# die frage: wenn der buchstabe oder char ein sepreatur also ein zeichen wie , ist dann tu es in current part und speicher es in result, danach lösche current part für den nächsten schritt, else also wenn es kein komma gibt füge die buchstaben zu currentpart hinzu
# am ende füge alles was in current part ist zu result und drucke result aus











# Task 3: Word Count and Length (20 P)
# Write a script that accepts a sentence from the user via input() and deter-
# mines the following properties:
# • The number of words.
# • The average word length (rounded to two decimal places).
# Also give a course definition of what you consider a word.
# Punctuation marks such as commas, periods, and quotation marks should
# neither be counted as words nor included in the word length calculation.
# Apply a simplified version of last week’s token cleaning method to the words
# before calculating their length. Store the result as a tuple in the variable
# result.

# text = input("Enter a sentence ")
# words = text.split() #teilt text bei leerzeichen -> ['Hallo',',','wie','gehts']
# word_count = 0
# total_length = 0
# for word in words:
# if word[-1].isalpha() or word[-1] in ',.!?:"-': #ist letzter buchstabe ein buchstabe oder letzter buchstabe ein satzzeichen
# word_count += 1 #wenn ja gültiges wort
# total_length += sum(1 for c in word if c.isalpha()) #geht durch alle char in word, zählt 1 f. buchstabe, ignoriert zeichen
# result = (word_count, round(total_length/word_count, 2) if word_count else 0)
# #erstellt tupel mit anzahl der wörter, durchschnittl. länge auf 2 gerundet, if .. else 0 wenn keine wörter, dann 0
# #wenn word_count größer als 0 ist (gibt wörter) wird round(total_length/word_count,2) berechnet
# #else 0: wenn word_count 0 ist (gibt keine wörter) wird der wert 0 zurückgegeben
# print(result)

# es gibt eine benutzereingabe bei der man satz eingeben soll, zb Hallo wie gehts
# text.split teilt bei leerzeichen und macht daraus ne liste also ['Hallo', ",", 'wie', 'gehts']

# man setzt den word count und die durchschnittslänge auf 0
# dann läuft die schleife für jedes wort durch die liste words und wenn ein wort mit einem buchstaben oder einem satzzeichen wie zb ,. endet dann zähle es als ein wort (+1) 

# dann wird die durchscnittslänge berechnet indem durch alle char in word gegangen wird, es zählt 1 (also +1) für jeden buchstaben (dabei werden satzzeichen nicht beachtet), von den buchstaben wird ingesamt die summe genommen 

# dann wird das result berechnent abschließend wird ein tupel erstellt mit runden klammern mit der anzahl der wörter, und die totale länge wird durch word count geteilt, das wird auf 2 stellen gerundet. wenn es word count gibt wird round(totaö.. berechnet, wenn nicht also wenns 0 ist wird der wert 0 zurückgegeben

# if word_count:    # wenn word_count größer 0 ist
#     average = round(total_length/word_count, 2)
#     result = (word_count, average)
# else:            # wenn word_count 0 ist
#     result = (word_count, 0)


# Task 4: Star Patterns (20 P)
# Write a script that uses for-loops to generate the following pattern. The
# maximum number of stars in a row should be provided at the beginning via
# input().
# *

# *

# *
# **
# *

# * p
# n = int(input("Gib die maximale Anzahl Sterne ein: ")) #zb 5
# # aufsteigend (1,6)
# for i in range(1, n + 1): #i=1, ... i=5
# print('*' * i) #'*' * 1 = ,.... '' * 5 = ***
# # absteigend (4, 0, -1) ende bei 1 (1 exklusive, n. gezählt)
# for i in range(n - 1, 0, -1): #i=4, i=3,.. i=1
# print('*' * i) # '*' * 4 = **,..... *

# zuerst gibt man eine zahl ein wieviele sterne man maximal haben will und castet es als ein int, dann geht man mit der schleife durch die zahlenfolge? mit der bedingung(start at 1 und gehe bis n+1 also 6 bei der eingabe 5) dann löuft i=1,...., i=5 und es wird ausgedruckt: stern * mal i ist erst ein stern,... bis stern * mal 5 sind 5 sterne

# jetzt kommt das absteigende mit der schleife durch die zahlenfolge mit der bedingung(start 4, stop 0 heist eig nur bis 1 weil es nicht inklusiv ist die 0 und rückwärts also -1) also i=4, ... bis i=1 und printet stern mal i also erst 4 stere  und immer weniger bis 1 stern






# Task 5: Binary Conversion (30 P)
# Write a script that accepts a decimal number from the user, converts it into
# a binary number, and displays it on the screen. Before conversion, check
# 2
# whether the input is a valid decimal number (only digits 0–9). If the input
# contains anything other than digits, display "Invalid Input!"

# num = input("Enter a decimal number: ") #13 wird als string '13'
# if num.isdigit(): #prüft ob nur nr von 0-9 (12a=false, 13 =true)
# n = int(num) # aus string zahl machen
# binary = '' #leerer string f. binärzahlen 0en und 1en
# while n: #solange n nicht 0 ist..
# binary = str(n % 2) + binary #n%2 rest bei division durch 2 , rest vorne anfügen
# n //= 2
# print(binary if binary else '0') #if binary nicht leer print binary, else wenns leer ist print 0
# else:
# print("Invalid Input!")

# es gibt eine benutzereingabe bei der man eine zahl eingeben soll die als string gespeihert wird
# dann wird geprüft ob die zahl eine zahl nur aus ziffern ist nicht aus buchstaben oder so. dann wird die zahl in einen integer gecastet. wir erstellen einen leeren string für die binary zahlen später. dann gibts ne while loop die löuft solange n nicht 0 ist und dabei wird die zahl mit % 2 genommen und als string gespeichert, zb 13 ergibt geteilt mit 2 rest 1 also steht vorne der rest (binary) 1 und n//=2 bedeutet es wird die ganzzahl geteilt mit 2 das wäre 6
# dann wird falls binary nicht 0 ist binary gedruckt ansonsten der string 0  gedruckt. ansonsten falls es eine falsche eingabe ist wird invalid inpit gedruckt












# """
