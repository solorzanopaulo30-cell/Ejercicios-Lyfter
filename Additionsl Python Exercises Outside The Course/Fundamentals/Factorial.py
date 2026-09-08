#7. Cree un programa que pida un número y calcule su factorial usando un bucle.


n = int(input("Ingrese un número: "))
resultado = 1
for numero in range(1, n + 1):
    resultado = resultado * numero
print(f"El factorial de {n} es {resultado}")