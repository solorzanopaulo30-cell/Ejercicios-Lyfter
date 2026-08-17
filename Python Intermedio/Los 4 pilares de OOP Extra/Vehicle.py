

class Vehicle():
    def __init__(self,brand,year):
        self._brand = brand
        self._year = year

    def get_info(self):
        return f"{self._brand} ({self._year})"


class Car(Vehicle):
    def __init__(self,brand,year,passengers):
        super().__init__(brand,year)
        self._passengers = passengers

    def get_info(self):
        return f"{super().get_info()} - {self._passengers} passengers"

class Motorcycle(Vehicle):
    def __init__(self, brand,year,model):
        super().__init__(brand,year)
        self._model = model

    def get_info(self):
        return f"{super().get_info()} - type: {self._model}"

#----------------------------

vehicle1 = Car("Toyota", 2020, 5)
vehicle2 = Motorcycle("Yamaha", 2022, "Sport")

print(vehicle1.get_info())  
print(vehicle2.get_info())  