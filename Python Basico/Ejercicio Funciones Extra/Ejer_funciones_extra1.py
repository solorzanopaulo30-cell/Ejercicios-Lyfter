def caracter(text, char):
    counter = 0
    for letter in text:
        if letter == char:
            counter += 1
    return counter

secret_word = "Perry el ornitorrinco o como se escriba xd"
result = caracter(secret_word, "r")
print(result)