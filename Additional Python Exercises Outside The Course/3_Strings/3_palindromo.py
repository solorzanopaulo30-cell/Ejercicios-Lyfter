#Métodos de texto: `.strip()`, `.lower()`, `.split()`, `.join()`, indexado, slicing.
#3. Cree una función que verifique si un texto es un palíndromo (ignorando mayúsculas y espacios).


def is_palindromo(text):
    clean_text = text.lower().replace(" ", "")
    reverse_text = clean_text[::-1]
    return clean_text == reverse_text

print(is_palindromo("Anita lava la tina"))
print(is_palindromo("Hola mundo"))