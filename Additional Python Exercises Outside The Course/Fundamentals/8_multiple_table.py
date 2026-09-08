#8. Cree un programa que genere la tabla de multiplicar de un número dado, del 1 al 10.


def multiple_table():
    n = int(input("Ingrese el numero a multiplicar: "))
    for number in range(1,11):
        result = n * number
        print(f"{n} x {number} = {result}")

multiple_table()