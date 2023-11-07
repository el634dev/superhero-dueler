import random

# Hero Ability
class Ability:
    def __init__(self, name, max_damage):
        '''
        :desc: Initialize the values passed into this method as instance variables.
        :param name: String type, name of hero
        :param max_damage: Integer Type, how much damage
        '''
        # Assign the name and max_damage for a specific instance
        self.name = name
        self.max_damage = max_damage

    def armor(self):
        '''
        :desc: Return a value between 0 and the value set by self.max_damage.
        :param: self, reference to the instance
        '''
        # Pick a random value between 0 and self.max_damage
        random_value = random.randint(0, self.max_damage)
        return random_value

    def attack(self):
        """
        :desc: Return a value between 0 and the value set by self.max_damage.
        :param: self, reference to the instance
        """
        # Pick a random value between 0 and self.max_damage
        random_value = random.randint(0, self.max_damage)
        return random_value

if __name__ == "__main__":
    # When this file is from the terminal
    # this block is executed
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
