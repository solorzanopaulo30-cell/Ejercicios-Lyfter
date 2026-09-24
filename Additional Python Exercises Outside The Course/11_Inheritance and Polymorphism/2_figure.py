#Clases hijas, sobrescritura de métodos.
#2. Cree una clase base `Figura` con un método `area()`, y clases hijas `Cuadrado`, `Circulo` y `Triangulo` que lo sobrescriban.


class Figura():
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio ** 2

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return 0.5 * self.base * self.altura