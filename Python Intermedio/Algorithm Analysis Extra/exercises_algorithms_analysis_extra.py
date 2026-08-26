

#Los siguientes dos algoritmos hacen lo mismo: calcular la suma de los primeros n números naturales

#version 1
def manual_add(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result


#version 2
def add_formula(n):
    return n * (n + 1) // 2


#Preguntas:



#¿Cuál es la complejidad de cada versión?

#-La version 1 va N cantidad de veces por el for, uno por uno mientras que la version 2 toma el valor de N para calcularlo de manera directa con una formula 



#¿Qué versión usaría si number = 1 000 000 000? ¿Por qué?

#- la version 2, ya que no recorreria todos las escenarios posibles 


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Considere los siguientes dos algoritmos:
#Preguntas:
#¿Cuál es la complejidad de cada algoritmo?

def linear_search(my_list, target):
    for item in my_list: #O(n)
        if item == target: #O(1)
            return True #O(1)
    return False #O(1)


def binary_search(my_list, target):
    low = 0 #O(1)
    high = len(my_list) - 1 #O(1)
    while low <= high: #O(n)
        mid = (low + high) // 2 #O(n)
        if my_list[mid] == target: #O(n)
            return True #O(1)
        elif my_list[mid] < target: #O(1)
            low = mid + 1 #O(1)
        else: 
            high = mid - 1 #O(1)
    return False #O(1)


#¿En qué condiciones conviene usar cada uno?

#- linear la usaria si todo esta en orden, si esta desordenada usaria binary_search



#¿Qué pasa si la lista no está ordenada?

#-linear no funcionaria ya que icupa estar ordenada, sin embargo binary_search lo va descartando



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Analice la siguiente función:

def print_all_pairs(my_dict):
    for key1 in my_dict:
        for key2 in my_dict:
            print(f"{key1}-{key2}")

#Preguntas:
#¿Cuál es la complejidad temporal?



#¿Cuanto dura si hay 1 millón de claves?