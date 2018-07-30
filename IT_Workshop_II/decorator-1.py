print "###### what is a decorator? basic srtucture ###################"
def decorator(f):
   def wrapper(arg):
      'add a wrapper around f'
      return f("Only this thing: " + arg)
   return wrapper

print "### code1 ###"
@decorator
def function(arg):
    return arg
print function("hello")

print "### code2 ###"
def function(arg):
    return arg

function = decorator(function)
print function("hello")
print "################### changing the input ########################"

def double_in(old):
    def wrapper(arg):
        return old(2*arg)
    return wrapper

def function(arg): return arg % 3
function = double_in(function)
print function(2)

print "# other way of writing the above code"
@double_in
def function (arg):return arg % 3
print function(2)

print "#####################changing the output ########################"
def double_out(old):
    def wrapper(arg):
        return 2 * old(arg)
    return wrapper

def function(arg): return arg % 3
function = double_out(function)
print function(2)

print "############# other way of writing the code############"
@double_out
def function (arg):return arg % 3
print function(2)
print "####################### changing input and output both ##############"

def decorator(old):
    def wrapper(*args, **kwds):
       # preprocessing
       new_args = []
       for arg in args:
           new_args.append("pre-" + arg)

       #calling the old function with modified input args
       ret = old(*new_args, **kwds)

       # postprocessing - modifying the output 
       new_args = []
       for arg in ret:
           new_args.append(arg + "-post")
       return new_args
    return wrapper

def function(a, b, c):
     return [a,b,c]

function = decorator(function)
print function("foo", "bar", "baz")

@decorator
def function(a, b, c):
     return [a,b,c]

print function("foo", "bar", "baz")
print "########################### timing a method #########################"
import time
def time_decorator(old):
   def time_wrapper(*args, **kwds):
	t1 = time.time()
        ret =  old(*args, **kwds)
        t2 = time.time()
        print "time taken to execute method ", old.__name__, "on ", args, " is ", (t2-t1) * 1000, 'ms'
	return ret
   return time_wrapper

@time_decorator
def mul(a, b, c): return a*b*c

p = mul(27653, 3156, 4298)
print "product is ", p


print "########################### counting function calls ##################"
def count_decorator(old):
   count = [0] #initialize count once before returning the wrapper function
   def count_wrapper(*args, **kwds):
      count[0] += 1
      print "count is ", count[0]
      return old(*args,  **kwds)  
   return count_wrapper

@count_decorator
def function (a,b,c): return a+b+c

function (1,2,3) 
function (1,2,3)
function (1,2,3)
function (1,2,3)  
function (1,2,3)   

print "######################### decorator class #############################"
import time
class TIMED(object):
    def __init__(self, f):
       print "inside constructor f=",f.__name__
       self.f = f

    def __call__(self, *args):
       start = time.time()
       ret = self.f(*args)
       stop = time.time()
       print "time taken to {0} is {1} ms.".format(self.f.func_name, 1000*(stop-start))
       return ret 

@TIMED
def div(x,y): return x/y 

div(938504395, 84775845)

@TIMED
def mul(x,y,z): return x*y*z

mul(27653, 3156, 4298)

print "############## decorating methods ####################"
def p_decorate(func):
   def func_wrapper(self):
       return "<p>{0}</p>".format(func(self))
   return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "Bunny"
        self.family = "Foo"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family

my_person = Person()
print my_person.get_fullname() #<p>Bunny Foo</p>

print "##################chain- multiple decorators ######################"
def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper

@div_decorate
@p_decorate
@strong_decorate
def greet(name):
   return "hello {0}".format(name)
print "code1: ", greet("Bunny")

def greet(name):
   return "hello {0}".format(name)

greet = div_decorate(p_decorate(strong_decorate(greet)))
print "code2: ", greet("Bunny")

print "############# Passing arguments to decorators #######################"
def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("div")
@tags("p")
@tags("strong")
def greet(name):
   return "hello {0}".format(name)

print greet("Bunny")



