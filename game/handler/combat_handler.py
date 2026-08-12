import random
from game.core.game_state import GameState


class CombatHandler:
    
    # Flusso della battaglia
    
    def __init__(self, input_handler, menu_manager, combat_manager):
        self.input_handler = input_handler
        self.menu_manager = menu_manager
        self.combat_manager = combat_manager
       
    
    def start_combat(self, player, enemy, tower):
        first, second = self.combat_manager.determine_turn_order(player, enemy)

        while player.is_alive() and enemy.is_alive():
            if first == player:
                battle_ended = self.handle_player_turn(player, enemy, tower)
            else:
                battle_ended = self.handle_enemy_turn(enemy, player, tower)
            
            if battle_ended:
                break
            
            if not second.is_alive():
                break
            
            if second == player:
                battle_ended = self.handle_player_turn(player,enemy,tower)
            else:
                battle_ended = self.handle_enemy_turn(enemy, player, tower)

            if battle_ended:
                break
            
        self.end_battle(player, enemy)

        # Per il momento
        return GameState.FLOOR_STATE
        
        
    
    def end_battle(self, player, enemy):

        if not player.is_alive():
            print(f"{player.name} has been defeated!")
            print("You lost!")

        elif not enemy.is_alive():
            print(f"{enemy.name} has been defeated!")
            print("You won!")
      
    def handle_player_turn(self, player, enemy, tower):
        print("------")
        self.menu_manager.show_player_stats(player)
        print("------")
        self.menu_manager.show_enemy_stats(enemy)
        print("------")
        
        self.menu_manager.show_combat_menu()
        tower.show_current_floor()
        choice = self.input_handler.get_number(1,2)
        
        if choice == 1:
            self.combat_manager.attack(player, enemy)
            return False # per fare in modo che la battaglia non finisca
            
        elif choice == 2:
            return self.combat_manager.escape(player, enemy)
            
    def handle_enemy_turn(self, enemy, player, tower):
        action = random.randint(1,10)
        
        if action <= 8: # per fare in modo che attachi più spesso
            self.combat_manager.attack(enemy, player)
            return False
            
        else:
            return self.combat_manager.escape(enemy, player)