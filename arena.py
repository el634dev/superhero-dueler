from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team


class Arena:
    def __init__(self):
        """
        :desc: Instantiate Properties
        :param: team_one, None
        :param: team_two, None
        """
        self.team_one = Team("team 1: ")
        self.team_two = Team("team 2:")

    def create_ability(self):
        """
        :desc: Prompt for Ability information.
        :return: Ability with values from user Input
        """
        name = input("What is the ability name? ")
        max_damage = input("What is the max damage of the ability? ")
        return Ability(name, max_damage)

    def create_weapon(self):
        """
        :desc: Prompt user for Weapon information
        :return: Weapon with values from user input.
        """
        # Prompt the user for the necessary information to create a new weapon object.
        weapon_name = input("What is the weapon name? ")
        weapon = input("What is max damage of the weapon? ")
        # return the new weapon object.
        return Weapon(weapon_name, weapon)

    def create_armor(self):
        """
        :desc: Prompt user for Armor information
        :return: Armor with values from user input
        """
        # Prompt the user for the necessary information to create a new armor object.
        armor_name = input("What is the armor name? ")
        armor = input("What is max damage of the armor? ")
        #  return the new armor object with values set by user.
        return Ability(armor_name, armor)

    def create_hero(self):
        """
        :desc: Prompt user for Hero information
        :return: Hero with values from user input.
        """
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1]Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                # Add an ability to the hero, First create the ability, then add it to the hero
                ability_input = input("Ability name: ")
                damage_input = int(input("Ability Damage: "))
                ability = Ability(ability_input, damage_input)
                hero.add_ability(ability)
            elif add_item == "2":
                # Add a weapon to the hero, First create the weapon, then add it to the hero
                weapon_input = input("Weapon name: ")
                damage_input = int(input("Max Damage: "))
                weapon = Weapon(weapon_input, damage_input)
                hero.add_weapon(weapon)
            elif add_item == "3":
                # Add an armor to the hero, First create the armor, then add it to the hero
                armor_input = input("Armor name: ")
                block_input = int(input("Block Damage: "))
                armor = Armor(armor_input, block_input)
                hero.add_armor(armor)
        return hero

    # build_team_one is provided
    def build_team_one(self):
        """
        :desc: Prompt the user to build team_one
        """
        # Prompt the user for the number of Heroes on team one
        num_of_team_members = int(input("How many members would you like on Team One?\n"))
        for i in range(num_of_team_members):
            # call self.create_hero() for every hero that the user wants to add to team one.
            hero = self.create_hero()
            # Add the created hero to team one.
            self.team_one.add_hero(hero)

    # Now implement build_team_two
    def build_team_two(self):
        """
        :desc: Prompt the user to build team_two
        """
        # Prompt the user for the number of Heroes on team two
        num_of_team_members_2 = int(input("How many members would you like on Team Two?\n"))
        for i in range(num_of_team_members_2):
            # call self.create_hero() for every hero that the user wants to add to team two.
            hero = self.create_hero()
            # Add the created hero to team two.
            self.team_two.add_hero(hero)

    def team_battle(self):
        """
        :desc: Battle team_one and team_two together.
        """
        # Call the attack method that exists in your team objects for that battle functionality.
        self.team_one.attack(self.team_two)
        self.team_two.attack(self.team_one)

    def show_stats(self):
        """
        :desc: Prints battle statistics to terminal including each team's average k/d ratio
        :param: self
        """
        # Required Stats:
        #     Show surviving heroes.
        #     Declare winning team
        #     Show both teams average kill/death ratio.
        # Some help on how to achieve these tasks:
        # for each team, loop through all of their heroes
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        # --------------------------------
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        alive_heroes = 0
        for hero in self.team_one.heroes:
            # and use the is_alive() method to check for alive heroes
            if self.team_one.heroes.is_alive(hero):
                # printing their names and increasing the count if they're alive.
                alive_heroes += 1
                print(f"{self.team_one.name} and there are {alive_heroes} alive.")

        for hero in self.team_two.heroes:
            # and use the is_alive() method to check for alive heroes
            if self.team_two.heroes.is_alive(hero):
                # printing their names and increasing the count if they're alive.
                alive_heroes += 1
                print(f"{self.team_two.name} and there are {alive_heroes} alive.")

        # Based off of your count of alive heroes, you can see which team has more alive heroes, and therefore,
        # declare which team is the winning team
        if self.team_one.heroes(alive_heroes) > self.team_two.heroes(alive_heroes):
            print("Team One wins!")
        else:
            print("Team Two wins!")

    def team_kd_ratio(self):
        """
        :desc: Calculate the average K/D ratio for both teams
        :return: average K/D ratio for each member in each teamm
        """
        # This is how to calculate the average K/D for Team One
        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.name + " average K/D ratio was: " + str(team_kills / team_deaths))

        # Now display the average K/D for Team Two
        team_2_kills = 0
        team_2_deaths = 0
        for hero in self.team_two.heroes:
            team_2_kills += hero.kills
            team_2_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_two.name + " average K/D ratio was: " + str(team_2_kills / team_2_deaths))

    def team_survivors(self):
        """
        :desc: List of heroes that survived from both teams
        :return: List of heroes that survived
        """
        team_survivors = list()
        team_kills = 0
        team_deaths = 0
        # Here is a way to list the heroes from Team One that survived
        for hero in self.team_one.heroes:
            team_deaths += hero.deaths
            team_kills += hero.kills
            if hero.is_alive():
                team_survivors.append(hero.name)
                print("Survived from " + self.team_one.name + ": " + hero.name)

        # Now list the heroes from Team Two that survived
        for hero in self.team_two.heroes:
            team_deaths += hero.deaths()
            team_kills += hero.kills
            if hero.is_alive():
                team_survivors.append(hero.name)
                print("Survived from " + self.team_two.name + ": " + hero.name)
        if len(team_survivors) > 0:
            print(f"The surviving members are {team_survivors}")



if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
