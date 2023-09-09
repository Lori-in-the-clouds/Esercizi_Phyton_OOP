class Shape:

    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):

    def __init__(self,l):
        super.__init__()
        self.l = l
    def area(self):
        return self.l**2



s = Shape()
print(s.area())
s =Square(3)

