from ex0.Card import Card

class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.attack = 10
        self.health = 5

    def play(self, game_state: dict) -> dict:
        print(f"Playing {self.name} with {self.total_mana} mana available:")
        if self.is_playable(self.total_mana) == True:
            print("Playable: True")
            self.total_mana -= self.cost
            result = {f'card_played': self.name, 'mana_used': self.cost, 'effect': 'Deal 3 damage to target'}
        else:
            print("Playable: False")
        if result is not None:
            print("Play result: ", end="")
            print(result)
        return result

    def resolve_effect(self, targets: list) -> dict:
        pass