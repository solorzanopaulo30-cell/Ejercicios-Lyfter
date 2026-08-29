#Analice el algoritmo de bubble_sort usando la Big O Notatio


def bubble_sort(list):
    for out_i in range(0, len(list) - 1 ): # O(n)
        for i in range(0,len(list) - 1 - out_i): # O(n)
            current_num = list[i]  # O(1)
            next_num = list[i + 1] # O(1)
            if current_num > next_num: # O(1)
                list[i] = next_num # O(1)
                list[i + 1] = current_num # O(1)


my_list_of_ages = [1,58,6,2,70,99,45,33]

bubble_sort(my_list_of_ages)
print(my_list_of_ages)
