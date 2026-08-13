from game.entity.entity import Entity

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
        print(f"Level: {self.level}")
        print(f"Exp: {self.exp}")
        print(f"Next Level (exp required): {self.exp_to_next_level}")

    
    def increase_stats(self, updated_exp):
        self.max_hp += 5
        self.hp = self.max_hp
        self.attack += 2
        self.defense += 1
        self.speed += 1
        self.exp = updated_exp
        
    
    # Per caricare i dati del player
    @classmethod
    def from_dict(cls, data):
        player = cls(data["name"])

        player.hp = data["hp"]
        player.max_hp = data["max_hp"]
        player.attack = data["attack"]
        player.defense = data["defense"]
        player.speed = data["speed"]
        player.level = data["level"]
        player.exp = data["exp"]
        player.exp_to_next_level = data["exp_to_next_level"]

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
            "exp_to_next_level": self.exp_to_next_level
        }
    
    