from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():

    print("=== DataDeck Tournament Platform ===\n")

    print("Registering Tournament Cards...\n")

    platform = TournamentPlatform()

    dragon = TournamentCard(
        "Fire Dragon",
        5,
        "Legendary",
        7,
        5,
        rating=1200
    )

    wizard = TournamentCard(
        "Ice Wizard",
        4,
        "Epic",
        5,
        6,
        rating=1150
    )

    dragon_id = platform.register_card(dragon, "dragon_001")
    wizard_id = platform.register_card(wizard, "wizard_001")

    print(f"\n{dragon.name} (ID: {dragon_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon.rating}")
    print(f"- Record: {dragon.wins}-{dragon.losses}")

    print(f"\n{wizard.name} (ID: {wizard_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard.rating}")
    print(f"- Record: {wizard.wins}-{wizard.losses}")

    print("\nCreating tournament match...")

    result = platform.create_match(dragon_id, wizard_id)

    print("Match result:", result)

    print("\nTournament Leaderboard:")

    leaderboard = platform.get_leaderboard()

    position = 1

    for card_id, name, rating, wins, losses in leaderboard:

        print(
            f"{position}. {name} - Rating: {rating} ({wins}-{losses})"
        )

        position += 1

    print("\nPlatform Report:")

    report = platform.generate_tournament_report()

    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")

    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()