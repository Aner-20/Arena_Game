from game.core.game_state import GameState

class PlayerHandler:
    
    def __init__(self, input_handler, menu_manager):
        self.input_handler = input_handler
        self.menu_manager = menu_manager
        
    def show_player_menu(self, player):
        self.menu_manager.show_player_menu(player)
        
        choice = self.input_handler.get_number(1, 3)
        
        while True:
            if choice == 1:
                player.show_info()
            
            elif choice == 2:
                player.inventory.show_items()
                
            elif choice == 3:
                return GameState.MAIN_MENU_STATE