def ft_data_alchemist() -> None:
    print("=== Data Alchemist Mastery ===\n")

    raw_data: list[tuple[str, int, str]] = [
        ("Alice", 120, "First Kill"),
        ("Bob", 85, "Treasure Hunter"),
        ("Charlie", 150, "Boss Slayer"),
        ("Alice", 50, "Speed Demon"),
        ("Eve", 200, "Perfectionist"),
        ("Bob", 30, "Collector")
    ]

    high_scorers: list[str] = [player for player, score, ach in raw_data if score > 100]
    print(f"High Scorers (List Comp): {high_scorers}")

    unique_achievements: set[str] = {ach for _, _, ach in raw_data}
    print(f"Unique Achievements (Set Comp): {unique_achievements}")

    player_status: dict[str, str] = {
        player: "Pro" if score > 100 else "Amateur" 
        for player, score, _ in raw_data
    }
    print(f"Player Status Map (Dict Comp): {player_status}")

    report: list[str] = [
        f"LOG: {p.upper()} achieved {a}" 
        for p, s, a in raw_data if s >= 150
    ]
    print("\n=== Advanced Report ===")
    for entry in report:
        print(entry)

if __name__ == "__main__":
    ft_data_alchemist()