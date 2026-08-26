

def bubble_sort(num_list):
    for out_i in range(0, len(num_list)):
        for i in range(0, len(num_list) - 1):
            current_num = num_list[i]
            next_num = num_list[i + 1]
            if current_num > next_num:
                num_list[i + 1] = current_num
                num_list[i] = next_num
    return num_list


def validated_bubble_sort(num_list):
    if len(num_list) == 0:
        print("Error: la lista esta vacia")
        return

    for i in num_list:
        if not isinstance(i, (int, float)):
            print("Error: La lista contiene elementos no numéricos")
            return

    result = bubble_sort(num_list)
    print(result)
    return result


validated_bubble_sort([5, "hola", 2])
validated_bubble_sort([])
validated_bubble_sort([5, 3, 8, 1, 9])