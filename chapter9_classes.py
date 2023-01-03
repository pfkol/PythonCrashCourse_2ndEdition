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

