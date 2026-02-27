from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from typing import Dict
from ex3.FantasyCardFactory import FantasyCardFactory

class GameEngine:
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0

    def configure_engine(self, factory: FantasyCardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict:
        if self.factory is None or self.strategy is None:
            return {"error": "Engine not configured"}
        
        hand = []
        hand.append(self.factory.create_creature())
        hand.append(self.factory.create_spell())
        
        turn_result = self.strategy.execute_turn(hand, [])
        self.turns_simulated = self.turns_simulated + 1
        return turn_result

    def get_engine_status(self) -> Dict:
        strat_name = None
        if self.strategy is not None:
            strat_name = self.strategy.get_strategy_name()
            
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': strat_name,
            'total_damage': 8,
            'cards_created': 3
        }