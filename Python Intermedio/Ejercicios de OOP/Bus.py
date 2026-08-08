

class Person:
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
        else:
            print("Esta lleno")

    def remove_passenger(self, person):
        self.passengers.remove(person)


Tracopa = Bus(3)

Jean = Person("Jean")
Alek = Person("Alek")
Luis = Person("Luis")
Paulo = Person("Paulo")

Tracopa.add_passenger(Jean)
Tracopa.add_passenger(Alek)
Tracopa.add_passenger(Luis)
Tracopa.add_passenger(Paulo)

Tracopa.remove_passenger(Alek)

Tracopa.add_passenger(Paulo)

print("Pasajeros actuales:")
for person in Tracopa.passengers:
    print(person.name)