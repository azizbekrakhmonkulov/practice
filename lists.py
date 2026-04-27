'''List
(1) Working with lists
(2) List methods
(3) Lambda function
(4) enumerate, map and filter
'''

print("=====Working with lists======")
# JAVA/PHP/NodeJS array => Python list


# literal
person = {"name": "Jastine", "age": 25}  # dict
people = ("Norman", "Aziz", "Alex")  # tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # list
for team in groups:
    print(f"the team: {team}")


# constroctor
letters = list("Hello World!")
print(f"the letters: {letters} and size: {len(letters)}")


print("-------")
fruits = ["apple", "orange", "lemon", "kiwi"]

a = fruits[0]
b = fruits[0:2]
c = fruits[::3]
d = fruits[::-1]

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)


print("=====List methods======")
# methods > append() insert() pop() remove() clear() sort() index()

letters = ["a", "d", "b"]

letters.append("c")  # add behind
print(f"the append result: {letters}")

letters.insert(0, "z")  # add front
print(f"the insert result: {letters}")

size = len(letters) - 1
result1 = letters.pop(size)  # pop behind
print(f"the pop result: {result1} and letters: {letters}")

result2 = letters.pop(0)  # pop front
print(f"the pop result: {result2} and letters: {letters}")


print("-------")
animals = ["dog", "cat", "capybara", "fish", "line"]
print("animals:", animals)

animals.remove("line")
print("remove:", animals)

del animals[2:4]
print("animals delete:", animals)

exist = animals.index("cat")
print("cat exist:", exist)

animals.clear()
print("animals clear;", animals)


if "cat" in animals:
    print("index of cat", animals.index("cat"))
else:
    print("cat does not exist")

print("------")
numbers = [2, 5, 17, 8, 12]
numbers.sort()
print("numbers:", numbers)
numbers.sort(reverse=True)
print("sort reverse:", numbers)

# immutable sorted sorted function & index() method
numbs = [2, 20, 47, 199]
new_numbs = sorted(numbs)
print(f"the sorted numbs: {numbs} and new nuw_numbs: {new_numbs}")


print("=====Lambda function======")
# lambda is small anonymous function


def calculate(x, y): return x * y


result = calculate(3, 5)
print("result:", result)

people = [
    ("Robert", 20),
    ("Steve", 19),
    ("Joseph", 25),
    ("Michael", 30),
    ("Ali", 40)
]

people.sort()
print("people(1)", people)

# sort by age via lambda
people.sort(key=lambda person: person[1])
print("person(2)", people)


print("=====enumerate, map and filter======")

animals = ["dog", "cat", "fish"]
for element in enumerate(animals):
    print("element:", element)

for (index, value) in enumerate(animals):
    print(f"index: {index} and value: {value}")

print("-------")

car_obj = dict(brand="Ferrari", years=2025)
result = car_obj.items()
for (key, value) in result:
    print(f"index: {key} and value: {value}")

print("-------")
# map
cars = [
    ("Ferrari", 78),
    ("Tayota", 87),
    ("Audi", 116),
    ("BMW", 109)
]

new_cars = []
for car in cars:
    new_cars.append(car[0])
    print("new_car:", new_cars)

result1 = map(lambda car: car[0], cars)
print(f"the result: {result1} and type: {type(result1)}")
new_cars = list(result1)
print("new_cars(1)", new_cars)

print("-------")
# filter
result_filter = filter(lambda car: car[1] > 80, cars)
print(f"the result_filter: {result_filter} and type: {type(result_filter)}")
print(list(result_filter))
