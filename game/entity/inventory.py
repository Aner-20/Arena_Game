from game.utils.utils import Utils

class Inventory:
    
    def __init__(self):
        self.items = {}
        
    def add_item(self, item):
        if item.id in self.items:
            self.items[item.id].quantity += 1
            
        else:  
            self.items[item.id] = item
        
    def remove_item(self, item):
        if item.id in self.items:
            del self.items[item.id]
        
    def show_items(self):
        print("=== Inventory === ")
        if not self.items:
            print("Inventory is empty")
            return 
        
        for index, item in enumerate(self.items.values(), start = 1):
            min_index = min(1, index)
            max_index = max(1, index)
           
            print(f"{index}. {item.name} - {item.item_type} x {item.quantity}")
            
            
        Utils.set_indexes(min_index, max_index)
    
        #for item in self.items.values():
        #    print(f" - {item.name} - {item.item_type} - {item.effect["value"]}")