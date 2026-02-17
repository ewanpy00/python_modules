def ft_data_alchemist() -> None:
    print("=== Data Alchemist Mastery ===\n")
    raw_data = [
        ("Alice", 120, "First Kill"),
        ("Bob", 85, "Treasure Hunter"),
        ("Charlie", "avb", "Boss Slayer"),
        ("Alice", 50, "Speed Demon"),
        ("Eve", 200, "Perfectionist"),
        ("Bob", 30, "Boss Slayer")
    ]
    print("=== List Comprehension Examples ===")
    try:
        high_scorers = [
            player for player, score, ach in raw_data if score > 100
            ]
        print(f"High Scorers: {high_scorers}")
    except Exception as e:
        print("An error occured:", e)
    print("\n=== Set Comprehension Examples ===")
    try:
        unique_achievements = {ach for _, _, ach in raw_data}
    except Exception as e:
        print("An error occured:", e)
    print(f"Unique Achievements: {unique_achievements}")
    print("\n=== Dict Comprehension Examples ===")
    try:
        player_status = {
            player: score
            for player, score, _ in raw_data
        }
        print(f"Player Status Map: {player_status}")
    except Exception as e:
        print("An error occured:", e)
    print("\n=== Combined Analysis ===")
    try:
        print(f"Total players: {len(raw_data)}")
        avg_score = sum(score for _, score, _ in raw_data) / len(raw_data)
        print(f"Average score: {avg_score:.1F}")
        print(f"Total unique achivements: {len(unique_achievements)}")
        top = max(raw_data, key=lambda x: x[1])
        print(f"Top performer: {top}")
    except Exception as e:
        print("An error occured:", e)


if __name__ == "__main__":
    ft_data_alchemist()
