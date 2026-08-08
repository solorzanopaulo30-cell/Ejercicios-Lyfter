

#-------radio calculator
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = 3.14 * (self.radius ** 2)
        return area


circle_radius = Circle(15)
print(f"the radius of the circle is {circle_radius.get_area()}")