#
#8. Cree una función que reemplace todas las vocales de un texto por el símbolo "*".


def replace(text):
    vowels = "aeiou"
    for letter in vowels:
        text = text.replace(letter,"*")
    print(text)

replace("hola mundo, como estan todos")