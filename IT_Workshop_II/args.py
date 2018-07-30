print "# what does * mean?"
def f(a,b,c):
    print a,b,c

f(1, 2, 3)
f(*[1,2,3])
f(1,*[2,3])
#f(*[2,3]) #error


print" ##### what does *args mean inside a function definition ############" 

def f(*args):
    print "args = ", args

f(1,2,3)
f(1)

def f(a, *args):
    print "a = ", a, "args = ", args, "sum=", sum(args)
    
f(1,2,3)
f(1)
f(1, *[2,3,4,5])
f(*[2,3,4,5])
f(1,*(2,3,4,5))
f(*(2,3,4,5))

print "version1: ###### how to pass variable number of arguments to another function ####"

def f3(*args): # can take variable number of arguments in form of a tuple called args
    print "f3:args=", args
    print "f3:sum =",sum(args) # no * here indicates args is a required sequence
    
def f2(a,b):
    print "f2: two args are ",a,b

def f1(*args): # can take variable number of arguments in form of a tuple called args
    print "f1:args=", args
    f2(*args)  # * here indicates unpacking of args tuple to corresponding formals of f2
    f3(*args)   # * means unpack args to positional arguments

f1(1,2)

print "version2: ###### how to pass variable number of arguments to another function ####"

def f3(*args): # can take variable number of arguments in form of a tuple called args
    print "f3:args=", args
    print "f3:sum =",sum(*args) #* here indicates unpacking of args tuple to match the first positional argument (sequence) in sum
    
def f2(a,b):
    print "f2: two args are ",a,b

def f1(*args): # can take variable number of arguments in form of a tuple called args
    print "f1:args=", args
    f2(*args)  # * here indicates unpacking of args tuple to corresponding formals of f2
    f3(args)   # no * - passing a tuple for first positional argument to f3 

f1(1,2)
print "################################################# use case ####"
def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)

multiply(4, 5)
multiply(10, 9)
multiply(2, 3, 4)
multiply(3, 5, 10, 6)

    
