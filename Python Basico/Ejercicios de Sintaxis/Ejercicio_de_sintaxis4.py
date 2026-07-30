
number1 = int(input("Ingrese el primer número: "))
number2 = int(input("Ingrese el segundo número: "))
number3 = int(input("Ingrese el tercer número: "))

if number1 >= number2 and number1 >= number3:
    print(f"El mayor es: {number1}")
elif number2 >= number1 and number2 >= number3:
    print(f"El mayor es: {number2}")
else:
    print(f"El mayor es: {number3}")