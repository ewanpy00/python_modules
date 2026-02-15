import sys


def ft_inventory_system() -> None:
    print("=== Inventory System Analysis ===")

    inventory = {}
    if len(sys.argv) == 1:
        print("Error: Ivalid amount of arguments!")
        return
    for arg in sys.argv[1:]:
        colon_index = -1
        for i in range(len(arg)):
            if arg[i] == ":":
                colon_index = i
                break
        if colon_index != -1:
            name = arg[:colon_index]
            quantity_str = arg[colon_index+1:]
            try:
                quantity = int(quantity_str)
                inventory.update({name: quantity})
            except ValueError:
                print("Error: invalid argument format", end="")
                print(f" '{arg}', should be name:quantity")
                return
    total_items = 0
    for total in inventory.values():
        total_items += total
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")
    print("\n=== Current Inventory ===")
    for item, val in inventory.items():
        percent = val/total_items * 100
        print(f"{item}: {val} units ({percent:.1f}%)")
    print("\n=== Inventory Statistics ===")
    min_key = None
    min_value = None
    max_key = None
    max_value = None

    for item, value in inventory.items():
        if min_value is None or min_value > value:
            min_key = item
            min_value = value
    for item, value in inventory.items():
        if max_value is None or max_value < value:
            max_key = item
            max_value = value
    print(f"Most abundant: {max_key} ({max_value} units)")
    print(f"Least abundant: {min_key} ({min_value} units)")

    print("\n=== Item Categories ===")
    moderate = dict()
    scarce = dict()
    abundant = dict()
    for item, quan in inventory.items():
        if(quan >= 1 and quan < 5):
            scarce.update({item: quan})
        elif(quan >= 5 and quan < 10):
            moderate.update({item: quan})
        elif(quan >= 10):
            abundant.update({item: quan})
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")
    print(f"Abundant: {abundant}")

    print("\n=== Management Suggestions ===")
    restock = dict()
    for item, value in inventory.items():
        if(value == 1):
            restock.update({item: value})
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")
    keys = list(inventory.keys())
    values = list(inventory.values())
    print(f"Dictionary keys: {keys}")
    print(f"Dictionary values: {values}")
    name = "swordd"
    exists = inventory.get(name)
    if(exists):
        print(f"Sample lookup - {name} in inventory: True")
    else:
        print(f"Sample lookup - {name} in inventory: False")


if __name__ == "__main__":
    ft_inventory_system()
