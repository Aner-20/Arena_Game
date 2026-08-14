class InputHandler:
    def __init__(self):
        pass
    
    def get_number(self, min_value, max_value):
        while True:
            try:
                value = int(input("Choice: "))
                
                if min_value <= value <= max_value:
                    return value
                
                print(f"Insert a number between {min_value} and {max_value}")
                
            except ValueError:
                print("Invalid input. Insert a number")
                
    def get_name(self):
        while True:
            name = input("Insert your name: ")
            if name.isalpha():
                print(f"Your name: {name}")
                break
            else:
                print("Invalid input! Insert only letters")
        
        return name
    
    def pick_item(self, min_value, max_value):
        while True:
            try:
                item = int(input("Item: "))
                
                if min_value <= item <= max_value:
                    return item
                
                print(f"Insert a number between {min_value} and {max_value}")
                
            except ValueError:
                print("Invalid input. Insert a number")