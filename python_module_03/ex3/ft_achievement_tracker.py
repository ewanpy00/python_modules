class Player:
    def __init__(self, achivements: list[str], name: str):
        self.achivements = achivements
        self.name = name

    def show_achivements(self) -> None:
        print(f"Player {self.name} achivements: {self.achivements}")


def ft_achievement_tracker() -> None:
    set_a = set({'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'})
    set_b = set({'first_kill', 'level_10', 'boss_slayer', 'collector'})
    set_c = set(
            {'level_10', 'treasure_hunter',
                'boss_slayer', 'speed_demon', 'perfectionist'}
            )

    alice = Player(set_a, "alice")
    bob = Player(set_b, "bob")
    charlie = Player(set_c, "charlie")

    print("=== Achievement Tracker System ===")
    alice.show_achivements()
    bob.show_achivements()
    charlie.show_achivements()

    unique = (
        set_a.difference(set_b.union(set_c))
        .union(set_b.difference(set_a.union(set_c)))
        .union(set_c.difference(set_a.union(set_b)))
    )
    print(f"All unique achievements: {set_a.union(set_b, set_c)}")
    print(f"Total unique achievements: {len(set_a.union(set_b, set_c))}")
    print(f"\nCommon to all players: {set_a.intersection(set_b, set_c)}")
    print(f"Rare achivements: {unique}\n")
    print(f"{alice.name} vs {bob.name} common: {set_a.intersection(set_b)}")
    print(f"{alice.name} unique: {set_a.difference(set_b, set_c)}")
    print(f"{bob.name} unique: {set_b.difference(set_a, set_c)}")


if __name__ == "__main__":
    ft_achievement_tracker()
