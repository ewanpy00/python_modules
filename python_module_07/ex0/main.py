from .CreatureCard import CreatureCard

def main():
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")
    card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    info = card.get_card_info()
    card.play(info)
    print(card.attack_target("Little Goblin"))
    print("Testing insufficient mana:")
    card.play(info)
    print("\nAbstract pattern successfully demonstrated!")

main()