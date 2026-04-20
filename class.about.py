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


print("======Ordinary vs static properties=======")
# Pythod's most common special methods are below:
# __init__ __new__ __str__ __call__ __getitem__ __eq__ __len__ ...


class Car():
    # state
    description = "This class makes cars"

    # constructor
    def __new__(cls, *args):
        print("*__new__*")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # method
    def start_engine(self):
        print(f"the {self.name} started engine!")

    def stop_engine(self):
        print(f"the {self.name} stopped engine!")

    def __str__(self):
        return f"the car.name: {self.name} was produced in {self.year} year!"

    def __call__(self):
        print("Object called as fanction!")
        return True


my_car = Car("Ferrari", 2026)
my_car.start_engine()
my_car.stop_engine()

print("-----")
your_car = Car("Tayota", 2026)
print(your_car)
response = your_car()  # CALL
print("response:", response)
