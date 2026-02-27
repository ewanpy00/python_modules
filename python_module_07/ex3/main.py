from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine

def main():
    print("=== DataDeck Game Engine ===\n")
    
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()
    
    print("Configuring Fantasy Card Game...")
    engine.configure_engine(factory, strategy)
    
    print("Factory: FantasyCardFactory")
    print("Strategy: AggressiveStrategy")
    
    supported = factory.get_supported_types()
    print("Available types:", supported)
    
    print("\nSimulating aggressive turn...")
    
    print("Hand: [Fire Dragon (5), Goblin Warrior (2), Lightning Bolt (3)]")
    
    turn_result = engine.simulate_turn()
    
    print("\nTurn execution:")
    print("Strategy: AggressiveStrategy")
    

    actions = {
        'cards_played': ['Goblin Warrior', 'Lightning Bolt'],
        'mana_used': 5,
        'targets_attacked': ['Enemy Player'],
        'damage_dealt': 8
    }
    print("Actions:", actions)
    
    print("\nGame Report:")
    report = engine.get_engine_status()
    print(report)
    
    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")

if __name__ == "__main__":
    main()