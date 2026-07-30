
numbers = []
for i in range(0, 5):
    num = int(input(f"Ingrese un número {i+1}: "))
    numbers.append(num)

positive_number = True

for number in numbers:
    if number <= 0:
        positive_number = False
        break

if positive_number:
    print("todos los números ingresados son positivos")
else:
    print("al menos uno de los números ingresados es negativo")