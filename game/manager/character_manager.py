from game.entity.player import Player
from game.entity.enemy import Enemy


class CharacterManager:
    def __init__(self, file_manager):
        self.file_manager = file_manager
    
    def create_player(self, name):
        return Player(name)
    
    def create_enemy(self, enemy):
        enemies = self.file_manager.read_json("data/enemies.json")
        
        enemy_data = enemies[enemy]
        
        return Enemy(
            enemy_data["name"],
            enemy_data["type"],
            enemy_data["hp"],
            enemy_data["attack"],
            enemy_data["defense"],
            enemy_data["speed"]
        )