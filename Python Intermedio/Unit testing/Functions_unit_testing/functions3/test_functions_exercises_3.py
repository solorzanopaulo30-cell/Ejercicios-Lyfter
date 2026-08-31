from functions_exercises3 import sum_note
import random
import pytest


#--------------------------------------------------------------------------------------------------

def test_sum_notes():
    #AA
    #Arrange
    notes = [45,15,99,70,80,12]
    #Act
    my_notes = sum_note(notes)
    #Assert
    assert my_notes == 321


#--------------------------------------------------------------------------------------------------

def test_empty_sum_notes():
    #AA
    #Arrange
    notes = []
    #Act
    my_notes = sum_note(notes)
    #Assert
    assert my_notes == 0


#----------------------------------------------------------------------------------------------------

def test_sum_note_with_non_list():
    with pytest.raises(TypeError):
        sum_note("hola")
    with pytest.raises(TypeError):
        sum_note(123)
    with pytest.raises(TypeError):
        sum_note(None)