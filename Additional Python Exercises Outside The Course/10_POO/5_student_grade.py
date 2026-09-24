#Clases, `__init__`, `self`, atributos, métodos.
#5. Cree una clase `Estudiante` con una lista de notas, y un método que calcule el promedio.


class Estudiante():
    def __init__(self, name, notes):
        self.name = name
        self.notes = notes


    def average(self):
        if len(self.notes) == 0:
            return 0 
        return sum(self.notes) / len(self.notes)


estudiante1 = Estudiante("Juan", [85, 90, 78, 92])
promedio = estudiante1.calcular_promedio()