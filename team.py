import random


class Team:
    def __init__(self, name):
        """
        :desc: Initialize your team with its team name and an empty list of heroes
        :param name: String
        """
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        """
        :desc: Remove hero from heroes list. If Hero isn't found return 0.
        :param name: String
        :return: Hero
        """
        found_hero = False
        # Loop through each hero in heroes list
        for hero in self.heroes:
            # If hero is found, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
                # set found_hero to True
                found_hero = True
        # If hero was not found return 0
        if not found_hero:
            return 0

    def view_all_heroes(self):
        """
        :desc: Prints out all heroes to the console.
        :param: self
        """
        # Loop over the list of heroes and print their names to the terminal one by one.
        for hero in range(len(self.heroes)):
            print(self.heroes[hero])
        return "Nothing found"

    def add_hero(self, hero):
        """
        :desc: Add Hero object to self.heroes.
        :param: self
        :param: hero, object
        """
        # Add the Hero object that is passed in to the list of heroes in self.heroes
        self.heroes.append(hero)

    def stats(self):
        """
        :desc: Print team statistics
        :return: stats
        """
        for hero in self.heroes:
            ratio = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths Ratio:{ratio}")

    def revive_heroes(self, health=100):
        """
        :desc: Reset all heroes health to starting_health
        :param: self
        :param: health
        """
        # for each hero in self.heroes
        for hero in self.heroes:
            # set the hero's current_health to their health
            hero.current_health = health

    def attack(self, other_team):
        """
         Battle each team against each other.
        :param other_team:
        :return:
        """
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            # 1) Randomly select a living hero from each team (hint: look up what random.choice does)
            random_heroes = random.choice(living_heroes)
            random_opponents = random.choice(living_opponents)
            # 2) have the heroes fight each other (Hint: Use the fight method in the Hero class.)
            remove_heroes = random_heroes.fight(random_opponents)
            remove_opponents = random_opponents.fight(random_heroes)
            # to reflect the result of the fight
            if remove_heroes in living_heroes:
                living_heroes.remove(remove_heroes)
            else:
                living_opponents.remove(remove_opponents)
