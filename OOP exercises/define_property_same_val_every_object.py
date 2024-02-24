class Vehicle:

    color = 'White'

    def __init__(self, name, max_speed, mileage,):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

bus = Bus('School Volvo', 180, 12)

car = Car('Audi Q5', 240, 18)

print('Color:', bus.color+',', 'Vehicle Name:', bus.name+',', 'Speed:', str(bus.max_speed)+',', 'Mileage', bus.mileage)
print('Color:', car.color+',', 'Vehicle Name:', car.name+',', 'Speed:', str(car.max_speed)+',', 'Mileage', car.mileage)