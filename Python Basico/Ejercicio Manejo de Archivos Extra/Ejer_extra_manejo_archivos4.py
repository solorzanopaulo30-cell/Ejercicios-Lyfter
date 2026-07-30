
def new_line(path):
    added = input("Ingrese su linea de texto: ")
    with open(path,'a') as file:
        file.write(added)
        print(added)


new_line('juan.txt')