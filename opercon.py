''' OPERATORS & CONDITIONS
(1) Operators
(2) Condition
(3) Logical Operatos 
'''

print("=======Operators=======")
# + - > >= < <= * /    // % += **

a = 19
b = 5

# print("a > b:", a > b)
# print("a * b:", a * b)
# print("a / b:", a / b)

print(a / b)
result = a // b
left = a % b
print(f"butun raqam: {result} va qoldiq: {left}")

# a = a + 100
a += 100
print("a:", a)

print("a*a:", a**2)
print("b*b*b:", b**3)

print("="*5)

c = dict(name="Aziz", age=24)
d = dict(name="Aziz", age=24)
e = c

print("c and d:", c == d)  # only value
print(id(c), id(d), id(e))

print("c is d:", c is d)
print("e is c:", e is c)
