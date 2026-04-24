'''Tuple
(1) What is tuple: typle vs list
(2) Unpacking arguments
(3) Zip
'''

print("======What is tuple: typle vs list=====")
# JAVA/PHP/NodeJS array => Python list

# Literal
numbs = [3, 5, 1, 2]
car_dict = {"brand": "Ferrari", "year": 1999}
print(numbs)

# Constractor
latter = list("Hello world!")
person_dict = dict(name="Martin", age=34)
print(latter)

fruits = ["apple", "lemon", "banana", "kiwi"]
print("before:", fruits)

fruits[2] = "melon"
print("after:", fruits)

# tuple
# we can not mutate tuple
animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 1000, True, None)

print(animals[3])
# animals[0] = "bird"
