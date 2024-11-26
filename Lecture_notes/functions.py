"""
def hello_func():
    pass #wollen ncihts mit machen aber n. blank lassen
    
    

print(hello_func()) -> None





def hello_func():
    print('Hello function")
    
    

(hello_func()) -> Hello Function



hello_func()
hello_func()
hello_func()
hello_func() -> Hello Function 4x






def hello_func():
    return 'Hello function"
    
print(hello_func()) -> Hello function (ohne print gehts hier ned)




print(len('Test')) ->4





def hello_func():
    return 'Hello function"
    
print(hello_func().upper) -> HELLO FUNCTION








def hello_func(greeting, name = 'You'):
    return '{}, {}'.format(greeting, name)
    
print(hello_func('Hi)) -> Hi, You





def hello_func(greeting, name = 'You'):
    return '{}, {}'.format(greeting, name)
    
print(hello_func('Hi', name = 'Corey')) -> Hi, Corey








def student_info(*args, **kwargs):
    -Docstring mit jeweils 3 anführungszeichen dazwischen-
        print(args)
        print(kwargs)
        
        
student_info('Math', 'Art', name='John', age=22) -> ('Math', 'Art') {'name': 'John', 'age': 22}





courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses,**info)  -> ('Math', 'Art') {'name': 'John', 'age': 22}





schaltjahr berechnen:

def is_leap(year):

    return year % 4 == 0 and (year % 100 != 0 or year % 400 ==0)


print(is_leap(2017))









VIDEO 2



def happy_birthday():
    print('Happy birthday')
    print('yeare old)
    Print('happy birthday to you)
    print()

happy_birthday() -> alles kommt raus
happy_birthday()
happy_birthday() ->3x





def happy_birthday(name):
    print(f'Happy birthday to {name}!') ->happy birthday to Bro
    print('yeare old)
    Print('happy birthday to you)
    print()

happy_birthday('Bro')








def happy_birthday(name,age):
    print(f'Happy birthday to {name}!') ->happy birthday to Bro
    print(f'yeare {age} years old')
    Print('happy birthday to you)
    print()

happy_birthday('Bro', 20)







def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice('BroCode', 42.34, '01/01') -> Hello BroCode
                                        -> your bill of 42.32 is due: 01/01
                                        







RETURN

def add(x,y):
    z = x+y
    return z
    

def subtract(x,y):
    z = x-y
    return z



print(add(1,2)) -> 3
print(subtract(1,2)) -> -1









def create_name(first,last):
    first = first.capitalize()
    last = first.capitalize()
    return first + " " + lat
    
full_name = create_name('bro', 'code')
print(full_name)
























nr 2 funktionen: 
def is_prime(number):
    if number <= 1:
        return False  # zahlen kleiner oder gleich 1(zb -5,0,1) keine primzahlen
    if number <= 3:
        return True  # 2 und 3 sind die einzigen kleinen primzahlen, hier wäre Zahl 2 oder 3=true
    if number % 2 == 0 or number % 3 == 0:
        return False  # ist zahl gerade?(außer 2), danach ist die durch 3 teilbar?(außer 3);  4,6,8 -> false


# für alle übrigen Zahlen Check...
#starten bei 5 , weil wir 2 und 3 schon geprüft haben
    # primzahlen-theorie, Primzahlen > 3 haben die Form 6k±1 die n. durch 2 oder 3 teilbar sind
    i = 5
    while i * i <= number: #schleife läuft nur, solange quadr. von i kleiner oder gleich der zahl nr ist
        # Wir prüfen nur bis zur Wurzel der Zahl
        # Beispiel für 25: 
        # i=5: 5*5=25 ≤ 25 (ja, prüfen)
        # i=11: 11*11=121 > 25 (nein, fertig)
        if number % i == 0 or number % (i + 2) == 0: #prüft ob number durch i oder i+2 teilbar ist, wenn teilbar dann false
            return False
        # Prüft zwei Zahlen auf einmal:
        # i und (i+2)
        # Bei i=5 prüfen wir also 5 und 7
        # Bei i=11 prüfen wir 11 und 13
        # usw.
        i += 6 #nach jedem durchlauf wird i um 6 erhöht
        # Der Trick: Wir springen in 6er-Schritten!
        # Von 5 zu 11 zu 17 zu 23...
        # Warum? Weil mögliche Primzahlen oft in der Form 6k±1 kommen

    return True
print(is_prime(7))    # True, weil 7 nur durch 1 und sich selbst teilbar
print(is_prime(12))   # False, weil 12 durch 2,3,4,6 teilbar
print(is_prime(2))    # True, weil 2 die kleinste Primzahl ist
print(is_prime(1))    # False, weil 1 per Definition keine Primzahl ist




aufgabe 3

#palindrom = text, der vorwärts und rückwarts gleich gelesen wird, zb "anna", "A man, a plan, a canal: Panama"
#char.isalnum(): prüft ob zeichen alphnum. ist(buchst. od. ziffern) A -> true, ' ' -> false, ',' -> false
#char.lower -> wandelt groß in kleinbuchst. um, damit groß/kleinschr. ignor. wird 'A' -> 'a'
#''.join(..) -> fügt bereinigte zeichen zu neuen string zsm : amanaplanacanalpanama
def is_palindrome(string):
    #groß,kleinschreibung wird ignoriert(lower())
    #sonderzeichen, leerzeichen,satzzeichen entfernt, isalnum()prüft nur buchstaben und zahlen
    #for char in string: itertiert d. jeden buchst. eingabe durchgänge: A, '', 'm',...
    cleaned = ''.join(char.lower() for char in string if char.isalnum())
    #cleaned[::-1] erstellt rückwärtsversion durch slicing: nimm ganzen string cleaned und lies ihn von hint. na. vorne
    #amanaplanacanalpanama wird zu amanaplanacanalpanama
    return cleaned == cleaned[::-1]
#prüft ob bereinigter string cleaned gleich mit rückwärsversion cleaned[::-1] ist, wenn ja palindrom


test_string_1 = "A man, a plan, a canal: Panama"
result_1 = is_palindrome(test_string_1)
print(result_1)  # Erwartet: True


aufgabe 4


def is_anagram(string1, string2):
    # for char in string1 und string2: nimmt jedes zeichen der eingaben einzeln zb 'a gentleman' -> 'A', '', 'g'
    # if char.isalnum() filtert alle n.alphanum. Zeichen(leerzeichen,satzzeichen), entf. leerzeichen,!,.
    # char.lower() wandelt großbuchs. in klein um A -> a
    # ''.join() fügt verbleibende zeichen zu neuen bereinigten string zsm a gentleman -> agentleman
    cleaned1 = ''.join(char.lower() for char in string1 if char.isalnum())
    cleaned2 = ''.join(char.lower() for char in string2 if char.isalnum())
    # sorted(cleaned1) zerlegt bereinigten string in liste v. buchstab., sortiert alphabetisch : agentleman: a,a,e,e,g
    #wenn sortierte zeichenlisten identisch sind ['a', 'a', 'e', 'e', 'g', = ['a', 'a', 'e', 'e', 'g', -> True
    return sorted(cleaned1) == sorted(cleaned2)


string1 = "listen"
string2 = "silent"
result = is_anagram(string1, string2)
print(result)  # True



aufgabe 5

def common_divisor(int1, int2, int3):
    # schleife beginnt bei 2 (weil 1 immer ein teiler ist) und schauen alle zahl. von 2 bis zur kleinsten zahl der drei eingaben an
    # wenn eingaben 12,18,24 sind, ist kleinste zahl 12. Schleife prüft zahlen 2,3,...12
    for i in range(2, min(int1, int2, int3) + 1):  # Teste von 2 bis zur kleinsten Zahl.
        #min weil, der ggt von den drei zahlen nie größer als die kleinste der drei zahlen sein kann
        #bedingung prüft, ob i gemeinsamer teiler der drei zahlen ist
        #wenn i die erste z, die zweite z. und die dritte z. teilt, dann ist i gemeinsamer teiler
        if int1 % i == 0 and int2 % i == 0 and int3 % i == 0:
            #sobald gemeinsamer teiler gefunden wird, wird zurückgegeben, f. 12,18,24 erster ggt 2 gefunden u. gegeben
            return i  # Rückgabe, sobald ein gemeinsamer Teiler gefunden wird.
#wenn keine ggt größer als 1 findet, gibt 1 zurück, zb wenn zahlen primzahlen sind und kein ggt auser 1 haben
    return 1  # Wenn kein gemeinsamer Teiler existiert, außer 1.


result = common_divisor(12, 18, 24)
print(result)  # Erwartet: 2

result = common_divisor(7, 11, 13)
print(result)  # Erwartet: 1


aufgabe 6

#zwei eingabewerte: string, der text, den wir kodieren od. dekodieren wollen
#decoding: ein optionaler wert, wenn er true ist, wird text dekodiert, ansonsten kodiert
def encode(string, decoding=False):
    #wenn decoding wahr ist:
    if decoding:
        # string.split: der text (der reihe von zahlen enthält, die durch leerzeichen getrennt) wird in liste v. einzelnen zahlen geteilt
        #int(num)+96: jede wird wird in ganzzahl gewandelt, u. wir addieren 96, um richtigen asci wert des buchst. zu haben
        #zb int("8") #96 = 104, asci wert für h
        #chr() wandelt asci wert zurückk in buchstaben um, zb chr(104) ergibt 'h'
        #join: alle buchstaben werden zu einzigen string zusammengef. ohne leerzeichen
        #zb: 'h','e',.. wird zu 'hello'
        return ''.join(chr(int(num) + 96) for num in string.split())
    else: # wenn decoding falsch:
        # string.lower: text in kleinbuchst. gewandelt, damit großbuch auch kodiert werden, HeLLo -> hello
        #if char.isalpha() schauen dass nur buchstab(keine zahlen oder zeichen kodiert werden)
        #ord(char) -96: für jeden buchstaben wird asci wert berechnet, und wir subtrah 96, um zahl zu erhalten
        #zb ord('h') = 104, also 104-96 = 8
        #str: zahl wird in str verwandelt
        #join: alle zahlen werden durch leerzeichen getrennt u zu einem einzigen string zusammengef.
        #zb '8', '5','12',.. wird zu '8 5 12,..'
        return ' '.join(str(ord(char) - 96) for char in string.lower() if char.isalpha())


# Test 1: Kodierung von "hello"
encoded = encode("hello")
print("Encoded:", encoded)  # Erwartet: "8 5 12 12 15"

# Test 2: Dekodierung von "8 5 12 12 15"
decoded = encode("8 5 12 12 15", decoding=True)
print("Decoded:", decoded)  # Erwartet: "hello"


















"""