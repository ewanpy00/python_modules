
def garden_operations():
    print("Testing ValueError...")
    try:
        10/0
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)
    print("Testing FileNotFoundError...")
    try:
        open("non_existent_file.txt", "r")
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e)
    print("Testing IndexError...")
    try:
        garden = ["flowers", "shrek", "42"]
        print(garden[5])
    except IndexError as e:
        print("Caught IndexError:", e)
    print("Testing ValueError...")
    try:
        int("not_a_number")
    except ValueError as e:
        print("Caught ValueError:", e)
    print("Testing multiple errors together...")
    try:
        int("not_a_number")
        15/0
        garden2 = ["flowers", "shrek", "42"]
        print(garden2[5])
        open("non_existent_file.txt", "r")
    except Exception as e:
        print("Caught an error, but program continues!")

def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("")
    print("All error types tested successfully!")
    

if __name__ == "__main__":
    test_error_types()