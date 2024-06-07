

# WAP to 

class Coordinates:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__ (self):
        return f"({self.x}, {self.y})"
    
    def __eq__ (self, other):
        
        if isinstance (other, Coordinates):
            return self.x == other.x and self.y == other.y
        
        return False
        

p1 = Coordinates(3, 4)
p2 = Coordinates(3, 4)

print(f"p1: {p1}")   
print(f"p2: {p2}")  

print(f"p1 equal to p2 : {p1 == p2}")