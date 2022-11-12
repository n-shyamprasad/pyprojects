'''
Create a Class with instance attributes

create a Vehicle class with max_speed and mileage instance attributes.
'''

class Vehicle:
    def __init__(self, max_speed, mailge):
        self.maxspeed = max_speed
        self.mailge = mailge

objVehicle = Vehicle(240, 50)
print(f"MAx Speed: {objVehicle.maxspeed}, Mailage: {objVehicle.mailge}")