

#-----------attributes
class Rectangle():
    def __init__(self, width,height):
        if width < 0 or height < 0:
            raise ValueError
        self.width = width
        self.height = height

#----area
    def get_area(self):
        area = self.width * self.height
        return area

#----perimeter
    def get_perimeter(self):
        perimeter = self.height + self.width
        return perimeter

width = int(input("Ingrese el ancho del rectangulo: "))
height = int(input("Ingrese el alto del rectangulo: "))

try:
    my_rectangle = Rectangle(width, height)
    print(f"tu area es de {my_rectangle.get_area()} y tu perimetro es {my_rectangle.get_perimeter()}")
except ValueError as error:
    print("El numero no debe ser negativo")