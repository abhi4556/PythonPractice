#/usr/bin/python

class Shape:
    def __init__(self,name,length,breadth=None):
        self.name = name
        self.length = length
        self.breadth = breadth

    def Area(self):
        pass

class Rectangle(Shape):
    def __init__(self,name,length,breadth=None):
        super().__init__(name,length,breadth)
    # displays the object in better format
    # when __str__ and __repr__ both present __str__ gets the previlage
    def __repr__(self):
        return "Rectangle({}-{}-{})".format(self.name,self.length,self.breadth)
    def __str__(self):
        return '{}-{}'.format(self.length,self.breadth)
    def area_of_rect(self):
        return self.length*self.breadth
    
class Square(Shape):
    def __init__(self,name,length,breadth=None):
        super().__init__(name,length,breadth=None)
    
    def area_of_sqr(self):
        return self.length * self.length

obj_sqr = Square('Square',5)
print("Area of square::{}".format(obj_sqr.area_of_sqr()))
obj_rect = Rectangle("Rectangle", 5, 6)
print("Area of rectangle::{}".format(obj_rect.area_of_rect()))
print(obj_rect)