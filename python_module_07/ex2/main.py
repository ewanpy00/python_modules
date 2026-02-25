from ex2.EliteCard import EliteCard

def main():
    print("=== DataDeck Ability System ===\n")

    card = EliteCard("name", 1, "rare")
    card.show_capabilities()
    card.get_combat_stats()
    card.get_magic_stats()
    print("Multiple interface implementation successful!")

if __name__ == "__main__":
    main()