#Funciones que envuelven a otras funciones (`@decorador`).
#1. Cree un decorador `medir_tiempo` que imprima cuánto tarda en ejecutarse la función que decora.


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

@medir_tiempo
def suma_lenta(n):
    total = 0
    for i in range(n):
        total += i
    return total

resultado = suma_lenta(1000000)
print(resultado)