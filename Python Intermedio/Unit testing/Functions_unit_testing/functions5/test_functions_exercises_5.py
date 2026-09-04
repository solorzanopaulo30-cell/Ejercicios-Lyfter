from functions_exercises5 import contar_mayus_minus


#--------------------------------------------------------------------------------------------------

def test_contar_mayus_minus():
    #AAA
    #Arrange
    text = "Hola Mundo"
    #Act
    result = contar_mayus_minus(text)
    #Assert
    assert result == (2,7)



#--------------------------------------------------------------------------------------------------

def test_contar_all_upper():
    #AAA
    #Arrange
    text = "HOLA"
    #Act
    result = contar_mayus_minus(text)
    #Assert
    assert result == (4,0)


#--------------------------------------------------------------------------------------------------

def test_contar_all_lower():
    #AAA
    #Arrange
    text = "hola"
    #Act
    result = contar_mayus_minus(text)
    #Assert
    assert result == (0,4)