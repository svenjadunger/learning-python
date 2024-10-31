# a complex conditional statement joined by and evaluates to True if and only if each component conditional statement has the value True
# a complex conditional statement joined by or evaluates to True if and only if at least one of the component conditional statements has the value True
"""
and =checks two or more conditions if true
or =checks if at least one conditios is true
not = true if condition is fale
"""

temp = 25

if temp > 0 and temp < 30:
    print('The temp is good')
else:
    print("the temp is bad")


if temp > 0 or temp >= 30:
        print('The temp is good')
else:
        print("the temp is bad")

sunny = False

if not sunny:
    print('its cloudy')
else:
    print("its sunny")