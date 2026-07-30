
numeros = []

for i in range(10):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

mayor = numeros[0]

for n in numeros:
    if n > mayor:
        mayor = n

print("Números ingresados:", numeros)
print("El número más alto es:", mayor)