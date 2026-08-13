class Item:
    
    def __init__(self, name, description, price, item_type, effect):
        self.name = name
        self.description = description
        self.price = price
        self.item_type = item_type
        self.effect = effect
        
    def show_info(self):
        print(f"Item: {self.name}")
        print(f"Description: {self.description}")
        print(f"Price: {self.price} gold")