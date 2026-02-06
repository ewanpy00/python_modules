def ValidateError(temp: int) -> None:
    if temp > 40:
        raise ValueError(f"Error: {temp}°C is too hot for plants (max 40°C)")
    elif temp < -20:
        raise ValueError(f"Error: {temp}°C is too cold for plants (min 0°C)")

def ft_first_exception(tmp_str: str) -> None:
    print(f"Testing temperature: {tmp_str}")
    try:
        value = int(tmp_str)
        ValidateError(value)
        print(f"Temperature {value}°C is perfect for plants!")
    except ValueError:
        print(f"Error: '{tmp_str}' is not a valid number")

def test_temperature_input() -> None:
    testcases = ["100", "Hello", "30", "-10", "-100", "abc"]
    print("=== Garden Temperature Checker ===")
    for tmp_str in testcases:
        ft_first_exception(tmp_str)
        print("")

if __name__ == "__main__":
    test_temperature_input()