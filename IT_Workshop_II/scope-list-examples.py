
#########################
#  a and b are referring to the same list
a= [1,2,3]
b = a
id(a) == id(b)
a.append(4)
print "id(a) == id(b):",id(a) == id(b)
print a
print b
###############################
a = [1,2,3,4]
def foo(x):
    "assignment makes a new list: no side effect"
    x = [5,6]
    return x

print foo.__doc__
print "id(a) == id(foo(a)):",id(a) == id(foo(a)) #False
print foo(a)
print a

###########################
a = [1,2,3,4]
def foo(x):
    "side effect: append changes the original list"
    x.append([5,6])
    return x

print foo.__doc__
print "id(a) == id(foo(a)):",id(a) == id(foo(a)) #True
print foo(a)
print a
################################
a= [1,2,3, 4]
def foo(x):
    "send the shallow copy of original list to avoid side effects to some extent"
    x.append([5,6])
    return x

print foo.__doc__
print "id(a) == id(foo(a[:])):",id(a) == id(foo(a[:])) #False
print foo(a[:])
print a
#########################################
a = [2,3,'hello',[4,'yes']]
def foo(x):
    "still side effects on sublists in original list"
    x[3][0]="GREAT"
    return x

print foo.__doc__
print "id(a) == id(foo(a[:]))", id(a) == id(foo(a[:])) #False 
print "id(a[3]) == id(foo(a)[3]):",id(a[3]) == id(foo(a[:])[3]) #True
print foo(a[:])
print a
#########################################
from copy import deepcopy
a = [2,3,'hello',[4,'yes']]
def foo(x):
    "deep copy eliminates side effects on sublists in original list"
    x[3][0]="GREAT"
    return x

print foo.__doc__
print "id(a[3]) == id(foo(deepcopy(a))):",id(a[3]) ==id(foo(deepcopy(a))) #False
print foo(deepcopy(a))
print a

