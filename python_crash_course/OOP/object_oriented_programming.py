# Object Oriented Programming

# Class - A blueprint for objects. A class describes what properties and functionality individual objects will contain.
class Dog:
    species = 'C. Lupus'
    num_dogs = 0

    @classmethod
    def register_stray(cls):
        return cls("Coming soon", "unknown", "unknown")

    def __init__(self, name, breed, location):
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []
        Dog.num_dogs += 1

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

# Class Attribute - class and all instances have this 
print(Dog.species)
print(finn.species)
print(jules.species)
print(Dog.num_dogs)

dog = Dog.register_stray()
print(dog.name, dog.breed)
print(Dog.num_dogs)

# Inheritance 
class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name} meows")


class Cougar(Cat):
    def purr(self):
        print(f"{self.name} purrs!!!")

dennis = Cougar("Dennis")
dennis.meow()
dennis.purr()

class Lion(Cat):
    def __init__(self, name, pride_name):
        super().__init__(name)
        self.pride_name = pride_name

    def roar(self):
        print(f"{self.name} ROARS!")

simba = Lion("Simba", "Pride 1")

simba.meow()
simba.roar()
print(simba.pride_name)

# Super 
