#Clases hijas, sobrescritura de métodos.
#1. Cree una clase base `Empleado` y clases hijas `Gerente` y `Vendedor`, cada una con su propio cálculo de salario.


class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base


class Gerente(Empleado):
    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self.bono = bono

    def calcular_salario(self):
        return self.salario_base + self.bono


class Vendedor(Empleado):
    def __init__(self, nombre, salario_base, comision):
        super().__init__(nombre, salario_base)
        self.comision = comision

    def calcular_salario(self):
        return self.salario_base + self.comision
