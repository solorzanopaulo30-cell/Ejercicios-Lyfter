#Funciones que envuelven a otras funciones (`@decorador`).
#4. Combine 2 decoradores sobre una misma función (uno que valide y otro que loguee), prestando atención al orden en que se aplican.


class validar_positivos:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Argumento {arg} no es positivo.")
        return self.func(*args, **kwargs)


class medir_tiempo:
    def __init__(self, funcion):
        self.funcion = funcion

    def __call__(self, *args, **kwargs):
        import time
        inicio = time.time()
        resultado = self.funcion(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
        return resultado


@validar_positivos
@medir_tiempo
def sumar(a, b):
    return a + b


print(sumar(5, 3))

try:
    print(sumar(-5, 3))
except ValueError as error:
    print(f"Error: {error}")