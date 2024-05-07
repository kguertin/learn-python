# Object Oriented Programming

# Class - A blueprint for objects. A class describes what properties and functionality individual objects will contain.
class Dog:
    def __init__(self, name, breed, location):
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []

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
