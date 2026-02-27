from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import Union, Dict

class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: Union[str, int, None] = None) -> CreatureCard:
        return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    def create_spell(self, name_or_power: Union[str, int, None] = None) -> SpellCard:
        return SpellCard("Fireball", 3, "Common", "damage")

    def create_artifact(self, name_or_power: Union[str, int, None] = None) -> ArtifactCard:
        return ArtifactCard("Mana Ring", 2, "Rare", 3, "Add 1 mana")

    def create_themed_deck(self, size: int) -> Dict:
        return {"theme": "Fantasy", "size": size, "status": "Ready"}

    def get_supported_types(self) -> Dict:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }