


"""

# list
courses = ['History', 'math', 'Physics', 'CompSci']
print(courses[0]) #index
# last value to get last item
print(courses[-1])

print(courses[0:2]) #index 2 not included
print(courses[2:]) #startet at index 2 und went to the end

# slicing
#append method

courses.append('Art')
print(courses)

courses_2 = ['Art', 'Education']
courses.insert(0, courses_2) #added to courses: ['Art', 'Education'] from courses_2
print (courses) #at the beginning of index 0
"""

"""
# extend
courses = ['History', 'math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']

courses.extend(courses_2)
print(courses) # setzt art und education ans ende; append würde die liste an sich ans ende setzen also , ['Art', 'Education']
# extend macht jedes individuelle item ans ende
"""

"""
#remove items

courses = ['History', 'math', 'Physics', 'CompSci']
courses.remove('math')
print(courses) # math removed

popped = courses.pop() # removes last item from list, compsci ist weg
print(popped) # print compsci aus
print(courses)

"""

"""
#sorting

courses = ['History', 'math', 'Physics', 'CompSci']
courses.reverse() # print compsci, physics...
print(courses)

courses.sort() # alphabetical order

nums = [1,5,2,4,3]
nums.sort() # sortet alphabetically
print(nums)

# sorting in descending order

courses.sort(reverse=True)
nums.sort(reverse=True)
print(courses)
print(nums) # 5,4,3,2,1
"""

courses = ['History', 'math', 'Physics', 'CompSci']
nums = [1,5,2,4,3]
"""
sorted_courses = sorted(courses) # getting sorted version of list without altering the original
print(sorted_courses)

#min, max, sum

print(min(nums)) #1
print(max(nums))

print(sum(nums)) #15 alle zusammengezählt

#index of compsci finden

print(courses.index('CompSci')) #3 index von compsci

print('Art' in courses) #checking if item is in list
"""
"""
#looping through each value of
for item in courses:
    print(item) #prints out all items, history, math, physiscs,, auf neuer zeile makes new line
    #koennten es auch for course in course nennen, egal
"""
"""
#
for index,course in enumerate(courses): #returns index were on and the value
    print(index,course) # prints 0 history, 1 math, ..

for index, course in enumerate(courses, start=1):  # fängt an mit 1 history
    print(index, course)  # prints 0 history, 1 math, ..
"""
"""
#join method
course_str = ' - '.join(courses)
print(course_str) # kriegen nun - seperat mit History - math - physics

new_list = course_str.split(' - ') # jetzt ist es nicht mehr mit - sondern , wie vorher mit komma
print(new_list)
"""




"""

# tuples cant modify tuples are not mudable

list_1 = ['History', 'math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2) # nun anstelte von history steht art am anfang
#aber ich habe nur list_1 geändert und art hinzugefügt, jedoch ist ebenso list 2 genauso verändert, das
#ist weil die sind beide das gleiche mutable objekt

"""


"""

#tuple macht man anstelle [ bei list die normelen (
#
tuple_1 = ('History', 'math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2) # gleiche werte

tuple_1[0] = 'Art' # kriegen error, tuple doesnt support item assignment, tuple
#man kann nix hinzufügen, loschen, bei tuples
#sonst verhalten die sich gleich, durchloopen, access values auch
#brauchst du was zum bearbeiten: list;
#wenn du nur was zum durchloopen und access braucht: tuple

print(tuple_1)
print(tuple_2)





"""
"""
#sets sind values that are unordered
#nutzen {
#the order changes all the time beim printen
cs_courses = {'History', 'math', 'Physics', 'CompSci'}
print(cs_courses)

#sets dont care about order, ob wert
art_courses = {'History', 'math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses)) # printet out history und math (gemeinsamkeiten)
print(cs_courses.difference(art_courses)) # printet out physis, compsci nicht in art courses
print(cs_courses.union(art_courses)) # printet out alle von beiden sets

#to create empty list:

empty_list = []
empty list = list()

#to create empfy tuple:

empty_tuple = ()
empty_tuple = tuple()

#empty set
empty_set = {}
empty_set = set()
"""