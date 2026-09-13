from logica import Entry, Spend, FinancialMgmt, Movement, Category

#---testing-----------------------------------------------------------------------------

def test_entry_apply_returns_positive_amount():
    # Arrange
    category = Category("Salary")
    entry = Entry("Sueldo", 1000, category)
    # Act
    result = entry.apply()
    # Assert
    assert result == 1000


def test_add_categories_success():
    # Arrange
    manager = FinancialMgmt()
    # Act
    manager.add_categories("Food")
    # Assert
    assert manager.categories[0].name == "Food"


def test_add_movements_insufficient_balance():
    # Arrange
    manager = FinancialMgmt()
    manager.add_categories("Comida")
    category = manager.categories[0]
    expense = Spend("Super", 5000, category)
    # Act & Assert
    import pytest
    with pytest.raises(ValueError):
        manager.add_movements(expense)
    assert manager.balance == 0
    assert manager.movements == []


def test_entry_apply_returns_full_amount():
    # Arrange
    category = Category("food")
    income = Entry("Bono", 2000, category)
    # Act
    result = income.apply()
    # Assert
    assert result == 2000


def test_spend_apply_returns_negative_amount():
    # Arrange
    category = Category("little things")
    expense = Spend("Snack", 4500, category)
    # Act
    result = expense.apply()
    # Assert
    assert result == -4500


def test_add_categories_empty():
    # Arrange
    manager = FinancialMgmt()
    # Act
    manager.add_categories("")
    # Assert
    assert manager.categories == []


def test_add_categories_duplicated():
    # Arrange
    manager = FinancialMgmt()
    # Act
    manager.add_categories("big things")
    manager.add_categories("big things")
    # Assert
    assert len(manager.categories) == 1


def test_total_per_category():
    # Arrange
    manager = FinancialMgmt()
    manager.add_categories("mid things")
    category = manager.categories[0]
    entry = Entry("Ingreso", 7500, category)
    spend = Spend("Gasto 1", 2500, category)
    spend_2 = Spend("Gasto 2", 5000, category)
    manager.add_movements(entry)
    manager.add_movements(spend)
    manager.add_movements(spend_2)
    # Act
    result = manager.total_per_category("mid things")
    # Assert
    assert result == 0