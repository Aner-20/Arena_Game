from game.entity.entity import Entity
from game.entity.inventory import Inventory

class Player(Entity):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 10
        self.max_hp = self.hp
        self.base_attack = 1
        self.attack = self.base_attack
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
          
        if self.left_hand == item or self.right_hand == item:
            print("This item is already equipped")  

        if hand.lower() == "left":
           
            self.left_hand = item    
        
        elif hand.lower() == "right":
            self.right_hand = item
        
        else:
            print("Invalid hand")
            

        self.update_stats()
        
    
    def unequip_item(self, hand):
        if hand.lower() == "left":
            print("The item has been unequipped")
            self.left_hand = None
            
        elif hand.lower() == "right":
            print("The item has been unequipped")
            self.right_hand = None
            
        else:
            print("Invalid hand")
            
        self.update_stats()
        

    
    def update_stats(self):
        self.attack = self.base_attack
        
        if self.left_hand:
            if self.left_hand.effect["type"] == "attack":
                self.attack += self.left_hand.effect["value"]
                
        if self.right_hand:
            if self.right_hand.effect["type"] == "attack":
                self.attack += self.right_hand.effect["value"]
        
    def is_alive(self):
        return self.hp > 0
    
    def increase_stats(self, updated_exp):
        self.max_hp += 5
        self.hp = self.max_hp
        self.base_attack += 2
        self.defense += 1
        self.speed += 1
        self.exp = updated_exp
        
        self.update_stats()
    
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
        
        if self.left_hand:
            print(f"Left hand: {self.left_hand.name}")
        else:
            print("Left hand: Empty")

        if self.right_hand:
            print(f"Right hand: {self.right_hand.name}")
        else:
            print("Right hand: Empty")
    
        
    
    # Per caricare i dati del player
    @classmethod
    def from_dict(cls, data, game_items):
        player = cls(data["name"])

        player.hp = data["hp"]
        player.max_hp = data["max_hp"]
        player.base_attack = data["base_attack"]
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
                
        # Ricostruisce l'equipaggiamento
        left_hand_name = data.get("left_hand")
        right_hand_name = data.get("right_hand")
        
        if left_hand_name:
            player.left_hand = game_items.get(left_hand_name)
            
        if right_hand_name:
            player.right_hand = game_items.get(right_hand_name)
            
        player.update_stats()
    
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
            "left_hand": (self.left_hand.name if self.left_hand else None),
            "right_hand": (self.right_hand.name if self.right.hand else None ),
            
            "inventory" : [item.name for item in self.inventory.items]
            
        }
    
    