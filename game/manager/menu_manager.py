class MenuManager:
    def __init__(self):
        pass
    
    def show_main_menu(self):
        print("=== Main Menu ===")
        print("1. Start New game")
        print("2. Load Game")
        print("3. Exit")
    
    def show_character_creation_menu(self):
        print("=== Character Creation === ")
        print("1. Create character")
        print("2. Back to the main menu")
    
    def show_tower_menu(self, tower, player):
        player.show_health()
        if tower.current_floor == 1:
            print("=== Tower ===")
            tower.show_info()
            print("-------------")
            print("1. Get into the tower")
            print("2. Back to the main menu")
        
        elif tower.current_floor > 1 and tower.current_floor < len(tower.floors):
            tower.show_current_floor()
            print("1. Advance to the next floor")
            print("2. Save")
            print("3. Quit (return to the main menu)")
            
        
    def show_combat_menu(self):
        print("=== Battle ===")
        print("1. Attack")
        print("2. Escape")
   
    def show_player_stats(self, player):
        player.show_health()
        
    def show_enemy_stats(self, enemy):
        enemy.show_health()
        
    
        