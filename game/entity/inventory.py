class Inventory:
    
    def __init__(self):
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
        
    def remove_item(self, item):
        self.items.remove(item)
        
    def show_items(self):
        print("=== Inventory === ")
        if not self.items:
            print("Inventory is empty")
            return 
        
        for item in self.items:
            print(item.name)