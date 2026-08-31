

def contar_mayus_minus(text):
    uppercase = 0
    lowercase = 0

    for letter in text:
        if letter.isupper():
            uppercase += 1
        elif letter.islower():
            lowercase += 1

    return uppercase, lowercase

if __name__ == '__main__':
    texto = input("Ingrese un texto: ")
    mayus, minus = contar_mayus_minus(texto)
    print(f"Mayúsculas: {mayus}")
    print(f"Minúsculas: {minus}")