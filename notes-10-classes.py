# Classes and Objects
# Author: Carl Dicioco
# 11 December 2025

import random


class Pokemon:
    def __init__(self):
        # Initialize the properties of Pokemon
        self.name = "Squirtle"
        self.species = "Squirtle"
        self.type = "Water"
        self.age = 0
        self.hassunglasses = True
        self.level = 1
        print("A pokemon is born!")
        # One out of 4096 should be shiny
        # self.shiny = random.randint(4096)
        if random.randint(0, 4096):
            self.shiny = False
        else:
            self.shiny = True
            print(f"✨{self.name} is shiny!✨")

    def talk(self):
        """Hear what the pokemon has to say."""
        print(f'{self.name} says, "{self.species}".')

    def stats(self):
        """Display the stats of the Pokemon"""
        print(f"---{self.species}----------")
        print(f" Name: {self.name}")
        print(f" Type: {self.type}")
        print(f" Age: {self.age}")
        print(f" Level: {self.level}")
        print("---------------------------")

    def find_something(self, how_many_things=1) -> list[str]:
        """Send pokemon to find something"""
        things = [
            "pinap berry",
            "razz berry",
            "nanab berry",
            "golden razz berry",
            "leftovers",
            "moon stone",
        ]
        found_things = []
        for _ in range(how_many_things):
            found_things.append(random.choice(things))
        return found_things


class Squirtle(Pokemon):
    def __init__(self):
        super().__init__()
        self.name = "Squirtle"
        self.species = "Squirtle"
        self.type = "Water"
        self.shell_health = 100

    def water_gun(self):
        """Use the water gun attack."""
        print(f"{self.name} used Water Gun!")

    def withdraw(self):
        """Squirtle hides in its shell to reduce damage."""
        print(f"{self.name} withdrew into its shell!")
        self.shell_health += 10


if __name__ == "__main__":
    pokemon_one = Pokemon()
    print("Pokemon Name:", pokemon_one.name)

    pokemon_one.name = "Gary"
    print("Pokemon Name:", pokemon_one.name)

    pokemon_two = Pokemon()
    print("Pokemon two's name:", pokemon_two.name)

    if pokemon_one == pokemon_two:
        print("These are the same pokemon?")
    else:
        print("They're individual, distinct pokemon")

    if type(pokemon_one) is Pokemon:
        print(f"{pokemon_one.name} is a Pokemon.")
    if type(pokemon_two) is Pokemon:
        print(f"{pokemon_two.name} is a Pokemon.")

    pokemon_one.talk()
    pokemon_two.talk()
    pokemon_one.stats()
    pokemon_two.stats()

    squirtle_one = Squirtle()
    squirtle_one.talk()
    squirtle_one.water_gun()
    squirtle_one.withdraw()
