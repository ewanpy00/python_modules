from ex0.CreatureCard import CreatureCard
from ex0.Card import Card

from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck

def main():
    print("=== DataDeck Deck Builder ===\n")
    deck = Deck()
    card3 = ArtifactCard("Mana Crystal", 2, "Common", 10, "Mana")
    card2 = SpellCard("Lightning Bolt", 3, "Legendary", "Effect")
    card1 = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print("Building deck with different card types...")
    deck.add_card(card1)
    deck.add_card(card2)
    deck.add_card(card3)
    print(f"Deck stats: {deck.get_deck_stats()}")
    print("\nDrawing and playing cards:")
    deck.draw_card()
    deck.draw_card()
    deck.draw_card()
    print("Polymorphism in action: Same interface, different card behaviors!")

if __name__ == "__main__":
    main()