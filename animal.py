# This will be the superclass
class Animal:
    def __init__(self, name):
        self.name = name

    def animal_eats(self):
        return f"{self.name} is eating!"

    def animaL_drinks(self):
        return f"{self.name} is drinking!"

# Class that will inherit from Animal
class Frog(Animal):
    def jump(self):
        return f"{self.name} is jumping!"

# Instance of Animal
animal_1 = Animal("Rex")
print(animal_1.animal_eats())
print(animal_1.animaL_drinks())
print("-------------------------")

# Instance of Frog
frog_1 = Frog("Froggy")
print(frog_1.animal_eats())
print(frog_1.animaL_drinks())
print(frog_1.jump())
