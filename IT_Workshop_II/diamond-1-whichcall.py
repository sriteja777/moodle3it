####### to test this code ###############
#1. try old style class using class A:
#   change it to new style class using class A(object):
#2. comment method call in B1 by renaming call to call1
#   in old style - order is ME->B1->A->... so, A's call is called
#   in new style - order is ME->B1->B2->B3>A, so B2's call is called

class A:
  def call(self):
    print "I am parent A"

# rename call to call1 to see who is next in method invocaton order
class B1(A):
  def call1(self):
    print "I am parent B1"
 
class B2(A):
  def call(self):
    print "I am parent B2"
 
class B3(A):
  def call(self):
    print "I am parent B3"
 
class C(A):
  def call(self):
    print "I am parent C"
 
class ME(B1, B2, B3):
  def whichCall(self):
    print self.call()
 
  def restructure(self, parent1, parent2, parent3):
    self.__class__.__bases__ = (parent1, parent2, parent3, )
 
  def printBaseClasses(self):
    print 'Old style:', self.__class__.__bases__

   
me = ME()
if  issubclass(A, object):
   print 'New Style:', ME.mro()
else:
  me.printBaseClasses()
me.whichCall()

#change the order of base classes at run time
me.restructure(B3, B2, B1)
if  issubclass(A, object):
   print 'New Style:', ME.mro()
else:
  me.printBaseClasses()
me.whichCall()

#change the base classes at run time
me.restructure(C, B3, B1)
if  issubclass(A, object):
   print 'New Style:', ME.mro()
else:
  me.printBaseClasses()
me.whichCall()
