class Puppy(object):
    count = 0
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
        Puppy.count +=1

    def showCount():
        print "total count=",Puppy.count

    showCount = staticmethod(showCount)
  

p1 = Puppy('beagle', 'Tabby')
Puppy.showCount() #total count= 1
p2= Puppy('bulldog', 'Hary')
Puppy.showCount() #total count= 2
p3= Puppy('Golden Retriever', 'Sam')
Puppy.showCount() #total count= 3

# assignment creates a new variable count in the instance p3
# class variable can not be modified from instance
p1.count += 1
p2.count += 2
p3.count += 3 
print Puppy.count, p1.count, p2.count, p3.count #3 4 5 6


