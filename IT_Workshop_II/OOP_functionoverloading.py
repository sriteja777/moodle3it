from  graphics import *
import time

#########################################################################
### Operator overloading (str, +, -)

class Shape(object):
   'Common base class for all shapes'
   shapeCount = 0  #1
   win =  GraphWin("Shapes display", 400, 400)
   
   def __init__(self, name, description):
      "constructor for shape class"
      self.name = name
      self.description = description
      print '------ shape->constructor name=', name, ' description=', description
      Shape.shapeCount += 1
      
   def __del__(self):
      print "------ shape->Destructor:", str(self)
      Shape.shapeCount -= 1
      if (Shape.shapeCount == 0):
        print 'reference count has reached zero: closing window'
        Shape.win.close()

      
class MyCircle(Shape):
    'circle class'
 
    def __init__(self, center, radius, name='circle', description='this is a class for creating and drawing circles'): 
        self.center = center
        self.radius = radius
        super(MyCircle, self).__init__(name, description)
        print Shape.shapeCount,' circle->constructor:'

    def draw(self, fillColor='brown', borderColor='gray', borderWidth = 5):
        o = Circle(self.center, self.radius)
        o.setFill(fillColor)
        o.setOutline(borderColor)
        o.setWidth(borderWidth)
        o.draw(self.win)
        super(MyCircle, self).win.getMouse()

    def __del__(self):
        print  Shape.shapeCount,' circle->destructor'
        super(MyCircle, self).__del__()

def test():
   # MyCircle is called with 4 arguments
   a = MyCircle(Point(50,50), 50, "circle-50-50-50", "circle created using optional arguments")
   
   # draw is called with 3 arguments
   a.draw('yellow', 'purple', 15)

   # MyCircle is called with 3 arguments
   b = MyCircle(Point(150,150), 50, 'circle-150-150-100')
   
   # draw is called with 2 arguments
   b.draw('green', 'pink')

   # MyCircle is called with 2 arguments
   c = MyCircle(Point(200,200), 50)
   
   # draw is called with 1 arguments
   c.draw('blue')

   # MyCircle is called with 2 arguments
   d = MyCircle(Point(250,250), 50)
   
   # draw is called with 0 arguments
   d.draw()
   
test() 



