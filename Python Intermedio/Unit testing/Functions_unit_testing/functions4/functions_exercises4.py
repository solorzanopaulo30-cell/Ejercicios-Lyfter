def reverse_string(text):
    reverse = ""
    for i in range(len(text) - 1, -1, -1):
        reverse = reverse + text[i]
    return reverse

if __name__ == '__main__':
    result = reverse_string(input("Ingrese un texto para invertir: "))
    print(result)