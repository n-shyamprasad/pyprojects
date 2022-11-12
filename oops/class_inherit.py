'''
Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
'''

class Vehicle:
    def __init__(self,name, maxspeed,mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage
    
    def show(self):
        print(f"Vehicle Name: {self.name} \nSpeed: {self.maxspeed} \nMileage: {self.mileage}")

class Bus(Vehicle):
    pass

school_bus = Bus("Volvo", 180, 50)
school_bus.show()
#print(f"Vehicle Name: {school_bus.name} \nSpeed: {school_bus.maxspeed} \nMileage: {school_bus.mileage}")