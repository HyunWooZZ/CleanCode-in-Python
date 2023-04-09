## when inheritance is good choice..
class Vehicle:
    def __init__(self, speed, fuel, position):
        self.speed = speed
        self.fuel = fuel
        self.position = position
        
    def move(self):
        self.position += self.speed
        
class Car(Vehicle):
    def __init__(self, speed, fuel, position, num_doors):
        super().__init__(speed, fuel, position)
        self.num_doors = num_doors
        
    def honk_horn(self):
        print("Beep beep!")
        
class Truck(Vehicle):
    def __init__(self, speed, fuel, position, cargo_capacity):
        super().__init__(speed, fuel, position)
        self.cargo_capacity = cargo_capacity
        
    def load_cargo(self):
        print("Loading cargo...")
        
class Motorcycle(Vehicle):
    def __init__(self, speed, fuel, position, has_passenger):
        super().__init__(speed, fuel, position)
        self.has_passenger = has_passenger
        
    def wheelie(self):
        print("Popping a wheelie!")


## when inheritance is not good choice..
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def resize(self, width, height):
        self.width = width
        self.height = height
        
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        
r = Rectangle(3, 4)
print(r.area())  # Output: 12

s = Square(5)
print(s.area())  # Output: 25

# violate LSP 
s.resize(3, 5)
print(s.width, s.height)

