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

































"""