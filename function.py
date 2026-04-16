'''FUNCTIONS
(1) DEFINE vs CALL
(2) Parametr vs Argument
(3) Keyword & default argument
(4) Scope
'''

print("======DEFINE(parametr) vs CALL(argument)=======")
# built in function > print() type()
# Function - reusable block of code!
# Instend of block {} in JAVA, Python uses indentation!


# DEFINE - build - parametr
def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL - execute - argument
result = greet('Norman')
print("result:", result)

result1 = greeting("Daniel")
print("result1:", result1)
