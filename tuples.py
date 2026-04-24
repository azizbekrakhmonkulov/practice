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

# try avoid this
people = "Norman", "John"

print("======Unpacking arguments=====")
groups = ["MIT", "FLEXY", "devEX", "MG"]
(x, v, *z) = groups
print(f"the x: {x} and v: {v}")
print("z:", z)  # list

# *args > tuple


def calculate(*args):
    print("*args >", args)
    total = 1
    for x in args:
        total *= x
    # print(f"the type(args) value: {type(args)}")
    print(f" the total value: {total}")
    return total


# call
calculate(1, 7, 2, 3)
print("-------")
calculate(0, 2, 200)
print("-------")
calculate(5, 8)


print("-------")

# **kwargs > dict


def introduce(**kwargs):
    print(f"the type value: {type(kwargs)}")
    print(f"Hi, I am {kwargs["name"]} and I am {kwargs["age"]} years old!")


# CALL
introduce(name="Norman", age=23)
introduce(name="Alex", age=34, single=True)


def greeting(*args, **kwargs):
    print("*args >", args)
    print("**kwargs >", kwargs)


# CALL
greeting("hi", True, 10, name="John", age=23)
