#Funciones que envuelven a otras funciones (`@decorador`).
#2. Cree un decorador `validar_positivos` que verifique que todos los argumentos numéricos de una función sean positivos, lanzando un error si no.


class validar_positivos:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Argumento {arg} no es positivo.")
        for key, value in kwargs.items():
            if isinstance(value, (int, float)) and value < 0:
                raise ValueError(f"Argumento {key}={value} no es positivo.")
        return self.func(*args, **kwargs)