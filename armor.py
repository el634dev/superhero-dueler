import random

# Hero Armor
class Armor:
    def __init__(self, name, max_block):
        '''
        :desc: Initialize the values passed into this method as instance variables.
        :param name: String type, name of hero
        :param max_block: Integer Type
        '''
        # Assign the name and max_damage for a specific instance
        self.name = name
        self.max_block = max_block

    def block(self):
        # Return a random value between 0 and max_block strength
        random_block = random.randint(0, self.max_block)
        return random_block


if __name__ == "__main__":
    # When this file is from the terminal
    # this block is executed
    ability = Armor("Debugging Shield", 20)
    print(ability.name)
    print(ability.block())
