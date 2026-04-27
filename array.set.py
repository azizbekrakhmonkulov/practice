'''Array & Set
(1) Array
(2) Set
(3) Specific operators with set
'''
from array import array
print("=====Array=====")
numbers = array("i", [1, 2, 4, 5, 56, 33])

numbers.append(100)
numbers.insert(0, 14)
print("numbrs(2)", numbers)

numbers.remove(5)
numbers.pop()
print("numbrs(3)", numbers)

del numbers[0:2]
print("numbrs(4)", numbers)
