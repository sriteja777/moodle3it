from  graphics import *
import time
import sys

#########################################################################
### destructor is called when reference count to object goes down to zero
### Operator overloading (str)

class Shape(object):
   'Common base class for all shapes'
   shapeCount = 0  #1
   win =  None 
   
   def __init__(self, name, description, color):
      "constructor for shape class"
      self.name = name
      self.description = description
      self.color = color
      print '------ shape->constructor'
      Shape.shapeCount += 1
      if (Shape.shapeCount == 1):
         Shape.win =  GraphWin("Shapes display", 500, 500)

   def __str__(self):
      return "Name:{0} center={1} radius={2}".format(self.name, self.center, self.radius)

   def draw(self): pass

   def __del__(self):
      print "------ shape->Destructor:", str(self)
      Shape.shapeCount -= 1
      if (Shape.shapeCount == 0):
        print 'reference count has reached zero: closing window'
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
        self.win.getMouse()

    def __del__(self):
        print  Shape.shapeCount,' circle->destructor'
        super(MyCircle, self).__del__() 

# new object a constructed with reference count 1
a = MyCircle(Point(50,50), 50, 'blue')
a.draw()
print "reference-count of a= ", sys.getrefcount(a)
#reference count goes up
aa = a
print "reference-count of a= ", sys.getrefcount(a)
#reference count goes up
aaa = [2,a]
print "reference-count of a= ", sys.getrefcount(a)
#reference count goes down
aa = 3
print "reference-count of a= ", sys.getrefcount(a)
#reference count goes down
aaa = [2, 4]
print "reference-count of a= ", sys.getrefcount(a)

# new object b constructed with reference count 1
b = MyCircle(Point(100,100), 50, 'red')
b.draw()
print "reference-count of b= ", sys.getrefcount(b)

# new object c[2] constructed with reference count 1
c = ['yes', 45, MyCircle(Point(150,150), 50, 'yellow')]
c[2].draw()
print "reference-count of c= ", sys.getrefcount(c)

# inside foo, new object d constructed with reference count 1 
def foo():
   d = MyCircle(Point(200,200), 50, 'green')
   d.draw()
   print "reference-count of d= ", sys.getrefcount(d)
foo()

# different ways to bring down the reference count
del a
b = 'hello'
c[2] = 'world'


print 'all shapes destroyed'
