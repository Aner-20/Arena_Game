class LevelManager:
    def __init__(self):
        pass
    
    def add_exp(self, player, amount):
        player.exp += amount
        
        # Si usa il while per gestire più avanzamenti di livello.
        # Con un if si perderebbe l'exp in eccesso e andrebbe persa
        while self.can_level_up(player):
            self.level_up(player)
        
    
    def can_level_up(self, player):
        return player.exp >= self.get_exp_required(player)
        
    def get_exp_required(self, player):
        return player.level * player.exp_to_next_level
    
    def level_up(self, player):
        player.level += 1
        player.exp -= self.get_exp_required(player)
        
        # Funzione player per gestire gli aumenti delle statistiche
        player.increase_stats()
        
        print(f"{player.name} reached level {player.level}!")