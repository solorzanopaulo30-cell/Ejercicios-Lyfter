

class Employee():
    def __init__(self,name,salary):
        self._name = name
        self.salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError ("Valor no puede ser negativo")
        self._salary = value

    def promote(self,increase): 
        self.increase = increase
        self.increase = (self._salary * self.increase) + self._salary
        self.salary = self.increase


#++++++++++++++++++++++++++++++++++++
employee = Employee("Ana", 1000)
employee.promote(0.1)
print(employee.salary)