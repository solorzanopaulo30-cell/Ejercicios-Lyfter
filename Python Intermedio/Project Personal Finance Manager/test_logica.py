from logica import Entry, Spend, FinancialMgmt, Movement

#---testing-----------------------------------------------------------------------------

def test_entry_apply_returns_positive_amount():
    #AAA
    #Arrange
    entry = Entry(1000, "Salary")
    #Act
    result = entry.apply()
    #Assert
    assert result == 1000


def test_add_categories_success():
    #AAA
    # Arrange
    gestor = FinancialMgmt()
    # Act
    gestor.add_categories("Food")
    # Assert
    assert gestor.categories == ["Food"]


def test_add_movements_insufficient_balance():
    #AAA
    # Arrange
    gestor = FinancialMgmt()
    gestor.add_categories("Comida")
    gasto = Spend(5000, "Comida")
    # Act
    gestor.add_movements(gasto)
    # Assert
    assert gestor.balance == 0
    assert gestor.movements == []


def test_add_amount():
    #AAA
    #Arrange
    Deposit = Entry(2000,"food")
    # Act
    result = Deposit.apply()
    # Assert
    assert result == 2000


def test_remove_amount():
    #AAA
    #Arrange
    Deposit = Spend(4500,"little things")
    # Act
    result = Deposit.apply()
    # Assert
    assert result == -4500


def test_add_categories_empthy():
    #AAA
    #Arrange
    category = FinancialMgmt()
    #Act
    category.add_categories("")
    #Assert
    assert category.categories == []


def test_add_categories_duplicated():
    #AAA
    #Arrange
    category = FinancialMgmt()
    #Act
    category.add_categories("big things")
    category.add_categories("big things")
    #Assert
    assert category.categories == ["big things"]


def test_total_per_category():
    #AAA
    #Arrange
    category = FinancialMgmt()
    category.add_categories("mid things")
    entry = Entry(7500, "mid things")
    spend = Spend(2500, "mid things")
    spend_2 = Spend(5000, "mid things")
    category.add_movements(entry)
    category.add_movements(spend)
    category.add_movements(spend_2)
    #Act
    result = category.total_per_category("mid things")
    #Assert
    assert result == 0