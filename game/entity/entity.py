class Entity:
    counter = 0
    
    def __init__(self, name):
        Entity.counter += 1
        self.id = Entity.counter
        self.name = name
        
    
    
    def show_info(self):
        print(f"Name: {self.name}")
    