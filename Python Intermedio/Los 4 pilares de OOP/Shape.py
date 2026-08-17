
import math
from abc import ABC, abstractmethod

#-------------main
class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

#------------ Other classes

class Circule(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
            return 2 * math.pi * self.radius

    def calculate_area(self):
            return math.pi * (self.radius ** 2)

#------------------------------------

class Square(Shape):
    def __init__(self, slide):
        self.slide = slide

    def calculate_perimeter(self):
        return self.slide * 4

    def calculate_area(self):
        return self.slide ** 2

#-------------------------------------


class Rectangle(Shape):
    def __init__(self, width,height):
        self.width = width 
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)

    def calculate_area(self):
        return self.height * self.width
#---------------------------



my_circle = Circule(15)
my_square = Square(10)
my_rectangle = Rectangle(15,20)

print(my_circle.calculate_perimeter())
print(my_circle.calculate_area())
print(my_square.calculate_perimeter())
print(my_square.calculate_area())
print(my_rectangle.calculate_perimeter())
print(my_rectangle.calculate_area())


