from ex3.GameStrategy import GameStrategy
from typing import List, Dict

class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        played_names = []
        total_mana = 0
        
        count = 0
        for card in hand:
            if count < 2:
                info = card.get_card_info()
                # played_names.append(info["name"])
                # total_mana = total_mana + info['cost']
                count = count + 1
        
        return {
            'cards_played': played_names,
            'mana_used': total_mana,
            'targets_attacked': ['Enemy Player'],
            'damage_dealt': 8
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List) -> List:
        reordered = []
        for target in available_targets:
            if target == 'Enemy Player':
                reordered.append(target)
        for target in available_targets:
            if target != 'Enemy Player':
                reordered.append(target)
        return reordered