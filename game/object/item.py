class Item:
    
    def __init__(self, name, description, price, item_type, quantity,  effect):
        self.name = name
        self.description = description
        self.price = price
        self.item_type = item_type
        self.quantity = quantity
        self.effect = effect
        
    def show_info(self):
        print(f"Item: {self.name}")
        print(f"Description: {self.description}")
        print(f"Price: {self.price} gold")
        print(f"Quantity: {self.quantity}")
        
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["description"],
            data["price"],
            data["item_type"],
            data["quantity"],
            data["effect"]
        )

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "item_type": self.item_type,
            "quantity": self.quantity,
            "effect": self.effect
        }