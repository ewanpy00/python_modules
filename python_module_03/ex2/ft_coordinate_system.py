import sys
import math


def parse_args(arg: str) -> tuple[int, int, int]:
    result = arg.split(",")
    x = int(result[0])
    y = int(result[1])
    z = int(result[2])
    return x, y, z


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===\n")
    origin = (0, 0, 0)
    if len(sys.argv) < 2:
        return
    for arg in sys.argv[1:]:
        print(f'Parsing coordinates: "{arg}"')
        try:
            current_pos = parse_args(arg)
            x1, y1, z1 = origin
            x2, y2, z2 = current_pos
            print(f"Position created: ({arg})")
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            distance = math.sqrt(pow(dx, 2) + pow(dy, 2) + pow(dz, 2))
            print(f"Distance between {origin}", end="")
            print(f" and {current_pos}: {distance:.2F}\n")
            x, y, z = current_pos
            print(f"Unpacking demonstration:\nPlayer at x={x}, y={y}, z={z}")
            print(f"Coordinates: X={x}, Y={y}, Z={z}\n")
        except ValueError as e:
            print("Error parsing coordinates:", e)
            print(f"Error details - Type: {type(e).__name__} ", end="")
            print(f"Args: {e}")


if __name__ == "__main__":
    ft_coordinate_system()
