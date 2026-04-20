'''OBJECTS
(1) What is object
(2) Iterable objects & RANGE
(3) DICTIONARY
(4) Error handling system
'''

import array  # package/module
import math
from math import ceil
print("======What is object======")
# An object has state and method propersties.
# Everything is object in Python!

print(type("Hello World"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigm > Functional Programming & OOP
# OOP 4 Concepts > Abstraction |Encaptulation | Inheritence | Polimorphism
result = math.ceil(97.7)  # CALL
print("result:", result)

result1 = ceil(98.7)
print("result1:", result1)


print("======Error handling system======")
car_dict = dict(name="Tayota", year=2026, electric=True)
try:
    print("passed here")
    a = car_dict.speed
    result = car_dict["origin"]
    print("result:", result)
except Exception as err:
    print("General found:", err)
else:
    print("Executed successfylly without errors")
finally:
    print("Final closing logic")
