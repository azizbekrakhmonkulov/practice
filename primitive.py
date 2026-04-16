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
