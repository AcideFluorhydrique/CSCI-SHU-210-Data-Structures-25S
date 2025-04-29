class Vehicle:
    # TODO: Please write your code here
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def get_description(self):
        return f"{self.year} {self.make} {self.model}"

    # pass


class Car(Vehicle):
    # TODO: Please write your code here
    def __init__(self, make, model, year, doors):
        super().__init__( make, model, year)
        self.doors = doors

    def get_description(self):
        YEAR = str(self.year)
        MAKE = str(self.make)
        MODEL = str(self.model)
        DOORS = str(self.doors)
        # return YEAR +" "+ MAKE +" "+ MODEL +", "+ DOORS + "-door"
        return f"{YEAR} {MAKE} {MODEL}, {DOORS}-door"

    # pass


class Truck(Vehicle):
    # TODO: Please write your code here
    def __init__(self, make, model, year, payload_capacity):
        super().__init__( make, model, year)
        self.payload_capacity = payload_capacity
    def get_description(self):
        YEAR = str(self.year)
        MAKE = str(self.make)
        MODEL = str(self.model)
        PAYLOAD = str(self.payload_capacity)
        return f"{YEAR} {MAKE} {MODEL}, Payload capacity: {str(PAYLOAD)} tons"
        # return YEAR +" "+ MAKE +" "+ MODEL +", Payload capacity: "+ str(PAYLOAD) + " tons"
    # pass


# Do not change or remove the code below this point
def main():
    car = Car("Toyota", "Corolla", 2021, 4)
    print(car.get_description())  # Expected: "2021 Toyota Corolla, 4-door"

    truck = Truck("Ford", "F-150", 2020, 1.5)
    print(truck.get_description())  # Expected: "2020 Ford F-150, Payload capacity: 1.5 tons"


if __name__ == "__main__":
    main()
