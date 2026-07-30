
def counting(path):
    with open(path, 'r') as file:
        words = file.readlines()
        count = []
        for word in words:
            count.extend(word.split())
        words_on_list = len(count)
        print(f"Este archivo contiene {words_on_list} palabras")
        return words_on_list


counting("extra.txt")