#4. Cree un programa que calcule el área y el perímetro de un triángulo.

class Triangle():
    def __init__(self,side1,side2,side3,base,height):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.base = base
        self.height = height

    def calculation(self):
        perimeter = int(self.side1 + self.side2 + self.side3)
        area = int((self.base * self.height) / 2)
        return perimeter, area

calculation = Triangle(5,6,8,18,20)
perimeter, area = calculation.calculation()

print(f"el perimetro es {perimeter}")
print(f"el area es {area}")