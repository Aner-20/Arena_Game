from game.object.item import Item

class ItemManager:
    
    def __init__(self, file_manager):
        self.file_manager = file_manager
        
        
    def create_item(self, item):
        items = self.file_manager.read_json("data/items.json")
        
        item_data = items[item]
        
        return Item(
            item_data["name"],
            item_data["description"],
            item_data["price"],
            item_data["item_type"],
            item_data["effect"]
        )