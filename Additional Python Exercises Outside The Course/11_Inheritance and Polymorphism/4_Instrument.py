#Clases hijas, sobrescritura de métodos.
#4. Cree una clase `Instrumento` con un método `tocar()`, y clases hijas `Guitarra` y `Piano` que lo sobrescriban con sonidos distintos.


class Instrumento:
    def __init__(self, nombre):
        self.nombre = nombre

    def tocar(self):
        pass


class Guitarra(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre)

    def tocar(self):
        return f"{self.nombre} está tocando la guitarra con acordes."


class Piano(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre)

    def tocar(self):
        return f"{self.nombre} está tocando el piano con notas."