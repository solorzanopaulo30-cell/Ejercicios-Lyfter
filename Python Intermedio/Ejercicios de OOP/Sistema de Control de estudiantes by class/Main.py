import Menu
import Data

#-------- Menu Interactivo 

def main():
    students_documentation = Data.import_from_csv()
    if students_documentation is None:
        students_documentation = []

    presentation = Menu.show_menu()
    Selection = Menu.menu_selection(students_documentation)


if __name__ == '__main__':
    main()