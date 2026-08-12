class SaveHandler:
    def __init__(self, save_manager):
        self.save_manager = save_manager
        
    def save_game(self, player, tower):
        self.save_manager.save_game(player, tower)