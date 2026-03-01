from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
        rating: int = 1200
    ):
        super().__init__(name, cost, rarity)

        self.attack_power = attack
        self.health = health

        self.wins = 0
        self.losses = 0
        self.rating = rating

    # Card
    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament creature deployed"
        }

    # Combatable
    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power
        }

    def defend(self, incoming_damage: int) -> dict:

        damage_blocked = self.attack_power // 2
        damage_taken = max(0, incoming_damage - damage_blocked)

        self.health -= damage_taken

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "health": self.health
        }

    # Rankable
    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16 * wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= 16 * losses

    def get_rank_info(self) -> dict:
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }