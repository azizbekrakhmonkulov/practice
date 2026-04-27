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

print("=====Set=====")
# set of unique collection without keeping order!
new_numbers = array("i", [1, 2, 4, 5, 56, 33])
numbs_set = set(new_numbers)

print(f"the numbs_set{numbs_set} and type {type(numbs_set)}")

numbs_set.add(200)
print("numbs_set1:", numbs_set)

numbs_set.add(5)
print("numbs_set2:", numbs_set)


print("=====Specific operators with set=====")
# | & - ^
a = {10, 20, 50}
b = {20, 40}

result1 = a | b  # union
result2 = a & b  # intersection
result3 = a - b  # difference
result4 = a ^ b  # symmetric difference

print("result1:", result1)
print("result2:", result2)
print("result3:", result3)
print("result4:", result4)
