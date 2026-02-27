from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.total_mana = 9
    
    @abstractmethod
    def play(self, game_state: dict) -> dict:
        print(f"Playing {self.name} with {self.total_mana} mana available:")
        if self.is_playable(self.total_mana) == True:
            print("Playable: True")
            self.total_mana -= self.cost
            return {f'card_played': self.name, 'mana_used': self.cost, 'effect': 'Creature summoned to battlefield'}
        else:
            print("Playable: False")

    def get_card_info(self) -> dict:
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity,
            'type': 'Creature',
            'attack': self.attack,
            'health': self.health
        }

    def is_playable(self, available_mana: int) -> bool:
        if self.cost <= available_mana:
            return True
        else:
            return False