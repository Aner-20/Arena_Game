class LevelManager:
    def __init__(self):
        pass
    
    def add_exp(self, player, amount):
        player.exp += amount
        
    
    def can_level_up(self, player):
        return player.exp >= player.exp_to_next_level
        
    
    
    def level_up(self, player):
        player.level += 1
        player.exp = 0
        
        # Funzione player per gestire gli aumenti delle statistiche
        
        print(f"{player.name} reached level {player.level}!")