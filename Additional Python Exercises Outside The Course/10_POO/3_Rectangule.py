#Clases, `__init__`, `self`, atributos, métodos.
#3. Cree una clase `Rectangulo` con métodos para calcular área y perímetro.


class Rectangule():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


rect = Rectangule(5, 3)
print(rect.area())        
print(rect.perimetro())   