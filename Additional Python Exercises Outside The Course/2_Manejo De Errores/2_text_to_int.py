#`try`/`except`, `raise`, excepciones específicas.
#2. Cree una función que convierta un texto a entero, mostrando un mensaje de error claro si no es posible.


def text_to_int():
    try:
        text = input("Ingrese un texto para convertir a entero: ")
        number = int(text)
        print(f"El texto convertido a entero es: {number}")
    except ValueError:
        print("Error: El texto ingresado no puede ser convertido a un número entero.")

text_to_int()