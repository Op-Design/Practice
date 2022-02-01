import json

"""
Practice Problem: https://pynative.com/python-json-exercise/#h-exercise-1-convert-the-following-dictionary-into-json-format
Exercise 6: Convert the following Vehicle Object into JSON
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
"""


class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

vehicle_dict = {
    "name": vehicle.name,
    "engine": vehicle.engine,
    "price": vehicle.price,
    }

vehicle_JSON = json.dumps(vehicle_dict, indent=4)
print(vehicle_JSON)





"""
Alternative solution (Uses JSONEncoder):


import json
from json import JSONEncoder

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class VehicleEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

print("Encode Vehicle Object into JSON")
vehicleJson = json.dumps(vehicle, indent=4, cls=VehicleEncoder)
print(vehicleJson)
"""