from .Card import Card

class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        if attack >= 0 and health >= 0:
            self.attack = attack
            self.health = health
        else:
            print("Invalid health or atatck input")
            self.attack = 0
            self.health = 0
            

    def get_card_info(self):
        info = super().get_card_info()
        print(info)
        

    def play(self, game_state: dict) -> dict:
        result = super().play(game_state)
        if result is not None:
            print("Play result: ", end="")
            print(result)
        return result

    def attack_target(self, target) -> dict:
        print(f"\n{self.name} attacks {target} Warrior:")
        print("Attack result: ", end="")
        return {
            'attacker': self.name,
            'target': target,
            'damage_dealt': 7,
            'combat_resolved': True
            }