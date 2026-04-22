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


print("=======Conditon=======")
x = 15

if x > 50:
    print("Case A")
elif x > 10:
    print("Case B")
else:
    print("Case C")

print("-----")

print("=======Conditon=======")
age = 21
# person = None

# if age > 16:
#     person = "adult"
# else:
#     person = "child"

# print("person:", person)

# Ternary
person = "adult" if age > 16 else "miner"
print("person:", person)

print("-----")

is_student = True
is_admin = False
is_parent = True
is_guest = False

if not is_student:
    print("Welcome here! do you wante to be student")
elif is_admin:
    print("Please go to this office")
elif is_parent or is_guest:
    print("Waiting room is over there!")
else:
    print("Other cases")
