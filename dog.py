# Create Dog class
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark_action(self):
        print("Woof!")

    def sit_action(self):
        print(f"{self.name} sits")

    def roll_action(self):
        print(f"{self.name} rolled over")

