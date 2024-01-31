from monster import Monster

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

    