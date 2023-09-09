import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_perimeter(self):
        return math.pi * 2 * self.radius

    def get_area(self):
        return math.pi * self.radius ** 2
