def validate_ingredients(ingredients: str) -> str:
    print(f"validate_ingredients(\"{ingredients}\"): ", end="")
    if (
        "fire" in ingredients
        or "air" in ingredients
        or "earth" in ingredients
        or "water" in ingredients
    ):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"