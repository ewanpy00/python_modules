class PlantError(Exception):
    """Base class for plant-related exceptions."""
    pass

class Plant():
    def __init__(self, name :str):
        self.name = name
        self.water_level = 50

    def water(self):
        print(f"Watering {self.name}")
        self.water_level += 30

def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise PlantError(f"Cannot water {plant} - invalid plant!")
            plant.water()
    except PlantError as e:
        print(f"Error: {e}")
    finally:
        print(f"Closing watering system (cleanup)")

def test_watering_system():
        print("=== Garden Watering System ===\n")
        plants = [Plant("rose"), Plant("tulip"), Plant("daisy")]
        plants_error = [Plant("rose"), Plant("tulip"), Plant("daisy"), None]
        print("Testing normal watering...")
        water_plants(plants)
        print("Watering completed successfully!\n")
        print("Testing with error...")
        water_plants(plants_error)
        print("\nCleanup always happens, even with errors!")

if __name__ == "__main__":
    test_watering_system()