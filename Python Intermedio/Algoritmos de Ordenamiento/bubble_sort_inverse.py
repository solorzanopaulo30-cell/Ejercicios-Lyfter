

def bubble_sort(list_of_ages):
    for out_i in range(0, len(list_of_ages) - 1):
        for i in range(0, len(list_of_ages) - 1 - out_i):
            current_num = list_of_ages[i]
            next_num = list_of_ages[i + 1]
            print(f"interacion {i}. Elemento actual {current_num}. Siguente elemento {next_num}.")
            if current_num < next_num:
                print("Numero esta siendo cambiado")
                list_of_ages[i] = next_num
                list_of_ages[i + 1] = current_num


def bubble_sort_right_to_left(list_of_ages):
    for out_i in range(0, len(list_of_ages) - 1):
        for i in range(len(list_of_ages) - 1, out_i, -1):
            current_num = list_of_ages[i]
            left_num = list_of_ages[i - 1]
            print(f"interacion {i}. Elemento actual {current_num}. Elemento a la izquierda {left_num}.")
            if current_num < left_num:
                print("Numero esta siendo cambiado")
                list_of_ages[i] = left_num
                list_of_ages[i - 1] = current_num


my_list_of_ages = [1, 58, 6, 2, 70, 99, 45, 33]

bubble_sort(my_list_of_ages)
print(my_list_of_ages)

my_list_of_ages_2 = [1, 58, 6, 2, 70, 99, 45, 33]

bubble_sort_right_to_left(my_list_of_ages_2)
print(my_list_of_ages_2)