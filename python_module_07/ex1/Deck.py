from ex0.CreatureCard import CreatureCard
from ex0.Card import Card

from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard

class Deck():
    def __init__(self):
        self.deck = []
    
    def add_card(self, card: Card) -> None:
        self.deck += [card]

    def remove_card(self, card_name: str) -> bool:
        i = 0
        for _ in self.deck:
            if self.deck[i].name == card_name:
                del self.deck[i]
                return True
            i += 1
        return False

    def shuffle(self) -> None:
        pass

    def draw_card(self) -> Card:
        tmp = self.deck[0]
        print(f"\nDrew: {self.deck[0].name} ({self.deck[0].__class__.__name__})")
        self.deck[0].play({"card played": self.deck[0]})
        self.remove_card(self.deck[0].name)
        return tmp

    def get_deck_stats(self) -> dict:
        total_sum = 0
        length = 0
        spellCard_count = 0
        artifactCard_count = 0
        creatureCard_count = 0
        for card in self.deck:
            if card.__class__ is SpellCard:
                spellCard_count += 1
            elif card.__class__ is ArtifactCard:
                artifactCard_count += 1
            elif card.__class__ is CreatureCard:
                creatureCard_count += 1
            length += 1
            total_sum += card.cost
        return {
             'total_cards': length,
             'creatures': creatureCard_count,
             'spells': spellCard_count,
             'artifacts': artifactCard_count,
             'avg_cost': f"{total_sum/length:.2F}"
            }
