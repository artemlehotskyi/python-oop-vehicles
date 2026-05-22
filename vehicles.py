class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
    def start_engine(self):
        print("Start engine")

class Car(Vehicle):
    def __init__(self, make, model, year, weight, num_doors, num_passengers):
        super().__init__(make, model, year, weight)
        self.num_doors = num_doors
        self.num_passengers = num_passengers
    def start_engine(self):
        print(f"{self.make}'s car engine is starting...")
    def drive(self):
        print(f"{self.make} {self.model} is Driving")

class Truck(Vehicle):
    def __init__(self, make, model, year, weight, cargo_capacity, towing_capacity):
        super().__init__(make, model, year, weight)
        self.cargo_capacity = cargo_capacity
        self.towing_capacity = towing_capacity
    def start_engine(self):
        print(f"{self.make}'s truck engine is starting...")
    def haul(self):
        print(f"{self.make}'s is hauling")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, weight, num_wheels, has_sidecar):
        super().__init__(make, model, year, weight)
        self.num_wheels = num_wheels
        self.has_sidecar = has_sidecar
    def start_engine(self):
        print(f"{self.make}'s motorcycle engine is starting...")
    def ride(self):
        print(f"Motorcycle {self.make} is Riding")



car = Car("Tesla", "Model S", 2016, 1000, 5, 5)
truck = Truck("Volvo", "FH16", 2020, 8000, 25000, 40000)
motorcycle = Motorcycle("Yamaha", "MT-07", 2021, 184, 2, False)

car.start_engine()
truck.start_engine()
motorcycle.start_engine()
print("------------------------------------------")
car.drive()