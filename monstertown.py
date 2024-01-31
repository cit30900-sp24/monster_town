import math
import random

class Town():

    def __init__(self, name: str, population: int, buildings: int, stoplights: int):
        """Create a new instance of Town"""
        self.name = name
        self.population = population
        self.buildings = buildings
        self.stoplights = stoplights
        self.monsters = [] # A list of Monster objects

    def description(self) -> str:
        return f"{self.name} has a population of {self.population}, {self.buildings} buildings, and {self.stoplights} stoplights."
    
    def update_population(self, amount: int):
        self.population += amount
    
    def update_buildings(self, amount: int):
        self.buildings += amount
    
    def update_stoplights(self, amount: int):
        self.stoplights += amount

class Monster():
    def __init__(self, name: str, height: float, weight: int):
        """Initialize a new instance of the Monster class. Height is measured in meters. Weight is measured in pounds."""
        self.name = name
        self.height = height
        self.weight = weight
        self.location = None # The datatype here will be a Town

    def say_hello(self):
        return f"Hi, my name is {self.name}."
    
    def describe_activity(self):
        if self.location == None:
            return f"{self.name} is totally bored."
        else:
            return f"{self.name} is terrorizing {self.location.name}."
        
    def terrorize_town(self, target: Town) -> Town:
        """Monster attacks modify the population, buildings, and stoplights"""
        
        # Update the Monster to set the location to the target
        self.location = target

        # Print a message to the screen about what is happening
        print("A monster is attacking!", self.describe_activity())

        # Subtract 50 from the population
        self.location.update_population(-50)

        # Subtract 10 from the buildings
        self.location.update_buildings(-10)

        # Subtract 5 from the stoplights
        self.location.update_stoplights(-5)

        return self.location
    
class Vampire(Monster):
    def __init__(self, name: str, height: float, weight: int):
        super().__init__(name, height, weight)

    def terrorize_town(self, target: Town) -> Town:
        
        # Set the monster's location to the target
        self.location = target

        # A vampire only takes out one person
        self.location.update_population(-1)

        # Print a message about what is happening
        print("A vampire is attacking!", self.describe_activity())

        return self.location
    
class Mutant(Monster):
    def __init__(self, name: str, height: float, weight: int):
        super().__init__(name, height, weight)

    def terrorize_town(self, target: Town) -> Town:
        """Mutant attacks result in random damage to population, buildings, and stoplights."""
        # TODO: Update the Monster to set the location to the target
        self.location = target

        # TODO: Print a message to the screen about what is happening
        print('\nA mutant is attacking!!', self.describe_activity(), '\n')

        # TODO: Get a random number from 1 to 10% of the population and subtract it from the population
        pop_change = random.randint(1, math.floor(target.population*.1))
        target.population = target.population - pop_change

        # TODO: Get a random number from 1 to 15% of the buildings and subtract it from the buildings
        building_change = random.randint(1, math.floor(target.buildings*.15))
        target.buildings = target.buildings - building_change

        # TODO: Get a random number from 1 to 12% of the stoplights and subtract it from the stoplights
        stoplights_change = random.randint(1, math.floor(target.stoplights*.12))
        target.stoplights = target.stoplights - stoplights_change

        return target