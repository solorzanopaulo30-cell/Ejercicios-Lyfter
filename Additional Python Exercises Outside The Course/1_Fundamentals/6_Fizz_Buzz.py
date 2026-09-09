#6. Cree un programa que muestre los números del 1 al 100, reemplazando los múltiplos de 3 por "Fizz", los de 5 por "Buzz", y los de ambos por "FizzBuzz".

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)