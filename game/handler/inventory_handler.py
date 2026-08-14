from game.core.game_state import GameState
from game.utils.utils import Utils

class InventoryHandler:
    
    def __init__(self, input_handler, menu_manager):
        self.input_handler = input_handler
        self.menu_manager = menu_manager
        
        
    def handle_inventory_menu(self, player):
        
        while True:
            self.menu_manager.show_inventory_menu(player)
                    
            min_index, max_index = Utils.get_indexes()
            highest_index = max_index + 1
            
            print(f"{highest_index}. Back to player menu")
            
            choice = self.input_handler.pick_item(min_index, max_index, highest_index)
            
            if min_index <= choice <= max_index:
                for index, item in enumerate(player.inventory.items.values(), start=1):
                    if index == choice:
                        item.show_info()
            
                return GameState.INVENTORY_STATE
                        
            
            elif choice == highest_index:
                return GameState.PLAYER_STATE
        
      
        