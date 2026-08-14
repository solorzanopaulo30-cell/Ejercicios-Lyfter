

#-----------attributes
class Animal():
    def __init__(self,name):
        self.name = name

class Dog(Animal):
    def speak(self):
        return "Guau"

class Cat(Animal):
    def speak(self):
        return "Miau"



dog = Dog("Firulais")
cat = Cat("Garfiel")

print(dog.speak())
print(cat.speak())