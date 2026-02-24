import alchemy.elements
import alchemy

def ft_sacred_scroll():
    print("=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access:")
    print(alchemy.elements.create_fire())
    print(alchemy.elements.create_air())
    print(alchemy.elements.create_earth())
    print(alchemy.elements.create_water())

    print("\nTesting package-level access (controlled by __init__.py):")
    try:
        print(alchemy.create_water())
        print(alchemy.create_fire())
        print(alchemy.create_earth())
    except AttributeError as e:
        print("AttributeError -", e)

    print("\nPackage metadata:")
    print(alchemy.__author__)
    print(alchemy.__version__)

ft_sacred_scroll()