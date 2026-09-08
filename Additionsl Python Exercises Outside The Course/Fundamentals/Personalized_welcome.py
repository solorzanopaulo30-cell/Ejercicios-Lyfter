#1. Cree un programa que pida el nombre y la edad del usuario, y muestre un saludo personalizado.


def greeting():
    name = input("Ingrese su nombre: ")
    age = int(input("Ingrese su edad: "))
    print(f"Hola bienvenido {name} de edad de {age}")

greeting()