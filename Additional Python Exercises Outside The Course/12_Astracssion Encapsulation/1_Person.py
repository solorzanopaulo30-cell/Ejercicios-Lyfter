#`@property`, `@setter`, atributos privados (`_algo`), `ABC`, `@abstractmethod`.
#1. Cree una clase `Persona` con un atributo privado `_edad`, usando `@property` para leerlo y un `@edad.setter` que valide que no sea negativo.


class Persona:
    def __init__(self, edad):
        self._edad = edad

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if valor < 0:
            raise ValueError("La edad no puede ser negativa.")
        self._edad = valor