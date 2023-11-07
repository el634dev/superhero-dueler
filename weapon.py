from ability import Ability
import random

class Weapon(Ability):
    def attack(self):
        """
        :desc: This method returns a random value between one half to the full attack power of the weapon.
        :return: A random integer
        """
        # Use // to find half of the max_damage value
        damage = self.max_damage // 2
        # Return a random integer between half of max_damage and max_damage
        random_value = random.randint(damage, self.max_damage)
        return random_value
