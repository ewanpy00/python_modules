import sys
import math

def parse_args(arg: str) -> tuple[int, int, int]:
    result = arg.split(",")
    # if len(result) != 3:
    #     raise ValueError("Error, expected 3 values")
    x = int(result[0])
    y = int(result[1])
    z = int(result[2])
    return x, y, z

def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===\n")
    if len(sys.argv) < 2:
        return
    x2, y2, z2 = [0, 0, 0]
    x1, y1, z1 = [0, 0, 0]
    for arg in sys.argv[1:]:
        try:
            print(f'Parsing coordinates: "{arg}"')
            try:
                x1, y1, z1 = parse_args(arg)
            except ValueError as e:
                print(f"Error paring the", e)
            print(f"Position created: {arg}")
        except ValueError as e:
            print("Error parsing coordinates:", e)
            print(f"Error details - Type: {type(e).__name__} ", end="")
            print(f"Args: {e}")
        dx = x1 - x2
        dy = y1 - y2
        dz = z1 - z2
        distance = math.sqrt(pow(dx, 2) + pow(dy, 2) + pow(dz, 2))
        print(f"Distance between  and: {distance}\n")

ft_coordinate_system()