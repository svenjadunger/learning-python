"""

Einlesen und Schreiben in Dateien

Eine der am häufigsten verwendeten Operationen, die Ihnen in Ihrem Studium wahrscheinlich begegnen werden, ist das Arbeiten mit Daten, die in Dateien gespeichert sind. Sie müssen die Daten wahrscheinlich systematisch einlesen und eine Aufgabe damit ausführen. Möglicherweise möchten Sie auch einige Ergebnisse Ihres Programms in Dateien ausgeben. Für alle diese Aufgaben benötigen Sie Dateiverwaltungsoperationen in Python.

Dieses Video aus unserer Tutorial-Reihe bietet eine gute Beschreibung der Arbeit mit Dateien mithilfe von Python-Dateiobjekten.

Bitte beachten Sie:

Die verschiedenen Modi zum Öffnen einer Datei, d. h. „r“, „w“, „a“ usw. und was sie bedeuten
Die verschiedenen Methoden zum Lesen von Inhalten aus einer Datei, d. h. alles auf einmal einlesen vs. Daten zeilenweise einlesen vs. Datenblöcke einer vordefinierten Größe einlesen usw.

Wenn Sie lieber lesen als ein Video anzusehen, finden Sie in diesem Blogbeitrag detaillierte Beschreibungen.
F-Strings
Die Übungen für diese Woche behandeln auch die sogenannten „F-Strings“. Sie haben nicht direkt mit der Dateiverwaltung zu tun, sondern betreffen die Formatierung von Strings und bieten Ihnen einige äußerst nützliche Möglichkeiten, Informationen entweder auf die Standardausgabe oder in Dateien auszudrucken, die auf bestimmte von Ihnen angegebene Weise formatiert sind.

Hier ist ein Tutorial-Video dazu


VIDEO1

file objects
test.txt file in the same directory
how to open up a file

f = open('test.txt', 'r') r ist for reading, w ist for writing to a file und a is appending to a file, read and write ist r+

print(f.name)
f.close() > test.txt

print(f.mode) f.close() ->r


f = open('test.txt', 'r') 
f.close() close is wichtig for application could throw a error

context manager: 
with keyword


with open('test.txt', 'r') as f:   (f ist hier der variable name)
they allow us to work with files from within this block and after we excit it automatic. close the file for us



with open('test.txt', 'r') as f:
    f_contents = f.read()

    print(f_contents)  druckt den ganzen content
    
    
bei großen files will man nicht alles



with open('test.txt', 'r') as f:
    f_contents = f.readlines() kriegt liste von allen lines of files  readline -> first line of a file
    print(f_contents)

bei jedem drucken nächste line of a file





with open('test.txt', 'r') as f:
    f_contents = f.readlines() kriegt liste von allen lines of files  readline -> first line of a file
    print(f_contents, end='')





with open('test.txt', 'r') as f:


    for line in f:
        print(line, end='') reading all the lines and get one line at the time of a file
        1) this is a test file  2) with multiple lines 3).....




with open('test.txt', 'r') as f:
 f_contents = f.read() 
    print(f_contents, end='') kriegt das geliche 1) this is a test file  2) with multiple lines 3).....




f.read(100) man kriegt first 100 characters of a file



with open('test.txt', 'r') as f:
 f_contents = f.read(100) 
    print(f_contents, end='')





with open('test.txt', 'r') as f:

    size_to_read = 100   nimmt first 100 charac. of a file
 f_contents = f.read(size_to:read)
   
   while len(f_contents) > 0:
    print(f_contents end='')
     f_contents = f.read(size_to:read)
     
     


















"""