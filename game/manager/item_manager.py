from game.object.item import Item

class ItemManager:
    
    def __init__(self, file_manager):
        self.file_manager = file_manager
        
        
    def create_item(self, item):
        items = self.file_manager.read_json("data/items.json")
        
        item_data = items[item]
        
        return Item(
            item_data["id"],
            item_data["name"],
            item_data["description"],
            item_data["price"],
            item_data["item_type"],
            item_data["effect"]
        )
        
    def load_items(self):
        items_data = self.file_manager.read_json("data/items.json")
        
        items = {}
        
        for item_name, item_data in items_data.items():
            item = Item.from_dict(item_data)
            items[item_name] = item
        
        return items
    
    def show_all_items(self, game_items):
        
        # load_items() trasforma i dati JSON in oggetti
        
        for item_key, item in game_items.items():
            print(item_key)
            item.show_info()
    
    def get_item(self, game_items, item_key):
        return game_items.get(item_key)
    
    
            
        