from game.core.game_state import GameState


class CharacterCreationHandler:
    def __init__(self, input_handler, menu_manager, character_manager):
        self.input_handler = input_handler
        self.menu_manager = menu_manager
        self.character_manager = character_manager
        
    def handle_character_creation_menu(self, game_items):
        self.menu_manager.show_character_creation_menu()
        
        choice = self.input_handler.get_number(1,2)
        
        if choice == 1:
            character_name = self.input_handler.get_name()
            player = self.character_manager.create_player(character_name)
            
            #sword = game_items.get("iron_sword")
            #potion = game_items.get("health_potion")
            starting_items = ["iron_sword", "health_potion"]
            
            for item_name in starting_items:
                item = game_items.get(item_name)
                
                if item:
                    #print("Item: ", item)
                    #print("Type: ", item.item_type)
                    player.inventory.add_item(item)
                    player.inventory.add_item(item)
                    player.inventory.add_item(item)          
                    
          
            
            return player, GameState.GAME_STATE
            
        elif choice == 2:
            return None, GameState.MAIN_MENU_STATE
    