#Métodos de texto: `.strip()`, `.lower()`, `.split()`, `.join()`, indexado, slicing.
#2. Cree una función que reciba una frase y la devuelva con cada palabra capitalizada.


def capitalized(text):
    words = text.split()
    capitalized_words = []
    for word in words:
        capitalized_words.append(word.capitalize())
    result = " ".join(capitalized_words)
    return result

print(capitalized("hola mundo cruel"))