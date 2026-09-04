from functions_exercises4 import reverse_string


#--------------------------------------------------------------------------------------------------

def test_reverse_string_simple_world():
    #AA
    #Arrange
    text = "hola"
    #Atc
    result = reverse_string(text)
    #Assert
    assert result == "aloh"



#--------------------------------------------------------------------------------------------------

def test_reverse_string_palindrome_world():
    #AA
    #Arrange
    text = "ana"
    #Atc
    result = reverse_string(text)
    #Assert
    assert result == "ana"



#--------------------------------------------------------------------------------------------------

def test_reverse_string_emptly_space():
    #AA
    #Arrange
    text = ""
    #Atc
    result = reverse_string(text)
    #Assert
    assert result == ""