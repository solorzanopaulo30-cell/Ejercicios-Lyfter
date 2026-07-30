vocales = ["a", "e", "i", "o", "u"]

def vocal(main):
    box = 0
    for caracter in main:
        if caracter in vocales:
            box = box + 1
    return box

str_1 = input("Ingrese su palabra por favor: ")
result = vocal(str_1)
print(result)
