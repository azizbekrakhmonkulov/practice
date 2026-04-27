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
