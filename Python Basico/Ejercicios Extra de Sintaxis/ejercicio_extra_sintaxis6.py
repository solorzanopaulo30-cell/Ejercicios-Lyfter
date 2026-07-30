
number = int(input("Ingrese un número del 1 al 10: "))
for numbers in range(1, 13):
    result = number * numbers
    print(f"{number} x {numbers} = {result}")