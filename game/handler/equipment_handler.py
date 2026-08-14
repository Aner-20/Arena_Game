from game.core.game_state import GameState

class EquipmentHandler:
    
    def __init__(self, input_handler, menu_manager):
        self.input_handler = input_handler
        self.menu_manager = menu_manager
        
    def handle_equipment_menu(self, player, selected_item):
        while True:
            self.menu_manager.show_equipment_menu(player)
            #print(selected_item.name)
            choice = self.input_handler.get_number(1, 4)
            
            if choice == 1:
                hand = self.input_handler.get_player_hand()
                player.equip_item(selected_item, hand)
            
            elif choice == 2:
                pass
            
            elif choice == 3:
                pass
            
            elif choice == 4:
                return GameState.INVENTORY_STATE