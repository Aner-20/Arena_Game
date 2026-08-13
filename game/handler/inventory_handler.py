from game.core.game_state import GameState

class InventoryHandler:
    
    def __init__(self, input_handler, menu_manager):
        self.input_handler = input_handler
        self.menu_manager = menu_manager
        
        
    def handle_inventory_menu(self, player):
        self.menu_manager.show_inventory_menu(player)
        
        choice = self.input_handler.get_number(1, 2)
        
        if choice == 1:
            pass
        
        elif choice == 2:
            return GameState.PLAYER_STATE