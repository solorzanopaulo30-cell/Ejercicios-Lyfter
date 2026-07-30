def contar_mayus_minus(text):
    uppercase = 0
    lowercase = 0

    for letter in text:
        if letter.isupper():
            uppercase += 1
        elif letter.islower():
            lowercase += 1

    print(f"Mayúsculas: {uppercase}")
    print(f"Minúsculas: {lowercase}")

contar_mayus_minus(input("Ingrese un texto: "))