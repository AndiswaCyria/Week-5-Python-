# Base class

class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self.power = power
        self._level = level

    def introduce(self):
        return f"I am {self.name}, my power is {self.power}!"

    def get_level(self):
        return self._level

    def level_up(self):
        self._level += 1
        return f"{self.name} has leveled up to level {self._level}!"

# Inherited class

class FlyingSuperhero(Superhero):
    def __init__(self, name, power, level, flight_speed):
        super().__init__(name, power, level)
        self.flight_speed = flight_speed

    def fly(self):
        return f"{self.name} is flying at a speed of {self.flight_speed} mph!"

# Create objects 
hero1 = Superhero("Spiderman", "Web-slinging", 5)
hero2 = FlyingSuperhero("Superman", "Flying", 10, 15)

# Test the methods
print(hero1.introduce())
print(hero1.level_up())
print(hero2.introduce())
print(hero2.fly())

#Activity 2 

class Vehicle:
    def move(self):
        pass
    
class Car(Vehicle):
    def move(self):
        return "Driving"
    
class Plane(Vehicle):
    def move(self):
        return "Flying"

class Boat(Vehicle):
    def move(self):
        return "Sailing"
    
vehicles = [Car(), Plane(), Boat()]   

for v in vehicles:
    print(v.move())
    
               


