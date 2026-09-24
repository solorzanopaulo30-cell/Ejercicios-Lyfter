#Clases hijas, sobrescritura de métodos.
#3. Cree una clase `Vehiculo` y clases hijas `Auto` y `Moto`, cada una con un método `descripcion()` distinto.


class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"Vehículo de la marca {self.marca}, modelo {self.modelo}"


class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def descripcion(self):
        return f"Auto de la marca {self.marca}, modelo {self.modelo} con {self.puertas} puertas"


class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def descripcion(self):
        return f"Moto de la marca {self.marca}, modelo {self.modelo} con {self.cilindrada} cc"