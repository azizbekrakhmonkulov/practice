print("===== number =====")
# in JAVA, variable is a name storage location!
# in Python, variable is named reference!

count = 100
count_type = type(count)
# print("count:", count, count_type)
print(f"The count: {count} and type: {count_type}")

result = count.bit_count()  # method
result1 = count.numerator  # state
print(result, result1)


print("===== string =====")
# Methods: upper(), lower(), title(), find(), replace()

course = "AI Python FillStack"
result = type(course)
print(f"The result (1); {result}")

result = course.title()
print(f"The result (2); {result}")

result = course.upper()
print(f"The result (3); {result}")

result = course.replace("FillStack", "MasterClass")
print(f"The result (4); {result}")
print(course)


print("===== boolean =====")
# functions > type() input() bool() int() str()

y = input("Give your value for y:")
print("y:", y)

result = y.isnumeric()
print(f"The input value is numeric: {result}")

# TRUTHY vs FALSY value
# TRUSHY: True 100 -100 "MIT"

test_falsy = "" or False or None or 0
print("test falsy:", bool(test_falsy))

test_truthy = "" "MIT"
print("test truthy:", bool(test_truthy))
