
def sort (text):
    words_list_1 = text.split("-")
    words_list_1.sort()
    result = "-".join(words_list_1)
    return result

print(sort("python-variable-funcion-computadora-monitor"))