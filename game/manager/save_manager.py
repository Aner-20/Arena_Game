import json

from game.entity.player import Player
from game.entity.tower import Tower

class SaveManager:
    def __init__(self, file_manager):
        self.file_manager = file_manager
        
        
    def save_game(self, player, tower):
        
        save_data = {
            "player": player.to_dict(),
            "tower": tower.to_dict()
        }

        self.file_manager.write_json("save/save.json",save_data)
        
        print("The game has been successfully saved")
    
    def load_game(self, file_path):
        save_data = self.file_manager.read_json(file_path)
        
        player_data = save_data["player"]
        tower_data = save_data["tower"]
        
        player = Player.from_dict(player_data)
        tower = Tower.from_dict(tower_data)
        
        print("The game has been successfully loaded")
        
        return player, tower

    
        
    def save_exists(self, file_path):
        if not self.file_manager.file_exists(file_path):
            return False
    
        try:
            save_data = self.file_manager.read_json(file_path)
        
        # Json non valido: json.JSONDecodeError
        except (json.JSONDecodeError, FileNotFoundError):
            return False 
        
        if "player" not in save_data:
            return False
        
        
        if "tower" not in save_data:
            return False 
        
        player = save_data["player"]
        tower = save_data["tower"]
        
        # I campi che devono essere presenti
        required_player_fields = {
            "name",
            "hp",
            "max_hp",
            "attack",
            "defense",
            "speed"
        }
        
        required_tower_fields = {
            "name",
            "current_floor",
            "completed"
        }
        
        # Controlla se tutti i campi obbligatori sono presenti nelle entità
        return (required_player_fields.issubset(player) and required_tower_fields.issubset(tower))
