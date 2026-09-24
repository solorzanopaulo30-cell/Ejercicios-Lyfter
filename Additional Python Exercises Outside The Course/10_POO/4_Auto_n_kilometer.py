#Clases, `__init__`, `self`, atributos, métodos.
#4. Cree una clase `Auto` con marca, modelo y kilometraje, y un método "conducir" que aumente el kilometraje.


class Auto():
    def __init__(self, marca, modelo, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.kilometraje = kilometraje

    def conducir(self, kilometros):
        if kilometros > 0:
            self.kilometraje += kilometros
            print(f"El auto ha recorrido {kilometros} kilómetros.")
        else:
            print("La cantidad de kilómetros debe ser positiva.")


miAuto = Auto("toyota","2020",2500)
miAuto.conducir(50)
print(miAuto.kilometraje)