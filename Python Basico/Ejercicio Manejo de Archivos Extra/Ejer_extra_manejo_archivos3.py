

def info_saved(path):
    new_file = []
    with open(path, 'r') as file:
            words = file.readlines()
            for word in words:
                new_file.append(word)
            return new_file

def new_info(path,lines):
    with open(path, 'w') as file:
        for line in lines:
            line_cap = line.upper()
            file.write(line_cap)

presentation = info_saved("hola_mundo.txt")
new_info("caps.txt", presentation)




