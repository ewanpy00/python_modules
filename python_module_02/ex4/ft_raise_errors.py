class PlantError(Exception):
    """Base class for plant-related exceptions."""
    pass

class Plant():
    def __init__(self, name :str, water_level: int, sunlight_hours: int):
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours
        self.check_plant_health(self.name, self.water_level, self.sunlight_hours)

    def check_plant_health(self, plant_name, water_level, sunlight_hours):
        if water_level < 1 or water_level > 10:
            raise PlantError(f" Water level {water_level} is invalid (max 10, min 1) ")
        elif not plant_name:
            raise PlantError(" Plant name cannot be empty!")
        elif sunlight_hours < 2 or sunlight_hours > 12:
            raise PlantError(f" Sunlight hours {sunlight_hours} is invalid (max 12, min 2) ")
        print(f"Plant {plant_name} is healthy!")


    # def water(self):
    #     print(f"Watering {self.name}")
    #     self.water_level += 30

def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")
    # plants = [Plant("rose", 5, 6), Plant("tulip", 3, 4), Plant("daisy", 2, 8)]
    # plants_error = [Plant("", 5, 6), Plant("tulip", 50, 4), Plant("daisy", 2, -2)]
    plants_data = [("rose", 5, 6), ("", 3, 4), ("daisy", 50, 8), ("lily", 2, -2)]
    for plant in plants_data:
        try:
            Plant(*plant)
        except PlantError as e:
            print(f"Error:{e}")
    print("All error raising tests completed!")

if __name__ == "__main__":
    test_plant_checks()