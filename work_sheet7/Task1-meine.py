
# def to_left_recursive(lst):
#     if len(lst) <= 1: #entweder leer oder genau 1
#         return lst #dann stoppe Rekursion
#     return [to_left_recursive(lst[:-1]), lst[-1]] 
# #if not, nehme alle Elemente außer letztes
# #funktion ruft sich selbst mit lst[:-1] auf. Der Rückgabewert wird zsm m. lst[-1] in neue liste gepackt



# print(to_left_recursive([]))          # []
# print(to_left_recursive([1, 2, 3, 4]))  # [[[1], 2], 3], 4]
# print(to_left_recursive([1])) 
