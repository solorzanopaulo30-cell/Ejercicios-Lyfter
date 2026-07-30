def reserve_string(text):
    reverse = ""
    for i in range(len(text) - 1, -1, -1):
        reverse = reverse + text[i]
    return reverse

result = reserve_string(input("Ingrese un texto para invertir: "))
print(result)