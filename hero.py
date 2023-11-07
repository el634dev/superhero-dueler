import random
from weapon import Weapon
from armor import Armor
from ability import Ability


class Hero:
    # Want a default starting health
    def __init__(self, name, health=100):
        """
        :Instance abilities: list
        :Instance armors: list
        :param name: String
        :param starting_health: Integer
        :Instance current_health: Integer
        """
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.deaths = 0
        self.kills = 0
        self.starting_health = health
        self.current_health = health

    def add_ability(self, ability):
        """
        :desc: Add ability to self.abilities list
        :param ability: Object
        :return: self.abilities
        """
        # Add ability objects to self.abilities
        self.abilities.append(ability)

    # -------------------------------------
    def attack(self):
        """
        :desc: Calculate the total damage from all ability attacks
        :return: total_damage, an integer
        """
        # Start at 0
        total_damage = 0
        # loop through all the hero's abilities
        for ability in self.abilities:
            # add the damage to each attack to total_damage
            current_damage = ability.attack()
            total_damage += current_damage
        return total_damage

    # -------------------------------------
    def add_kill(self, num_kills):
        """
        :desc: Update self.kills by num_kills amount
        :param num_kills:
        :return: self.kills
        """
        self.kills += num_kills

    # -----------------------------------------
    def add_death(self, num_deaths):
        """
        :desc: Update deaths with num_deaths
        :param: self
        :param: num_deaths
        """
        # This method should add the number of deaths to self.deaths
        self.deaths += num_deaths

    # -----------------------------------------
    def add_weapon(self, weapon):
        """
        :desc: Add weapon to self.abilities
        :param: self
        :param: weapon
        """
        # This method will append the weapon object passed in as an argument to self.abilities.
        # This means that self.abilities will be a list of abilities and weapons.
        self.abilities.append(weapon)
    # -------------------------------------

    def defend(self, armor):
        """
        :desc: Calculate the total block amount from all armor blocks
        :param: self, self.armor is a list
        :return: total_block, an integer
        """
        # Start at 0
        total_block = 0
        # loop through all the hero's armor
        for block in self.armors:
            # run the block method on each armor in self.armors
            total_block += block.block()
        return total_block

    # -------------------------------------
    def add_armor(self, armor):
        """
        :desc: Add armor to self.armors similar to the add_abilities method
        :param armor: Object
        :return: self.armors
        """
        # Add armor that is passed into self.armor
        self.armors.append(armor)

    # -------------------------------------
    def take_damage(self, damage):
        """
        :desc: Updates self.current_health to reflect the damage minus the defense.
        :parm self: Reference to the instance
        :param damage: Integer
        """
        # Create a method that updates self.current_health to the current health minus the amount
        # returned from calling self.defend(damage).
        if damage <= self.current_health:
            self.current_health -= self.defend(damage)
            return self.current_health
        else:
            self.current_health -= damage
            return self.current_health

    # -------------------------------------
    def is_alive(self):
        """
        :desc: Return True or False depending on whether the hero is alive or not.
        :param: self
        """
        # if self.current_health <= 0, then return False. Otherwise, they still have health
        if self.current_health <= 0:
            return False
        else:
            return True
        # and are therefore alive, so return True

    # -------------------------------------
    def fight(self, opponent):
        """
        :desc: Current Hero will take turns fighting the opponent hero passed in.
        :param: self
        :param: opponent, uses properties from the Hero Class
        """
        # TODO: Fight each hero until a victor emerges.
        # Phases to implement:
        # 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
        loser = self
        round_count = 0
        if len(self.abilities) == 0 or len(opponent.abilities) == 0:
            print("Draw")
        else:
            # 1) else, start the fighting loop until a hero has won
            while self.is_alive() == True and opponent.is_alive() == True:
                # the hero (self) and their opponent must attack each other and
                # each must take damage from the other's attack
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())
                round_count += 1
                # 3) After each attack, check if either the hero (self) or the opponent is alive
                if not self.is_alive():
                    self.deaths += 1
                    print(f"After fighting {round_count} round_count(s) and {self.deaths} deaths")
                    print(f"{self.name} lost! Opponent has {self.kills} kills")
                    return loser
                if not opponent.is_alive():
                    opponent.deaths += 1
                    print(f"After fighting {round_count} round_count(s) and {self.deaths} deaths")
                    print(f"{opponent.name} lost! Hero has {self.kills} kills")
                    loser = opponent
            # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop
            return f"{loser} wins!"

# If ran from the terminal, this block is executed
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
