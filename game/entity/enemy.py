from game.entity.entity import Entity

class Enemy(Entity):
    def __init__(self, name, type, hp, attack, defense, speed):
        super().__init__(name)
        self.type = type
        self.hp = hp
        self.max_hp = self.hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        
    def is_alive(self):
        return self.hp > 0
    
    def show_health(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.hp}/{self.max_hp}")
    
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.hp}/{self.max_hp}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Speed: {self.speed}")
    