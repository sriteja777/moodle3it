print "########## functions as objects #######################"
def foo(s):
    'I am a function object'
    print s

bar = foo

bar("hello")
print "my doc string is: ", bar.__doc__
print "my dictionary is: ", bar.__dict__
print "my module name is: ", bar.__module__
print "my name is: ", bar.__name__
print "my address is:", bar

print "########### functions as arguments #################################"
def call_func(f, *args):
  return f(*args)

#call_func takes another function(anonymous) as its first argument
print call_func(lambda x, y: x + y, 4, 5)

print "################ nested functions when returned #######################"
def outer():
   def inner(a):
      return a
   return inner

f1 = outer()
f2 = outer()
print "outer is :", outer
print "inner is :", f1
print "inner is :", f2

print "################## closures ##################################"
def outer(a):
   def inner(b):
    return a + b
   return inner

add1 = outer(1) #a is set to 1
print "add1 is ", add1
print "add1(4) is ", add1(4)
print "add1(5) is ", add1(5)
add2 = outer(2) #a is set to 2
print "add2 is ", add2
print "add2(4) is ", add2(4)
print "add2(5) is ", add2(5)

print "###################### scoping problem and solution ################"
def outer():
    count = 0
    def inner():
        print "inside inner count is ", count
        count += 1
        return count
    return inner

counter = outer()
#UnboundLocalError: local variable 'count' referenced before assignment
#print counter()
print "#####use mutable type - list to allow changes to variable in outer scope from inner scope"
def outer():
    count = [0]
    def inner():
        count[0] += 1
        return count[0]
    return inner

counter = outer()
print counter()
print "######################### When mutablility matters? ####"
container = {"hello", "world", "end"}
string_build = ""
for data in container:
    string_build += str(data)
    print "id of string_build is ", id(string_build)

list_build = []
for data in container:
    list_build.append(str(data))
    print "id of list_build is ", id(list_build)
print "######################### When mutability fails? ######"
print "###### in doSomething- version1 #########"
def doSomething(param=[]):
    param.append("thing")
    return param
 
a1 = doSomething() 
print id(a1),"=",a1 #140114778712904 = ['thing']
a2 = doSomething() 
print id(a2),"=",a2 #140114778712904 = ['thing', 'thing']
a3 = doSomething() 
print id(a3),"=",a3 #140114778712904 = ['thing', 'thing', 'thing']
a4 = doSomething(["passed_1"])
print id(a4),"=",a4 #140114778713408 = ['passed_1', 'thing']
a5 = doSomething(["passed_2"])
print id(a5),"=",a5 #140114778713336 = ['passed_2', 'thing']


print "################## in doSomething- version2 : solution: don't assign mutable object to input parameter as default"

def doSomething(param=None):
    if param == None:
        param = []
 
    param.append("thing")
    return param
 
a1 = doSomething() 
print id(a1),"=",a1 #140114778713552 = ['thing']
a2 = doSomething() 
print id(a2),"=",a2 #140114778713480 = ['thing']
a3 = doSomething() 
print id(a3),"=",a3 #140114778656712 = ['thing']
a4 = doSomething(["passed_1"])
print id(a4),"=",a4 #140114778712904 = ['passed_1', 'thing']
a5 = doSomething(["passed_2"])
print id(a5),"=",a5 #140114778713408 = ['passed_2', 'thing']






