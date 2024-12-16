"""




Hier sind die wichtigsten Punkte zu Sets in Python:

Sets werden mit geschweiften Klammern {} oder set() erstellt
Hauptmerkmale von Sets:

Ungeordnet (keine feste Reihenfolge der Elemente)
Nur eindeutige Elemente (keine Duplikate)
Können nur unveränderbare (hashable) Datentypen enthalten wie:

Strings
Zahlen
Tuples
(NICHT: Listen, Sets, Dictionaries)




Praktischer Anwendungsfall:

Liste in Set umwandeln um Duplikate zu entfernen
Schnelles Identifizieren eindeutiger Werte in einer Datenmenge



Also kurz: Sets sind nützlich wenn man eine ungeordnete Sammlung eindeutiger, unveränderlicher Elemente braucht.
we can add und remove aber nicht duplikate

Video1:
sets no dpulikats, unordered

cs_courses = {'history', 'math', 'physics', 'compsci'}
print(cs_courses)
---> die order changes bei ausführen, they dont care about order

print('math' in cs_courses) -> true

print(cs_courses.intersection(art_courses)) what do they have in common : history and math
.difference -> verschiedene courses


empty list: [] oder list()

empty tuple: () oder tuple()

empty set: {}(its a dictonary!) oder set()




print(dir(fruits)) printet alles aus

fruits.add("pineapple")
.remove
.pop() removes the first element?
.clear() alle elemente löschen

tuples: duplikates ok, faster, ordered und unchangeable

.count()




DICTONARIES

Grundkonzept:

Speichert Schlüssel-Wert-Paare (key-value pairs)
Jeder Schlüssel (key) ist mit einem Wert (value) verbunden


Eigenschaften:

Schlüssel müssen "hashable" (unveränderbar) sein
Werte können beliebige Datentypen sein
Schneller Zugriff auf Werte über ihre Schlüssel


Praktisches Beispiel:

Wörterbuch mit Wörtern (keys) und ihren Vektoren (values)
Schnelles Nachschlagen von Werten über ihre zugehörigen Schlüssel



Also kurz: Dictionaries sind ideal, wenn man Daten in Paaren organisieren und schnell über einen Schlüssel darauf zugreifen möchte.



CS50

DICTONARY

word and definitions
keys and values, something assoziating with someting else
is two dimensional
words with their definitions 


students = ['hermione', 'harry', 'ron']
hoouses = ['gryffindor', 'griffindor', 'griffindor', 'slytherin']

student with a house assoziating

students = {
'hermione': 'griffindor',
'harry': 'griffindor,
'ron': 'grffindor',
'draco': 'slytherin'
}

they allow words as indexes: hermione ist der key und griffendor der value

print(students['hermione']) griffendor
print(students['harry'])
print(students['ron'])
print(students['draco']) slytherin


for student in students:
    print(student) // hermione, harry, ron, draco (just the keys)
    
for student in students:
    print(student, students[student]) //mit haus dazu hermione griffendor, harry griffendor
    
for student in students:
    print(student, students[student, sep=", "]) #seperator, dann hermione, griffendor
    


students = [ #its a list with dictonaries inside(collection of key value pairs)
#4 dictonaries with three keys: name, house, patronus, values: hermione, house, otter
    {"name": "hermione", "house": "griffendor", "patronus": "otter},
    {"name": "harry", "house": griffendor, "Patronus": "stag},
    {"name": "ron", "house": "grirfendor", "patronus": "jack russell tierr"},
    {"name": "dracO", "house": "slytherin", "patronus": None}
]

    
for student in students:
    print(student["name"], student["house"], student["patronus"] sep=", ") name + hose




student = {'name: 'John, 'age: 25, 'courses: ['Math, 'compsi]}

print(student['courses]) ->math, compsi

print(student['phone]) - key error, exist. nicht

print(student.get('name)) - john 
print(student.get('phone)) None

print(student.get('phone, 'Not found)) Not found



Adding:
student['phone'] = "555-555"
student['name'] = "Jane " - jetzt ist name Jane

student.update({'name': 'Jane', 'age': 26, 'phone: '555-555'}) alles geupdatet

Delete values:

del student['age]  age is gelöscht
oder age = student.pop('age)
print(age) age wurde aus direc. gelsöscht und zu age variable hinzugef.

print(len(student)) 3

print(student.keys()) alle keys
oder.values()
oder items() alles, keys und values

for key, values in student.items():
    print(key, value)















"""