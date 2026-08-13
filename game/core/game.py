from game.core.game_state import *
from game.handler.input_handler import InputHandler
from game.handler.menu_handler import MenuHandler
from game.handler.combat_handler import CombatHandler
from game.handler.character_creation_handler import CharacterCreationHandler
from game.handler.tower_handler import TowerHandler
from game.handler.save_handler import SaveHandler
from game.handler.player_handler import PlayerHandler
from game.manager.tower_manager import TowerManager
from game.manager.menu_manager import MenuManager
from game.manager.combat_manager import CombatManager
from game.manager.character_manager import CharacterManager
from game.manager.file_manager import FileManager
from game.manager.save_manager import SaveManager
from game.manager.level_manager import LevelManager

class Game:
    def __init__(self):
        self.running = True
        self.current_state = GameState.MAIN_MENU_STATE
        
        self.player = None
        self.enemy = None
        self.enemy_type = None
        self.tower = None
        
        self.save_file_path = "save/save.json"
        
        self.file_manager = FileManager()
        self.menu_manager = MenuManager()
        self.combat_manager = CombatManager()
        self.character_manager = CharacterManager(self.file_manager)
        self.tower_manager = TowerManager(self.file_manager)
        self.save_manager = SaveManager(self.file_manager)
        self.level_manager = LevelManager()
        
        self.input_handler = InputHandler()
        self.menu_handler = MenuHandler(self.input_handler, self.menu_manager, self.save_manager)
        self.character_creation_handler = CharacterCreationHandler(self.input_handler, self.menu_manager, self.character_manager)
        self.combat_handler = CombatHandler(self.input_handler, self.menu_manager, self.combat_manager, self.level_manager)
        self.tower_handler = TowerHandler(self.input_handler, self.menu_manager, self.tower_manager, self.save_manager)
        self.save_handler = SaveHandler(self.save_manager)
        self.player_handler = PlayerHandler(self.input_handler, self.menu_manager)
        
        
    def run(self):
        while self.running:
            if self.current_state == GameState.MAIN_MENU_STATE:
                self.current_state, self.player, self.tower = self.menu_handler.handle_main_menu(self.save_file_path)
            
            elif self.current_state == GameState.CHARACTER_CREATION_STATE:
                self.player, self.current_state = (self.character_creation_handler.handle_character_creation_menu())
            
            elif self.current_state == GameState.GAME_STATE:
                # Così la torre viene creata una sola volta
                if self.tower is None:
                    self.tower = self.tower_manager.create_tower("tower_1")
                
                self.current_state, self.enemy_type = ( self.tower_handler.handle_tower_menu(self.tower, self.player) )
            
            elif self.current_state == GameState.COMBAT_STATE:
                self.enemy = self.character_manager.create_enemy(self.enemy_type) # i dati vengono caricati con successo
                self.current_state = self.combat_handler.start_combat(self.player, self.enemy, self.tower) 
            
            
            elif self.current_state == GameState.FLOOR_STATE:
                self.tower.next_floor()
                self.current_state, self.enemy_type = (self.tower_handler.handle_tower_menu(self.tower, self.player))
             
            elif self.current_state == GameState.PLAYER_STATE:
                self.current_state = self.player_handler.handle_player_menu(self.player)
             
            elif self.current_state == GameState.EXIT_STATE:
                self.running = False