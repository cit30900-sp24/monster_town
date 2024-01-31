from town import Town

class Monster:
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