
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
    e1 = Employee("Foo", 1000)
    e2 = Employee("Bar", 2000)
    e1.displayEmployee()
    e2.displayEmployee()
    e1.displayCount()
    e2.displayCount()
 
    print  "Employee.empCount:",Employee.empCount
    print "Employee.__doc__:", Employee.__doc__
    print "Employee.__name__:", Employee.__name__
    print "Employee.__module__:", Employee.__module__
    print "Employee.__bases__:", Employee.__bases__
    print "Employee.__dict__:", Employee.__dict__
    print  "e1.empCount:",Employee.empCount

    #name and bases properties are defined on class not on instance
    print "e1.__doc__:", e1.__doc__
    print "e1.__class__.__name__:", e1.__class__.__name__
    print "e1.__module__:", e1.__module__
    print "e1.__class__.__bases__:", e1.__class__.__bases__
    print "e1.__dict__:", e1.__dict__
 

test()
    

