from enum import Enum

class GameState(Enum):
    MAIN_MENU_STATE = 1
    GAME_STATE = 2
    EXIT_STATE = 3
    CHARACTER_CREATION_STATE = 4
    COMBAT_STATE = 5
    FLOOR_STATE = 6
    PLAYER_STATE = 7
    INVENTORY_STATE = 8
    EQUIPMENT_STATE = 9
    