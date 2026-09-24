#Métodos de texto: `.strip()`, `.lower()`, `.split()`, `.join()`, indexado, slicing.
#5. Cree una función que cuente cuántas veces aparece una palabra específica dentro de un texto.


def count_word(text, word):
    words = text.lower().split()
    return words.count(word.lower())


print(count_word("The quick brown fox jumps over the lazy dog", "the"))