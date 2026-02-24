from alchemy.grimoire import validate_ingredients

def ft_circular_curse():
    print("=== Circular Curse Breaking ===\n")
    print("Testing ingredient validation:")
    print(validate_ingredients("fire"))
    print(validate_ingredients("ai r"))
    print("\nTesting spell recording with validation:")
    from alchemy.grimoire.spellbook import record_spell
    print(record_spell("Fireball", "fire air"))
    print(record_spell("Dark Magic", "shadow"))
    print("\nTesting late import technique:")
    print(record_spell("Lightning", "air"))
    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")

ft_circular_curse()