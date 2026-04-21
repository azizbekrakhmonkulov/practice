'''CLASS deep diving
(1) ENCAPSULATION <
(2) INHERITENCE
(3) POLIMORPHISM
'''

print("=======INHERITENCE=======")
# PARENT > CHILD
# Parent only give public & protected properties(state, method) to children!


class Animal:
    # state
    description = "This class is parent for animals"

    # constractor
    def __init__(self, voice):
        self.voice = voice
        self.status = "animal is alive"

    # method
    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):
    # constractor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def intraduce(self):
        print(f"{self.name} says: {self.sound}--{self.sound}")

    def protect(self):
        print("Yes I can protect you!")


class Cat(Animal):
    # constractor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def intraduce(self):
        print(f"{self.name} says: {self.sound}--{self.sound}")

    def play(self):
        print("Yes I can play with your child!")


class Fish(Animal):
    # constractor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def intraduce(self):
        print(f"{self.name} says: {self.sound}--{self.sound}")

    def swim(self):
        print("Yes I can swim under water!")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myow", True)
fish = Fish("Nemo", "ZzZ", False)

dog.intraduce()
fish.intraduce()
cat.intraduce()

print("------")
dog.make_voice()
fish.make_voice()

print("------")
print(Animal.description)
print(Dog.description)

print(dog.voice, fish.voice)
print("dog status:", dog.status)
