from game.core.game_state import GameState

class TowerHandler:
    def __init__(self, input_handler, menu_manager, tower_manager, save_manager):
        self.input_handler = input_handler
        self.menu_manager = menu_manager
        self.tower_manager = tower_manager
        self.save_manager = save_manager
        
    def handle_tower_menu(self, tower, player):
       
        while True:
            if tower.current_floor == 1:
                self.menu_manager.show_tower_menu(tower, player)
                
                choice = self.input_handler.get_number(1, 2)
                
                if choice == 1:
                    return self.handle_current_floor(tower)
                
                elif choice == 2:
                    return GameState.MAIN_MENU_STATE, None 
                
            elif tower.current_floor > 1 and tower.current_floor < len(tower.floors):
                self.menu_manager.show_tower_menu(tower, player)
                
                choice = self.input_handler.get_number(1, 3)
                
                if choice == 1:
                    return self.handle_current_floor(tower)
                
                elif choice == 2:
                    self.save_manager.save_game(player, tower)
                    
                
                elif choice == 3:
                    tower.reset_floor()
                    return GameState.MAIN_MENU_STATE, None
                    
    
    def handle_current_floor(self, tower):
        floor = tower.floors[tower.current_floor - 1]
        
        if floor["floor_type"] == "battle":
            return GameState.COMBAT_STATE, floor["enemy"]
        
        
  
        
   
    