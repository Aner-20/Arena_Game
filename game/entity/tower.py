class Tower:
    def __init__(self, name, description, floors):
        self.name = name
        self.description = description
        self.floors = floors
        self.current_floor = 1
        self.completed = False

    def show_info(self):
        print(f"Tower: {self.name}")
        print(f"Description: {self.description}")
        print(f"Number of floors: {len(self.floors)}")

    def show_current_floor(self):
        print(f"Floor: {self.current_floor}/{len(self.floors)}")

    def next_floor(self):
        print("You've advanced to the next floor")
        
        if self.current_floor < len(self.floors):
            self.current_floor += 1
            self.show_current_floor()
            
    def reset_floor(self):
        self.current_floor = 1
            
    def is_completed(self):
         return self.current_floor == len(self.floors) and self.completed
     
     
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "floors": self.floors,
            "current_floor": self.current_floor,
            "completed": self.completed
        }
        
    @classmethod
    def from_dict(cls, data):
        # cls rappresenta la classe Tower ovvero Tower(...)
        tower = cls(
            data["name"],
            data["description"],
            data["floors"]
        )
        
        # Sono fuori per ripristinare lo stato precedente
        tower.current_floor = data["current_floor"]  
        tower.completed = data["completed"]
        
        return tower
     
     
     