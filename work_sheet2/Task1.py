from math import sqrt

a = float(input("Whats number a? "))
b = float(input("Whats number b? "))
c = float(input("Whats number c? "))

print(f"Number a is: {a}")
print(f"Number b is: {b}")
print(f"Number c is: {c}")

if (b**2 - 4 * a * c) > 0:
    x1 = round((-b - sqrt(b**2 - 4 * a * c)) / (2*a), 4)
    x2 = round((-b + sqrt(b**2 - 4 * a * c)) / (2*a), 4)
    print(f"The result for x1 is: {x1}")
    print(f"The result for x2 is: {x2}")


