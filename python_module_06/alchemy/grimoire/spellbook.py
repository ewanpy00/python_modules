def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    print(f"record_spell {spell_name}: ", end="")
    validation_res = validate_ingredients(ingredients)
    if "VALID" in validation_res:
        return f"Spell recorded, {validation_res}"
    else:
        return f"Spell rejected, {validation_res}"