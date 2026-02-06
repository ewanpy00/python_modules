class Plant():
    def __init__(self, name :str, water_level:int):
        self.name = name
        self.water_level = water_level
    def water(self, amount:int):
        
class GardenError(Exception):
    """Base class for garden-related exceptions."""
    pass

class PlantError(GardenError):
    """Exception raised for errors related to plants."""
    pass

class WaterError(GardenError):
    """Exception raised for errors related to watering."""
    pass

def ft_custom_errors()