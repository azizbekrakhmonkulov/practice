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
