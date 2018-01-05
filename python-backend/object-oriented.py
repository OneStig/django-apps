import numpy

class Sample():
    pass

x = Sample()
print(type(x))

class Circle():
    pi = numpy.pi

    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius * Circle.pi

    def set_radius(self, r):
        self.radius = r

myc = Circle(321)
print(myc.radius)
myc.set_radius(123)
print(myc.radius)
