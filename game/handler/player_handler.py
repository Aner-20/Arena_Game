from game.core.game_state import GameState

class PlayerHandler:
    
    def __init__(self, input_handler, menu_manager):
        self.input_handler = input_handler
        self.menu_manager = menu_manager
        
    def handle_player_menu(self, player):
       
        while True:
            self.menu_manager.show_player_menu()
            
            choice = self.input_handler.get_number(1, 3)
            
            if choice == 1:
                player.show_info()
            
            elif choice == 2:
                #player.inventory.show_items()
                return GameState.INVENTORY_STATE
                
            elif choice == 3:
                return GameState.GAME_STATE