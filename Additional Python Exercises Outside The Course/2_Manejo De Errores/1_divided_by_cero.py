#try`/`except`, `raise`, excepciones específicas.
#1. Cree una función que reciba dos números y los divida, capturando el error si el segundo es 0.


def div():
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        result = num1 / num2
        print(f"El resultado de la división es: {result}")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")

div()