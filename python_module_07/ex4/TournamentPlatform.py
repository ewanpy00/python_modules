from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self):

        self.cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard, card_id: str) -> str:

        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:

        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        if card1.attack_power >= card2.attack_power:

            winner = card1
            loser = card2
            winner_id = card1_id
            loser_id = card2_id

        else:

            winner = card2
            loser = card1
            winner_id = card2_id
            loser_id = card1_id

        winner.update_wins(1)
        loser.update_losses(1)

        self.matches_played += 1

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self):

        sorted_cards = sorted(
            self.cards.items(),
            key=lambda x: x[1].rating,
            reverse=True
        )

        leaderboard = []

        for card_id, card in sorted_cards:

            leaderboard.append(
                (card_id, card.name, card.rating, card.wins, card.losses)
            )

        return leaderboard

    def generate_tournament_report(self):

        total_cards = len(self.cards)

        avg_rating = sum(
            card.rating for card in self.cards.values()
        ) // total_cards

        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }