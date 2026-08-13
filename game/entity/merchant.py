from game.entity.npc import NPC

class Merchant(NPC):
    
    def __init__(self, name, inventory):
        super().__init__(name)
        self.inventory = inventory
    