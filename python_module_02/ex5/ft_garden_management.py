class GardenError(Exception):
    """Base class for garden-related exceptions."""
    pass

class PlantError(GardenError):
    """Exception raised for errors related to plants."""
    pass

class WaterError(GardenError):
    """Exception raised for watering errors."""
    pass


class Plant:
    def __init__(self, name: str, water_level: int, sunlight_hours: int):
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours
        self.check_plant_health()

    def check_plant_health(self):
        if not self.name:
            raise PlantError("Plant name cannot be empty!")
        if self.water_level < 1 or self.water_level > 10:
            raise PlantError(f"Water level {self.water_level} is invalid (max 10, min 1)")
        if self.sunlight_hours < 2 or self.sunlight_hours > 12:
            raise PlantError(f"Sunlight hours {self.sunlight_hours} is invalid (max 12, min 2)")

    def water(self):
        if self.water_level >= 10:
            raise WaterError(f"Cannot water {self.name}: water level already full ({self.water_level})")
        self.water_level += 3
        print(f"Watering {self.name} - success")


class GardenManager:
    def __init__(self):
        self.plants = []
        self.watering_open = False

    def add_plant(self, name, water_level, sunlight_hours):
        try:
            plant = Plant(name, water_level, sunlight_hours)
            self.plants.append(plant)
            print(f"Added {name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def open_watering_system(self):
        print("Opening watering system")
        self.watering_open = True

    def close_watering_system(self):
        print("Closing watering system (cleanup)")
        self.watering_open = False

    def water_all_plants(self):
        self.open_watering_system()
        try:
            for plant in self.plants:
                try:
                    plant.water()
                except WaterError as e:
                    print(f"Error watering {plant.name}: {e}")
        finally:
            self.close_watering_system()

    def check_all_plants_health(self):
        for plant in self.plants:
            try:
                plant.check_plant_health()
                print(f"{plant.name}: healthy (water: {plant.water_level}, sun: {plant.sunlight_hours})")
            except PlantError as e:
                print(f"Error checking {plant.name}: {e}")

    def test_error_recovery(self):
        try:
            raise GardenError("Not enough water in tank")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
            print("System recovered and continuing...")


def test_garden_management():
    print("=== Garden Management System ===\n")
    
    print("Adding plants to garden...")
    manager = GardenManager()
    manager.add_plant("tomato", 5, 8)
    manager.add_plant("lettuce", 15, 10)  
    manager.add_plant("", 3, 6)           

    print("\nWatering plants...")
    manager.water_all_plants()

    print("\nChecking plant health...")
    manager.check_all_plants_health()

    print("\nTesting error recovery...")
    manager.test_error_recovery()

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()