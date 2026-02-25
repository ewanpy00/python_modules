from ex0.Card import Card

class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        print(f"Playing {self.name} with {self.total_mana} mana available:")
        if self.is_playable(self.total_mana) == True:
            print("Playable: True")
            self.total_mana -= self.cost
            result = {f'card_played': self.name, 'mana_used': self.cost, 'effect': 'Permanent: +1 mana per turn'}
        else:
            print("Playable: False")
        if result is not None:
            print("Play result: ", end="")
            print(result)
        return result

    def activate_ability(self) -> dict:
        pass