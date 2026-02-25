from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.Card import Card
from abc import ABC

class EliteCard(Card, Combatable, Magical):
    def __init__(self, name, cost, rarity):
        super().__init__(name, cost, rarity)

    def play(self, game_state: dict) -> dict:
        if game_state["game state"] == "Combat phase":
            atack_result = self.attack("Enemy")
            print(f"Attack result: {atack_result}")
            defence_result = self.defend(5)
            print(f"Defence result: {defence_result}")
            return atack_result
        elif game_state["game state"] == "Magic phase":
            cast_result = self.cast_spell(self.name, ["Enemy1, Enemy2"])
            print(f"Spell cast: {cast_result}")
            mana_result = self.channel_mana(5)
            print(f"Manna channel: {mana_result}")
            return cast_result

    def attack(self, target) -> dict:
        return {'atacker': self.name, "target": target, "damage": 5, "combat type": "melee"}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return  {'caster': 'Arcane Warrior', 'spell': 'Fireball', 'targets': ['Enemy1', 'Enemy2'], 'mana_used': 4}

    def defend(self, incoming_damage) -> dict:
        damage_blocked = 3
        damage_taken = incoming_damage - damage_blocked
        health_status = incoming_damage > damage_blocked
        return {'defender': self.name, 'damage_taken': damage_taken, 'damage_blocked': 3, 'still_alive': health_status}
    
    def channel_mana(self, amount) -> dict:
        return {'channeled': amount, 'total_mana': 7}
    
    def get_combat_stats(self) -> dict:
        print(f"\nPlaying {self.name} (Elite Card):\n")
        print("Combat phase:")
        return self.play({"game state": "Combat phase"})
    
    def get_magic_stats(self):
        print(f"\nPlaying {self.name} (Elite Card):\n")
        print("Magic phase:")
        return self.play({"game state": "Magic phase"})

    def show_capabilities(self):
        print("EliteCard capabilities:")
        print(f"- Card: {Card.play.__name__, Card.get_card_info.__name__, Card.is_playable.__name__}")
        print(f"- Combatable: {Combatable.attack.__name__, Combatable.defend.__name__, Combatable.get_combat_stats.__name__}")
        print(f"- Magical: {Magical.cast_spell.__name__, Magical.channel_mana.__name__, Magical.get_magic_stats.__name__}")