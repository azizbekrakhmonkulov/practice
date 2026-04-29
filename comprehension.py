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


print("==== Set and dictionary comprehesion ====")
numbs = [1, 4, 5, 14, 4, 5, 14]
set_numbs = {*numbs}
print("set_numbs:", set_numbs)  # a version

dict_people = {person[0]: person[1] for person in people}
print("dict_people:", dict_people)  # b version

dict_people2 = {person[0]: person[1] for person in people if person[1] > 20}
print("dict_people2:", dict_people2)  # c version
