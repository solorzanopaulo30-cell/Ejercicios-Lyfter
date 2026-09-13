#Acceso por clave, `.keys()`, `.items()`, diccionarios anidados.
#1. Cree un programa que cuente cuántas veces aparece cada palabra en un texto, usando un diccionario.


def count_words(text):
    word_count = {}
    words = text.split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

text = "esto es un ejemplo. este texto se utiliza para pruebas."
print(count_words(text))
