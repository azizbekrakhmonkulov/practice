'''LOOP Operators
(1) For
(2) Break/else
(3) While
'''

print("===== for operator =====")
# Iterable objects > string dict tuple list range map filter
text = "MIT"
numb = [2, 7, 4, 29]
car_obj = dict(brand="BMW", year=2025)
range_obj = range(5)

for latter in text:
    print(f"the letter: {latter}")

print("======")
for number in numb:
    print(f"the number: {number}")

print("======")
for x in range_obj:
    print(f"the element: {x}")

print("======")
for key in car_obj:
    print(f"the key:{key} => value: {car_obj.get(key)}")

print("======")
for x in range(1, 20, 4):
    print(f"the x is: {x}")


print("===== break/else =====")

for x in range(1, 20, 4):
    print(f"the x is: {x}")
    if x > 15:
        print("Action stoped!")
        break
    else:
        print("error not ocured!")

print("===== while operator =====")
numb = 40
while numb > 0:
    numb -= 10
    print(f"the number is: {numb}")

print("------")
count = 0
while True:
    count += 1
    x = int(input("find number: "))

    if x == 41:
        print(f"you found the number in {count} attempt!")
        break
    else:
        print("wrong please search again!")
