#Métodos de texto: `.strip()`, `.lower()`, `.split()`, `.join()`, indexado, slicing.
#4. Cree una función que reciba un texto y devuelva la palabra más larga.


def longest_word(text):
    words = text.split()
    return max(words, key=len)

print(longest_word("El perro corre rapidamente por el parque"))