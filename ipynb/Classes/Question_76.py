class Rectangle:

    def __init__(self,lenght,width):
        self.lenght = lenght
        self.width = width

    def get_perimeter(self):
        return self.width*2 + self.lenght*2

    def get_area(self):
        return self.width*self.lenght
        