#`open()`, `.readlines()`, `.write()`, modos `'r'`/`'w'`/`'a'`.+
#2. Cree un programa que lea un archivo de texto y cuente cuántas líneas tiene.


test = ["1","5","6","8","9"]
counting = 0
with open("test.txt","w") as file:
    for i in test:
        file.write(i + "\n")
        counting += 1

print(counting)