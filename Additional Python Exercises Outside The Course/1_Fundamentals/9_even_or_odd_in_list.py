#9. Cree un programa que cuente cuántos números pares e impares hay en una lista fija de 10 números.


def even_or_odd_in_list():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_count = 0
    odd_count = 0

    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print(f"Cantidad de números pares: {even_count}")
    print(f"Cantidad de números impares: {odd_count}")

even_or_odd_in_list()