class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        self.radius = radius

    def get_radius(self):
        """ Returns the radius of self """
        return self.radius

    def __add__(self, c):
        """ c is a Circle object 
        Returns a new Circle object whose radius is 
        the sum of self and c's radius """
        return Circle(self.radius + c.get_radius())

    def __str__(self):
        """ A Circle's string representation is the radius """
        return str(self.radius)

#TESTS
c1 = Circle(5)
c2 = Circle(10)
c3 = Circle(15)

print(c1)
print(c2)
print(c3)

print(c1 + c2)
print(c1 + c3)