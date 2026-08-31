
def sort (text):
    words_list_1 = text.split("-")
    words_list_1.sort()
    result = "-".join(words_list_1)
    return result

if __name__ == '__main__':
    print(sort("python-variable-funcion-computadora-monitor"))