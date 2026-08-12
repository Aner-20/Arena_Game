from game.entity.entity import Entity

class Player(Entity):
    def __init__(self, name):
        super().__init__(name)
        self.hp = 10
        self.max_hp = self.hp
        self.attack = 1
        self.defense = 0
        self.speed = 1
    
    
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

    
    # Per caricare i dati del player
    @classmethod
    def from_dict(cls, data):
        player = cls(data["name"])

        player.hp = data["hp"]
        player.max_hp = data["max_hp"]
        player.attack = data["attack"]
        player.defense = data["defense"]
        player.speed = data["speed"]

        return player

    # Per salvare i dati del player
    def to_dict(self):
        return {
            "name": self.name,
            "hp": self.hp,
            "max_hp": self.max_hp,
            "attack": self.attack,
            "defense": self.defense,
            "speed": self.speed
        }
    
    