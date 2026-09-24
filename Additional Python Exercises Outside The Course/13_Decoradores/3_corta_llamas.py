#Funciones que envuelven a otras funciones (`@decorador`).
#3. Cree un decorador `contar_llamadas` que lleve la cuenta de cuántas veces se llamó a la función decorada.


class contar_llamadas:
    def __init__(self, funcion):
        self.funcion = funcion
        self.contador = 0

    def __call__(self, *args, **kwargs):
        self.contador += 1
        print(f"La función {self.funcion.__name__} ha sido llamada {self.contador} veces.")
        return self.funcion(*args, **kwargs)