from bubble_sort import bubble_sort
import random
import pytest

#1. Cree los siguientes unit tests para el algoritmo bubble_sort:
#1. Funciona con una lista pequeña.


def test_short_bubble_sort():
    #AA
    #Arrange
    previous_list = [5,1,99,47,15,6]
    #Act
    my_list = bubble_sort(previous_list)
    #Assert
    assert my_list == [1, 5, 6, 15, 47, 99]


#---------------------------------------------------------------------------------------------------------------------------------
#2. Funciona con una lista grande (de más de 100 elementos.)


def test_large_bubble_sort():
    #AA
    #Arrange
    previous_list = [random.randint(1, 1000) for _ in range(200)]
    #Act
    my_list = bubble_sort(previous_list)
    #Assert
    assert my_list


#---------------------------------------------------------------------------------------------------------------------------------
#3. Funciona con una lista vacía.


def test_empty_bubble_sort():
    #AA
    #Arrange
    previous_list = []
    #Act
    my_list = bubble_sort(previous_list)
    #Assert
    assert my_list == []


#---------------------------------------------------------------------------------------------------------------------------------
#4.No funciona con parámetros que no sean una lista.


def test_bubble_sort_with_non_list():
    with pytest.raises(TypeError):
        bubble_sort("hola")
    
    with pytest.raises(TypeError):
        bubble_sort(123)
    
    with pytest.raises(TypeError):
        bubble_sort(None)