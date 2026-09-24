#Clases, `__init__`, `self`, atributos, métodos.
#1. Cree una clase `Libro` con título, autor y año, y un método que muestre su información.


class Libro():
    def __init__(self, titule, author, year):
        self.titule = titule 
        self.author = author
        self.year = year

    def show_info(self):
        print(f"titulo: {self.titule}, autor: {self.author}, año: {self.year}")