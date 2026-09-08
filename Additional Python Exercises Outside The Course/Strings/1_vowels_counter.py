#Métodos de texto: `.strip()`, `.lower()`, `.split()`, `.join()`, indexado, slicing.
#1. Cree una función que reciba un texto y devuelva cuántas vocales tiene.


def counter(text):
    count = 0
    vowels = "aeiou"
    for letter in text.lower():
        if letter in vowels:
            count += 1
    print(count)

counter("Programacion")