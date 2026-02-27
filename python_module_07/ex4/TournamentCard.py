from ex2.Combatable import Combatable
from ex0.Card import Card
from Rankable import Rankable

class TournamentCard(Rankable, Card, Combatable):
    def play(self, game_state: dict) -> dict:
        pass

    def attack(self, target) -> dict:
        pass

    def calculate_rating(self) -> int:
        pass

    def get_tournament_stats(self) -> dict:
        pass
