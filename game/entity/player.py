from game.entity.entity import Entity
from game.entity.inventory import Inventory

class Player(Entity):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 10
        self.max_hp = self.hp
        self.attack = 1
        self.defense = 0
        self.speed = 1
        self.level = 1
        self.exp = 0
        self.exp_to_next_level = 5
        
        self.left_hand = None
        self.right_hand = None
        
        self.inventory = Inventory()

    def equip_item(self, item, hand):
        if item.item_type != "weapon":
            print("This item cannot be equipped")
            return False

        if hand == "left".lower():
            self.left_hand = item
        
        elif hand == "right".lower():
            self.right_hand = item
        
        else:
            print("Invalid hand")
            return False

        return True
     
        
    def is_alive(self):
        return self.hp > 0
    
    def increase_stats(self, updated_exp):
        self.max_hp += 5
        self.hp = self.max_hp
        self.attack += 2
        self.defense += 1
        self.speed += 1
        self.exp = updated_exp
    
    def show_health(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.hp}/{self.max_hp}")
    
    def show_info(self):
        print("=== Stats === ")
        print(f"Name: {self.name}")
        print(f"Health: {self.hp}/{self.max_hp}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Speed: {self.speed}")
        print(f"Level: {self.level}")
        print(f"Exp: {self.exp}")
        print(f"Next Level (exp required): {self.exp_to_next_level}")
        print(f"Left hand: {self.left_hand}")
        print(f"Right hand: {self.right_hand}")
    
    
        
    
    # Per caricare i dati del player
    @classmethod
    def from_dict(cls, data, game_items):
        player = cls(data["name"])

        player.hp = data["hp"]
        player.max_hp = data["max_hp"]
        player.attack = data["attack"]
        player.defense = data["defense"]
        player.speed = data["speed"]
        player.level = data["level"]
        player.exp = data["exp"]
        player.exp_to_next_level = data["exp_to_next_level"]
        player.left_hand = data["left_hand"]
        player.right_hand = data["right_hand"]

        # Ricostruisce l'inventario
        for item_name in data["inventory"]:
            item = game_items
            
            if item:
                player.inventory.add_item(item)
    
        return player

    # Per salvare i dati del player
    def to_dict(self):
        return {
            "name": self.name,
            "hp": self.hp,
            "max_hp": self.max_hp,
            "attack": self.attack,
            "defense": self.defense,
            "speed": self.speed,
            "level": self.level,
            "exp": self.exp,
            "exp_to_next_level": self.exp_to_next_level,
            "left_hand": self.left_hand,
            "right_hand": self.right_hand,
            
            "inventory" : [item.name for item in self.inventory.items]
            
        }
    
    