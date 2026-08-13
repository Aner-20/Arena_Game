from game.entity.entity import Entity

class NPC(Entity):
    
    def __init__(self, name):
        super().__init__(name)
        
    def talk(self):
        pass