import sys

def ft_command_quest():
    print("=== Command Quest ===\n")
    i = 1
    print(f"Program Name: {sys.argv[0]}")
    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments recieved: {len(sys.argv) - 1}\n")
    for args in sys.argv:
        print(f'Argument {i}: {args}')
        i += 1
    print(f"Total arguments: {i - 1}")

if __name__ == "__main__":
    ft_command_quest()