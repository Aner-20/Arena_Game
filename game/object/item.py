class Item:
    
    def __init__(self, id, name, description, price, item_type, quantity,  effect):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.item_type = item_type
        self.quantity = quantity
        self.effect = effect
        
    def __str__(self):
        return self.name    
    
    def show_info(self):
        print("---------")
        print(f"Item: {self.name}")
        self.show_value()
        print(f"Description: {self.description}")
        print(f"Price: {self.price} gold")
        print(f"Quantity: {self.quantity}")
        print("---------")
    
    def show_value(self):
        if self.item_type == "consumable":
            print(f"Healing points: {self.effect["value"]}")
            
        elif self.item_type == "weapon":
            print(f"Attack points: {self.effect["value"]}")
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"], 
            data["name"],
            data["description"],
            data["price"],
            data["item_type"],
            data["quantity"],
            data["effect"]
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "item_type": self.item_type,
            "quantity": self.quantity,
            "effect": self.effect
        }