
number = int(input("Ingrese un número: "))
total_sum = 0
for numbers in range(1, number + 1):
    total_sum = total_sum + numbers
print(f"La suma total de los números del 1 al {number} es: {total_sum}")