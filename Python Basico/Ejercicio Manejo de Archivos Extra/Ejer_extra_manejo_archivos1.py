
def reading(path):
    with open(path,'r') as file:
        lines = file.readlines()
        cleaned_lines = []
        for line in lines:
            cleaned_lines.append(line.strip())
        final_text = " ".join(cleaned_lines)
        return final_text


def new_file(path1,text):
    with open(path1, 'w') as file:
        file.write(text)


def main():
    x = reading("extra.txt")
    new_file("new_file.txt", x)


if __name__ == '__main__':
    main()








