# shapes################################################
class Rectangle:
    def __init__(self, l=1, w=1):
        self.length = l
        self.width = w

    def setLength(self, n):
        self.length = n

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

    def setWidth(self, n):
        self.width = n

    def area(self):
        return self.width * self.length


class Square:
    def __init__(self, side=1):
        self._rectangle = Rectangle(side, side)

    def setSide(self, n):
        self._rectangle.setLength(n)
        self._rectangle.setWidth(n)

    def getSide(self):
        return self._rectangle.getLength()

    def area(self):
        return self._rectangle.area()


# main#############################################

def measure_rectangle(r):
    print(r.getWidth(), "x", r.getLength())
    print("Area:", r.area())

    print("double length...")
    r.setLength(2 * r.getLength())

    print(r.getWidth(), "x", r.getLength())
    print("Area:", r.area())


def measure_square(s):
    print(s.getSide(), "x", s.getSide())
    print("Area:", s.area())

    print("double side...")
    s.setSide(2 * s.getSide())

    print(s.getSide(), "x", s.getSide())
    print("Area:", s.area())


a = Square(6)
b = Rectangle(8, 3)

print("\nsquare")
measure_square(a)
print("\nrectangle")
measure_rectangle(b)