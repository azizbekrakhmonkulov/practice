'''CLASS
(1) What is class
(2) ordinary vs static properties
(3) special methods
'''

print("=======What is class======")
# Class - blueprint for object creation!
# Struction > state constructor method


class Person():
    # State
    message = "static state property"

    # Constructor
    def __init__(self, name, age,):
        self.name = name
        self.age = age

    # Method
    def introduce(self):
        print(f"{self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} says I am {self.age}!")

    @classmethod
    def explain(cls):
        print("static method property executed!")


person1 = Person("Norman", 23)
person2 = Person("Jonh", 33)
person3 = Person("Alex", 42)

# Ordinary state
print("person1:", person1.name)

# Ordinary method
person1.introduce()
person2.say_age()

print("======Ordinary vs static properties=======")
# static method
new_massage = Person.message
print("new_massage:", new_massage)

# static method
Person.explain()
