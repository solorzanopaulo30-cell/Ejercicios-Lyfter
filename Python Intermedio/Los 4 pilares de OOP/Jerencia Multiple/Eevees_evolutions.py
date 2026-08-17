

#---------types
class WaterType():
    def water_attack(self):
        return "use hydrobomb"


class ElectricType():
    def electric_attack(self):
            return "use thunder"

class Aquavee(WaterType,ElectricType):
    def __init__(self,name,attack,defense):
        self.name = name
        self.attack = attack
        self.defense = defense
    

my_pokemon = Aquavee("Aquavee",45,80)
print(my_pokemon.water_attack())
print(my_pokemon.electric_attack())
