import Menu
import Actions #Creo que no lo usare pero aja, se queda just in case
import Data

#-------- Menu Interactivo 

def main():
    presentation = Menu.show_menu()
    Selection = Menu.menu_selection(Data.students_info())




if __name__ == '__main__':
    main()
    