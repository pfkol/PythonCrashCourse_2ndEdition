class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"pies {self.name} szczeka")

    def roll(self):
        print(f"{self.name} turla się")

class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def read_odometer(self):
        print(f"ODO:{self.odometer_reading}")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"


class Battery:
    
    def __init__(self, batterySize=75):
        self.batterySize = batterySize
    
    def describe_battery(self):
        print(f"Your elctric car has {self.batterySize} battery capacity")

    def get_range(self):
        if self.batterySize == 75:
            range=100
        if self.batterySize == 100:
            range=200
        return range


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    
    
    