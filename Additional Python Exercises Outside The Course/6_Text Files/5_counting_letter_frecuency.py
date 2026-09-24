#`open()`, `.readlines()`, `.write()`, modos `'r'`/`'w'`/`'a'`.+
#5. Cree un programa que lea un archivo de texto y cuente la frecuencia de cada letra del abecedario.


with open("alfa.txt", "r") as file:
    text = file.read()

text = text.lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    count = text.count(letter)
    print(f"{letter}: {count}")