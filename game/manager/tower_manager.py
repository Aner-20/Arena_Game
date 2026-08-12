from game.entity.tower import Tower

class TowerManager:
    
    def __init__(self, file_manager):
        self.file_manager = file_manager

    
    def create_tower(self, tower_name):
        towers = self.file_manager.read_json("data/towers.json")
        
        tower_data = towers[tower_name]
        
        return Tower(
            tower_data["name"],
            tower_data["description"],
            tower_data["floors"]
        )
        