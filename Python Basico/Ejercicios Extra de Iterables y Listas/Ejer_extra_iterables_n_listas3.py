

numbers = [5, 2, 9, 1, 7]
smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print(f"El valor más pequeño de la lista es: {smallest}")