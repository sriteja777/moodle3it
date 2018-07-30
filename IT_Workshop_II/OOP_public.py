from  graphics import *
import time

#######################################################################
### Inheritance, polymorphism, private/public members, data-abstraction

class Shape:
   'Common base class for all shapes'
   shapeCount = 0  #1
   win =  GraphWin("Shapes display", 400, 400)
   
   def __init__(self, name, description, color):
      "constructor for shape class"
      self.name = name
      self.description = description
      self.color = color
      Shape.shapeCount += 1 #2


   def displayShape(self):
      print "Name : ", self.name,  ", Description: ", self.description

   def displayCount(self):
      print "Number of shapes on window : ",Shape.shapeCount #3

   def draw(self): pass
   
############################################      
class MyCircle(Shape):
    'circle class'
    def __init__(self, center, radius, color):
        'constructor for circle'
        self.center = center
        self.radius = radius
        Shape.__init__(self, 'circle', 'this is a class for creating and drawing circles',color)
        

    def draw(self):
       o = Circle(self.center, self.radius)
       o.setFill(self.color)
       o.draw(self.win)
       self.win.getMouse()
       
############################################# 
class MyLine(Shape):
    'line class'
    def __init__(self, pt1, pt2, color):
        'constructor for line'
        self.pt1 = pt1
        self.pt2 = pt2
        Shape.__init__(self, 'line', 'this is a class for creating and drawing lines', color)
        
    def draw(self):
       o = Line(self.pt1, self.pt2)
       o.setFill(self.color)
       o.setWidth(5)
       o.draw(self.win)
       self.win.getMouse()
        
#############################################

class MyOval(Shape):
    'line class'
    def __init__(self, pt1, pt2, color):
        'constructor for oval'
        self.pt1 = pt1
        self.pt2 = pt2
        Shape.__init__(self, 'oval', 'this is a class for creating and drawing ovals', color)

    def draw(self):
       o = Oval(self.pt1, self.pt2)
       o.setFill(self.color)
       o.draw(self.win)
       self.win.getMouse()
                
############################################
class MyRectangle(Shape):
    'line class'
    def __init__(self, pt1, pt2, color):
        'constructor for oval'
        self.pt1 = pt1
        self.pt2 = pt2
        Shape.__init__(self, 'rectangle', 'this is a class for creating and drawing rectangles', color)

    def draw(self):
       o = Rectangle(self.pt1, self.pt2)
       o.setFill(self.color)
       o.draw(self.win)
       self.win.getMouse()
                
############################################

lshapes = []
lshapes.append(MyCircle(Point(50,50), 50, 'blue'))
lshapes[-1].displayCount()
lshapes.append(MyLine(Point(100,100), Point(200,150), 'green'))
lshapes[-1].displayCount()
lshapes.append(MyOval(Point(150,150), Point(350,250), 'red'))
lshapes[-1].displayCount()
lshapes.append(MyRectangle(Point(10,200), Point(110,300), 'yellow'))
lshapes[-1].displayCount()

#AttributeError: MyRectangle instance has no attribute '__shapeCount'
print "accesing shapeCount directly :", lshapes[-1].shapeCount #4

for shape in lshapes:   
   shape.draw()
   shape.displayShape()


for shape in lshapes:
   del shape

print 'all shapes destroyed'
 
