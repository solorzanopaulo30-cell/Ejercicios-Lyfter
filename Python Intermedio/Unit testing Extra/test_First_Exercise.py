from First_Exercise import Calulator

#----------------------------------------------------------

def test_calulator_sum():
    #AAA
    #Arrange
    num = 5
    num2 = 5
    calc = Calulator()
    #Act
    result = calc.sums(num,num2)
    #Assert
    assert result == 10

#----------------------------------------------------------

def test_calulator_rest():
    #AAA
    #Arrange
    num = -10
    num2 = -5
    calc = Calulator()
    #Act
    result = calc.rests(num,num2)
    #Assert
    assert result == -5

#----------------------------------------------------------

def test_calulator_divs():
    #AAA
    #Arrange
    num = 0
    num2 = 2
    calc = Calulator()
    #Act
    result = calc.divs(num,num2)
    #Assert
    assert result == 0