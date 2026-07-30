
words = []
for i in range(5):
    word = input(f"Ingrese la palabra {i + 1}: ")
    words.append(word)

words_with_more_than_4_letters = []
for word in words:
    if len(word) > 4:
        words_with_more_than_4_letters.append(word)

print("Palabras ingresadas:", words)
print("Palabras con más de 4 letras:", words_with_more_than_4_letters)    