class Inventory:
    
    def __init__(self):
        self.items = {}
        
    def add_item(self, item):
        self.items[item.id] = item
        
    def remove_item(self, item):
        if item.id in self.items:
            del self.items[item.id]
        
    def show_items(self):
        print("=== Inventory === ")
        if not self.items:
            print("Inventory is empty")
            return 
        
        for item in self.items.values():
            print(f" - {item.name}")