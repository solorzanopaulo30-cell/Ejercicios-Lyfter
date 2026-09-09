#2. Cree un programa que reciba un número y muestre si es par o impar.

def even_or_odd(num):
    result = num % 2
    if result == 0:
        print(f"tu numero {num} es par")
    else:
        print(f"tu numero {num} es impar")

even_or_odd(10)