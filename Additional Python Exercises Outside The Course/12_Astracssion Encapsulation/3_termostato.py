#`@property`, `@setter`, atributos privados (`_algo`), `ABC`, `@abstractmethod`.
#3. Cree una clase `Termostato` con un atributo privado `_temperatura`, validando con un setter que esté entre 0 y 40 grados.


class Termostato:
    def __init__(self, temperatura):
        self._temperatura = None
        self.temperatura = temperatura

    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if 0 <= valor <= 40:
            self._temperatura = valor
        else:
            raise ValueError("La temperatura debe estar entre 0 y 40 grados.")