from functions_exercises6 import sort


def test_sort_five_words():
    #AAA
    # Arrange
    text = "python-variable-funcion-computadora-monitor"
    # Act
    result = sort(text)
    # Assert
    assert result == "computadora-funcion-monitor-python-variable"



#-----------------------------------------------------------------------------------------------------

def test_sorted_words():
    #AAA
    # Arrange
    text = "a-b-c-d-e"
    # Act
    result = sort(text)
    # Assert
    assert result == "a-b-c-d-e"



#-----------------------------------------------------------------------------------------------------

def test_inverse_words():
    #AAA
    # Arrange
    text = "z-y-x-a-b"
    # Act
    result = sort(text)
    # Assert
    assert result == "a-b-x-y-z"