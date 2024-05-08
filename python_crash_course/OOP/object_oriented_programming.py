# Object Oriented Programming

# Class - A blueprint for objects. A class describes what properties and functionality individual objects will contain.
class Dog:
    def __init__(self, name, breed, location):
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []

    def bark(self):
        print(f"{self.name} says 'WOOF!'")

    def learn_trick(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)

    def perform_trick(self, trick):
        if trick in self.tricks:
            print(f"{self.name} performs {trick}")
        else:
            print(f"{self.name} does not know {trick} :(")


finn = Dog("Finn", 'Cockapoo', "Toronto")
print(isinstance(finn, Dog))
print(finn.name)
print(finn.location)
print(finn.breed)
print(finn.tricks)

jules = Dog("Jules", "Corgi", "New York")
print(isinstance(jules, Dog))
print(jules.name)
print(jules.location)
print(jules.breed)
print(jules.tricks)

# Instance Methods
finn.bark()
finn.learn_trick("sit")
finn.learn_trick("down")
finn.learn_trick("down")
print(finn.tricks)
finn.perform_trick('down')
finn.perform_trick('rollover')

jules.learn_trick("stay")
jules.perform_trick("stay")
jules.perform_trick("sit")

