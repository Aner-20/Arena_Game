class LevelManager:
    def __init__(self):
        pass
    
    def add_exp(self, player, amount):
        print(f"{player.name} earned {amount} exp!")
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
        
        player.exp -= self.get_exp_required(player)
        
        player.level += 1  
        player.exp_to_next_level = player.level * 5
        
        player.increase_stats(player.exp)
        
        print(f"{player.name} reached level {player.level}!")
        
        
        
            