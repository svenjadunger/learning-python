"""
while
„Tu etwas, bis eine bestimmte Bedingung erfüllt ist“, am besten durch eine sogenannte „while-Schleife“ ausdrücken, die die folgende grundlegende Syntax hat:

while [BEDINGUNG, die eine Variable verwendet]:
# tue dies, solange die Bedingung erfüllt ist
# aktualisiere die Bedingungsvariable, sodass die Bedingung irgendwann nicht mehr erfüllt ist und die Schleife endet


Das zweite Szenario, d. h. „Tu etwas mit jedem Element in einer Sammlung von Elementen“, lässt sich am besten durch eine sogenannte „for-Schleife“ mit der folgenden Syntax ausdrücken:


for num in [1,2,3,4,5]:
# drucke die Zahl aus, die die Schleifenvariable „num“ in der aktuellen Iteration annimmt
print(num)


for [LOOP_VARIABLE] in [ITERABLE OBJECT]:
# tue dies


print("meow")
print("meow")
print("meow")

i = 3
while i != 0:
    print("meow") -> endless loop
    
    i = i - 1 // asking question again again aber changing value immer 1 weniger bis es irgendwann 0 erreicht
    

i = 0
while i < 3: up to but not through 3
    print("meow")
    i = i + 1 normalerw. zählt man von 0 aus -----> i += 1 ++ gibts ned in python
    

for i in [0,1,2]:
    print("meow") -> meow meow meow  -> nicht gut
    
    
for _ in range(3):
    print("meow") -> 3 values  _ heißt ja its a variable but its not necessary to name
    
    
print("meow" * 3) meowmeowmeow


print("meow\n" * 3, end="") jezt gibts am ende kein leerzeichen mehr
    


while: infinitve loop the answer is always true, wenn wir nbr haben ausbrechen aus loop
while True:
    n = int(input("whats n?"))
    if n > 0:
        break
        
for _ in range(n):
    print("meow")

// wenn wir 10 eingeben kommt 10x meow


funktionen::
def main():
    meow(3)
    
    
def meow(n):
    for _ in range(n):
        print("meow")
        
main() meow meow meow




def main():
    number = get_number()
    meow(number)
    
    
def get_number():
    while True:
        n = int(input("Whats n?"))
        if n > 0:
            break
        return n
    
    
def meow(n):
    for _ in range(n):
        print("meow")
        


LIST

students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)
    

for i in range(len(students)):
    print(studetns[i])   //hermione harry ron
    

for i in range(len(students)):
    print(i + 1, studetns[i])  1 hermione, 2 harry, 3 ron




for _ in range(3):
    print("#")

def main()
    print_column(3)
    
def print_column(height):
    print('#\n * height, end="")
        
main()





def main():
    print_row(4)
    
def print_row(width):
    print("?" * width)  /????
    
    
main()






def main()
    print_square(3)
    
    
    
def print_square(size):

#for each row in square
    for i in range(size):
    
    #for each brick in row
        for j in range(size):
        
        #print brick
            print('#', end="")
        print()
        
      /  ###
        ###
        ###


main()








def print_square(size)

    for i in range(size):
        print('#' * size)

main()



VIDEO 2





nums = [1,2,3,4,5]

for num in nums:
    if num == 3:
     print('found!')
     break
    print(num) // 1,2,3,4,5
    


nums = [1,2,3,4,5]

for num in nums:
    if num == 3:
     print('found!')
     break
  print (num) // 1,2 found!
    


for num in nums:
    if num == 3:
     print('found!')
     continue
  print (num) // 1,2 found! 4,5
  
  
nums = [1,2,3,4,5]

for num in nums:
    for letter in 'abc':
        print(num,letter) / 1a, 1b, 1c, 2a, 2b, 2c


WHILE LOOP













































"""
