
numbers = []
for i in range(0, 10):
    num = int(input(f"Ingrese un número {i+1}: "))
    numbers.append(num)

search_number = int(input("Ingrese un número a buscar: "))

counter = 0
for n in numbers:
    if n == search_number:
        counter += 1

print(f"El número ingresado aparece {counter} veces en la lista.")
