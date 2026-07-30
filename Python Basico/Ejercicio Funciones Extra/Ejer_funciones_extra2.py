
def words(word, n):
    words_over = []
    for carater in word: 
        if len(carater) > n:
            words_over.append(carater)
    return words_over


parraf = "breaking news perry el ornitorinco es encontrado muerto por sobre dosis"
list_1 = parraf.split()
n = int(input("Ingrese el numero de letras minimas en la palabra:"))

result = words(list_1, n)
print(result)