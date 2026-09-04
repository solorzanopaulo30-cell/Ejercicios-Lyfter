

def bubble_sort(previous_list):
    for out_i in range(0, len(previous_list) - 1 ):
        for i in range(0,len(previous_list) - 1 - out_i):
            current_num = previous_list[i]
            next_num = previous_list[i + 1]
            if current_num > next_num:
                previous_list[i] = next_num
                previous_list[i + 1] = current_num
    return previous_list


