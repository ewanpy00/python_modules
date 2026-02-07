class GardenError(Exception):
    """Base class for garden-related exceptions."""
    pass

class PlantError(GardenError):
    """Exception raised for errors related to plants."""
    pass

class WaterError(GardenError):
    """Exception raised for errors related to watering."""
    pass

class Plant():
    def __init__(self, name :str):
        self.name = name
        self.water_level = 50
        self.time = 0
        self.tunk = 0

    def fill_tunk(self, amount:int):
        self.tunk += 60

    def water(self, amount:int):
        if self.tunk <= 0:
            raise WaterError(f"The tunk is empty! Cannot water the {self.name} plant.")
        self.water_level += 30
        self.tunk -= 30

    def pass_time(self):
        if self.water_level <= 0:
            raise PlantError(f"The {self.name} plant is wilting!")
        self.time += 1
        self.water_level -= 30

def ft_custom_errors():
    print("=== Custom Garden Errors Demo ===\n")
    plant = Plant("tomato")
    try:
        print("Testing PlantError...")
        plant.pass_time()
        plant.pass_time()
        plant.pass_time()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    try:
        print("Testing WaterError...")
        plant.water(30)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    try:
        print("Testing catching all garden errors...")
        plant.pass_time()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        plant.water(30)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

if __name__ == "__main__":
    ft_custom_errors()