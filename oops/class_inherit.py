'''
Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
'''

class Vehicle:
    color = "White"
    def __init__(self,name, maxspeed,mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage
    
    def show(self):
        print(f"Vehicle Name: {self.name} \nSpeed: {self.maxspeed} \nMileage: {self.mileage}")
    def seating_capacity(self, capacity):
        print(f"Seating capacity of a {self.name} is {capacity} passengers.")
    def fare(self, capacity):
        return capacity * 100

class Bus(Vehicle):
    def fare(self, capacity):
        amt = super().fare(capacity)
        amt = amt + amt * 10/100
        return amt

class Taxi(Vehicle):
    #assign default value to capacity
    def seating_capacity(self, capacity=6):
        return super().seating_capacity(capacity)
    def fare(self, capacity):
        amt = super().fare(capacity)
        discout = amt * 7/100
        amt = amt - discout
        return amt

# case 1
school_bus = Bus("Volvo", 180, 50)
school_bus.show()
print(f"color: {school_bus.color}")
print(f"Total fare: {school_bus.fare(50)}")

# case 2
taxi_o = Taxi("Limo", 120, 15)
taxi_o.show()
print(f"color: {taxi_o.color}")
taxi_o.seating_capacity()
print(f"Total fare: {taxi_o.fare(6)}")
#print(f"Vehicle Name: {school_bus.name} \nSpeed: {school_bus.maxspeed} \nMileage: {school_bus.mileage}")