from functions_exercises7 import is_prime, get_primes


#-----------------------------------------------------------------------------------------------------

def test_get_primes_mixed_list():
    #AAA
    # Arrange
    numbers = [1, 4, 6, 7, 13, 9, 67]
    # Act
    result = get_primes(numbers)
    # Assert
    assert result == [7, 13, 67]


#-----------------------------------------------------------------------------------------------------

def test_get_primes_is_empthy():
    #AAA
    # Arrange
    numbers = [1, 4, 6, 9]
    # Act
    result = get_primes(numbers)
    # Assert
    assert result == []



#-----------------------------------------------------------------------------------------------------

def test_get_primes_all_of_are_prime():
    #AAA
    # Arrange
    numbers = [2, 3, 5, 7, 11]
    # Act
    result = get_primes(numbers)
    # Assert
    assert result == [2,3,5,7,11]