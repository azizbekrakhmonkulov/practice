'''Comprehension
(1) What is comprehension & list comp.
(2) Set and dictionary comp.
'''

print("==== What is comprehension & list comprehension====")
# Comprehension acts like spread operator!

''' Comprehension general syntax:
(a) *iterable
(b) <expression> for item in iterable
(c) <expression> for item in iterable <conditon>
'''

# list comp.
numbers = [1, 2, 4, 8, 15, 33]
list_numbers = [*numbers]  # a version

print("list_numbers:", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))

print("-----")
people = [("Robert", 21), ("Steve", 19), ("Joseph", 32)]
list_people = [name[0] for name in people]  # b version
print("list_people:", list_people)

print("-----")
cars = [
    ("Ferrari", 78),
    ("Tayota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("MERS", 68)
]
list_cars = [car[0] for car in cars if car[1] > 80]  # c version
print("list_cars", list_cars)
