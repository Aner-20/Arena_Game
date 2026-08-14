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
        
    def show_player_menu(self):
        print("=== Player Menu === ")
        print("1. Show stats")
        print("2. Show inventory")
        print("3. Back to game")    
    
    def show_inventory_menu(self, player):
        player.inventory.show_items()
    
    def show_equipment_menu(self, player):
        print("=== Equipment ===")
        print(f"Left Hand: {player.left_hand}")
        print(f"Right Hand: ")
        print("1. Equip Item")
        print("2. Unequip left hand")
        print("3. Unequip right hand")
        print("4. Back to inventory")
    
    def show_tower_menu(self, tower, player):
        #player.show_health()
        
        if tower.current_floor == 1:
            print("=== Tower ===")
            tower.show_info()
            print("-------------")
            print("1. Get into the tower")
            print("2. View character")
            print("3. Back to the main menu")
        
        elif tower.current_floor > 1 and tower.current_floor < len(tower.floors):
            tower.show_current_floor()
            print("1. Advance to the next floor")
            print("2. Save")
            print("3. View character")
            print("4. Quit (return to the main menu)")
    
       
        
    def show_combat_menu(self):
        print("=== Battle ===")
        print("1. Attack")
        print("2. Escape")
   
    def show_player_stats(self, player):
        player.show_health()
        
    def show_enemy_stats(self, enemy):
        enemy.show_health()
        
    
        