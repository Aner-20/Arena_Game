from game.core.game_state import GameState

class MenuHandler:
    def __init__(self, input_handler, menu_manager, save_manager):
        self.input_handler = input_handler
        self.menu_manager = menu_manager
        self.save_manager = save_manager
        
    def handle_main_menu(self, file_path):
        self.menu_manager.show_main_menu()
        
        choice = self.input_handler.get_number(1,3)
        
        if choice == 1:
            return GameState.CHARACTER_CREATION_STATE, None, None
        
        elif choice == 2:
            if self.save_manager.save_exists(file_path):
                player, tower = self.save_manager.load_game(file_path)

                return GameState.GAME_STATE, player, tower
            
            print("No save file found")
            return GameState.MAIN_MENU_STATE, None, None
        
        elif choice == 3:
            return GameState.EXIT_STATE, None, None
    
        