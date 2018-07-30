
class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      "constructor for employee class"
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

   def __del__(self):
      self.__class__.empCount -= 1
      print  self.__class__.__name__, "destroyed", "empCount = ", self.__class__.empCount

def test():      
   print '__name__=', __name__
   e1 = Employee("Foo", 1000)
   e2 = Employee("Bar", 2000)
   e1.displayEmployee()
   e2.displayEmployee()
   e1.displayCount()
   e2.displayCount()
   del e1
   del e2
   print  "Employee.empCount:",Employee.empCount
   print "Employee.__doc__:", Employee.__doc__
   print "Employee.__name__:", Employee.__name__
   print "Employee.__module__:", Employee.__module__
   print "Employee.__bases__:", Employee.__bases__
   print "Employee.__dict__:", Employee.__dict__

#checks to see if code is being imported or is main entry point
#when you invoke code using python filename.py then __name__ will be
#set to '__main__'
if __name__ == '__main__':
   test()
else:
   print "Current module is imported and not main entry point and __name__=", __name__

