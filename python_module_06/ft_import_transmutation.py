def ft_import_transmutation():
    print("=== Import Transmutation Mastery ===")

    import alchemy.elements
    print("\nMethod 1 - Full module import:")
    print(alchemy.elements.create_fire())

    from alchemy.elements import create_water
    print("\nMethod 2 - Specific function import:")
    print(create_water())

    from alchemy.potions import healing_potion as heal
    print("\nMethod 3 - Aliased import:")
    heal()

    from alchemy.elements import create_air, create_earth, create_fire, create_water
    from alchemy.potions import streng_potion, wisdom_potion, healing_potion, invisibility_potion
    print("\nMethod 4 - Multiple imports:")
    print(create_earth())
    print(create_fire())
    streng_potion()

ft_import_transmutation()