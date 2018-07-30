from graphics import *
import time

def main(color, x, y, max):
    g = GraphWin('Back and Forth', 300, 300)

    c = Circle(Point(0,0), 25)
    c.setFill(color)
    c.setOutline("black")
    c.draw(g)
    
    # move down to right 
    for i in range(max):
        c.move(x, y)
        time.sleep(.05)
        
    # move up to left 
    for i in range(max):
        c.move(-x, -y)
        time.sleep(.05)

    g.close()

colors  =  ['red','yellow','green','blue','brown','pink']
for i in range(len(colors)):
   x, y, max = (i+1)*5, (i+1)*5,  60/(i+1)
   main(colors[i], x, y, max)
