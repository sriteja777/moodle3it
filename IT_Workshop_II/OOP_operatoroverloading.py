from  graphics import *
import time

#########################################################################
### Operator overloading (str, +, -)

class Shape(object):
   'Common base class for all shapes'
   shapeCount = 0  #1
   win =  GraphWin("Shapes display", 400, 400)
   
   def __init__(self, name, description, color):
      "constructor for shape class"
      self.name = name
      self.description = description
      self.color = color
      print '------ shape->constructor'
      Shape.shapeCount += 1
      
   def __del__(self):
      print "------ shape->Destructor:", str(self)
      Shape.shapeCount -= 1
      if (Shape.shapeCount == 0):
        print 'reference count has reached zero: closing window'
        time.sleep(2)
        Shape.win.close()

      
class MyCircle(Shape):
    'circle class'
    def __init__(self, center, radius, color): 
        self.center = center
        self.radius = radius
        super(MyCircle, self).__init__('circle', 'this is a class for creating and drawing circles',color)
        print Shape.shapeCount,' circle->constructor:', str(self)

    def draw(self):
        o = Circle(self.center, self.radius)
        o.setFill(self.color)
        o.draw(self.win)
        super(MyCircle, self).win.getMouse()

    def __del__(self):
        print  Shape.shapeCount,' circle->destructor'
        super(MyCircle, self).__del__()

    def __str__(self):
        return "Name:{0} center={1} radius={2}".format(self.name, self.center, self.radius)

    def __add__(self, obj):
        new_pt = Point(self.center.x + obj.center.x, self.center.y + obj.center.y)
        new_rad = self.radius + obj.radius
        new_obj = MyCircle(new_pt, new_rad, 'green')
        print str(new_obj)
        return new_obj

    def __sub__(self, obj):
        new_pt = Point(self.center.x - obj.center.x, self.center.y - obj.center.y)
        new_rad = self.radius - obj.radius
        if new_rad < 0:
           new_rad = 0 - new_rad
           
        new_obj = MyCircle(new_pt, new_rad, 'yellow')
        print str(new_obj)
        return new_obj
        

def test(): 
   a = MyCircle(Point(50,50), 50, 'blue')
   a.draw()
   b = MyCircle(Point(150,150), 100, 'red')
   b.draw()
   c = a + b
   c.draw()
   d = b - a
   d.draw()
   
test() 



