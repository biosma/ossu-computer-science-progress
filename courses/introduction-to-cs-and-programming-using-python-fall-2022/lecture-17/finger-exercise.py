class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        self.radius = radius

    def get_radius(self):
        """ Returns the radius of self """
        return self.radius

    def set_radius(self, radius):
        """ radius is a number
        Changes the radius of self to radius """
        self.radius = radius

    def get_area(self):
        """ Returns the area of self using pi = 3.14 """
        return 3.14 * self.radius * self.radius

    def equal(self, c):
        """ c is a Circle object
        Returns True if self and c have the same radius value """
        return self.radius == c.radius

    def bigger(self, c):
        """ c is a Circle object
        Returns self or c, the Circle object with the bigger radius """
        if self.radius > c.radius:
            return self
        else:
            return c

#TESTS
c1 = Circle(5)
c2 = Circle(10)
c3 = Circle(15)

print(c1.get_radius())
print(c2.get_radius())
print(c3.get_radius())

print(c1.get_area())
print(c2.get_area())
print(c3.get_area())

print(c1.equal(c2))
print(c1.equal(c3))

print(c1.bigger(c2))    # c1 is bigger
print(c2.bigger(c1))    # c2 is bigger
print(c1.bigger(c3))    # c1 is bigger
print(c3.bigger(c1))    # c3 is bigger
